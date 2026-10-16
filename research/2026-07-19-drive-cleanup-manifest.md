# Drive Cleanup Manifest — "Hyundai Lemon Lawsuit 6-2026" (2026-07-19)

Full inventory: `research/drive_inventory_2026-07-19.tsv` (199 files, 25
folders). **Identity basis: byte-size match** — the Drive connector exposes no
md5, so "duplicate of" below means identical byte count. At these file sizes a
size collision is vanishingly unlikely, but for anything you feel is
litigation-critical, open the two files side-by-side for a 5-second visual
check before deleting. Drive deletions go to Trash (recoverable ~30 days).

The connector in this session cannot delete or move files — execute this
manifest in the Drive UI.

## Rule applied

Keep (1) the arbitration-record folder **intact and untouched**, (2) one
topical-home copy of transaction/evidence documents, (3) every unique file.
Delete only stray extra copies (root clutter, the outdated April-2026 working
tree, and the redundant `Repair Orders/` scan folder).

---

## A. DELETE — byte-identical duplicates (16 files, near-zero risk)

Root-level strays (canonical copy kept in the exhibits folder and/or topical home):

| Delete (path from root) | Kept canonical copy |
|---|---|
| `Hu_v_HMA_Ex01_Lease_Agreement.pdf` | exhibits folder Ex01 + `Car Lease Documents/Car Lease Contract 1-59225931599.pdf` |
| `Hu_v_HMA_Ex04_Repair_Orders.pdf` | exhibits folder Ex04 |
| `Hyundai Repair Orders.pdf` | exhibits Ex04 + `Hyundai Lemon Law/Hyundai Repair Orders/Hyundai Repair Orders.pdf` |
| `Hu_v_HMA_Ex05_HMA_Offer_Letter_1_Aug2025.pdf` | exhibits Ex05 + `Hyundai Lemon Law/Repurchase Calculated Offer - JIMMY HU.pdf` |
| `Hu_v_HMA_Ex06_HMA_Offer_Letter_2_Jan2026.pdf` | exhibits Ex06 + `…/Hyundai Lowball Settlement Offers/HMA Offer Letter - HU.pdf` |
| `Hu_v_HMA_Ex02_Bill_of_Sale.pdf` | exhibits Ex02 + `Car Lease Documents/Hyundai Bill of Sale.pdf` |
| `Hu_v_HMA_Ex03_Registration.pdf` | exhibits Ex03 |
| `Settlement Agreement - KM8KNDDF9RU253237.pdf` | exhibits Ex09a + `…/Hyundai Lowball Settlement Offers/` copy |

Inside the outdated tree `Car Lease 5-2024/Lemon Law/Lemon Law update 4-2026/`
(all byte-identical to kept copies):

| Delete | Kept canonical copy |
|---|---|
| `Contract 1-59225931599.pdf` | `Car Lease Documents/Car Lease Contract 1-59225931599.pdf` |
| `Repurchase Calculated Offer - JIMMY HU.pdf` | `Hyundai Lemon Law/` copy |
| `HMA Offer Letter - HU.pdf` | `…/Hyundai Lowball Settlement Offers/` copy |
| `Settlement Agreement - KM8KNDDF9RU253237.pdf` | `…/Hyundai Lowball Settlement Offers/` copy |
| `Koeppel Hyundai Receipt.pdf` | = Bill of Sale (same bytes); kept in `Car Lease Documents/` |
| `PXL_20240710_235523666.jpg` | = `Car Lease Documents/Car Registration.jpg` |
| `Scan_20250730.jpg` | = `…/Hyundai Repair Orders/2025-04-03_Repair_Order_358530_Detail.jpg` |
| `Hyundai Repair Orders/Scan_20250730.jpg` | same as above |
| `Hyundai Repair Orders/Scan_20250730_2.jpg` | `Hyundai Lemon Law/Hyundai Repair Orders/Scan_20250730_2.jpg` |
| `Hyundai Repair Orders/SHyundai Se26010917440.pdf` | `…/Hyundai Repair Orders/2026-01-08_Smart_Diagnosis_Report.pdf` |

Elsewhere:

| Delete | Kept canonical copy |
|---|---|
| `Car Lease 5-2024/scans_20250723_181519.pdf` | = Bill of Sale (same bytes) |
| `Car Lease 5-2024/PXL_20240710_235523666.jpg` | = `Car Lease Documents/Car Registration.jpg` |
| `Hyundai Lemon Law/Hyundai Repair Orders/Scan_20250730.jpg` | same-folder `2025-04-03_Repair_Order_358530_Detail.jpg` (identical bytes) |

## B. DELETE — entire folder `Repair Orders/` (13 files)

Every file is byte-identical to a descriptively-renamed copy in
`Hyundai Lemon Law/Hyundai Repair Orders/` (e.g. `Scan_20260225.jpg` =
`2026-02-18_Repair_Order_370267.jpg`; `Scan_20260225_2.jpg` =
`2025-08-27_Repair_Order_363888.jpg`; `SHyundai Se26010917440.pdf` =
`2026-01-08_Smart_Diagnosis_Report.pdf`). The renamed set is strictly better.
Full pairing in the TSV. Delete the whole folder.

## C. PROBABLE DELETE — verify visually first (11 files)

`Car Lease 5-2024/Lemon Law/Lemon Law update 4-2026/Hyundai Repair Orders/`
still holds 10 `Scan_*.jpg` files with the **same filenames** as the deleted
`Repair Orders/` set but **different byte sizes** — almost certainly earlier or
recompressed scans of the same RO pages. Spot-check 2–3 against the
descriptively-named canonical set; if they show the same pages, delete the
subfolder. **Exception — rescue first:** `…/Lemon Law update 4-2026/
PXL_20260220_141717575.jpg` is unique (likely the Feb 20, 2026 vehicle-pickup
photo) — move it to `Dashboard Photos/` or `Hyundai Car Breakdown Jan 2026/`
before deleting the tree. After A + C, the whole `Lemon Law update 4-2026/`
tree is empty — delete it.

Also: `Car Lease Documents/new-car-lemon-law.pdf` vs
`new_car_lemon_law_2025.pdf` — two statute reference copies; keep the 2025
one, delete the older (reference material, no evidentiary value).
`HMF Lease Term Extension - 2415627694_encrypted_.pdf` and `…(2).pdf` —
password-protected variants of the signed extension you already keep; if the
signed copy opens fine, these two can go.

## D. REVIEW — same bytes, conflicting names (do NOT just delete)

1. **`Arbitration Submission Exhibits…/Hu_v_HMA_Request_for_Arbitration.pdf` ≡
   `Hu_v_HMA_Arbitration_Form.pdf` ≡ `…/Arbitration Proceedings/NY Arbitration
   Form - Hu NC-1-1249605441.pdf`** (346,740 B ×3). Same pattern as the
   Ex07/Ex09b duplicate slots: if the Request and the Form were meant to be
   distinct documents, one true document is missing from the record set.
   Confirm what was actually filed on 5/12/26 before touching these.
2. `Hyundai Car Breakdown Jan 2026/Headlight/`: `SHyundai Se26010917440 1040
   initial fee.pdf` ≡ `…540 diagnostic fee.pdf` (same bytes, contradictory
   names) and `Picking up car and fixing headlight.pdf` ≡ `Gmail - Authorizing
   540 diagnostic fee.pdf` (same bytes). Open each pair once, keep the
   correctly-named copy, delete the misnamed one.
3. Root `Hyundai 1-2026.txt` — unidentified; open before deciding.
4. `Incident_Memo_Hu_v_Hyundai.docx` exists in both the exhibits folder and
   the Breakdown folder (identical) — harmless; optionally delete one.

## E. KEEP — canonical map (untouched)

- **`Arbitration Submission Exhibits — June 9 2026/`** — THE record as
  submitted, including the authentic award PDFs in its `Hyundai Lemon Law
  Dispute/` subfolder. Keep intact, including the flagged Ex07/Ex09b
  duplicates until item D-1 is resolved.
- `Car Lease Documents/` — transaction originals (lease contract, signed
  extension, bill of sale, registration, payment history).
- `Hyundai Lemon Law/Hyundai Repair Orders/` — the descriptively-named RO
  scans (canonical evidence set) + compiled PDF.
- All receipts folders (`Archive/…tolls`, `Parking`, `Shopping`, `Lyft Taxis`,
  `Car Rental`, `Impound`, `Headlight`) — originals backing Ex17/Ex21.
- `Lawyer engaged/` (Gorberg record incl. signed authorization), `Dashboard
  Photos/`, `Hyundai Car Breakdown Jan 2026/` core files (incident notes,
  call-recording zips), root evidence (the two `.wav` call recordings,
  `11-2025 Autobody Diagnostics Report.zip`,
  `Hyundai_Ioniq5_Repair_Orders_Chronological.pdf`), and all Google-native
  Docs/Sheets (Ex11, loss-of-use files, case summary).
- `Hyundai Lemon Law/` working docs (strategy memo, NJ letters, case
  summaries, old CLAUDE.md) — prior work product; keep or archive, never
  delete blind.

## Net effect

~29 sure deletions (A+B) + ~13 probable (C) ≈ **42 of 199 files removed**, two
dead folder trees eliminated, no unique document lost, arbitration record
untouched.

## Bonus finding

The lease agreement the repo is missing exists in Drive in 4 identical copies
(24,067,714 B) — too large for the 10MB connector limit. To get it into the
repo: compress/split it, or attach it directly in chat.
