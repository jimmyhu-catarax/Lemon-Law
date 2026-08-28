# Session log — Hu v. Hyundai Motor America

> **Audit trail. Relocated from `CLAUDE.md` on 2026-07-30**, where it was
> loading ~13,600 est. tokens into every session. Nothing was edited; the
> addenda below are verbatim and in original order.
>
> **⚠ READ THIS FILE BEFORE TOUCHING ANY FILING.** The addenda are where
> retractions, halt-and-confirm flags, and evidentiary-status notes live. Several
> facts asserted in early addenda were later refuted — the operative brief in
> `CLAUDE.md` carries the corrected versions, but the reasoning and the sourcing
> are here.
>
> **Start with Addendum 25** (the most recent): the retainer has been read, it
> is still unsigned, and two clarifications gate the signature.

## Index

| # | Date | Subject |
|---|---|---|
| 1 | 2026-07-18 | Claude Code repo; source verification |
| 2 | 2026-07-18 | Exhibits + email record ingested |
| 3 | 2026-07-19 | Adversarial review → Memo v4 |
| 4 | 2026-07-25 | Filing mechanics resolved; Petition drafted |
| 5 | 2026-07-27 | Attorney case summary v3 |
| 6 | 2026-07-28 | Packet review → Petition v2, Notice v2, Memo v5 |
| 7 | 2026-07-28 | Full-project review; brief reconciled |
| 8 | 2026-07-29 | Krukas engaged; arbitration form read for the first time |
| 9 | 2026-07-29 | Attorney Case Summary v7 — deference pass |
| 10 | 2026-07-29 | Krukas substantive reply; the November 23 lease wall |
| 11 | 2026-07-29 | How the buyback died; the § 198-a(n) hook |
| 12 | 2026-07-29 | Krukas reply finalized; prior counsel disclosed |
| 13 | 2026-07-29 | The body-repair precondition |
| 14 | 2026-07-30 | State reconciliation before /clear |
| 15 | 2026-07-30 | The fee ask added to the Krukas reply |
| 16 | 2026-07-30 | Fee structures made concrete |
| 17 | 2026-07-30 | **Counsel said yes; NJ closed; earlier read retracted** |
| 18 | 2026-07-30 | **The $5,000 declined; fee restructure asked with numbers** |
| 19 | 2026-07-30 | Tightened reply; superseded drafts pending deletion |
| 20 | 2026-07-30 | Register: gratitude and counsel's own indignation |
| 21 | 2026-07-30 | User's revision adopted; "marginally higher" flagged |
| 22 | 2026-07-30 | **Break-even correction — economics conceded too far** |
| 23 | 2026-07-31 | ✅ **Fee email SENT — text of record** |
| 24 | 2026-08-03 | ✅ **COUNSEL RETAINED — $3,000 + $1,000/appearance; retainer received, unsigned** |
| 25 | 2026-08-03 | ⚠ **The retainer READ — conditional cap, reordered waterfall; two asks gate signature** |

---

## SESSION ADDENDUM — 2026-07-18 (Claude Code repo; source verification)

*Additive log. Nothing above was edited; discrepancies below are flagged for
user confirmation per the Prime Directive, not silently resolved.*

**Repo state.** `materials/` holds the Decision_Letter__Hu.zip contents
(5 authentic PDFs: Decision Letter, Hu Decision, Bill of Sale, Repair Orders,
NOH) + Memo of Law v2 DOCX; extracted text in `materials/_extracted/`.
True types verified by magic bytes — these uploads are real PDFs / real DOCX
(the extension corruption afflicts only the claude.ai mirror). `reboot.py` at
root (sandbox blocked direct execution this session; equivalent inventory and
extraction performed manually). Multi-agent config in `.claude/agents/` and
`.claude/workflows/` (see PR #1).

**Award verified against text layer.** Dispositive "no allegation" sentence,
"WAGON ION," "Hyundai Brooklyn," "RO 258530," "RO 363888 mileage 8662
2/18/2026," refusal-reason language, lease-extension "as," and the
Issues↔Findings numbering swap — all confirmed verbatim. Checkbox states are
not in the text layer; prior rasterization findings stand.

**RESOLVED — Feb 2026 RO # (open item 1): it is RO #370267** (Respondent's
own record: opened 18FEB26 16:21, ready 19FEB26 12:37). The award's "RO
363888" is a separate **Aug 27–30, 2025 "NWP — NO WORK PERFORMED"** visit
(free NACS adapter check) at 8,662 mi. Project records were correct.

**⚠ NEW DISCREPANCIES — halt-and-confirm before filing (Memo v2 affected):**
1. **Odometer at the Feb 2026 event: 11,230 in / 11,231 out** per RO #370267
   — not "~8,662." The 8,662 figure is the award's conflation with RO 363888.
   Memo v2 currently asserts "approximately 8,662 miles … none of those facts
   is disputed" — **must be corrected before filing** (and note: the
   corrected figure still sits within 18,000 mi, and the argument anchors on
   date + "too dead to complete," so no substantive damage).
2. **RO #370267 documents a 12-volt battery replacement** (part 00275-18001
   "INTERSTATE BATTERY-H5," $286.16; "VERIFIED NEEDS JUMP TO START. TOO DEAD
   TO COMPLETE GDS … DC800 FAIL REPLACE BATTERY BATTERY FAILED. REPLACED
   BATTERY NO FURTHER STARTING ISSUE") — **not a second high-voltage pack
   replacement.** The only HV pack replacement in the ROs on hand is RO
   #358530 (37501-GI351-RM battery system assy $11,422.40; warranty total
   $17,483.69). Memo v2's "high-voltage battery was replaced a second time"
   is **unsupported by these ROs**. Hold until the full arbitration exhibits
   arrive — if no second HV-replacement RO exists, the memo and the "two full
   HV battery replacements" row above must be revised.
3. **Jan 8, 2026 Smart Diagnosis printout** (in the Repair Orders PDF, p.13):
   7 DTCs including **P1BAD92** (VCMS) and **C110213 Battery Voltage Low**,
   with a handwritten quote of ~$1,040 / 4 hrs to diagnose. A January 2026
   event absent from the timeline — confirm its significance (it may
   strengthen the recurrence narrative between Offer 2 and the Feb 18 event).

**Re-verified from the ROs (Respondent's own records):** RO #358530 — status
"VEH. DISABLED," opened 03APR25 10:59, READY 05AUG25 16:18, mileage
8,148→8,151 (+3 mi), = the 124-day anchor ✓. RO #356398 — 12FEB25, 7,026→
7,028 mi, recalls TCP / 272 (ICCU SW) / 9B5 ✓.

**Still missing vs. the arbitration record (user attaching next):** lease,
AG arbitration request/form, HMA offer letters, repurchase calc, Settlement
Agreement & Release, registration, Ex11 Days Out of Service.

---

## SESSION ADDENDUM 2 — 2026-07-18 (exhibits + email record ingested)

**Repo state.** `materials/exhibits/` now holds 28 files from Drive folder
"Hyundai Claude Code Project" (magic-byte verified; text in
`materials/exhibits/_extracted/`). Email record verified and summarized in
`materials/email_record_summary.md` (verbatim quotes + Gmail message IDs).
Law-firm research in `research/2026-07-18-law-firm-candidates.md`.

**RESOLVED — discrepancy 2 from Addendum 1 (second HV battery):**
`Ex04_Repair_Orders.pdf` is **md5-identical** to the 13-page RO set already
verified. **No second HV-pack-replacement RO exists in the arbitration
record.** The only HV pack replacement is RO #358530. The Feb 2026 event
(RO #370267) was a 12-volt battery. **Memo v2's "high-voltage battery was
replaced a second time" and the "two full HV battery replacements" row in
VERIFIED FACTS above must be revised before filing.** The strongest accurate
framing: same underlying electrical/battery defect recurred (P1BAD92 +
C110213 present on the Jan 8, 2026 Smart Diagnosis), vehicle stranded and
"TOO DEAD TO COMPLETE GDS," and Paramus confirmed on 2/19/26 the failure was
a warranty-covered defect (Hu→css email, verbatim in email summary).

**Verified against exhibit text this session:**
- Ex05 (Aug 18, 2025 offer): two options — keep car + **$4,000.00** cash, or
  repurchase, restitution **$7,977.00** ($5,024 payments + $2,953 down),
  mileage deduction "**WAIVED**" (formula recited "mileage at first report of
  concern **8151**"). ✓
- Ex06 (Jan 29, 2026 offer): keep car + **$5,000** cash, or repurchase,
  restitution **$5,388.51** with deduction **($4,326.49)** on cash price
  $53,360.77 × (**8148**−40)/100,000. ✓ ($598.71 overstatement math ✓.)
  ⚠ Both offers used RO-358530 mileage (8148/8151) as "first report" — the
  statutory first report is 7,026 (RO #356398). Useful for Argument 7.
- Ex09a (Aug 2025 Settlement Agreement): §1542 waiver (Cal. Civ. Code),
  confidentiality, indemnity clauses confirmed in text. ✓
- Ex08 pair: $2,500 conveyed only via Gorberg (Laura Wolfe email 5/11/26);
  consumer-built cover sheet states no standalone HMA writing exists. ✓
- Sept 30, 2025 Hu→HMA email (in Gmail; also relevant to Ex22): written
  pre-counsel objections to release scope / confidentiality / §1542.

**⚠ NEW halt-and-confirm items:**
1. **Duplicate exhibit slots in Drive:** Ex07_Repurchase_Calculated_Offer is
   md5-identical to Ex05, and Ex09b_Settlement_Agreement_Jan2026 is
   md5-identical to Ex06. If distinct documents were intended for Ex07/Ex09b,
   they are missing — confirm what was actually submitted to the arbitrator.
2. **Expense total conflict inside Ex21_Loss_of_Use_Record:** claims
   **$1,793.43** (citing Ex17 ledger) in one place and **$1,989.25** (citing
   the Expense Receipt Packet) in another. **RESOLVED 2026-07-19: user
   confirms $1,793.43 is correct.** Memo v3 already uses $1,793.43 ✓. The
   $1,989.25 sentence inside Ex21 remains wrong on its face — if Ex21 is
   ever re-served or refiled, correct it there.
3. **Missing from repo (transfer failed, >10MB or errors):** ~~Lease
   Agreement~~ **RESOLVED 2026-07-19** — user uploaded it directly; now at
   `materials/exhibits/Hu_v_HMA_Ex01_Lease_Agreement.pdf` (24,067,714 B,
   byte-size-identical to all 4 Drive copies). **Lease anchor figures now
   source-verified against the lease text layer:** date 05/23/2024 ✓,
   odometer at delivery 40 mi ✓, VIN ✓, lessor KOEPPEL HYUNDAI, 34-54 44th
   St, Long Island City NY ✓, $314.00/mo (due 23rd) ✓, cap-cost reduction
   $2,953.00 ✓, agreed value $53,360.77 ✓, gross cap cost $54,597.70 ✓,
   24-month term ✓. **Ex21 Expense Packet RESOLVED 2026-07-19** — uploaded
   directly (66 pp., 6.4MB) along with Ex21_RAP_Response and
   Ex21_Hyundai_Case_Management_42053079 (both new to repo; uploaded
   Loss_of_Use_Record was md5-identical to repo copy). **The packet's own
   cover states TOTAL $1,793.43, expressly reconciling to Ex17** (stated 3×)
   — so the $1,989.25 sentence inside Ex21_Loss_of_Use_Record is now
   source-refuted, not merely user-overridden. Packet covers incident period
   Jan 6 – Feb 20, 2026; Tab A (rentals) subtotal $1,237.81.
   **The repo's arbitration record is now COMPLETE — no missing documents.**
4. Aug-2025 "sent to wrong email" note (offer trajectory table above) is not
   corroborated by the email record — the 8/18/25 offer email went to
   jimmy.hu@gmail.com (it may merely have skipped the inbox). Confirm or drop.

**Settlement-history precision (from email record — supersedes the coarse
trajectory table above where they differ):** 9/26/25 Hu accepted the $4,000
cash-keep option in principle ("Let's get started on next steps"); deal
failed solely on release terms (9/30/25 objections); HMA never responded
substantively in writing. Offer 2 (1/29/26) was stated "valid for 60 days"
(2/6/26 email) → lapsed ≈3/30/26 while Gorberg held the file; $2,500 came
via Gorberg 5/11/26; representation ended 5/12/26; arbitration filed
5/12/26 (Decision Letter "File Date").

**Memo of Law v3 produced** (`materials/Hu_v_HMA_Memo_of_Law_Article75_v3.docx`).
Changelog v2→v3: corrected the two record-contradicted assertions — Feb 2026
event now 11,230 mi / RO #370267 / battery replaced under warranty after
dealer confirmed warranty-covered defect (no "second HV replacement" claim);
"two complete HV battery replacements" → one HV pack replacement at recorded
cost $17,483.69; footnote 1 placeholder resolved (12-volt battery, part
00275-18001, with the award's own 8,662-mi error turned into a Point VI
exhibit); Point VI conflation passage now states both errors affirmatively.
XSD-validated against v2 (200 paragraphs unchanged). ⚠ LibreOffice is broken
in this sandbox (even v2 fails to convert), so pagination was NOT visually
re-verified — open in Word before filing. v2 retained for diff.

**Vehicle status (user-reported 2026-07-18):** still in Petitioner's
possession under the month-to-month lease extension; odometer **~15,000 mi**
(approximate — confirm exact reading before it enters any filing). Legal
effect: none on the refund math (statutory deduction runs from the 7,026-mi
first report), none on the merits (current operability irrelevant per
DaimlerChrysler), helpful on mootness (vehicle available for inspection).
Note: still under 18,000 mi — if any NEW battery/electrical event occurs,
get a dealer RO immediately; it would be within the statutory coverage
window. Attorney-outreach email drafts created in Gmail 7/18 (Bromberg,
Krukas, Kimmel & Silverman, Lemberg) — To-addresses are self-placeholders
pending verification of each firm's intake email (proxy blocked site
fetches; do not trust unverified addresses).

**⚠ Defensive prep — collision-damage angle:** right-headlamp damage existed
since 12/22/24; Mizzoni's Auto Body repair (self-pay, Ex16) 1/22–2/9/26;
Paramus initially floated the damage as possible cause of the Jan-2026
no-start; several Jan-8 DTCs (tail lamp, radar) are plausibly
collision-related. **Neutralizer (record-verified):** Paramus completed
diagnostics and confirmed warranty-covered defect, replaced battery
(RO #370267; Hu 2/19/26 email). Expect HMA to raise it; brief any counsel.

---

## SESSION ADDENDUM 3 — 2026-07-19 (adversarial review → Memo v4)

**Full adversarial review of Memo v3 run against the complete record**
(3 blockers, 12 should-fixes, 5 nits). **Memo of Law v4 produced**
(`materials/Hu_v_HMA_Memo_of_Law_Article75_v4.docx`; XSD-validated, 200
paragraphs unchanged; pagination still not visually verified — LibreOffice
broken in sandbox; open in Word).

**⚠ CORRECTIONS TO THIS BRIEF (source-refuted; trajectory table above is
superseded on these points):**
1. **There is NO California choice-of-law clause in the release.** Ex09a's
   only CA reference is the §1542 waiver "as well as any similar law of any
   state or territory of the United States." The award's "clause related to
   the state of CA" = the §1542 waiver. All filings must frame the objection
   around the §1542 unknown-claims waiver, never "choice of law."
   (The Jan-2026 release's contents are NOT in the record — Ex09b is a dup
   of Ex06 — so claims about "each" release's contents must be qualified.)
2. **The dispositive "no allegation" sentence sits in the SAME paragraph as
   the consumer summary it contradicts** (per the authentic award text
   layer), not "two paragraphs earlier." Same-paragraph is the stronger and
   accurate framing; Argument 2's description updated accordingly.
3. Offer-1 "sent to wrong email" — dropped (refuted); Offer-3 timing: Jan
   offer stated valid 60 days, lapsed ≈3/30/26; $2,500 conveyed via counsel
   5/11/26, no standalone HMA writing (Ex08 cover sheet).

**v3→v4 changelog:** removed wrong-email claim; reframed both
choice-of-law passages around §1542 (+"any similar law" quote); offer-3 row
and Point VII prose re-dated to the 60-day lapse and 5/11/26 $2,500 via
counsel; Feb-2026 sentence re-anchored to RO #370267 as the record source
(open date ≠ failure date); "failed repeatedly" opener replaced with
one-HV-replacement framing; Point II recitation now quotes the award's
actual words; "She observed" → "The award recites" (both spots); "manifest
disregard" recast; "sole stated basis" → "only stated reasoning" +
checkbox acknowledgment; Finding No. 2 → cited by language; 176 days
reframed as a span; 198–201 clarified as aggregate; "statutory formula" →
"formula recited in Respondent's own offers"; Point VII now leads with the
9/25/25 written acceptance + 9/30/25 three requested release edits +
HMA's refusal (all record-based, Ex22); Leonidou quote boundary fixed;
Riina "citing" parenthetical → "see also"; (b)(1) quote bracketed
"[the]"; footnote-1 warranty attribution moved to Ex22.

**⚠ NEW OPEN ITEM — the 12,000-mile deduction question (potential
$3,727.78 swing):** if official §198-a(c)(1) allows a use allowance only
beyond the first 12,000 miles, the statutory deduction at a 7,026-mi first
report is ZERO. Verify against official text before filing; see
`research/prefiling-verification-checklist.md` (which also lists every
case/statute quotation requiring Official Reports verification — the
sandbox proxy blocks all legal-text sites).

**⚠ Ex22 says RO #370267 "opened" 02/13/26; the RO document says 18FEB26
16:21.** v4 anchors on the RO document. Reconcile (likely: arrival 2/13,
RO opened 2/18) before HMA probes the inconsistency.

---

## SESSION ADDENDUM 4 — 2026-07-25 (filing mechanics resolved; Petition drafted)

**Deliverables added:**
- `materials/Hu_v_HMA_Verified_Petition_v1.docx` — 72 numbered paragraphs,
  five enumerated Grounds, WHEREFORE, CPLR 402 verification page, and an
  Index of Exhibits (A–L). XSD-validated (204 paragraphs).
- `materials/Hu_v_HMA_Notice_of_Petition_v1.docx` — CPLR 403(b) form,
  return-date and answering-papers demand, venue recital, service block.
  XSD-validated (62 paragraphs).
- `research/2026-07-25-filing-mechanics.md` — the procedural memo.
- ⚠ **LibreOffice is still broken in this sandbox** (control test fails on
  untouched files too). Neither filing has been visually paginated. **Open
  both in Word before filing.**

**RESOLVED — the three "WHERE TO GO FROM HERE" questions:**

1. **Caption / parties.** Name **HMA as sole respondent**. Do NOT name
   NYSDRA, the NY Peace Institute CDRC, the Attorney General, or the
   arbitrator. Bases: 13 NYCRR Part 300 has no appeal or party-designation
   provision (**§ 300.17 is "Recordkeeping"**, not appeals); CPLR 7511 runs
   on the application of "a party"; the award's own CONCLUSION says "a
   dissatisfied party … may seek judicial relief"; and both First Dept
   templates (*Leonidou*, *Riina*) are captioned manufacturer v. consumer,
   two parties only. Recommended non-jurisdictional courtesy copy to
   lemonlaw@nysdra.org.
2. **Venue.** New York County is proper under **CPLR 7502(a)(i)** — Petitioner
   resides at 320 W 38th St. Apt. 2427, New York, NY 10018 (address verified
   on both the award and the Decision Letter). First Department. ✓
3. **Service / return date.** CPLR 304 (commencement by filing); CPLR 402
   (petition must be verified); **CPLR 403(b)** — serve ≥8 days before the
   return date, ≥12 days if demanding an answer 7 days out (late service
   defeats jurisdiction); CPLR 403(c) — served like a summons. Corporate
   service: **BCL § 306** (Secretary of State) if HMA is an authorized
   foreign corporation, **BCL § 307** (extra mailing + affidavit of
   compliance) if not. Index fee $210, RJI $95, file ≥5 business days before
   the return date. **Use a licensed process server — a party may not serve
   his own papers.**

**⚠ OPEN — the only thing blocking service:** run "Hyundai Motor America" on
the NY DOS Corporation and Business Entity Search (or call (518) 473-2492) to
get (a) authorized/unauthorized status, (b) state of incorporation — currently
bracketed in Petition ¶ 6, (c) the DOS process address, (d) any registered
agent. Hyundai *Capital* America is a different entity; do not reuse its agent.

**⚠ MILEAGE DEDUCTION — near-resolved, in Petitioner's favor.** Three
independent search renderings define the statutory "mileage deduction
formula" as mileage **"in excess of twelve thousand miles"** × price ÷
100,000. If confirmed, the deduction at a 7,026-mile first report (and at
HMA's erroneous 8,148-mile basis) is **$0.00** — HMA's $4,326.49 deduction
was wholly unauthorized, not merely overstated by $598.71, and Memo v4
concedes $3,727.78 that is not owed. **Not written into any filing** (Prime
Directive); the Petition carries a bracketed drafting note instead. The one
remaining step is reading § 198-a(a) and (c)(1) in the official text — the
sandbox proxy 403s every legal-text host. See
`research/prefiling-verification-checklist.md` § 3.

**Memo v4 is now behind the Petition on two points** (the mileage deduction,
and the § 300.17/caption research). A v5 should follow once the statutory
text is confirmed.

---

## SESSION ADDENDUM 5 — 2026-07-27 (attorney case summary v3)

User reports the outreach e-mails to the lemon-law firms have been **sent**.
Deliverable added for the reply: `materials/Hu_v_HMA_Attorney_Case_Summary_v3.docx`
— a **one-page** briefing sheet to attach when a firm responds. XSD-validated
(17 paragraphs). Times New Roman 9.5 pt, 0.65" margins, 0.9 leading; layout
sized to ~93% of one US-Letter page **by calculation, not by visual
pagination** (LibreOffice still broken in this sandbox) — open in Word and
confirm it holds to one page before sending.

**v2→v3 changelog** (v1/v2 were produced in the pre-repo claude.ai sessions and
are not in this repo): rebuilt from the current verified record. Now reflects
**one** HV pack replacement (RO #358530), not two; frames the release objection
as the **Civil Code § 1542 unknown-claims waiver**, not a California
choice-of-law clause; states the September 2025 acceptance-in-writing and that
the deal died on release terms rather than price; anchors the Feb-2026 event
away from the award's conflated "RO 363888 / 8,662 mi"; adds a candid
"WHAT CUTS AGAINST ME" section (current operability, remittal-not-judgment as
the likely remedy under CPLR 7511(d), the headlamp collision damage, pro se
posture). Fee-shifting is stated with its scope flagged as to-be-confirmed,
consistent with `research/prefiling-verification-checklist.md` § 4. The
mileage-deduction question is **not** mentioned — it stays gated.

**v3→v4 (2026-07-27, same session) — tone.** User's direction: the summary is
a request for help, not a set of instructions to counsel; protect the
attorney's judgment and ego. v4 reframes every conclusion as the user's own
reading, offered subject to the lawyer's judgment — "WHAT MY RESEARCH
SUGGESTS — subject entirely to your judgment," bullets recast as "appears
to," "may rest on," "you may weigh them differently, or set them aside." The
drafted petition/memo are now expressly offered as "a starting point, not a
prescription," with an explicit statement that counsel is free to rewrite or
discard them. Adds an invitation to be told the case is not viable, defers
valuation ("no firm view of what the matter is worth"), and closes on the
distinction between reading cases and practicing law. **No factual content
changed** — same figures, dates, RO number, quotations, and citations, except
that the Gurau pinpoint cite and two minor details were dropped for space.
Set in 9 pt / 0.55" margins; ~90% of one page by calculation. v3 retained.

**v4→v5 (2026-07-27) — two pages, detail restored.** User lifted the
one-page constraint. v5 (`materials/Hu_v_HMA_Attorney_Case_Summary_v5.docx`,
XSD-validated, 19 paragraphs) keeps v4's deferential voice verbatim and
restores the evidence that had been cut for space, plus material never in
v3/v4:
- **New THE FEBRUARY 2026 RECURRENCE section** — the Jan 8, 2026 Smart
  Diagnosis (7 DTCs incl. P1BAD92 and C110213), the Feb 18 no-start at
  11,230 mi, RO #370267's "VERIFIED NEEDS JUMP TO START. TOO DEAD TO
  COMPLETE GDS," and an **affirmative disclaimer** that this was the 12-volt
  battery and not a second HV pack (inoculates against the award's
  conflation and against any impression of overclaiming).
- **New THE AWARD section** quoting the arbitrator's reasoning in full —
  backorder parts / free loaner / "no guarantee … of a defect free car" /
  "[t]he manufacturer's argument is compelling" / the dispositive sentence.
- Restored: the Gurau pinpoint, the "RO 258530" and "RO 363888 mileage 8662"
  specifics, odometer 8,148→8,151, $17,483.69 warranty charges, $314/month
  and $53,360.77, the 7,026-vs-8,148 deduction-basis error, the sixty-day
  lapse, and the May 11, 2026 $2,500-via-counsel date.
- Added: "I am flexible on fee structure."
Set in 10.5 pt / 0.8" margins; ~91% of two pages by calculation (LibreOffice
still broken — open in Word). v3 and v4 retained. **The mileage-deduction
question remains out of the summary**, gated as before; it is the one live
option to add if the user wants counsel's read on it.

**v5→v6 (2026-07-28) — the mileage-deduction question, un-gated for counsel
only.** User directed that the deduction question be added to the summary.
`materials/Hu_v_HMA_Attorney_Case_Summary_v6.docx` (XSD-validated, 20
paragraphs, 10 pt / 0.8" margins, ~91% of two pages by calculation) adds:
1. **New section "ONE QUESTION I COULD NOT RESOLVE"** — the twelve-thousand-
   mile threshold, stated as a question and expressly not asserted ("I could
   not confirm the language against an official source, so I am not asserting
   it"), noting that if it holds the $4,326.49 was unauthorized rather than
   miscalculated. **This does not un-gate the point for filings** — the
   Petition's bracketed note and Memo v4 are untouched, and
   `research/prefiling-verification-checklist.md` § 3 now records the
   distinction.
2. **"Nothing has been filed: no proceeding is pending, and the ninety days
   have not run"** — counsel needs to know the posture is pre-commencement.
3. **The lease extension reframed as a mitigant** — the award itself records
   that the lease was extended to keep the car available for inspection,
   which cuts against a staleness/mootness objection.
Also dropped the duplicated pro-se admission from THE AWARD (it already
appears in WHAT I THINK CUTS AGAINST ME). v3–v5 retained.

---

## SESSION ADDENDUM 6 — 2026-07-28 (packet review → Petition v2, Notice v2, Memo v5)

Full cross-document review of the four deliverables before packet assembly.
Two blocking findings, both fixed; everything produced by XML surgery on the
prior version (paragraph counts unchanged: 204 / 62 / 200; all XSD-validated).

**⚠ BLOCKER 1 — RESOLVED: the "M.D." / "practicing physician" assertion was
unsourced.** It appeared **9 times** across three documents (Petition ×5
including the CPLR 402 verification page, Notice ×2, Memo ×2) and originated
in Memo v2 during the pre-repo claude.ai sessions. The only record support
anywhere is the award's "Consumer: **Dr.** Jimmy Hu" — and "Dr." does not
establish "M.D." A sworn verification is the wrong place for an unverified
credential, and it carried no legal weight: consumer status under
§ 198-a (a) turns on leasing for personal/family/household purposes, which
Petition ¶ 5 already alleges. **All nine occurrences removed, and the
sentence "He is a practicing physician." deleted from ¶ 5.** The caption
already read "JIMMY Y. HU" so the documents are now internally consistent.
If a credential is accurate the user may restore it; nothing depends on it.

**⚠ BLOCKER 2 — RESOLVED: the packet contradicted itself on the mileage
deduction.** Summary v6 raised it as possibly $0.00, Petition ¶ 68 bracketed
it, but **Memo v4 affirmatively conceded "the correct deduction is
$3,727.78" in three places** plus "an overstatement of $598.71." Memo v5
now: (a) offer-table cell states the 8,148-vs-7,026 basis error without a
figure; (b) the arithmetic block's bold label changed from "Overstatement:
$598.71" to "Difference attributable to the erroneous basis: $598.71";
(c) Point VII prose reads "computed the deduction from the wrong odometer
basis"; (d) Point VIII relief now reads "Applying to that basis the formula
recited in Respondent's own offers yields $3,727.78. Petitioner does not
concede that any allowance for use is authorized on these facts, and
expressly reserves the question whether the statutory formula permits a
deduction for mileage below twelve thousand miles." **No document in the
packet now concedes money that may not be owed**, and the reservation is
phrased to survive being filed as-is.

**Also fixed in Memo v5:**
- `(Ex. 22.)` → `(Ex. I.)` — the Memo had been citing arbitration exhibit
  numbers while the Petition cites Exhibits A–L. Now one system.
- "**Respondent declined to alter any term**" → "**Respondent did not agree
  to any of them**." The email record (Addendum 2) shows HMA *never responded
  substantively in writing*; an affirmative refusal overstated it. The new
  wording is true under either reading.

**Verified clean in review:** captions identical across all three filings;
all three carry DRAFT — FOR ATTORNEY REVIEW; Memo free of the retracted
"second HV replacement" and "California choice-of-law" claims; the Petition's
Exhibit A–L index maps correctly onto the files in `materials/exhibits/`.

**Known-and-accepted:** Exhibits K and L are indexed but never cited in the
Petition body (annexing an uncited exhibit is not an error); `[telephone]`
remains blank in the Notice (user to fill).

**New deliverable:** `research/2026-07-28-attorney-packet.md` — a three-tier
send plan (summary alone → record bundle → drafts), with an explicit
do-NOT-include list covering the Ex07/Ex09b duplicates, the
Ex21_Loss_of_Use_Record $1,989.25 contradiction, and the Mizzoni collision
invoice, plus the six items still open before filing.

**Superseded:** Petition v1, Notice v1, Memo v4 (all retained for diff).

---

## SESSION ADDENDUM 7 — 2026-07-28 (full-project review; brief reconciled)

Whole-workstream review, not just the filings. One structural defect found and
fixed, one research gap identified, one scheduling risk escalated.

**⚠ FIXED — this brief contradicted itself.** The top half still carried three
facts that Addenda 1–3 had already retracted, so a fresh session reading
top-down would pick up refuted material before ever reaching the corrections:
(1) "two full HV battery replacements" in VERIFIED FACTS; (2) the Feb-2026 row
still reading "~8,662 mi / RO UNRESOLVED"; (3) "**California choice-of-law
clause**" in the release paragraph, plus the refuted "sent to wrong email" note
and the superseded "~Apr 2026" rescission date. **All corrected in place with
pointers to the addendum that resolved each.** The DELIVERABLES table (which
still called Memo v2 current and told the reader to copy it into the project)
and the WHERE TO GO FROM HERE section (three questions resolved back in
Addendum 4) were replaced wholesale. The offer-trajectory table now also warns
against restating $3,727.78 as "the correct deduction."

**Lesson for future sessions:** append-only addenda work for an audit trail but
rot the head of the file. When an addendum retracts a fact, edit the fact where
it lives *and* log it below.

**⚠ NEW RESEARCH GAP — CPLR 306-b (service after filing).** Nothing in this
repo addresses how long after filing service must be made. Article 75's period
is 90 days — under four months — and 306-b is understood to impose a short
fixed window after expiration of such a period, rather than the 120 days that
apply to ordinary actions. If the petition is filed close to Sept 9, that
window could bind hard, and defective service on a foreign corporation is the
classic way these proceedings die. **Unverified — the sandbox proxy blocks
every legal-text host. Confirm before choosing a filing date.** Added to the
"WHERE TO GO FROM HERE" list above.

**⚠ SCHEDULING — the binding constraint is now the calendar, not the law.**
43 days to the deadline as of this review. Outreach went out 2026-07-27.
**Recommended decision date: ~August 17, 2026** — if no firm has engaged by
then there is no longer time to onboard one, and the choice collapses to filing
pro se or losing the claim. This is the user's call and is not being reopened;
it is flagged because the date is now close enough to matter.

**Verified sound in this review:** the 124-day anchor and its source; the
Petition/Notice/Memo captions; the Exhibit A–L index against the files on disk;
Memo v5's reservation of the deduction question; Summary v6's affirmative
12-volt disclaimer. No new factual errors found in the four current documents
beyond those fixed in Addendum 6.

---

## SESSION ADDENDUM 8 — 2026-07-29 (Krukas engaged; ARBITRATION FORM READ FOR THE FIRST TIME)

**Counsel contact.** Eugene Krukas (Lemon Freedom, (516) 203-4001) called
2026-07-28, was sent the award, and replied 2026-07-29 02:07 UTC: *"from my
perspective, the decision is insane… The only argument about days is that back
ordered parts are a challenge in the industry… it's exactly the sort of thing
that the state lemon laws are meant to address."* He asked for **the Repair
Orders and the Request for Arbitration Form**, and looped in his partner
**Michael Vicario (mvicario@lemonfreedom.com)**, who "handled the litigation
end of things." Gmail draft prepared in the thread (reply to message
19fabaab5a59a645); **attachments must be added by hand** — the draft tool does
not support them.

**`materials/exhibits/Hu NC-1-1249605441.pdf` IS the Request for Arbitration
Form.** It had never been read in any prior session — the text layer is
symbol-mangled and the checkbox states are not recoverable from it. Read
visually this session. Case No. NC-1-1249605441, referred to NYSDRA 5/5/26,
Filing Date 5/12/26.

**⚠ FINDING 1 — Q16 CONTRADICTS THE FILINGS' FIRST-REPORT DATE.** The form's
Q16 ("On what date and at what mileage did you **first** report this
problem(s)?") reads **04/03/2025, mileage 8148** — not February 12, 2025 at
7,026 miles. **This is Petitioner's own filed statement to the AG program, and
it is why Hyundai used 8,148 in both offers.** Consequences:
- Memo v5 Point VII ("computed the deduction from the wrong odometer basis")
  and Petition ¶ 68 ("must be measured from 7,026 miles") are **materially
  weakened**; as drafted they put Petitioner in conflict with his own filing.
- RO #356398 (2/12/25, 7,026 mi, incl. Recall 272 ICCU) is real and is in the
  record; whether it is a "first report" of the *same* nonconformity is
  arguable — but it is now an argument, not an anchor.
- **The 124-day anchor is UNAFFECTED**, and is in fact corroborated: 4/3/2025
  is the first day of RO #358530.
- **Do not revise the filings until the user decides how to reconcile this.**
  Halt-and-confirm.

**✔ FINDING 2 — Q15 CORROBORATES GROUND II.** Q15 ("Does the problem(s) for
which you seek relief substantially impair the value of the vehicle to you?")
is checked **YES**. The award's dispositive sentence says there was "no
allegation that the use and value is impaired." **The initiating document in
the arbitrator's own file alleges exactly that**, in the program's own words.
This is stronger corroboration than the same-paragraph contradiction the Memo
currently relies on, and should be added to Ground II / Memo Point II.

**Other form data (all new to the project):** Q5 date of delivery **05/22/24**
(the lease says 05/23/2024 — reconcile); current mileage at filing **12,800**;
Q10 purchase price **$54,597.40** (cf. gross cap cost $54,597.70 — 30¢ off);
Q6 purchased/leased in NY **Yes**; Q7 registered in New York **No**; Q8
personal/family/household **Yes**; Q14 problem part: "car battery system."
Lessor: Hyundai Lease Titling Trust, Lease Acct #2415627694.

**Lesson:** the arbitration form was sitting in `materials/exhibits/` under a
non-obvious filename (`Hu NC-1-1249605441.pdf`) and its OCR text is unusable,
so seven sessions of verification never touched it. **Any exhibit whose
extracted text is symbol-mangled must be read visually before the record is
called "complete."**

---

## SESSION ADDENDUM 9 — 2026-07-29 (Attorney Case Summary v7 — deference pass)

**Health check run** (`/doctor` equivalent — the built-in command does not run
in a non-interactive remote session). Claude Code 2.1.220; branch
`claude/install-orchestration-drjo97` clean and level with origin at `8513c74`;
30 GB free; 31 exhibit PDFs present; all four Word deliverables XSD-valid
(Summary 20 ¶¶ / Petition 204 / Notice 62 / Memo 200). `claude mcp list`
reports no servers — expected, the remote harness injects them rather than
using local config. Nothing was broken and nothing needed committing.

**v6→v7 (user direction: "less authority and more deference … we are not
lawyers and cannot tell the attorneys what to do").**
`materials/Hu_v_HMA_Attorney_Case_Summary_v7.docx`, XSD-validated, 22
paragraphs, 10 pt / 0.75" margins, **~94.5% of two pages by calculation**
(tighter than v6's 84% — the disclosure paragraph and the split of the
standard-of-review discussion cost roughly a page-third; **open in Word**).

Register changes:
- The four analytical bullets are now **questions**, not assertions —
  "Does the award contradict itself?", "Does the 'currently operating'
  rationale hold up?", "Did the findings ever reach the thirty-day claim?",
  "Do the errors in the award amount to anything?" — under a new heading
  **"THINGS I NOTICED, PUT AS QUESTIONS"** that invites counsel to call them
  naive.
- Case law pulled out of the argument and quarantined in its own section,
  **"ON THE STANDARD OF REVIEW — offered only so you know where I got the
  idea,"** which states outright: "I cite them only so you can see my
  reasoning and correct it, not as authority for anything." Pinpoint cites
  dropped (75 NY2d 175; 33 AD3d 1149; 7 NY3d 653) — a pinpoint reads as a
  claim to have shepardized.
- "I am not a lawyer. Everything below the facts is guesswork by someone who
  has read too much and practiced nothing" added to the opening.
- § 198-a(d)(2) recast from "As I read [it], thirty cumulative days …
  triggers the presumption" to "My understanding is that § 198-a(d)(2) works
  off a thirty-day threshold, and you will know that provision far better
  than I do."
- Closing line now separates the two registers explicitly: **"The facts I
  stand behind. The analysis is a layman's."**

**⚠ SUBSTANTIVE ADDITION — the Q16 conflict is now disclosed in the summary.**
New section **"AN INCONSISTENCY IN MY OWN PAPERS — please see it from me
first"** states that the Request for Arbitration Form answers the
first-report question **04/03/2025 at 8,148 miles** while RO #356398 is dated
**02/12/2025 at 7,026 miles**, that both are in the file, that Petitioner has
**not** attempted to reconcile them, and that it likely explains Hyundai's use
of 8,148. This is a **disclosure, not a resolution** — it does not pick a
reading and so does not violate halt-and-confirm. Rationale: the form is one
of the two documents being sent to Krukas, so the conflict was going to
surface within minutes; a summary that asserted 7,026 as "the" first report
alongside it would have looked either careless or evasive.

Consequently **SETTLEMENT HISTORY no longer says the January deduction was
computed "rather than the 7,026 miles at which I first reported the defect"** —
it now says only that the deduction was "computed from an 8,148-mile reading."
The characterization was the overclaim; the figure is not.

**Still untouched pending the user's decision:** Petition ¶ 68 ("must be
measured from 7,026 miles") and Memo v5 Point VII ("computed the deduction
from the wrong odometer basis"). Those are Tier-3 documents and are not in
the Krukas send.

v3–v6 retained for diff. The packet plan and the Krukas draft-email note now
point at v7.

---

## SESSION ADDENDUM 10 — 2026-07-29 (Krukas substantive reply; the November 23 lease wall)

**Counsel's second reply** (ekrukas@lemonfreedom.com, 7/29/26 12:18 UTC, cc
mvicario@lemonfreedom.com) — seven numbered points. Four corroborate the
existing analysis; **two attack the case on posture and economics, not merits.**

**⚠ NEW HARD DEADLINE — the lease cannot outlive November 23, 2026.**
`Ex15_Lease_Extension_Agreement.pdf` was **read for the first time this
session** (extracted text had been on disk since 7/18 but never opened).
Verbatim: extension letter dated **May 22, 2026**; "**Maximum Months Extended:
6    Maximum Maturity Date: 11/23/2026**"; month-to-month at **$314** due the
23rd; early-termination provisions do not apply between Original and Maximum
Maturity Date. **This is a second clock and it was not in the project's model
of the case.** Recorded in VERIFIED FACTS and under the filing deadline above.

**⚠ Krukas's two adverse points (do not paper over these):**
1. **Standing after the lease ends.** The lease was already in extension at the
   arbitration. Case law on maintaining a claim after the vehicle is returned
   at lease end is *"far from settled law"*; he warns against handing HMA an
   extra issue in dispute. **Buying the vehicle out** is the identified
   preservation option — he notes it complicates any repurchase calculation and
   is "throwing more good money after bad." **UNDECIDED — the user's call.**
2. **Economics.** He rated the exposure off `24 × $314 = $7,536` and doubted it
   justifies a ~$5,000 fee against only possible court-ordered reimbursement.
   **His figure was low** — see the correction below.

**✔ Krukas corroborates, unprompted:** *DaimlerChrysler v Spitzer* forecloses
the condition-at-hearing standard (his ¶6 = our Argument 3); § 198-a(e) does not
excuse supply shortages (his ¶7 = our Argument 5); **the Request for Arbitration
Form never alleged 4+ repair attempts**, so he "question[s] why the arbitrator
added that as an issue in dispute" (independent support for Argument 4, the
disjunctive-prongs point); and **RO #358530 "should be sufficient to justify a
LL repurchase 100% of the time."** Also: *"this arbitrator has no business
handling such matters."*

**⚠ THE TWELVE-THOUSAND-MILE QUESTION — practitioner confirmation, NOT official
text.** Krukas, unprompted: *"In NY you wouldn't be charged usage on the first
12,000 miles — so the usage offset in your settlement discussions should have
been nothing or almost nothing."* This is a practicing NY lemon-law attorney
independently stating the reading the project could not verify (proxy 403s every
legal-text host). **It does NOT clear the Prime Directive on its own** — the
official § 198-a(c)(1) text is still unread, and no filing may assert it yet.
Consequence if it holds: HMA's **$4,326.49** January deduction was *unauthorized*,
not merely computed from the wrong odometer basis. Memo v5's reservation was
drafted correctly and needs no change. `research/prefiling-verification-checklist.md`
§ 3 remains open.

**✔ Q16 disclosure vindicated.** Krukas built his ¶2 partly on the mileage-basis
conflict volunteered in the 7/29 email and Summary v7. Disclosing it bought
credibility rather than costing it.

**⚠ ECONOMICS CORRECTED (new, computed from Ex19 this session).**
`Ex19_Lease_Payment_History.pdf` (Hyundai Motor Finance, statement dated
6/2/2026) — 46 payment rows across **25 distinct due dates, 05/23/2024 through
05/23/2026**, each $314.00 split **$297.26 base + $16.74 sales tax**, totalling
**$7,552.74**. Plus the **$2,953.00** cap-cost reduction = **≈$10,505.74**, plus
extension payments since, plus **$1,793.43** incidentals ≈ **$13,000** — not the
$7,536 Krukas assumed. ⚠ "Amount Funded **39,958.70**" appears on the history and
**does not reconcile** to agreed value $53,360.77 / gross cap cost $54,597.70
less the $2,953 reduction. **Do not assert how the $7,500 federal credit was
handled** — unresolved; the lease was sent to counsel to speak for itself.

**Reply drafted** in thread `19faaa4dcaaeaca8` (reply to message
`19fadcff2f7f22b7`, draft id `r2391943105547565973`): thanks for the informal
agreement; explains **leased in NY / registered in NJ because Petitioner resides
in Manhattan and commutes to work in New Jersey**, with all service at Paramus,
and notes the form disclosed it (Q6 Yes / Q7 No) and the program arbitrated
anyway; gives the corrected money figures; states the 11/23/2026 wall; asks for
a fee structure or a plain no. **Attachments must be added by hand** — the Gmail
connector cannot attach. ⚠ `Ex01_Lease_Agreement.pdf` is **23.0 MB**, at the edge
of Gmail's 25 MB post-encoding limit; expect Gmail to convert it to a Drive link.

**Lesson (second time this pattern has cost us — cf. Addendum 8):** an exhibit
whose text sat extracted-but-unread for eleven days contained a hard deadline.
**Extraction is not reading.** Before the record is called "complete," every
exhibit needs eyes on its substance, not just a successful text dump.

---

## SESSION ADDENDUM 11 — 2026-07-29 (how the buyback actually died; the § 198-a(n) hook)

**User-confirmed fact, new to the project:** the August 2025 buyback did not
lapse into silence. Sequence, now recorded in the release paragraph above and
in Argument 7:

| Date | Event | Source |
|---|---|---|
| 8/18/2025 | HMA offers repurchase ($7,977.00, mileage deduction **waived**) **or** $4,000 cash-keep | Ex05 ✓ |
| 9/25–26/2025 | **Hu accepts in writing** ("Let's get started on next steps") | Gmail ✓ |
| 9/30/2025 | Hu sends **three requested edits** to the release (§1542 waiver, scope, confidentiality) | Gmail ✓ |
| 9/30/2025 | **HMA css replies the same day asking for "best time to call"** — and never answers substantively in writing | `materials/email_record_summary.md` line 17 ✓ |
| on that call | **Hu is told the buyback terms are "not negotiable."** | **Hu's testimony — UNDOCUMENTED** |

**Evidentiary posture — do not overstate.** The call is Petitioner's own
recollection; there is **no writing memorializing it**. What *is* documented is
HMA's same-day email moving the conversation to the phone, and the absence of
any substantive written response. Filings and correspondence may say **what Hu
was told**; they may **not** assert as fact that HMA's position was
non-negotiable.

**Why this matters — the § 198-a(n) hook.** The arbitrator treated Petitioner's
refusal of offers as weighing against him. The record now shows he **accepted**
and that the deal died on a **notarized §1542 unknown-claims waiver** (plus
confidentiality and indemnity) presented take-it-or-leave-it. If § 198-a(n)
voids waivers of rights under the section, HMA conditioned a statutory remedy on
a term it could not lawfully demand, and the award's use of the "refusal" rests
on that unlawful condition — an improper basis, not merely an unfair one.

**⚠ § 198-a(n)'s TEXT HAS NEVER BEEN READ.** It has been asserted since the
pre-repo sessions on the same unverified footing as (c)(1) and (l). New
`research/prefiling-verification-checklist.md` **§ 2a** records what must be
confirmed: the exact scope of what is void, whether it reaches a **pre-suit
settlement release** as opposed to warranty/contract terms only, and whether any
case law applies it that way. **No filing may assert (n)'s scope until then.**

**Also corrected this session:** the user's initial framing of the objection as
a waiver of "rights in California, which didn't apply" is **refuted by Ex09a**
and would have cost credibility with counsel. Clause (j) reads: *"Releasor
specifically waives section 1542 of the California Civil Code, **as well as any
similar law of any state or territory of the United States**."* It is an
unknown-claims waiver reaching every state's equivalent — not a choice-of-law
provision, and not inapplicable. This is the third time the "California" reading
has had to be corrected (cf. Addendum 3). **The accurate framing is the stronger
one:** Petitioner declined to sign away claims he did not know he had.

**Krukas reply draft** updated accordingly (thread `19faaa4dcaaeaca8`; draft id
rotated to `r-7536188808672574741`). It now opens with why the repurchase did
not close, corrects the California characterization in Petitioner's own voice
before counsel finds it, states the evidentiary gap on the call, and closes by
asking Krukas what **he** would do in Petitioner's position. Reply requested by
**August 7**.

---

## SESSION ADDENDUM 12 — 2026-07-29 (Krukas reply finalized; prior counsel disclosed)

**The reply draft was restructured and is final** (thread `19faaa4dcaaeaca8`,
draft id `r-7536188808672574741`). Order now tracks Krukas's own numbered
points — registration (his ¶2) → the NJ question → lease wall (¶4) → the money
(¶5) → why the repurchase didn't close (¶3) → prior counsel → asks. The NJ
question was moved **up**, ahead of the defensive material, because it is the
item most likely to change his answer. **No reply date is set** (user's
direction: counsel has been prompt without being asked).

**⚠ NEW DISCLOSURE — the Gorberg representation is now on the record with
counsel.** It had never been mentioned to Krukas. Verbatim anchors from
`materials/email_record_summary.md`:

| Date | Event | Verbatim |
|---|---|---|
| 2026-02-25 | Hu signs Authorization to Represent | — |
| 2026-02-26 | Gorberg (jackie) → Hu | *"Based on our review we have confirmed that you have a valid claim for damages and are now representing you in this matter."* |
| ≈2026-03-30 | HMA's Offer 2 lapses **while Gorberg holds the file** | — |
| 2026-05-11 | Laura Wolfe, Esq. → Hu | *"David indicated that the best we can do is resolve the claim for $2500, plus HMA pays our legal fee in addition."* |
| 2026-05-12 | Hu → Wolfe | Declines; *"Since David does not want to file, and is dropping this case, I ask that you release me…"* |
| 2026-05-12 | Wolfe → Hu | *"HMA has been advised we no longer represent you."* Arbitration filed same day. |

**Why disclosing helps rather than hurts:** a second firm confirmed **in
writing** that the claim was valid, then declined to litigate it and proposed a
$2,500 exit **with its own fee paid by HMA on top**. Petitioner's refusal was
that $2,500 was *less than HMA had offered before Gorberg was retained* — which
is a sound judgment, not a stubborn one. The email states the assessment and the
recommendation "pointed in different directions" and leaves the inference to
counsel.

**Three accuracy fixes in the same pass:**
1. *"I accepted in writing"* → *"I accepted **the cash option** in writing"* —
   the record shows Hu accepted the **$4,000 cash-keep**, not the repurchase.
   The old wording read as though he had accepted the buyback.
2. *"I intend to file by September 9 either way"* → *"I would rather preserve
   the claim imperfectly than lose it cleanly, and I'll file pro se if it comes
   to that."* The original asserted a decision the user **has not made** — pro
   se vs. counsel remains open and is his call.
3. § 198-a(n) **deliberately omitted** from the email. Its text is still
   unverified (checklist § 2a); floating an unverified statutory theory at a
   practitioner costs credibility. The underlying facts are all in the email, so
   counsel can reach the argument independently.

**Still true and unchanged:** attachments must be added by hand (the connector
cannot attach); `Ex01_Lease_Agreement.pdf` at 23.0 MB will likely be converted
to a Drive link by Gmail.

**⚠ WHY THE LEASE WAS EXTENDED — new, and it matters (user recollection,
2026-07-29).** The extension was **not** a drift into month-to-month. Hu took it
**on Gorberg's advice**, because Gorberg told him the vehicle would need to
still be in his possession when anything was filed. **Krukas's ¶4 standing
concern was therefore reached independently by prior counsel months earlier.**
Two consequences: (a) the award's recital that the lease was extended to keep
the car available for inspection is corroborated by the reason it was actually
done; (b) any mootness/staleness answer can say the preservation step was taken
deliberately on legal advice, not by accident.

**Why Gorberg declined — business model, not merits (user recollection, same
call).** As Hu understood him: the firm's work is mostly **quick pre-suit
settlements**, and once Gorberg saw HMA had already made **two repurchase
offers**, he did not regard this as that kind of case. He was not available for
further discussion; the $2,500 came through the office.

**⚠ EVIDENTIARY STATUS — UNDOCUMENTED.** Both points above come from **one brief
phone conversation** and there is **nothing in writing** behind either. Same
posture as the 9/30/2025 HMA call (Addendum 11). Filings and correspondence may
state **what Hu was told and what he understood**; they may **not** assert
Gorberg's reasoning as fact. The Krukas email is phrased that way ("what follows
is my understanding of it with nothing in writing behind it").

**Strategic read:** this materially *improves* the Gorberg disclosure. A firm
declining because a case does not fit its quick-settlement model is a very
different signal from a firm declining on the merits — especially alongside its
own written "we have confirmed that you have a valid claim for damages." The
email now carries both halves and the reason, and adds one line to THE LEASE
WALL section ("I took the extension on prior counsel's advice, for the same
reason you raise") so counsel's ¶4 is answered where he raised it.

---

## SESSION ADDENDUM 13 — 2026-07-29 (the body-repair precondition — documented, and previously unused)

**⚠ MATERIAL FINDING. This was sitting in `Ex22_Communication_Log` and no prior
session used it.** The user's recollection ("Hyundai wanted unrelated body damage
repaired before the repurchase") is **corroborated by the log itself**, in the
log's own analytical language:

| Date | Ex22 entry (verbatim fragments) |
|---|---|
| 10/03 & 10/14/2025 | HMA "moving toward repurchase"; requests current mileage + Aug/Sep payment history |
| **10/14/2025** | HMA asked about "the **status of vehicle body repairs**" — Ex22: "**the first appearance of the body-repair condition tied to closing the deal**" |
| 10/17/2025 | Hu reports a **new** EV issue — charging Level 1 only; will need to return the car |
| **10/24/2025** | Hu "was completing **rear bumper** body repairs and would return the vehicle once those were done" — Ex22: "**corroborating that body work had become a precondition to executing Offer #1**" |
| **11/05/2025** | HMA unable to reach Hu; "**Offer #1 was never executed before the second failure event**" |

**Why it matters.** The award and Respondent both lean on Petitioner having
"refused" offers. The record now shows the August 2025 repurchase did not fail on
price or on Petitioner's refusal — **HMA gated it on repairing unrelated
collision damage**, and the reason that damage sat unrepaired was that the
vehicle was **disabled at Paramus from April 3 to August 5, 2025** (RO #358530).
Then the battery failed again in January 2026 and the next offer dropped to
$5,388.51, then $2,500. **This strengthens Argument 7 substantially and is fully
documented** — unlike the 9/30/2025 call.

**⚠ TWO SEPARATE BODY-DAMAGE EPISODES — do not conflate (this resolves an
apparent conflict):**
1. **Rear bumper** — the item gating Offer #1; underway 10/24/2025. **No
   completion date is in the record.** The user recalls November 2025;
   **unverified — do not assert it.**
2. **Right headlamp** — `Ex16_Mizzoni_Auto_Body_Invoice`, a **Preliminary
   Estimate dated 1/13/2026**, inspection **01/09/2026**, repair **1/22–2/9/26**,
   self-pay. This is the one Paramus floated as a possible cause of the January
   2026 no-start.
   The prior defensive-prep note (Addendum 2) treated the collision damage as a
   single headlamp item. **It is two items, months apart.**

**⚠ INSURANCE INVOLVEMENT — partly corroborated.** Hu's 9/30/2025 release
objections cite an "insurance claim" among the confidentiality problems, and on
**1/22/2026** HMA's css asks for "any updates from the insurance company
regarding the approval needed to move forward with the diagnosis or repair." So
an insurer was in the loop in both episodes. **The Mizzoni estimate itself has
Policy #, Claim #, and Insurance Company all blank**, and Addendum 2 recorded the
Mizzoni repair as self-pay. **Which episode ran through insurance and which was
self-paid is UNRESOLVED — halt and confirm before either enters a filing.**

**Krukas email updated accordingly.** ⚠ Draft id superseded — see Addendum 14
for the send-ready draft. It uses only the documented October dates, asserts
**no** completion date for the bumper work, and closes the section: "the buyback
ended up gated on body work, and the reason that work had not already been done
was that the car spent four months disabled at the dealership. I don't know
whether that matters legally."

**⚠ GMAIL TOOLING LESSON.** `update_draft` has **no `replyToMessageId`
parameter** — only `create_draft` does. Editing a reply draft therefore **strips
its threading** and silently moves it to a new thread. This happened here and
went unnoticed for six revisions. **Any revision to a reply must be a fresh
`create_draft` with the reply ID.** There is no delete-draft tool in this
connector, so superseded drafts must be trashed by hand.

---

## SESSION ADDENDUM 14 — 2026-07-30 (state reconciliation before /clear)

**Read this addendum first. It supersedes draft ids and adds analysis that exists
nowhere else in the repo.**

### THE KRUKAS EMAIL — SEND-READY, NOT SENT

| | |
|---|---|
| ⚠ **OBSOLETE — see Addendum 17** | every draft before `r2138320854833607067` replies to a superseded message. **Do not send any of them.** |
| Delete by hand | `r-7536188808672574741` — **orphaned onto thread `19faf39d09d78f0a`** (earlier superseded drafts already cleared) |
| Attach by hand | `Ex01_Lease_Agreement.pdf` (**23.0 MB** — Gmail will likely convert to a Drive link), `Ex15_Lease_Extension_Agreement.pdf`, `Ex19_Lease_Payment_History.pdf` |

**Final structure** (restructured 2026-07-30 on user direction — "keep them
interested and enticed … and ultimately end on the same point"): thanks →
attachments → registration → **NJ question** → lease wall → numbers → why the
repurchase didn't close → prior counsel → *"there is a good deal more in the file
than I have put in front of you … I'll send whatever is useful and won't send
anything that isn't"* → limited-scope offer folded in → **the closing question
standing alone** → *"There is no need to answer everything, or quickly."*
**The multi-question list was deliberately CUT.** Questions read as homework; the
facts are the hook, and the closing question must be the last thing read.

### ⚠ READ OF COUNSEL'S POSTURE (assessment, not fact)

Krukas's 7/29 email is structured as a **soft decline**: ¶¶1, 3, 6, 7 agree with
the analysis; ¶¶4 and 5 are why he is unlikely to take it. His ¶3 tell —
*"If this was your first time contacting me (and the lease wasn't already in
extension), I would rate this a very strong case"* — is a lawyer explaining why
the case he wants is not the case in front of him. He proposed no fee, sent no
engagement letter, and asked for nothing further. **Do not build the plan on a
yes.** He has not formally declined and may yet engage; treat that as upside.

### ⚠ TWO QUESTIONS HELD BACK FOR THE NEXT EXCHANGE (deliberately not asked)

1. **How is HMA actually served in NY?** Authorized foreign corporation
   (BCL § 306, Secretary of State) or unauthorized (BCL § 307 + extra mailing +
   affidavit of compliance)? What address, what agent? **This is still the only
   open item blocking a filing**; the DOS entity search has been unrunnable for
   weeks (proxy 403s dos.ny.gov). A NY lemon-law practitioner would know it cold.
2. **Should anything be preserved before the car goes back on 11/23/2026?**
   Current dealer inspection, written odometer reading, statement from Paramus.
   **This has its own clock** — the battery, fault history, and odometer leave
   with the car, and after November they are gone permanently. Nobody has raised
   this in fourteen addenda.

A third, lower priority: does **§ 198-a(l)** fee-shifting reach an Article 75
proceeding? It is the direct answer to his own ¶5 economics objection.

### SETTLEMENT STRATEGY — new analysis, nowhere else in the repo

**Leverage: weaker than Aug 2025, not zero.** The 90-day window is open and a
filed petition costs HMA outside counsel and motion practice — plausibly more
than the claim is worth. HMA's own pre-arbitration valuation was **$7,977 with
the deduction waived**. Against that: an award "FOR THE MANUFACTURER," a lease
dying 11/23/2026, and no counsel on the letterhead.

**⚠ TWO POINTS NOT PREVIOUSLY IN THE FILE:**
1. **The "cash and keep the car" option is now meaningless.** Petitioner leases;
   the car goes back 11/23/2026 regardless. Any cash-keep offer is just cash.
   Do not let HMA frame it as a choice again.
2. **⚠ END-OF-LEASE CHARGES ARE UNQUANTIFIED AND ENTIRELY ABSENT FROM THE FILE.**
   Ex15 expressly preserves **disposition fee, excess wear, and excess mileage**.
   Any settlement must have HMA *and Hyundai Motor Finance* waive them and
   confirm no further lease obligation. **The lease's annual mileage allowance
   was never recorded** — at ~15,000 mi the mileage may be fine, but the
   disposition fee almost certainly applies. **Request a payoff/termination
   statement from HMF to quantify the exposure.**

| | |
|---|---|
| Ask | sums paid ≈ **$10,500** (payments $7,552.74 + down $2,953) + extension payments since + **$1,793.43** incidentals, **no usage deduction**, lease terminated, all end-of-lease charges waived |
| Justification | HMA's own Aug-2025 formula and its own waiver of the deduction, updated |
| Realistic landing | **$6,000–9,000** |
| Walk-away floor | **≈$5,000** — below that it is worse than the Jan-2026 cash offer already declined |

**Tactics.** (a) **Lead with the release terms, not the number** — the 2025 deal
died on the §1542 waiver, not price; state up front what will be signed (release
limited to this vehicle's battery defect, **no unknown-claims waiver**, no
indemnity, confidentiality narrow enough to permit disclosure to insurer, tax
advisors, counsel). (b) **Not customer service** — the case-manager tier only
re-issues templates and the award closed their file; send to HMA legal /
National Consumer Affairs escalation with the case number. (c) **Send when the
petition is finished, not before.** (d) A demand letter on counsel's letterhead
is exactly the narrow paid task the Krukas email already offers to fund.
(e) **Do not disclose that filing is undecided** — a demand only works if the
alternative is real.

### HOUSEKEEPING VERIFIED THIS SESSION

Branch `claude/install-orchestration-drjo97` clean and level with origin;
8 commits this session. All four Word deliverables XSD-valid (Summary v7 22 ¶¶ /
Petition v2 204 / Notice v2 62 / Memo v5 200). 31 exhibit PDFs. Claude Code
2.1.220 = latest published. No local settings files exist; no hooks; no MCP
servers in local config (this session's are harness-injected). Legal-text hosts
remain **403 by egress policy** — § 198-a(n), (c)(1), (l) and CPLR 306-b are all
still unread and unusable in a filing.

### ⚠ THIS FILE IS 1.9× THE LARGE-MEMORY WARNING THRESHOLD

76,016 chars ≈ **19,000 est. tokens loaded every session**; the 14 addenda are
**~72% of it**. A relocation of the addenda to a separate log was proposed
2026-07-30 — if it has not happened, it is still worth doing, because the
operative brief is the top ~338 lines and everything else is audit trail.

---

## SESSION ADDENDUM 15 — 2026-07-30 (the fee ask added to the Krukas reply)

**Draft `r2236505439958967567`** (thread `19faaa4dcaaeaca8`) supersedes
`r8063655648528527666`. Only change: a new **ON THE FEE** section, placed
immediately before the closing question, at the user's direction to "ask about
either a restructured fee or a limited scope engagement."

**Why it was added.** Krukas's ¶5 was one of his two adverse points: a ~$5,000
fee "with only the possibility of reimbursement by order of the court" against
what he believed was $7,536 at stake. The earlier draft corrected the money
(≈$13,000) but only offered limited scope, leaving his fee objection standing as
an unanswered obstacle. The section now converts it into two answerable
questions rather than a wall.

**Ask 1 — restructure the whole engagement:** contingency or hybrid; hourly with
a **cap** so exposure is defined; or an arrangement looking to fee-shifting if
fees are recoverable from HMA. ⚠ Phrased as a **question**, not a claim:
*"I genuinely don't know whether § 198-a(l) reaches an Article 75 petition rather
than only the underlying claim. You would."* **This is the correct posture —
(l)'s scope is still UNVERIFIED** (checklist § 4) and no filing may assert it.
It also surfaces the fee-shifting point that was previously held back, without
overclaiming.

**Ask 2 — narrower engagement:** review the drafted petition pre-filing; an hour
of consultation; **a demand letter to HMA over counsel's signature** ("nobody has
gone back to them since the award, and I suspect a letter from you would land
differently than one from me"); or a second look once something is on file and
has survived a first motion.

**Structure preserved.** The closing "what would you do if it were your car and
your money" question still stands alone as the final substantive item, followed
only by the no-deadline / no-pressure close. The fee section sits *before* it so
the email still ends where the user wanted it to end.

**Housekeeping.** `~/.claude/settings.json` created with
`permissions.defaultMode: "auto"` (user scope; reversible by deleting the key;
will not survive this ephemeral container). CLAUDE.md was reduced to ~5,700 est.
tokens by relocating these addenda here — see the commit `7bdf482` message.

---

## SESSION ADDENDUM 16 — 2026-07-30 (fee structures made concrete)

**Draft `r2412345025725400001`** supersedes `r2236505439958967567`. The ON THE
FEE section was rewritten from three generic options to **three named structures
the user proposed**, which are how lemon-law firms actually unbundle work. A
lawyer can answer these yes/no without first working out what is being asked.

1. **Reduced retainer against fee-shifting** — retainer sized to what the matter
   can bear, balance looking to **§ 198-a(l)** if fees are recoverable from HMA.
   ⚠ Still framed as a question, not a claim: *"I don't know whether that
   provision reaches an Article 75 petition rather than only the underlying
   claim. You would."* **(l)'s scope remains UNVERIFIED — checklist § 4.**
2. **Limited scope — counsel reviews and signs the petition and appears on the
   return date**; Petitioner does assembly, exhibits, service, legwork.
3. **Court appearance only** — Petitioner files pro se, counsel appears at the
   hearing.

Fallback if none work: an hour of consultation, or **a demand letter to HMA over
counsel's signature** (the cheapest yes available, and the highest-leverage
settlement move in the file — see Addendum 14).

**⚠ TWO FRICTIONS DELIBERATELY NAMED IN THE EMAIL RATHER THAN GLOSSED.** Both
were raised because a NY practitioner will think of them immediately, and
proposing around them would read as naive:
- **Signing is certifying.** An attorney who signs a filing in NY certifies it is
  not frivolous and that reasonable inquiry was made. "Just review and sign"
  understates the ask. The email says so: *"asking you to sign something I
  drafted means putting your own certification behind it, which is not a small
  thing,"* and invites him to rewrite or decline.
- **A limited appearance may not stay limited.** Appearing can put counsel on the
  record for the duration rather than the single date. The email raises this
  against its own interest and defers: *"That is entirely your call and I have no
  view on it."*

**Nothing else in the email changed.** Structure and the standalone closing
question are unchanged from Addendum 14.

---

## SESSION ADDENDUM 17 — 2026-07-30 (⚠ COUNSEL SAID YES — earlier read RETRACTED)

**⚠ RETRACTION.** Addendum 14 recorded an assessment that Krukas's 7/29 email was
a **soft decline**. **That was wrong.** He has since answered the closing
question directly and **offered to take the case.**

**⚠ ALSO: the thread moved on without the repo knowing.** The user sent his own
edited version of the reply on **7/29 23:13** (he cut the fee section), and
Krukas replied **twice** on 7/30. Every draft built between Addendum 12 and
Addendum 16 replies to a superseded message and **must not be sent.**

### What Krukas actually said (verbatim, msgs `19fb317867437cc9` and `19fb36be0e7a6e2f`)

| Point | Verbatim |
|---|---|
| **NJ is dead** | *"Having brought the NY arbitration, you would not be able to subsequently bring a NJ case due to **collateral estoppel**."* / *"NJ isn't an option due to collateral estoppel. The only option is to file the Article 75."* |
| **Merits** | *"I think it's a **winnable petition**.. but the lease extension ending soon worries me. You could win the petition and not be able to complete a LL repurchase anyway. As mentioned, there is some case law we could try to rely upon - but it's iffy."* |
| **His valuation** | *"By my rough count, should you win your case you would be entitled to **around $6,500**."* — materially below the ≈$13,000 gross in Addendum 14, because he nets out **rent charge under the NY statute** and **usage** |
| **His fee** | *"It's a **$5k attorney fee up front** for a chance to get back $6.5k and your attorney fee reimbursed. If it was like a 90% chance of winning it might be worth it - but **the odds are probably considerably less**. It probably comes down to **which judge you're assigned**."* |
| **⚠ THE ANSWER** | *"**If you want to do it anyway, I would be very happy to take the case. I don't like what this arbitrator did and it would bother me if nothing came of it.**"* |

**So the posture is a qualified yes:** he will take it, he thinks it is winnable,
and he is advising against it on economics alone. Asking what he would *actually*
do — rather than asking him to take the case — is what produced this.

### ⚠ CLOSED: the NJ track

`research/2026-07-29-nj-lemon-law-prelim.md` flagged two unresolved questions as
probably dispositive. **Question (a) is now answered: collateral estoppel bars
it.** The file should be treated as closed. No NJ work should be done.

### ⚠ OPEN AND MATERIAL: the $6,500 vs ~$13,000 gap, and a possible tension

Krukas nets to ~$6,500 citing **rent charge** and **"some usage now that we're
over 12,000 miles."** But his own 7/29 ¶2 said *"In NY you wouldn't be charged
usage on the first 12,000 miles — so the usage offset in your settlement
discussions should have been nothing or almost nothing."* Those may be
reconcilable (usage computed on **current** odometer rather than **first-report**
mileage) — **but it is not resolved, and it moves the number.** Posed to him as a
question, not an argument, in the reply below. **Do not assert either reading.**
**Rent charge (lease interest) as a deduction is also new to this file and
unquantified.**

### The live draft

✅ **SENT 2026-07-31 00:04 UTC** as message `19fb57cac5a84420` — see Addendum 23
for the text as actually sent. **No draft is pending.** Any remaining drafts in
this thread are dead and can be binned. Short and businesslike, matching his register now that the
long-form phase is over. It: accepts his framing; says the user is **inclined to
proceed** without committing to the $5,000; asks the three structures (reduced
retainer against § 198-a(l); limited scope — review, sign, appear; appearance
only, with the on-the-record-for-the-duration caveat named); asks the usage
question above; and offers the drafts *or* offers to withhold them.

**⚠ ALL EARLIER DRAFTS MUST BE DELETED BY HAND.** This connector has **no
delete-draft tool**; `apply_sensitive_message_label` needs *message* ids, drafts
do not surface in `get_thread`, and the orphan's thread `19faf39d09d78f0a`
returns "caller does not have permission."

### ⚠ THE DECISION IS NOW LIVE

Pro se vs. counsel is no longer abstract: **$5,000 up front, reimbursed only if
he wins, on odds he puts well below 90% and pins largely to judicial assignment.**
That is the user's call and his alone. Nothing in this repo should presume it.

---

## SESSION ADDENDUM 18 — 2026-07-30 (⚠ THE $5,000 IS DECLINED — position fixed)

**⚠ USER DECISION, RECORDED: he will NOT pay a $5,000 up-front retainer.**
Representation happens only on a restructured basis. This is a settled position,
not an opening bid — do not draft anything that presumes otherwise.

**Draft `r-2968709523769102880`** supersedes `r2138320854833607067`, which had
said *"I am inclined to go ahead … before I commit to the $5,000."* That framing
invited the reply *"the fee is $5,000"* and would have ended the conversation.

**The framing that replaced it — declining is AGREEING with him.** Krukas wrote:
*"Strictly speaking, from a financial perspective it doesn't make sense to pay
what we would charge."* So the email adopts his own analysis rather than
haggling:

> "I am not going to pay $5,000 up front. That is less reluctance than agreement
> with your own analysis: a $5,000 fee for a shot at $6,500, on odds you would
> put well under 90% and that turn substantially on which judge I draw, does not
> make sense."

**Three structures, each now asking for a NUMBER rather than a yes/no** — "what
would that cost?" instead of "is there an arrangement?":
1. **Fee looking to recovery or § 198-a(l) fee-shifting**, with or without a
   modest retainer. ⚠ (l)'s scope still **UNVERIFIED** — asked as a question.
2. **Limited scope at a reduced fee** — counsel reviews and signs the filing and
   appears on the return date; Petitioner does assembly, exhibits, service.
3. **Appearance only** — Petitioner files; counsel represents at the hearing.
   Includes the on-the-record-for-the-duration caveat.

**Explicit exit given:** *"If none of those work, I will file pro se and take my
chances… I would rather have a clean no than have you take something on terms
that don't work at your end."*

**⚠ REALISTIC READ (assessment, not fact).** Option 1 is the least likely — a
firm bearing fee risk on a petition counsel himself rates well under 90%, under
a provision nobody has read. **Options 2 and 3 are the likely landing zone**
because they cut his labour rather than his security. If a number comes back, it
should be materially below $5,000; if it comes back at or near $5,000, that is
effectively a no and **pro se is the path.**

**The usage question is retained and is the one item with money in it.** Krukas's
two emails reconcile only if usage runs on the **current** odometer rather than
**first-report** mileage; if it runs on first report (7,026 or 8,148 — both under
12,000), usage is **zero** and his $6,500 rises. **Neither reading may be
asserted.**

---

## SESSION ADDENDUM 19 — 2026-07-30 (tightened; drafts pending deletion)

**SEND `r8206308063604041995`.** Same position as Addendum 18, cut from ~450 to
~250 words. Krukas now writes five-line emails; a long reply invites skimming
past the three asks, which are the only part that needs an answer.

**What was cut:** the thank-you preamble, the expanded certification explanation,
the standalone "clean no" paragraph (folded into one line), and the closing
about moving early. **What was kept verbatim in substance:** the decline framed
as agreement with his own analysis; all three structures, each demanding **a
number**; the § 198-a(l) caveat as a question; the on-the-record-for-the-duration
caveat; the pro se fallback; and the usage question.

**⚠ SUPERSEDED DRAFTS AWAITING MANUAL DELETION** (no delete-draft tool in this
connector — see Addendum 17): `r-2968709523769102880`, `r2138320854833607067`,
`r2236505439958967567`, and the orphan `r-7536188808672574741` on thread
`19faf39d09d78f0a` if it still exists.

**Next inbound decides the path.** A number materially under $5,000 is a real
offer. A number at or near $5,000 is a polite no and **pro se is the path** —
at which point the blocking item is unchanged and unresolved: **how HMA is served
in New York** (BCL § 306 vs § 307; the DOS entity search has never been runnable
from this environment).

---

## SESSION ADDENDUM 20 — 2026-07-30 (register: gratitude, and counsel's own indignation)

**SEND `r8166413635158683041`.** Position identical to Addendum 18 — **the $5,000
is still declined and all three structures still ask for a number.** Only the
register changed, on the user's direction: sound genuinely grateful, and enlist
the fact that **Krukas is angry about this award.**

**Why this is a real lever and not flattery.** Krukas has volunteered indignation
three separate times, unprompted and unbilled:
- *"from my perspective, the decision is insane"* (7/29)
- *"this arbitrator has no business handling such matters"* (7/29, ¶ after 7)
- *"I don't like what this arbitrator did and it would bother me if nothing came
  of it."* (7/30)

He also made the **systemic** argument first: *"If nobody holds manufacturers
accountable for making warranty parts available in a timely manner, why should
they ever address that industry wide problem?"* The email quotes his own line
back and **attributes the systemic point to him** rather than inventing it, then
reframes the fee as the obstacle to the outcome *he* said he wants: *"I would
rather solve the fee problem than let it be the reason nothing comes of this."*

**Gratitude is specific, not general** — he gave more straight analysis unbilled
than the firm that actually represented the user, including points against his
own interest, and closing NJ in one line saved weeks. Specific thanks reads as
observation; general thanks reads as softening before an ask.

**⚠ THE EXIT RAMP WAS DELIBERATELY WIDENED, not narrowed.** An appeal to shared
principle can tip into obligation, which would backfire with someone who has
already been generous. So: *"a one-line no to any of them is a complete answer"*
is retained, and the fallback is warmer and unconditional — *"I will file it
myself and take my chances, with no hard feelings at all. I am already ahead for
having talked to you."* **If a future session revises this email, keep that
line.** The appeal only works while the no stays genuinely free.

Length ~380 words — between the ~250-word tightened version and the ~450-word
original. The added length is all in the opening; the three asks and the usage
question are unchanged.

---

## SESSION ADDENDUM 21 — 2026-07-30 (user's revision adopted; one open judgment call)

**SEND `r-4992051048113065183`.** This is **the user's own rewrite**, not Claude's.
Two of his changes are improvements and should survive any future edit:
- *"validation for the frustrations I have had for much of this year"* — more
  human than the drafted version, and true.
- *"I did most of the assembly and exhibits for the arbitration already"* —
  **concrete evidence he can carry the limited-scope option**, not just a claim.
  This materially strengthens ask #2, which is the likeliest to land.

**Fixes applied:** typo "arbirtation"; grammar on the $5,000 sentence; restored
the signature block; restored **"September 9 either way, so I would rather move
early than late"** (the revision had dropped the deadline entirely, losing the
prompt for a fast reply); restored one concrete instance of what counsel gave —
*"than I got from the firm that actually represented me — and none of it billed.
Closing off New Jersey in a single line probably saved me weeks"* — because
specific thanks reads as observation while general thanks reads as softening
before an ask.

**⚠ OPEN JUDGMENT CALL — "marginally higher potential payoff" may concede too
much.** Krukas's own words were *"a chance to get back $6.5k **and your attorney
fee reimbursed**."* So the upside is not $6,500 against a $5,000 fee; it is
$6,500 **plus** potential fee recovery. And **the usage question, if it resolves
on first-report mileage, raises the $6,500.** Conceding the economics builds
rapport and is deliberate, but the concession is larger than the record
supports. Hedged to *"doesn't make this a cost-effective endeavor **on its
face**"* — **the user was flagged and it is his call.** Do not harden this into
a settled fact about the case's value.

---

## SESSION ADDENDUM 22 — 2026-07-30 (⚠ the break-even correction — stop conceding the economics)

**SEND `r-6387151239611226988`.** Addendum 21's open judgment call is now
resolved **against** the concession. The phrase *"marginally higher potential
payoff"* is **removed** and replaced with counsel's own arithmetic worked
through.

**⚠ THE ARITHMETIC, from Krukas's own words** — *"a $5k attorney fee up front for
a chance to get back $6.5k **and your attorney fee reimbursed**"*:

| Outcome | Result |
|---|---|
| Win | recover ≈**$6,500**, and the **$5,000 fee comes back** → net ≈ **+$6,500** |
| Lose | fee spent, no recovery → **−$5,000** |

**Break-even probability = 5,000 ÷ (6,500 + 5,000) ≈ 43.5%.**

Krukas framed the bet as needing *"like a 90% chance"* to be worth it. **On his
own numbers it is positive expected value above roughly 44%** — and he separately
called the petition *"winnable."* Those two statements sit in tension, and the
email now asks him about it rather than accepting the 90% framing.

**Posed as a question, not an argument** — this is the whole point of the
phrasing, and a future revision must preserve it: *"That is a very different bet
from the one I had in my head. I may be missing something about how often fees
are actually awarded in these proceedings, or at what fraction of what was
billed. Am I reading it correctly?"* The genuine unknowns (award frequency,
award as a fraction of billed) are named so it reads as a client checking his
understanding rather than out-lawyering counsel.

**⚠ Two live unknowns keep this from being asserted as fact:**
1. **§ 198-a(l)'s scope is still UNVERIFIED** (checklist § 4). Krukas's casual
   *"and your attorney fee reimbursed"* implies he believes fees are recoverable
   here — **that is inference from his phrasing, not a holding.**
2. **Fee awards are discretionary and often reduced.** The break-even assumes
   full recovery of the $5,000; a partial award moves it upward.

**The usage question is retained and is now labelled "one more thing,"** since
the fee arithmetic took the lead position. If usage runs on first-report mileage
(7,026 or 8,148 — both under 12,000), usage is **zero** and **$6,500 rises**,
lowering break-even further. **Two independent questions now both point the same
way: the economics are better than the 7/30 email assumed.**

---

## SESSION ADDENDUM 23 — 2026-07-31 (the fee email WAS SENT — text of record)

**✅ SENT** 2026-07-31 00:04 UTC, message **`19fb57cac5a84420`**, thread
`19faaa4dcaaeaca8`, to ekrukas@ cc mvicario@. **No draft is pending; all
remaining drafts in the thread are dead.**

**The user edited before sending. This is the text of record — not any draft.**
Four deviations from Addendum 22's draft, all his:

1. **Gratitude narrowed.** *"You have given me a straight analysis, and
   validation for the frustrations I have had for much of this year."* He **cut**
   the comparison to the firm that actually represented him, the "none of it
   billed" line, and the New Jersey credit. Reads as unwillingness to disparage
   prior counsel to prospective counsel — defensible.
2. **Break-even paragraph made clearer and softer.** *"the downside is paying
   $5,000 in attorney fees, and the upside is roughly the $6,500 (and having fees
   reimbursed) — which would put break-even nearer a 45% chance than a 90% one?"*
   He turned the assertion into a **question mark**. Better: it cannot read as
   out-lawyering counsel.
3. **Added** *"I really appreciate your candor. Would you be willing to explore
   other fee structure options?"* — restores his own collaborative framing ahead
   of the three asks.
4. **⚠ The September 9 reminder was dropped again** (also dropped from the 7/29
   send). There is now **no urgency prompt anywhere in the thread.** Counsel
   knows the date, but nothing in the correspondence asks him to answer quickly.
   **If a reply has not come within ~3 days, that is the reason, and a one-line
   nudge is warranted.**

**Everything load-bearing survived:** the decline of $5,000; the break-even
arithmetic; all three fee structures each asking for a number; the § 198-a(l)
scope caveat; the on-the-record-for-the-duration caveat; the pro se fallback with
no hard feelings; and the usage question.

### ⏭ WHAT THE NEXT REPLY DECIDES

| Counsel's answer | Meaning |
|---|---|
| A number **materially under $5,000** (e.g. $1,500–2,500 for review/sign/appear) | Real offer — take it |
| A number **at or near $5,000** | Polite no → **pro se** |
| Confirms break-even ≈45% and stands by "winnable" | The economics argument is won; the fee structure is the only open term |
| Usage runs on **first-report** mileage | Usage = **$0**, the $6,500 rises, break-even drops further |

**⚠ IF PRO SE: the blocking item is unchanged and still unresolved — how HMA is
served in NY.** BCL § 306 (authorized) vs § 307 (unauthorized, extra mailing +
affidavit of compliance). The DOS entity search has never been runnable from this
environment (proxy 403s dos.ny.gov). **NY DOS: (518) 473-2492.** Filing deadline
**9/9/2026**; service wall **9/24/2026**; lease dies **11/23/2026**.

---

## SESSION ADDENDUM 24 — 2026-08-03 (✅ COUNSEL RETAINED — and six questions still unanswered)

**The pro se / counsel question is closed. Krukas & Vicario are engaged**, on
terms the firm proposed and Petitioner accepted without further negotiation.

### The terms as accepted

| Term | Value |
|---|---|
| Retainer up front | **$3,000** |
| Per court appearance | **$1,000** |
| Reimbursement | Petitioner **"reimbursed first out of any attorney fee awarded by the court"** |
| Expected appearances | Possibly **zero** — "the court just decides on the papers" (Krukas 7/31) |
| Scope | **All or nothing.** "We're not comfortable handling this case collaboratively or being partially involved… if we are involved we would want to handle every aspect of the Petition." |

Break-even at these numbers, with the fee reimbursed on a win:
**$3,000 → 31.6%; $4,000 → 38.1%; $5,000 → 43.5%.** (`p = C / (R + F)`, R ≈
$6,500 per counsel's rough count.) The "90% chance" figure Krukas originally
invoked is not the break-even for this bet under any assumption. He did not
dispute the arithmetic when it was put to him; he answered by cutting the price
40% at the floor.

### ⚠ LEAD COUNSEL CHANGED — Vicario, not Krukas

Krukas, 8/3 14:07, to Petitioner alone:

> "I am going to have Michael get back to you on these questions, **as he is
> going to be handling this matter. He is the litigator between the two of
> us.**"

**This matters for expectation-setting.** Every merits judgment in the file —
"the decision is insane," "RO 358530 should be sufficient… 100% of the time,"
"this arbitrator has no business handling such matters," "it would bother me if
nothing came of it" — is **Krukas's**, and Krukas is now the intake partner,
not the litigator. Vicario has said nothing on the merits in writing at any
point. Do not attribute Krukas's conviction to the firm's litigator.

Firm of record: **Krukas & Vicario**, 2704 Grand Ave, Ste 4, Bellmore NY 11710,
(516) 780-0760 x702, KVJustice.com. "Attorneys Licensed in New York, New Jersey
& Pennsylvania."

### The retainer

`Hu Article 75 Retainer.pdf`, attached to Vicario's 8/3 16:27 email
(msg `19fc87366749cf52`):

> "See attached retainer. Let me know if you have any additional questions
> after reading. You can either print out and sign, or I can send you on a
> Docusign… Once signed, Eugene will invoice you for the initial charge."

**UNSIGNED as of this addendum.** Not yet read — Petitioner has reserved the
review for a later step.

### ⚠ SIX QUESTIONS PUT TO THE FIRM, NONE ANSWERED IN WRITING

Petitioner's 8/3 08:00 acceptance (msg `19fc77ebe292bda9`) asked six things.
Krukas deferred them to Vicario; Vicario sent the retainer without addressing
any of them. **Check each against the PDF before signing; whatever the PDF does
not cover is still open.**

1. **November 23.** "If the petition is still pending when the lease matures and
   a stay isn't available, where does that leave us — and is there anything
   worth doing in August to be better positioned for it?" **This is the
   substantive one, and it is the risk counsel himself called unsolved.**
2. Whether the **stay motion** falls within the $3,000, and whether it counts as
   an appearance.
3. A **ceiling on appearances**, or ones past the first coming out of the fee
   recovery.
4. Out-of-pocket **reimbursed first out of any fee recovery — settlement as well
   as court award.** ⚠ The term as Krukas wrote it says "awarded by the court,"
   but he separately predicts settlement is the likelier path. **As drafted the
   protection may not reach the branch he thinks most likely.** The spread is
   the entire retainer: ~$6,500 net if it reaches settlements, ~$3,500 if not.
5. **Any settlement stating Petitioner's recovery and the fee separately**
   rather than as a single number. Guards the classic fee-shifting conflict:
   a package generous on fees and thin on the repurchase makes the firm whole
   and not the client.
6. **Who carries disbursements** — index number, RJI, service through the
   Department of State. None of the figures discussed to date include these.

### What counsel established on 7/31 (recorded here because it changed the decision)

**§ 198-a(l) — quoted by counsel, still not officially verified.** Krukas pulled
and highlighted the language:

> "**prevails in any judicial action or proceeding arising out of an arbitration
> proceeding held pursuant to subdivision (k) of this section.**"
>
> "My reading is that prevailing in the Article 75 would justify an award of
> fees."

But discretionary: *"the statute does indicate… 'a court **may** award' attorney
fees. It's within the discretion of the judge — who may or may not award what we
consider to be reasonable… I would expect in most instances a judge would be
reasonable, but it's **not a certainty**."* **Counsel's quotation is not the
official text. Checklist § 2a stays open.**

**What winning produces — the question that had never been asked.** Krukas,
7/31 15:31 and 15:32:

> "I think it's likely to result in a **remand** if you win. Good chance it just
> settles at that point for a repurchase."
>
> "If you won the Art. 75 I think it **likely settles right away at that
> juncture for attorney fees and the repurchase.** If the arbitrator's decision
> is found to be irrational then it's **sort of a foregone conclusion what
> happens on remand.**"

**⚠ And the timing problem, in counsel's own words — this is now the dominant
risk, not the merits:**

> "The timing is an issue though. I'm not sure if it would be possible to get a
> court order **staying the bank from taking back possession of the lease.** We
> would probably have to ask for one. **The timing is a big issue and we're
> basically making that part up as we go along. There is no clear mechanism for
> dealing with that.**"

**Settlement before filing is out:** *"As things stand you have no leverage."*
*"I don't think you have any leverage for a settlement from Hyundai."* Filing is
what creates leverage.

**Usage:** *"Usage runs on the current odometer. Not first report."* If right,
the Q16 first-report conflict may not affect damages — though it remains an
inconsistency in a document Petitioner signed.

### An upside nobody has counted

A § 198-a lessee repurchase terminates the lease. The lease matures 11/23/2026
and Petitioner is currently exposed to a **disposition fee, excess-wear and
excess-mileage charges** — **none of which appear anywhere in this file, and
none of which are in counsel's ~$6,500 estimate.** Pull them from the lease
documents; they are real money on top of the recovery.

### Live action items

1. **Read `Hu Article 75 Retainer.pdf` against the six questions above.** Next
   step, at Petitioner's direction.
2. **Do not sign until item 4 above is resolved** — settlement-branch
   reimbursement is worth the whole retainer.
3. Deliverables in `materials/` are now **counsel's raw material, not the
   filing.** The firm wants "every aspect of the Petition." Stop polishing them
   for filing; hand them over if asked.
4. The NY DOS entity search passes to counsel. Retained in the brief because the
   answer must exist before service. **(518) 473-2492.**
5. Clocks unchanged: file **9/9/2026**, serve **9/24/2026**, lease dies
   **11/23/2026**.

---

## SESSION ADDENDUM 25 — 2026-08-03 (the retainer READ; two asks gate the signature)

**`Hu Article 75 Retainer.pdf` — 3 pp., dated August 3, 2026, signed Michael A.
Vicario, Esq. Read in full.** Preserved at
**`materials/Hu_Article_75_Retainer.pdf`** — it arrived only in an ephemeral
uploads directory and would have been lost with the container.

### What the document says (this text governs, not the emails)

Contracting entity: **"Eugene Krukas PLLC d/b/a Krukas & Vicario Attorneys at
Law."**

| Term | Text |
|---|---|
| Fee | `"an attorney fee of $3,000 + $1,000 for each in person court appearance, whether we win or lose the case"` |
| **Ceiling (granted)** | `"The total out of pocket cost for Dr. Hu is limited to $5,000, even if there are more than 2 court appearances"` |
| Rates behind any overage | **$500/hr attorneys, $175/hr paralegals** |
| Scope **includes** | `"preparing and filing pleadings and motions, appearing at court conferences and ultimately conducting a hearing"` |
| Scope **excludes** | `"The scope of this retainer does not extend to a subsequent arbitration proceeding, should one be ordered… a separate retainer will be needed."` |
| Withdrawal | `"We may, at our option, withdraw from the case… for any reason"` (unused fees returned) |
| Settlement | `"You will decide whether to accept or reject the offer"` — but `"you agree to not settle this matter on your own without the written consent of this office"` |

### Three findings

**1. ⚠ THE $5,000 CAP IS CONDITIONAL, NOT A CAP.** It holds only
`"provided that none of the four (4) circumstances described below arises"`.
The live trigger: `"(2) you accept a settlement offer that does not include
compensation for all of the attorney fees incurred by our firm."` If tripped,
exposure reverts to hourly — **a 30–40 hour petition at $500/hr is
$15,000–$20,000**, three to four times the stated ceiling. This is **standard**
in fee-shifting consumer retainers and protects the firm from a client settling
cheap; the ask is to **bound** it, not remove it. Note the internal tension with
the same document's `"You will decide whether to accept or reject the offer."`

**2. ⚠ THE REIMBURSEMENT WATERFALL WAS REORDERED — AND STILL MISSES THE LIKELY
BRANCH.** Krukas's email (7/31): *"**You** get reimbursed first out of any
attorney fee awarded by the court."* The retainer:

> `"If attorney fees and costs are awarded by the Court, actual costs or
> disbursements, will be reimbursed to the firm first, and then the attorney fee
> award will be used to reimburse you for attorney fees personally paid…, before
> then going to the firm for any 'additional attorney fees'."`

Petitioner moved from **first** to **second**, behind the firm's disbursements
(practically small — index number, RJI, service — so it bites only if the award
itself is small). **The larger half: it is still keyed to fees "awarded by the
Court," while counsel expects a settlement**, where no such award exists.
Spread ≈ the entire retainer (~$6,500 net if it reaches settlements, ~$3,500 if
not).

**3. THE REMAND EXCLUSION SITS EXACTLY WHERE THE MONEY ARRIVES.** Counsel's
predicted path is vacatur → **remand** → settle. If Hyundai forces a
re-arbitration instead, that is a **new engagement at an unquoted price**. The
$5,000 buys the vacatur only.

### Scoring Addendum 24's six questions against the document

| # | Question | Status |
|---|---|---|
| 2 | Stay motion inside the fee? | ✅ **Yes** — "motions" are in scope |
| 3 | Ceiling on appearances | ✅ **Granted — $5,000** (better than the email) |
| 6 | Disbursements | ◐ Firm advances and recovers first. **Silent on who bears them on a loss** |
| 4 | Reimbursement on **settlement** | ❌ Not addressed — now ask (b) |
| 5 | Settlement stating recovery and fee separately | ❌ Not addressed; the four-trigger clause cuts the other way |
| 1 | **November 23** | ❌ **Still unanswered by anyone** |

Note: the "$1,000 per **in person** court appearance" wording favors Petitioner
— NY does many conferences virtually. **Do not ask them to clarify it.**

### The email as sent — msg `19fc929af4f05976`, 8/3 19:46 UTC, to Vicario cc Krukas

Two asks framed as gating signature: **(a)** bound the four triggers — *"limit
the settlement trigger to instances where I accept a settlement over your
written objection, or establish a stated ceiling on additional fees"*; **(b)**
*"Can the same order apply to fees recovered by settlement?"* Closing: *"Happy
to sign as soon as the first two are settled."* Four non-blocking questions:
remand retainer cost, November 23 + whether lease maturity implicates the
vehicle provision, disbursements on a loss, and — see below — the incidentals.

**Petitioner's three edits to the draft:**
1. Trimmed the thanks for the ceiling.
2. **Dropped the request for periodic time records.** That was the monitoring
   mechanism for the very exposure ask (a) addresses. **If ask (a) is refused,
   re-raise it** — otherwise the hourly meter runs unseen.
3. **Added:** *"Should I try to contact Hyundai customer service separately
   regarding the $1800 of incidental expenses…"* (verified figure:
   **$1,793.43**).

### ⚠ HALT-AND-CONFIRM — do not contact HMA before counsel answers

Three independent reasons, all from documents already in this file:

1. The retainer: *"you agree to not settle this matter on your own without the
   written consent of this office."*
2. Trigger **(4)**, refusal to cooperate, is one of the four that lifts the
   $5,000 cap.
3. **The incidentals are part of the § 198-a(c)(1) recovery, not a side claim.**
   Settling them separately could undercut the repurchase.

Krukas has already said *"As things stand you have no leverage"* and *"I don't
think you have any leverage for a settlement from Hyundai."* **Asking counsel
first was the correct move; wait for the answer.**

### Not asserted

The engagement letter carries **no notice of the right to arbitrate a fee
dispute** (22 NYCRR Part 137). Believed applicable to a NY engagement letter of
this size — **medium confidence, UNVERIFIED**; the rule text is unreachable
under the egress policy. **Deliberately left out of the email**: the right
exists independent of the notice, so raising it buys nothing and reads as
auditing the firm's compliance.

### Live action items

1. **DO NOT SIGN** until asks (a) and (b) return in writing.
2. **DO NOT CONTACT HYUNDAI** about the incidentals until counsel answers.
3. **November 23 remains unanswered by anyone** — Krukas deferred it to Vicario,
   Vicario sent the retainer without addressing it, and it was re-asked 8/3.
   It is the risk counsel himself called unsolved.
4. If ask (a) is refused, re-raise the time-records request.
5. Still uncounted anywhere: **end-of-lease disposition fee, excess-wear and
   excess-mileage charges**, which a § 198-a repurchase would extinguish. Pull
   them from the lease documents.
6. Clocks unchanged: file **9/9/2026**, serve **9/24/2026**, lease dies
   **11/23/2026**.

---

## SESSION ADDENDUM 26 — 2026-08-05/06 (both asks granted IN THE DOCUMENT; retainer clear to sign; Ex17 double-count; HMA draft verified)

### The revised retainer — verified against the document, not the email

Vicario replied **8/5/2026 15:30Z** (msg `19fd28bc83e49c54`): *"I have no issue
who [sic] the 2 proposed changes. See attached updated retainer. I will also
send a Docusign."* The revised PDF is preserved at
**`materials/Hu_Article_75_Retainer_v2.pdf`** (sha256 `7b3be227…`, 3 pp.); the
8/3 baseline (`5d16ba7a…`) is retained. **Both asks are in the DOCUMENT** —
verified 2026-08-06 by text extraction against both PDFs; each sentence present
in v2, absent from the baseline:

| Ask | Inserted language (verbatim) | Location |
|---|---|---|
| **(b)** settlement waterfall | *"The same order would apply to attorney fees recovered by settlement."* | end of fee-shifting ¶, p. 2 |
| **(a)** bound the triggers | *"Notwithstanding, recovery from you personally will be limited to $5,000."* | immediately after the four cooperation triggers, p. 2 |

This mattered because the last time an email promised a term, the document said
the opposite (Krukas 7/31 *"**You** get reimbursed first"* vs. retainer 8/3
*"reimbursed to **the firm** first"* — Addendum 25). This time the document
delivers. Ask (a) landed in the **stronger** of the two forms offered — a
ceiling placed after *all four* triggers, so the $500/hr overage is bounded at
$5,000 whichever trigger fires. Combined with the untouched *"total out of
pocket cost… limited to $5,000,"* there are now **two independent $5,000
ceilings**. Soft spot, recorded: the new sentence sits inside the COOPERATION
section, so a narrow reading confines it there — immaterial, because the fee
section caps total out-of-pocket independently.

Unchanged in v2 (verified): the no-independent-settlement clause (*"you agree
to not settle this matter on your own without the written consent of this
office"*), trigger (3) *"sell or trade-in,"* the remand scope exclusion, and
the date — still **August 3, 2026** (DocuSign execution date governs).

### Vicario's four answers (same email, verbatim)

1. **Remand pricing:** *"Our general rates for an arbitration are $6,000 win or
   lose or $7,500 on contingency. If we win the article 75 petition and you
   want us to represent you in the arbitration, that would be a new negotiated
   retainer, and we can re-address the cost then. You would also be free to
   represent yourself."*
2. **November 23:** *"If the lease matures and you give back the vehicle, then
   I'm not sure what will legally happen to the petition. We will be in
   uncharted territory for these cases. Our position will be that the case
   survives and that you would be entitled to full reimbursement and then
   Hyundai has to figure out how to take the car (their problem, not ours).
   However, I'm sure their attorney will argue the opposite. I will write a
   letter to the Court explaining the situation."*
3. **Disbursements on a loss:** *"If we lose the fee is flat, you will not owe
   disbursements. Disbursements will only come into play if there is an
   attorney fee award after winning the case."*
4. **Incidentals:** *"Your incidental expenses will not be part of the
   petition. You are free to contact Hyundai separately, though I'm not sure
   they will deal with you once you are represented by counsel."*

### Analysis (must survive any compact)

1. **Maximum personal exposure is now $5,000**, from two independent clauses.
   **The retainer is clear to sign.**
2. **The remand branch is the live economic risk** — petition $3,000–5,000 +
   remand $6,000 = $9,000–11,000 against a ~$6,500 case. Underwater *if* HMA
   forces re-arbitration; Krukas predicts it won't (*"likely settles right
   away"*). Outs: self-represent on remand (now in writing), or the $7,500
   contingency variant — **"contingency" is undefined**; ask Vicario what it
   means.
3. **Disbursements-on-a-loss is in the email, not the document.** Practically
   moot (inside the $5,000 ceiling), but the document is silent.
4. **The incidentals permission is in the email, not the document.** The
   no-independent-settlement clause binds **on execution** — hence the
   sequence: **send the HMA escalation first, then sign.** Vicario's own
   caveat (*"I'm not sure they will deal with you once you are represented"*)
   is itself the argument for sending now.
5. **November 23 finally has an answer on the record** — counsel's position,
   a letter to the Court, *"uncharted territory."* It resolves nothing; the
   **buyout remains the user's call** (Addendum 10).

### ⚠ Exhibit 17 — the $195.82 double-count (found 2026-08-05)

Localized: Ex17's ride-share block claims **$700.59** vs. the receipt packet's
**$504.77** — exactly **$195.82** high. Ex17 claims $216.87 on 01/09 (receipts:
$131.91, Jan 7), plus $86.93 (01/21) and $23.93 (01/23) that appear in no
receipt; its ride dates do not match the receipts. Ex21 Tab B expressly states
individual rides were counted once and summaries not double-counted — **Ex17
appears to have counted a Lyft daily summary on top of the rides it
summarizes.** So Ex17's total **$1,989.25** is wrong; the receipt-supported
figure is **$1,793.43**. **Ex17 carries a certification under penalty of
perjury and was served on the arbitrator — it cannot be unserved.** Moved to
the do-NOT-send list in `research/2026-07-28-attorney-packet.md`; counsel must
be told (it is in the Vicario draft). Full detail: `docs/open-items.md`.

### HMA escalation draft — reviewed and corrected 2026-08-06

`materials/2026-08-05-email-to-HMA-Executive-Office-DRAFT.md` (+ 56-pp receipts
attachment, sha `ff257b8f…`). All five quoted HMA statements verified against
Ex21 Tab E / Gmail. Two corrections made on review:

1. **Attribution fixed:** the $391.25 approval came under **Hyundai
   Reimbursement Request 2026-6680**, not RA Case #76530936 (that is the Feb 9
   tow reference).
2. **"Reimbursed" → "approved" → back to "reimbursed":** the record documents
   approval and a promised secure payment link, not actual receipt — but the
   **user confirmed 2026-08-06 that the $391.25 payment landed** (user
   testimony; HMA can verify against its own payment records), so the stronger
   wording was restored.
   Also noted: HMA already **declined the $15.65 once in writing** (*"outside
   the policy of reimbursement"*) — the email is an executive review of that
   decision, and expectations on that line should be tempered accordingly.

### Clocks (unchanged)

File **9/9/2026** · serve **9/24/2026** (understanding — CPLR 306-b still
unverified) · lease dies **11/23/2026**.

---

## SESSION ADDENDUM 27 — 2026-08-06 (HMA escalation SENT — verified; retainer SIGNED — user-confirmed; the no-settle clause is now LIVE)

### The two events

1. **HMA escalation SENT and verified in the record.** Sent **8/6/2026
   05:50Z** from jimmy.hu@gmail.com to customercare@hmausa.com (msg
   `19fd59f767605548`, thread `19fd5952e8cdabc1`). Full content pulled and
   checked: body matches the reviewed draft **word-for-word** (including the
   corrected "reimbursed under Hyundai Reimbursement Request 2026-6680"
   attribution), and the 56-page receipts PDF **is attached**
   (`20260805HMAExecutiveOfficereceiptsattachment.pdf`, application/pdf).
   Benchmark from July 2025: the executive office answered in ~21 hours.
   Realistic recovery: **$1,200–$1,400** of the $1,793.43 asked.
2. **Retainer SIGNED — user testimony, 8/6/2026.** The user reports signing
   the DocuSign. ⚠ **No DocuSign completion certificate is in the inbox yet**
   (searched 8/6). When it arrives: save the executed PDF + certificate to
   `materials/` as the operative contract (the executed copy, not v2,
   governs). Sequence integrity confirmed: the HMA email (05:50Z) predates
   the signature.

### Consequences — now binding

- **The no-independent-settlement clause is LIVE**: *"you agree to not settle
  this matter on your own without the written consent of this office."* From
  now on, **any substantive money response to HMA goes through Vicario
  first** — including acceptance of the incidentals reimbursement itself.
  A straight reimbursement with no release is arguably not "settling the
  matter," but the clause is broad and a one-line written OK from Vicario
  costs nothing. **If HMA sends any document to sign or any settlement
  number: forward to Vicario, do not respond substantively.**
- **Krukas invoices $3,000 on signature** — expect it; pay promptly.
- The firm is now counsel of record in fact; the pro-se posture of the HMA
  email was accurate **when sent** and is preserved in the record.

### Next actions (live queue)

1. Send the Vicario follow-up note (`materials/2026-08-06-email-to-Vicario-DRAFT.md`,
   updated to post-signature tense) and **forward the sent HMA email** to
   Vicario for his file.
2. **Send counsel the case packet** per
   `research/2026-07-28-attorney-packet.md` — Tier 1 + Tier 2 (Ex17 stays on
   the do-NOT-send list; the Ex17 disclosure is item 4 of the follow-up
   note). The firm asked for "every aspect of the Petition."
3. Preserve the executed retainer + DocuSign certificate when the email
   arrives.
4. Watch for the HMA response; route per the rule above.
5. Ask Vicario for the expected **filing timeline** — 9/9 is 34 days out and
   is now counsel's deadline to hit; service wall 9/24 (Petitioner's
   understanding). The buyout-vs-return call (11/23) remains open — item 2 of
   the follow-up note asks Vicario's recommendation.

---

## SESSION ADDENDUM 28 — 2026-08-10 (⚠ Ex11 and the Impact Statement were never attached; Alvarez identified; no written arbitrator directive)

**Trigger:** Vicario's 8/9 email (filed "this week"; wants both evidence
packets + who appeared) and his 8/10 phone call (forward all emails submitted
to the arbitrator, with a summary; asked about an arbitrator directive to the
manufacturer).

**⚠ FINDING — the served record is short two listed documents.** Attachment
lists of all seven submission emails (June 3–5, thread `19e416e69f35788f`)
were read 2026-08-10:

- **Exhibit 11 (Days Out of Service Summary) was never attached.** The 6/5
  00:54 email *lists* it in the body but attaches only the Ex21 Expense
  Packet and a **signed, edited version of Ex17** (same wrong $1,989.25).
  Consistent with the award's "He summarized the days out of service as
  listed in his form" — the arbitrator worked from the RFA form, not Ex11.
  The 124-day anchor is unaffected (RO #358530). Ex11 also remains a Google
  Doc only.
- **The Consumer Personal Impact Statement** is on the 6/3 master index but
  in no email's attachments.
- The 6/3 12:05 cover email itself carried **no attachments** (the four
  "procedural documents" on its index — cover letter PDF, NOH, arbitration
  form, RFA — were already in the program's hands via the AG/NYSDRA, except
  the cover letter PDF, which appears never to have been sent).
- Ex17 was therefore **served twice**, both times at $1,989.25.

**Who appeared for HMA: Danielle Alvarez** — *user's recollection, supplied
8/10*; the award says only "Counsel for manufacturer," and no document in the
record names her. Treat as testimony until NYSDRA's file confirms.

**Arbitrator directive to the manufacturer: NONE — written or oral.** Nothing
in the written record (no production order, no subpoena; only the CDRC's
conditional 5/27 vehicle-inspection note, and no inspection was ordered), and
the **user confirmed 2026-08-10 there was no oral directive at the hearing**
(testimony — he attended). The bracket in the reply draft is resolved and
removed.

**Deliverable:** `materials/2026-08-10-reply-to-Vicario-DRAFT.md` (v2) — the
per-email forwarding map, the three candor notes (Ex17 error, Ex11/Impact
Statement gap, bundle flags), the HMA-packet answer (NYSDRA file, Don
Raiano), Alvarez, and the directive answer. User fills one bracket (oral
directive memory) and the Drive link, forwards the seven emails + NY Peace
confirmation, sends.

**Packet status:** rebuilt 8/10 after adversarial verification (4 blockers
fixed — the retracted "wrong 8,148 basis" framing, the unverified (c)(1)
scope assertion, the MVMA/Gurau attribution, and two new flags: Q16/Q15 and
the HV-vs-12-volt mischaracterization in served exhibits; now EIGHT flags,
183 pp). `Hu_v_HMA_Counsel_Packet_2026-08-06.pdf`.

---

## SESSION ADDENDUM 29 — 2026-08-12 (Ex11 read from Drive and exported; five errata; transmittal drafted)

**Trigger:** Vicario asked for Exhibit 11. The reply disclosing its
never-served status (Addendum 28) had already gone out — user sent it to
Krukas/Vicario.

**Ex11 read in full from the Drive original**
(`15okCHDSDrKdbppmFbCi9yzIh41pXPaU2fz2vGkO4JdM`) and exported to
**`materials/exhibits/Hu_v_HMA_Ex11_Days_Out_of_Service_UNSERVED.pdf`**
(5 pp., fidelity verified via text layer). Drafted ~early May 2026,
pre-arbitration, **before the project's corrections — five errata against
the verified record:**

1. **"NY GBL §198-a Threshold: 15 days" (citing "(b)(2)"), "13.4× minimum"**
   — the presumption threshold is **30 days** (verified-facts;
   § 198-a(d)(2); the ND-4 form's own issue language). All multiplier math
   in the document is wrong.
2. **"second HV battery replacement" for RO #370267** — refuted (Addendum
   2): 12-volt battery; ONE HV pack replacement (2025). Same
   mischaracterization as served Ex12/Ex22/Loss-of-Use (packet Flag 8).
3. **Lease date "May 22, 2024"** — verified: May 23, 2024 (Ex01; same slip
   as the RFA form, Addendum 8 reconcile list).
4. **Leads with 201/198 total days** — the standing rule: 124 days on RO
   #358530 is the anchor; the aggregate is secondary.
5. **"Filing Date: May 4, 2026"** — NYSDRA file date is May 12, 2026 (fee
   May 11, Ex18).

Accurate and possibly useful: Ex11's note that ROs #358530 and #363888
carry customer email "jimmy.hu25@gmail.com" (not Petitioner's address) —
**Ex11's own assertion; not re-verified against the RO images this session**
(the extraction carries no email text).

**Deliverable:** `materials/2026-08-12-Ex11-to-Vicario-DRAFT.md` — short
transmittal attaching the PDF with the five errata stated plainly, the
124-day pointer, and the do-not-cite handling note. **No corrected Ex11
variant was or should be created.**

---

## SESSION ADDENDUM 30 — 2026-08-12 (petition + client affirmation reviewed; VIN typo and five other catches; sign only after fixes)

**Received:** Vicario's petition (14 pp — Notice of Petition, Verified
Petition ¶¶1–39, attorney Verification under CPLR Rule 2106) and the client
affirmation (Exhibit F, 20 ¶¶) for the user's signature. Reviewed in full
against the verified record. **The petition is verified by VICARIO, not the
user — the user signs only Exhibit F** (perjury affirmation).

### Affirmation (Exhibit F) — signature-blocking

1. **¶1 VIN wrong: "KM8KNDDF9U253237" (16 chars, missing R).** Correct:
   KM8KNDDF9RU253237.
2. **¶15 "Hyundai did not present any evidence or provide any documents"**
   — unqualified, sweeps beyond user's knowledge (HMA's written response was
   due at NYSDRA 5/27; never shared with user; existence unknown). Fix:
   "At the hearing, …" Petition ¶¶14, 28 lean on this sentence.
3. **¶8 typo** "200 hundred days"; the ~200-day aggregate is acceptable as
   testimony (matches hearing testimony; includes non-facility downtime) but
   the case rests on the 125-day RO.
4. **¶18** "did not prove or attempt to prove any affirmative defenses" —
   HMA counsel argued "operating as intended"; safer: "offered no evidence
   in support of any affirmative defense."
5. **¶12 Exhibit E check** — "all evidence provided to the arbitrator is
   attached" is accurate only if Exhibit E = the actually-served set
   (Addendum 28: Ex11 + Impact Statement never attached).
6. **¶11 May 4 AG application date** — plausible (referred to NYSDRA 5/5);
   user to confirm from his receipt or soften.
7. Clean: lease date 5/23 ✓ (correct where the petition is not), Apr 3–Aug 5
   ✓, 8,151 mi ✓, hearing facts ✓; ¶¶16–17 are the user's own testimony
   memory (the load-bearing rebuttal to "no allegation") — he must be
   comfortable he said it.

### Petition — comments relayed (Vicario's pen)

1. **Captions (Notice + Petition) name "HYUNDAI OF AMERICA"** — wrong
   entity; body ¶4 and affirmation say Hyundai Motor America.
2. **¶12 "May 22, 2024" delivery** contradicts its own Ex C (lease: 5/23)
   and Exhibit F ¶1.
3. **125-day convention** used throughout (inclusive count Apr 3–Aug 5) —
   defensible alternative to the project's 124 (elapsed); the only real
   problem is ¶17's "125 consecutive calendar days LATER" (arithmetically
   124). Suggested inclusive phrasing.
4. ¶13 "filed with NYSDRA on or about May 4" — application went to the AG;
   NYSDRA file date 5/12.
5. ¶16 RO quotes not machine-verifiable (image scans) — counsel to eyeball
   vs. his Exhibit D.
6. **Strategy positives:** claim submitted solely on (d)(2), four-attempts
   prong expressly not invoked → sidesteps the Q16 conflict (April 3 @
   8,148 as operative visit); Feb 2026 correctly a 12-volt replacement;
   Ground III uses Q15 + the four-corners contradiction; Ground V uses the
   award's carelessness; Ground VI (loaner) adds Wenqing He v BMW (2025 NY
   Slip Op 34739(U)) + the § 198-b(c)(2)(b) parts-delay contrast (Kepenis);
   Ground VII + Wherefore ¶D pre-litigate lease maturity (Kucher; Diaz v
   Audi). Service via CSC, 80 State St, Albany — the BCL 306/307 question
   is resolved. New citations are counsel's own (outside the project's
   verified set — his reporters, his responsibility); DaimlerChrysler
   pinpoint given as 659–60 (project verified 658 — same discussion).

**Deliverable:**
`materials/2026-08-12-petition-comments-to-Vicario-DRAFT.md` — items 1–4
blocking signature, 5–6 confirmations, petition items 7–11, sign-same-day
close. **Do not sign Exhibit F until the VIN and ¶15 are fixed.**

---

## SESSION ADDENDUM 31 — 2026-08-13 (queue status: missing-docs resolved; no video email exists; HMA silent 6 days)

1. **Vicario's 8/10 missing-documents request is RESOLVED** — the user's 8/11
   02:43Z forward (msg `19feeb43afafcdc6`) carried all three attachments:
   `Contract 1-59225931599.pdf` (lease), `Hyundai Bill of Sale.pdf`,
   `Car Registration.jpg`. Verified from the message's attachment list.
2. **The "email where you sent pictures and videos of the problems" does not
   exist.** Sent-mail searches (filename:mp4/mov/jpg, all case
   correspondents) surface no such email. The photographs in the record are
   **Exhibit 20 (dashboard photos)**, served June 3 and in the counsel
   packet; any videos were never emailed — presumably on the user's phone.
   Counsel should be told this plainly so he stops waiting for it.
3. **The comments email on the petition/affirmation was SENT** 8/12 23:47Z
   (msg `19ff85f712b869fe`) — the tightened v2. Also confirmed: Vicario's
   8/12 cover (msg `19ff739ddab106d2`) asks for a signed, scanned
   affirmation back.
4. **HMA: six days of silence** on the 8/6 incidentals escalation (July 2025
   benchmark: ~21 hours). The executive-office channel is not repeating its
   speed. Any nudge is one line on the same thread; any substantive response
   still routes through Vicario. No DocuSign completion certificate yet.

---

## SESSION ADDENDUM 32 — 2026-08-26 (affirmation SIGNED 8/13; Ex11 removed from Exhibit E; ⚠ FILING STATUS UNKNOWN; Vicario OOO)

**The 8/13 sequence (all verified from the thread):**

1. Vicario 19:08Z: *"I made the changes and sent you the affirmation to sign
   by zohosign. The only discrepancy is the arbitration exhibits. I compiled
   everything you sent me as 1 exhibit. Should exhibit 11 be taken out?"* —
   counsel independently caught the Ex11 problem.
2. User 23:30Z: yes, remove it — *"listed on my original index but never
   actually sent to the arbitrator."* **Exhibit E is now the served set
   without Ex11** (msg `19ffd7650bcee950`).
3. **User signed the corrected affirmation via Zoho Sign 23:32Z.** Signed
   copy: msg `19ffd78085ee0b41` / `19ffd77e59b10675` (attachment not
   independently inspected — the Gmail connector has no attachment download;
   Vicario's "I made the changes" is the basis for believing the VIN/¶15/
   ¶8/¶18 fixes landed. If verification is wanted, the user must upload the
   signed PDF).
4. Vicario 23:33Z: *"Thank You. I will try to file the petition tomorrow"*
   (= 8/14).

**⚠ OPEN AND TIME-SENSITIVE — no filing confirmation exists.** Searches for
NYSCEF/index-number/court emails 8/14–8/26: nothing. Thirteen days since
"file tomorrow." **Today (8/26 14:10Z) an out-of-office auto-reply arrived
from Vicario** ("limited access to email... call 516-780-0760") on a "Re: Hu
v Hyundai" subject — with no triggering email in this mailbox after 8/14
(user may have written from another account). Eugene has NOT bounced.
**9/9 filing deadline is 14 days out; service wall 9/24.** Next action:
confirm filing status and get the index number — call the office or email
Eugene (ek@lemonfreedom.com / (516) 203-4001). A filed special proceeding
would have an index number and a return date; the user should also ask for
the as-filed papers.

Other: still no HMA response to the 8/6 incidentals escalation (20 days);
still no retainer completion certificate.

---

## SESSION ADDENDUM 33 — 2026-08-26 (⚠ CORRECTION of Addendum 32 + THE LIVE EVENT: petition FILED AND SERVED; Rigby revives the $5k offer; Eugene asks which clauses to strike)

**Correction first:** Addendum 32's "filing status unknown / firm silent"
was WRONG — an artifact of Gmail thread-preview truncation (search previews
show only the ~5 oldest messages per thread; the 8/26 messages sat at the
end of the "Hu v Hyundai" thread and were missed). The full thread was
pulled 8/26; the record below supersedes.

### The 8/26 exchange (all verified, full texts read)

1. **Eugene 13:23Z** (msg `1a03e3d6b7e269a7`): Michael is on vacation this
   week. **"The Petition was filed and served."** They were contacted by
   **Jane Rigby, Hyundai's internal counsel**: *"the prior $5k offer is
   still on the table … If that offer isn't accepted, her intention is to
   send the case to outside counsel to oppose the Petition."* Eugene's
   framing: *"either be up $2k after attorney fees and give back the car
   now that the lease is over, or down $3k with a chance to recover the
   full LL refund and reimbursement of your attorney fees if you win."*
2. **User 14:09Z:** "What is your advice in this situation?"
3. **Eugene 14:15Z** (msg `1a03e6d36e5fc4e2`): *"It comes down to your risk
   tolerance … winning the petition … involves essentially putting $5k on
   the table (the $3k you already paid plus the $2k you are walking away
   from) and rolling the dice. Also the additional risk of more attorney
   fees if we have to appear in court."*
4. **User 14:43Z** (msg `1a03e86f02c23e17`): willing to accept IF (1) the
   boilerplate is fixed — he cited "the waiver of my rights in California
   and the gag order" — and (2) ~$2,000 incidentals reimbursed.
5. **Eugene 14:59Z** (msg `1a03e952f14b6110`): *"1. I can ask about the
   changes to their boilerplate agreement. **Please specify exactly what
   you want taken out.** 2. I can request the reimbursement but it's likely
   to be a dealbreaker … The indication from the rep seemed to be $5k, take
   it or leave it."*
6. (Separately, Vicario's OOO auto-reply 14:10Z — matches "on vacation.")

### Open facts / cautions

- **Index number and as-filed papers still not in hand** — get them.
- **Which "$5k offer"?** The Jan 2026 letter had two variants: $5,388.51
  with surrender vs $5,000 cash-and-keep. Eugene's "give back the car"
  suggests the surrender variant, but this is UNCONFIRMED — the
  clarification is in the reply draft. Lease mechanics (month-to-month to
  11/23 hard wall) interact with any surrender.
- The user's "waiver of my rights in California" phrasing is imprecise —
  the clause is Ex09a ¶(j), the §1542 UNKNOWN-CLAIMS waiver reaching "any
  similar law of any state." The reply draft corrects this silently.
- Filing-fee refund on settlement ($250) is invited by NYSDRA's own 5/11
  letter — added as a low-cost ask.
- All communication is running through counsel — consistent with the
  no-independent-settlement clause. **Do not contact Rigby or HMA.**

### Deliverable

`materials/2026-08-26-settlement-clauses-to-Krukas-DRAFT.md` — answers
Eugene's "specify exactly" with Ex09a's own paragraph letters: strike
**(j)** (§1542 waiver — the clause refused in Sept 2025), **(i)**
(confidentiality/gag — removed or mutual+amount-only), **(h)** (third-party
indemnity); notarization indifferent once (j) is out; plus the $250 fee
refund, the corrected $1,793.43 figure with the Feb 20 "will not affect"
quote, and the which-variant clarification.

### Process lesson (recorded so it is not repeated)

**Gmail `search_threads` previews only the ~5 oldest messages of a thread.**
For any thread that may have new activity, `get_thread` (or a dated
`get_message`) is MANDATORY before reporting "no response" — Addendum 32's
false "filing unknown" conclusion came from skipping this.

---

## SESSION ADDENDUM 34 — 2026-08-26 (v2 of the clause-strike reply: as-is surrender + HMF lease closure added; Ex06's own ¶3 is the incidentals hook)

Per the user's instruction, the reply to Eugene/Michael was rewritten as v2
(same file, `materials/2026-08-26-settlement-clauses-to-Krukas-DRAFT.md`):

1. Strikes unchanged: Ex09a ¶¶ (j) §1542 all-states waiver, (i)
   confidentiality, (h) indemnity.
2. **NEW — as-is surrender package:** express no-charge clause for wear and
   tear / cosmetic damage / paint; **HMA responsible for ALL HMF lease-end
   charges** (disposition, excess wear, excess mileage) with written
   account-closure, no-deficiency, and no-negative-credit-reporting
   confirmations. Rationale on the record: the 2025 repurchase died partly
   on the body-repair precondition (Ex22, Addendum 13), and HMF is a
   separate entity — an HMA-only release would not stop later HMF billing.
3. **Ex06 read 2026-08-26 (verbatim):** its ¶3 — HMA "may reimburse,
   subject to proof, any related incidental damages/expenses, including but
   not limited to reasonable repair, towing, and car rental costs actually
   incurred" — makes the $1,793.43 an item inside Hyundai's own repurchase
   formula, no statutory assertion needed. Its ¶5 warns excess-mileage
   penalties "may not be included" — the exact surprise-charge category the
   as-is package excludes.
4. Variant clarification retained: Rigby's "$5k" vs the January letter's
   own $5,388.51 repurchase calculation.
5. **Record honesty, restated:** the January 2026 release contract was
   never received (Ex09b = duplicate of Ex06). The user was told this when
   he asked for "the second contract" — Ex06 (offer letter) + Ex09a (Aug
   2025 release, the amendment target) were delivered instead.

---

## SESSION ADDENDUM 35 — 2026-08-27 (Eugene's substantive reply: the $5k is A CHECK, not a repurchase; boilerplate strikes unlikely wholesale; "negotiate the cash higher")

User sent the clause-specification email 8/27 16:56Z (with the 8/10 HMA
receipts email attached), prefaced "if you were in my position, what would
you do?" Eugene replied 20:03Z (msg `1a044d28064da183`), verbatim points:

1. **Deal-structure CORRECTION:** *"The offer HMA made is not contingent
   upon you returning the vehicle… Their offer doesn't include a formal
   reacquisition of the vehicle. Just a check. You could conceivably buy
   out the vehicle instead if you wanted to."* His earlier "give back the
   car" meant only an ordinary lease return at maturity. **Consequences:**
   the $5,388.51-vs-$5,000 variant question dissolves (it is a flat $5k
   check); the as-is-surrender package (items 4–6) mostly dissolves — there
   is no surrender to HMA; lease-end wear/mileage exposure is an HMF matter
   that exists whether or not he settles.
2. **Boilerplate:** *"they won't typically agree to wholesale changes which
   take out substantive parts of the agreement… If there is a small change
   sometimes we can get it done."*
3. **Entity point:** *"HMA can't make any promise or representation on
   behalf of Hyundai Finance… a different entity."* And accepting a vehicle
   sight unseen *"would be legal malpractice for any lawyer to agree to."*
4. **His advice:** *"focus on negotiating the cash amount higher and not be
   so concerned about the release terms."* Presenting the full demand list
   *"we will assuredly end up getting a decision from the court. Which is
   fine! But I want to make sure you understand that strong likelihood."*
5. **The no-release exit:** *"If the arbitrator's decision is vacated you
   could then presumably have an arbitration hearing and get a mandated
   decision — which requires no Release Agreement."* (Note: that is the
   remand branch — separate retainer $6,000/$7,500, Addendum 26.)

**Analysis for the user (delivered in chat):** the correction is favorable
(pure additive cash; keep the car to 11/23); Eugene's cash-first advice is
sound negotiation but inverts the user's revealed priority — he walked from
$4,000 in Sept 2025 over these exact clauses, and the award records the
refusal was "not due to the $ amount." The sellable middle: one-sentence
scope qualifier limiting the release to claims arising from this vehicle +
amount-only confidentiality + one higher number (~$7,000 absorbing the
incidentals and fee) — the "small change + more cash" shape Eugene says
works. Decision is the user's.

---

## Addendum 36 (2026-08-28) — New PRIME DIRECTIVE rule; attachment capability mapped; signed Exhibit F finally verified

**1. New standing rule, hardcoded into CLAUDE.md PRIME DIRECTIVE ¶4 (user's
order, 2026-08-28):** any decision, analysis, or recommendation resting on
incomplete information (an unreadable attachment, an uninspected document, an
unverified text, testimony-only facts) must disclose that **in the deliverable
itself, at the point the conclusion is stated** — not only in the log. Name
what's missing, what was relied on instead, and how the gap could change the
conclusion.

**2. Gmail attachment capability, established by test:** there is no
attachment-download tool, but `get_message` with `messageFormat: "RAW"`
returns the complete base64 MIME, and attachments decode locally with
Python's `email` module. Verified working on a 32KB message and on the
**545KB Zoho email `19ffd78085ee0b41`**; verified FAILING ("MCP server Gmail
session expired", 3 attempts) on the user's **9.3MB email `1a04427f59b714ba`**.
The ceiling sits somewhere between ~545KB and 9.3MB. For oversized emails:
ask the user to upload the attachment. (The 9.3MB email's own attachment
content was already held locally and sha-verified —
`materials/2026-08-05-HMA-Executive-Office-receipts-attachment.pdf`,
sha ff257b8f.)

**3. Signed Exhibit F affirmation independently verified — Addendum 32's
caveat CLOSED.** Extracted from the Zoho completion email (8/13/2026,
Vicario, "Exhibit F - Hu Client Aff.pdf has been signed"), 2 pp, 208,147
bytes, sha256 107fe56f…, preserved to
`materials/Hu_v_HMA_ExF_Client_Affirmation_SIGNED_2026-08-13.pdf`.
Checked against the Addendum 30 comments:
- ¶1 VIN **KM8KNDDF9RU253237** — the missing "R" is FIXED ✓
- ¶15 now reads "**At the hearing,** Hyundai did not present any evidence or
  provide any documents." — qualifier added ✓
- ¶8 typo fixed: "about two-hundred (200) days" (was "200 hundred") ✓
- ¶18 now "Hyundai did not **prove** any affirmative defenses" — resolves
  the "attempt" concern by a different (acceptable) route ✓
- Caption reads HYUNDAI MOTOR AMERICA ✓; ¶1 lease date May 23, 2024 ✓
- ¶7's 8,151 miles reconciles: 8,148 at drop-off (user's Q16) + 3 mi on RO
  #358530 = 8,151 at pickup ✓
- Zoho Sign Document ID stamped on both pages. ⚠ One per-¶4 disclosure: the
  text layer shows the affirmation date and signature lines blank — the
  signature/date are presumably image overlays (not text-extractable), so
  visual confirmation of the executed signature block has not been done.
  The email is the "document completed / digitally signed" copy, which is
  strong but indirect evidence of execution.

**Environment note:** the container was reclaimed since the packet build —
pypdf/pikepdf/reportlab gone, `pdftotext` absent, and the system
`cryptography` package broken (`_cffi_backend` missing — `pip install cffi`
fixes it, then pypdf imports).

---

## Addendum 37 (2026-08-28) — DECISION: terms-first counter drafted; the scratch/dent fact; lease wear standard unreadable

**User's decision:** go with the terms-first package. His stated reading of
Eugene's advice — accept boilerplate + negotiate higher (~$7,000 absorbing
$1,793.43 + $250); ask which small changes are removable; confidentiality
mutual and amount-only — adopted with one correction: the package does not
"accept the boilerplate first," it asks for the two small changes and the
number in the same counter (scope-qualifier sentence + mutual amount-only
confidentiality + $7,000). The wholesale ¶(j)/§1542 strike and the ¶(h)
indemnity fight are dropped.

**New fact [user statement, 8/28 — no document]:** the vehicle has minor
paint scratches and dents; user estimates **<$500** exposure at lease
turn-in; not disclosed to anyone. Handling: by **price, not terms** — the
as-is package is moot under the flat-check structure (Addendum 35: no
surrender to HMA; HMA cannot bind HMF; lease-end wear is an HMF matter
either way). Options given: send at $7,000; ask $7,500 as buffer; or buyout
(no turn-in inspection at all). No duty to volunteer condition in a
flat-check settlement; make no affirmative condition representation if one
appears in the final agreement.

**⚠ Disclosure (PRIME DIRECTIVE ¶4):** the lease's excess-wear-and-use
standard is **UNREAD** — Ex01 pp. 5–8 are image-only scans (pypdf: 0 chars),
no OCR tooling in this environment (`tesseract`/`pytesseract` absent), and
the old `_extracted` text holds only the first-page form fields. Whether
minor scratches/dents are even chargeable under the lease's own threshold is
unverified; general lease-industry norms were NOT asserted as fact. To
clear: user reads his paper lease's wear section or uploads a legible copy.

**Deliverable:** `materials/2026-08-28-settlement-counter-to-Krukas-DRAFT.md`
(v1) — two small term asks + $7,000 built up from HMA's own documents
($5,000 + $1,793.43 via Ex06 ¶3 + $250 via NYSDRA letter = $7,043.43,
rounded down). $5,388.51 question dropped as moot. Awaiting user review;
the $7,000-vs-$7,500 choice is flagged in the handling notes.

---

## Addendum 38 (2026-08-28) — HMF Lease-End Kit reviewed; Ex15 re-read in full: the scratch worry dissolves, and three better facts surface

User uploaded the **HMF Lease-End 120-Day Kit** (4-spread brochure,
HMF-SC-LeaseEnd120-DM-0221, read in full — text + visual). Cross-read with
the **full text of Ex15** (Lease Term Extension Agreement, all 4 pages).

**1. Acceptable wear per HMF's own published standard:** scratches < 4",
dings/dents < 4", windshield cracks < 2", window/paint chips < 1/2", tire
tread ≥ 1/8". The user's minor scratches/dents ("not noticeable at a casual
glance," est. <$500 — Addendum 37) are almost certainly **chargeable at
$0**. ⚠ Brochure is marked ADVERTISEMENT, printed 2021, non-binding; final
charges come from a formal post-turn-in inspection; the contractual
standard ("Lessor's standards for normal use," Ex15 ¶2) lives in the
lease's still-unread fine print. Mitigation: free non-binding
pre-termination inspection — Lease-End Advisor (855) 463-5378; self-assess
at HMFUSA.com/lease-end. **Counter stays at $7,000** (draft updated).

**2. Ex15 ¶2 — mid-extension return carries NO early-termination penalty:**
"If your Lease terminates after the Original Maturity Date but before the
Maximum Maturity Date, for any reason, the Early Termination provisions of
your Lease will not apply and the termination shall be treated as a
full-maturity termination." Return before the next month's due date (the
23rd) or be billed the next month; payments are NOT prorated (¶5); must
call (844) 363-7477 before returning. **Consequence: once a settlement
closes, return at the next monthly boundary and stop paying $314/mo — up
to ~$942 saved vs. riding to 11/23.** (If NO settlement: keep the car —
standing preservation — decision needed by ~late October.)

**3. Ex15 ¶3 — buyout wipes ALL turn-in charges and gets credit for
extension payments:** "If you exercise your purchase option, you will not
owe Lessor for excess mileage or excess wear" (and the disposition fee
applies only "if the lessee does not purchase"); "any monthly payments you
make during the extended lease term (excluding the portions allocable to
taxes and rent) will be deducted from the Vehicle purchase price" — i.e.,
each $297.26 base payment since 5/23/26 reduces the buyout price. Quote:
(855) 537-8542.

**4. Known turn-in costs regardless of wear:** disposition fee "specified
in the lease contract," brochure says up to $400 (Ex01 form fields show a
400.00 — probable but unlabeled); excess mileage $.20/mi over allowance —
allowance number unread (Ex01 fine print), but odometer 11,230 on
2/18/2026 (RO #370267) makes excess mileage a non-issue under any
plausible allowance, and Ex15 ¶2 adds 1/12 of the annual allowance per
extension month.

**5. Ex15 ¶7 adds a MANDATORY ARBITRATION clause (FAA, AAA/JAMS, class
waiver) to the HMF lease** — any future dispute with HMF/HLTT over
lease-end charges goes to arbitration, EXCEPT "we will not choose to
arbitrate any claim you bring in small claims court" — the small-claims
route for a bogus wear bill is expressly preserved. (HMF ≠ HMA; no
apparent effect on the Article 75 case.)

**6. Turn-in checklist (brochure):** return only to an authorized Hyundai
dealer; all original equipment present (EV charging cable, both fobs);
remove toll tag; cancel autopay after the final payment; keep insurance in
force through return (Ex15 ¶4); cancel/transfer the NJ plates — liability
for tickets/tolls continues until done.
