#!/usr/bin/env python3
"""
reboot.py — Session bootstrap for the Hu v. Hyundai Motor America
            CPLR Article 75 petition project (Claude Code).

WHAT IT DOES
  1. Walks a source directory of case materials.
  2. Determines each file's TRUE type from its magic bytes (extensions in this
     matter are unreliable: many ".pdf" files are actually DOCX/ZIP, and some
     ".docx" files are actually plain text). Flags every extension<->content
     mismatch.
  3. Sorts each file into the buckets the reboot is meant to surface:
       SUBMISSION  - materials submitted to the arbitration
       VERDICT     - the arbitration award and its cover letter
       PROCEDURAL  - notices / scheduling that are part of the record
       WORK_PRODUCT- prior drafts, summaries, memos, agent memory
       OTHER       - anything uncategorized
  4. Extracts readable text into ./_extracted/, choosing the backend by TRUE
     type (pdftotext for real PDFs; pandoc/zipfile for DOCX; copy for text;
     OCR flagged for images). Also drops a corrected-extension copy in
     ./_extracted/normalized/ so downstream tools don't choke.
  5. Writes _manifest.json (machine-readable) and prints a human report plus a
     gap check and the "where to go from there" banner.

USAGE
  python3 reboot.py                     # source = ./materials (or CWD if absent)
  python3 reboot.py --source ./case     # explicit source dir
  python3 reboot.py --no-extract        # inventory only, skip text extraction
  python3 reboot.py --no-normalize      # don't write corrected-extension copies

DEPENDENCIES (all optional; the script degrades gracefully and reports gaps)
  poppler-utils (pdftotext, pdfinfo) . pandoc . python3 stdlib only otherwise.
  For image OCR: tesseract (optional).

No pip installs are required. Safe to re-run (idempotent).
"""

from __future__ import annotations
import argparse
import json
import os
import shutil
import subprocess
import sys
import zipfile
from datetime import date
from pathlib import Path

# ----------------------------------------------------------------------------- 
# Constants for this matter (do not invent; these are verified in CLAUDE.md)
# ----------------------------------------------------------------------------- 
CASE = "Hu v. Hyundai Motor America — AG Case NC-1-1249605441"
FILING_DEADLINE = date(2026, 9, 9)  # CPLR 7511(a): 90 days from award (6/11/2026)
BRIEF_FILE = "CLAUDE.md"            # the persistent project brief Claude Code loads

# Magic-byte signatures (hex prefixes)
SIGNATURES = [
    ("25504446", "pdf",  "PDF"),
    ("504b0304", "zip",  "ZIP/OOXML (docx/xlsx/pptx)"),
    ("504b0506", "zip",  "ZIP (empty)"),
    ("504b0708", "zip",  "ZIP (spanned)"),
    ("d0cf11e0", "ole",  "OLE legacy (.doc/.xls/.ppt)"),
    ("ffd8ff",   "jpg",  "JPEG image"),
    ("89504e47", "png",  "PNG image"),
    ("47494638", "gif",  "GIF image"),
    ("7b5c7274", "rtf",  "RTF"),
    ("255044462d", "pdf", "PDF"),
]

# Ordered categorization rules: (substring, category, human label).
# First match wins; matched case-insensitively against the filename.
CATEGORY_RULES = [
    ("decision_letter",        "VERDICT",      "Award cover letter (90-day / 20-day language)"),
    ("hu_decision",            "VERDICT",      "Arbitration Award (the verdict)"),
    ("_decision",              "VERDICT",      "Arbitration Award / decision"),
    ("noh",                    "PROCEDURAL",   "Notice of Hearing"),
    ("notice_of_hearing",      "PROCEDURAL",   "Notice of Hearing"),
    ("request_for_arbitration","SUBMISSION",   "Demand / Request for Arbitration"),
    ("lemon_law_request",      "SUBMISSION",   "Demand / Request for Arbitration"),
    ("arbitration_form",       "SUBMISSION",   "AG arbitration intake form"),
    ("nc11249605441",          "SUBMISSION",   "AG arbitration form (case no.)"),
    ("arbitration__hu",        "SUBMISSION",   "Arbitration submission packet"),
    ("lease",                  "SUBMISSION",   "Lease agreement (standing / terms)"),
    ("bill_of_sale",           "SUBMISSION",   "Bill of sale"),
    ("registration",           "SUBMISSION",   "Vehicle registration"),
    ("203_ex04",               "SUBMISSION",   "Exhibit 04 — Repair Orders"),
    ("repair_orders",          "SUBMISSION",   "Repair Orders (RO #356398 / #358530 / etc.)"),
    ("hma_offer",              "SUBMISSION",   "HMA settlement offer letter"),
    ("offer_letter",           "SUBMISSION",   "HMA settlement offer letter"),
    ("repurchase_calculated",  "SUBMISSION",   "HMA repurchase calc (mileage-deduction offer)"),
    ("settlement_agreement",   "SUBMISSION",   "Settlement Agreement & Release (§1542 / CA-law)"),
    ("ex11",                   "WORK_PRODUCT", "Exhibit 11 — Days Out of Service summary"),
    ("days_out_of_service",    "WORK_PRODUCT", "Exhibit 11 — Days Out of Service summary"),
    ("memo_of_law",            "WORK_PRODUCT", "Memorandum of Law (Article 75)"),
    ("appeal_memo",            "WORK_PRODUCT", "Memorandum of Law (Article 75)"),
    ("case_summary",           "WORK_PRODUCT", "Attorney case summary / intake"),
    ("strategy",               "WORK_PRODUCT", "Legal strategy memo"),
    ("claude.md",              "WORK_PRODUCT", "Project brief / agent memory (this reboot)"),
]

# Loose expected-inventory for the gap check (match by any keyword in the tuple).
EXPECTED = [
    ("Demand/Request for Arbitration", ("request_for_arbitration", "lemon_law_request")),
    ("AG arbitration form",            ("arbitration_form", "nc11249605441")),
    ("Lease agreement",                ("lease",)),
    ("Repair Orders exhibit",          ("repair_orders", "203_ex04")),
    ("Bill of sale",                   ("bill_of_sale",)),
    ("Vehicle registration",           ("registration",)),
    ("HMA offer letter",               ("hma_offer", "offer_letter")),
    ("Repurchase calc offer",          ("repurchase_calculated",)),
    ("Settlement Agreement & Release", ("settlement_agreement",)),
    ("Arbitration Award (verdict)",    ("hu_decision", "_decision")),
    ("Award cover letter",             ("decision_letter",)),
    ("Notice of Hearing",              ("noh", "notice_of_hearing")),
]

CATEGORY_ORDER = ["VERDICT", "SUBMISSION", "PROCEDURAL", "WORK_PRODUCT", "OTHER"]


# ----------------------------------------------------------------------------- 
def rel(path: Path, base: Path) -> str:
    """Path relative to base if possible; otherwise the absolute path."""
    try:
        return str(path.relative_to(base))
    except ValueError:
        return str(path)


def have(cmd: str) -> bool:
    return shutil.which(cmd) is not None


def magic_type(path: Path) -> tuple[str, str]:
    """Return (kind, human) from the file's leading bytes."""
    try:
        with open(path, "rb") as fh:
            head = fh.read(16)
    except OSError:
        return ("unreadable", "unreadable")
    hexs = head.hex()
    for sig, kind, human in SIGNATURES:
        if hexs.startswith(sig):
            if kind == "zip":  # refine OOXML by inner path
                return refine_zip(path, human)
            return (kind, human)
    # Heuristic: printable ASCII/UTF-8 -> text
    try:
        head.decode("utf-8")
        return ("text", "text/markdown/plain")
    except UnicodeDecodeError:
        return ("binary", f"unknown [{hexs[:8]}]")


def refine_zip(path: Path, human: str) -> tuple[str, str]:
    import re
    try:
        with zipfile.ZipFile(path) as z:
            names = z.namelist()
            page_txt = [n for n in names if re.fullmatch(r"\d+\.txt", n)]
            if "manifest.json" in names and page_txt:
                return ("bundle", "Claude page-bundle (page images + OCR text)")
            if any(n.startswith("word/") for n in names):
                return ("docx", "DOCX (Word)")
            if any(n.startswith("xl/") for n in names):
                return ("xlsx", "XLSX (Excel)")
            if any(n.startswith("ppt/") for n in names):
                return ("pptx", "PPTX (PowerPoint)")
    except zipfile.BadZipFile:
        pass
    return ("zip", human)


def categorize(name: str) -> tuple[str, str]:
    low = name.lower()
    for sub, cat, label in CATEGORY_RULES:
        if sub in low:
            return (cat, label)
    return ("OTHER", "Uncategorized")


def true_ext(kind: str) -> str:
    return {
        "pdf": ".pdf", "docx": ".docx", "xlsx": ".xlsx", "pptx": ".pptx",
        "jpg": ".jpg", "png": ".png", "gif": ".gif", "rtf": ".rtf",
        "text": ".md", "ole": ".doc", "zip": ".zip", "bundle": "",
    }.get(kind, "")


# ----------------------------------------------------------------------------- 
# Text extraction, routed by TRUE type
# ----------------------------------------------------------------------------- 
def extract_text(path: Path, kind: str) -> tuple[str | None, str]:
    """Return (text_or_None, status)."""
    if kind == "pdf":
        if have("pdftotext"):
            try:
                out = subprocess.run(
                    ["pdftotext", "-layout", str(path), "-"],
                    capture_output=True, text=True, timeout=120,
                )
                if out.returncode == 0 and out.stdout.strip():
                    return (out.stdout, "pdftotext")
            except Exception as e:  # noqa: BLE001
                return (None, f"pdftotext error: {e}")
        try:
            import pypdf  # type: ignore
            reader = pypdf.PdfReader(str(path))
            txt = "\n".join((pg.extract_text() or "") for pg in reader.pages)
            if txt.strip():
                return (txt, "pypdf")
        except Exception:  # noqa: BLE001
            pass
        return (None, "no PDF backend (install poppler-utils or pypdf)")

    if kind == "bundle":
        import re
        try:
            with zipfile.ZipFile(path) as z:
                names = z.namelist()
                pages = sorted((n for n in names if re.fullmatch(r"\d+\.txt", n)),
                               key=lambda s: int(s.split(".")[0]))
                parts = []
                for n in pages:
                    parts.append(f"----- page {n.split('.')[0]} -----")
                    parts.append(z.read(n).decode("utf-8", "ignore").strip())
                txt = "\n".join(parts).strip()
                if txt:
                    return (txt, f"page-bundle OCR ({len(pages)} pages)")
        except Exception as e:  # noqa: BLE001
            return (None, f"bundle error: {e}")
        return (None, "bundle with no page text")

    if kind in ("docx", "zip"):
        if have("pandoc"):
            try:
                out = subprocess.run(
                    ["pandoc", "-f", "docx", "-t", "markdown", str(path)],
                    capture_output=True, text=True, timeout=120,
                )
                if out.returncode == 0 and out.stdout.strip():
                    return (out.stdout, "pandoc")
            except Exception:  # noqa: BLE001
                pass
        # stdlib fallback: pull word/document.xml and strip tags
        try:
            import re
            with zipfile.ZipFile(path) as z:
                if "word/document.xml" in z.namelist():
                    xml = z.read("word/document.xml").decode("utf-8", "ignore")
                    xml = re.sub(r"</w:p>", "\n", xml)
                    xml = re.sub(r"<[^>]+>", "", xml)
                    txt = re.sub(r"[ \t]+", " ", xml).strip()
                    if txt:
                        return (txt, "zipfile+regex")
        except Exception as e:  # noqa: BLE001
            return (None, f"docx error: {e}")
        return (None, "no DOCX backend (install pandoc)")

    if kind == "xlsx":
        return (None, "spreadsheet — open with a sheet tool / pandas")

    if kind == "text":
        try:
            return (path.read_text(encoding="utf-8", errors="ignore"), "read")
        except Exception as e:  # noqa: BLE001
            return (None, f"read error: {e}")

    if kind in ("jpg", "png", "gif"):
        if have("tesseract"):
            try:
                out = subprocess.run(
                    ["tesseract", str(path), "stdout"],
                    capture_output=True, text=True, timeout=120,
                )
                if out.returncode == 0 and out.stdout.strip():
                    return (out.stdout, "tesseract OCR")
            except Exception:  # noqa: BLE001
                pass
        return (None, "IMAGE — needs OCR (tesseract) or a vision model")

    return (None, f"no extractor for {kind}")


# ----------------------------------------------------------------------------- 
def main() -> int:
    ap = argparse.ArgumentParser(description="Reboot the Hu v. HMA Article 75 project.")
    ap.add_argument("--source", default=None, help="Directory of case materials.")
    ap.add_argument("--out", default="_extracted", help="Output dir for extracted text.")
    ap.add_argument("--no-extract", action="store_true", help="Inventory only.")
    ap.add_argument("--no-normalize", action="store_true", help="Skip corrected-ext copies.")
    args = ap.parse_args()

    here = Path(__file__).resolve().parent
    src = Path(args.source).resolve() if args.source else (
        here / "materials" if (here / "materials").is_dir() else here
    )
    out = (src / args.out) if not Path(args.out).is_absolute() else Path(args.out)
    norm = out / "normalized"

    if not src.is_dir():
        print(f"[FATAL] source directory not found: {src}", file=sys.stderr)
        return 2

    files = sorted(
        p for p in src.iterdir()
        if p.is_file() and p.name != Path(__file__).name and not p.name.startswith("_")
    )

    print("=" * 78)
    print(f"REBOOT :: {CASE}")
    days_left = (FILING_DEADLINE - date.today()).days
    print(f"FILING DEADLINE (CPLR 7511[a]): {FILING_DEADLINE.isoformat()}  "
          f"({days_left} days from today {date.today().isoformat()})")
    print(f"SOURCE : {src}")
    print("=" * 78)

    tools = {t: have(t) for t in ("pdftotext", "pandoc", "unzip", "tesseract")}
    print("Extraction tools: " + ", ".join(
        f"{t}={'yes' if ok else 'NO'}" for t, ok in tools.items()))
    print()

    if not args.no_extract:
        out.mkdir(parents=True, exist_ok=True)
        if not args.no_normalize:
            norm.mkdir(parents=True, exist_ok=True)

    manifest = []
    buckets: dict[str, list] = {c: [] for c in CATEGORY_ORDER}

    for p in files:
        kind, human = magic_type(p)
        cat, label = categorize(p.name)
        labeled = p.suffix.lower()
        expected_ext = true_ext(kind)
        if kind == "bundle":
            mismatch = True
            corrected = "(page-bundle -> use extracted .txt)"
        else:
            mismatch = bool(expected_ext) and labeled and labeled != expected_ext
            corrected = expected_ext if mismatch else labeled

        rec = {
            "file": p.name,
            "bytes": p.stat().st_size,
            "labeled_ext": labeled or "(none)",
            "true_type": human,
            "true_kind": kind,
            "mismatch": mismatch,
            "corrected_ext": corrected,
            "category": cat,
            "role": label,
            "extract_status": "skipped",
            "extract_backend": None,
            "text_out": None,
            "normalized_out": None,
        }

        if not args.no_extract:
            text, status = extract_text(p, kind)
            rec["extract_backend"] = status
            if text is not None:
                stem = p.stem
                tp = out / f"{stem}.txt"
                tp.write_text(text, encoding="utf-8")
                rec["extract_status"] = "ok"
                rec["text_out"] = rel(tp, src)
            else:
                rec["extract_status"] = "manual"  # see backend note

            if not args.no_normalize and mismatch and expected_ext and kind != "bundle":
                npath = norm / f"{p.stem}{expected_ext}"
                try:
                    shutil.copy2(p, npath)
                    rec["normalized_out"] = rel(npath, src)
                except Exception:  # noqa: BLE001
                    pass

        manifest.append(rec)
        buckets.setdefault(cat, []).append(rec)

    # ---- Human report, grouped by the buckets the user asked to surface ----
    titles = {
        "VERDICT":      "THE VERDICT (arbitration award + cover letter)",
        "SUBMISSION":   "MATERIALS SUBMITTED TO THE ARBITRATION",
        "PROCEDURAL":   "PROCEDURAL / RECORD",
        "WORK_PRODUCT": "PRIOR WORK PRODUCT (drafts, summaries, agent memory)",
        "OTHER":        "UNCATEGORIZED",
    }
    for cat in CATEGORY_ORDER:
        recs = buckets.get(cat) or []
        if not recs:
            continue
        print("-" * 78)
        print(titles[cat])
        print("-" * 78)
        for r in recs:
            flag = "  <-- EXT MISMATCH" if r["mismatch"] else ""
            print(f"  {r['file']}")
            print(f"      role      : {r['role']}")
            print(f"      true type : {r['true_type']}  "
                  f"(labeled {r['labeled_ext']}){flag}")
            if not args.no_extract:
                where = r["text_out"] or f"[{r['extract_backend']}]"
                print(f"      text      : {r['extract_status']}  {where}")
                if r["normalized_out"]:
                    print(f"      corrected : {r['normalized_out']}")
        print()

    # ---- Gap check ----
    found_low = " ".join(r["file"].lower() for r in manifest)
    missing = [name for name, keys in EXPECTED
               if not any(k in found_low for k in keys)]
    print("-" * 78)
    print("GAP CHECK (expected arbitration-record items)")
    print("-" * 78)
    if missing:
        for m in missing:
            print(f"  MISSING (or renamed): {m}")
    else:
        print("  All expected arbitration-record items are present.")
    print()

    # ---- Manifest ----
    if not args.no_extract:
        mpath = out / "_manifest.json"
        mpath.write_text(json.dumps(
            {"case": CASE, "deadline": FILING_DEADLINE.isoformat(),
             "source": str(src), "files": manifest}, indent=2), encoding="utf-8")
        print(f"Manifest: {mpath}")
        print(f"Extracted text dir: {out}")
        print()

    # ---- Where to go from there ----
    brief = src / BRIEF_FILE
    print("=" * 78)
    print("WHERE TO GO FROM HERE")
    print("=" * 78)
    if brief.is_file():
        print(f"  1. READ {BRIEF_FILE} in full — it carries the verified facts,")
        print(f"     pinpointed citations, the arbitrator's verbatim language and")
        print(f"     errors, the 8-point argument architecture, and the open items.")
    else:
        print(f"  1. {BRIEF_FILE} NOT FOUND in source — place it here; it is the")
        print(f"     project brief with all verified analysis and the roadmap.")
    print("  2. Re-read the extracted VERDICT text and confirm the four adverse")
    print("     findings and the dispositive 'no allegation' sentence.")
    print("  3. Next deliverable: Verified Petition + Notice of Petition, then")
    print("     CPLR 403 / 7503 / 311 service mechanics on HMA (foreign corp).")
    print("  4. Open items to resolve before filing:")
    print("       - RO # for the 2/18/2026 event (award says 363888; records 370267)")
    print("       - Caption: name NYSDRA / AG program? (check 13 NYCRR Part 300)")
    print("       - NJ Lemon Law parallel track (N.J.S.A. 56:12-29) — evaluate")
    print("       - pro se vs. counsel — user's call; do NOT re-litigate")
    print("  5. PRIME DIRECTIVE: no figure, date, quote, or citation enters a")
    print("     filing without verification against source. Never fabricate a cite.")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
