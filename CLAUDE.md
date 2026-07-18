# Lemon-Law

Jimmy's lemon-law case against Hyundai. This repository holds case documents,
research notes, timelines, and correspondence drafts.

## Repository layout

- `docs/` — case documents: demand letters, complaints, correspondence drafts
- `research/` — legal research notes and statute summaries
- `evidence/` — repair-order summaries, timelines, and supporting records

(Directories are created as content is added.)

## Multi-agent orchestration

This repo is configured for multi-agent work via custom subagents and saved
workflows.

### Subagents (`.claude/agents/`)

- **case-researcher** — read-only research agent for statutes, case law, and
  lemon-law procedure (California Song-Beverly Act, Magnuson-Moss, Hyundai
  warranty/BBB Auto Line process). Spawn several in parallel for independent
  research questions.
- **doc-drafter** — drafts and revises case documents (demand letters,
  timelines, complaint sections) in `docs/`, matching the tone and structure
  of existing documents.
- **doc-reviewer** — adversarial reviewer for drafts: checks factual claims
  against files in `evidence/` and `research/`, flags unsupported assertions,
  missing statutory elements, and tone problems. Read-only; reports findings
  without editing.

### Saved workflows (`.claude/workflows/`)

Run these with the Workflow tool by name, passing `args` as shown:

- **case-research** — fans out research questions to parallel case-researcher
  agents, adversarially verifies each key claim, and synthesizes a cited
  research memo. `args`: array of research-question strings.
- **doc-review** — reviews one document across accuracy, completeness, legal
  sufficiency, and tone dimensions, verifies each finding, and returns only
  confirmed issues. `args`: path to the document to review.

### Conventions

- Research output goes in `research/` as dated markdown files
  (`research/YYYY-MM-DD-topic.md`) with sources cited inline.
- Drafts in `docs/` are working documents — never send or file anything
  without Jimmy's explicit review.
- Nothing in this repo is legal advice; agents summarize and draft, a lawyer
  decides.
