# Tooling — legal plugins

> Moved out of `CLAUDE.md` on 2026-08-03. Which plugin to reach for is
> task-shaped, not something every session needs resident. **The one part that
> stayed in the brief is the Prime Directive guardrail** — a "never do X" rule
> must not live behind a lazy load, or it may not be present when it matters.

**Read this before invoking any legal plugin surface**, and before installing
or enabling a `claude-for-legal` plugin under the standing permission.

⚠ **Local config is NOT the source of truth for plugins.** claude.ai-catalog
plugins do not write to `enabledPlugins` or `pluginUsage` in `~/.claude.json` —
both read `{}` while seven plugins are enabled. Use the `ListPlugins` /
`SearchPlugins` tools, never the local files. (A `/doctor` pass on 2026-08-03
reported "no plugins installed" off local config and was **wrong**.)

**Enabled as of 2026-08-04** (claude.ai catalog): `legal`, `pdf-viewer`,
`brand-voice`, `design`, `finance`, `enterprise-search`,
`cowork-plugin-management`.

## TOOLING — the `legal` plugin (enabled; use it where it fits)

**Check it is loaded at session start** and reach for it whenever the task is
contract-shaped. Enabled from the claude.ai catalog (`knowledge-work-plugins`);
it does not appear in local `enabledPlugins`, so absence there is not evidence
it is off.

Surfaces: `/legal:review-contract`, `/legal:triage-nda`, `/legal:brief`,
`/legal:vendor-check`, and the `legal:legal-risk-assessment` skill.

**Where it genuinely fits this matter:**
- **`/legal:review-contract`** on `materials/Hu_Article_75_Retainer.pdf`, on any
  revised retainer counsel sends, and on any HMA settlement release (Ex09a and
  whatever replaces it). Clause-level review of a contract is exactly its job.
- **`legal:legal-risk-assessment`** when weighing a settlement term or a fee
  structure — e.g. the four "cooperation" triggers, the reimbursement waterfall.

**Where it does NOT fit — do not force it.** This plugin is built for in-house
and transactional counsel: contracts, NDAs, vendor diligence. It carries **no
NY lemon-law, GBL § 198-a, or CPLR Article 75 knowledge.** Do not use it for the
petition, the memorandum of law, case law, or statutory text. For those, the
project's own `case-researcher` / `doc-drafter` / `doc-reviewer` agents and the
`case-research` / `doc-review` workflows are the right tools.

⚠ **The PRIME DIRECTIVE outranks the plugin.** Nothing it outputs is a source.
No figure, date, quotation, clause reading, or citation it produces enters a
filing — or a message to counsel — without verification against the underlying
document. Treat its output exactly as you would a draft from a colleague who
has not seen the file.

### The `claude-for-legal` marketplace — NOT INSTALLED

⚠ **Corrected 2026-08-04.** An earlier version of this file said these were
"installed but not enabled." **They are not installed.** `litigation-legal` and
`cocounsel-legal` exist in the `claude-for-legal` marketplace and both read
`enabled: false`. An install card was rendered 2026-08-03 and again 2026-08-04;
installation happens **only when the user clicks it** — no tool available to
this project can install a plugin directly.

**Confirm current state with `SearchPlugins` before relying on either.**

Of the two, **`litigation-legal` is the one worth having**; `cocounsel-legal` is
speculative (the catalog exposes no description or skill list for it, and the
co-counsel role is now filled by actual retained counsel).

✅ **STANDING PERMISSION (granted 2026-08-03): once installed, enable either one
yourself when the task calls for it.** No need to stop and ask. Conditions:
1. **Say so in the same turn** — name which one and why, so the user can turn it
   back off. Enabling is reversible via `/plugin`.
2. **Enable only what the task needs.** Do not switch both on by reflex; the
   marketplace also carries `product-legal`, `ip-legal`, `employment-legal`,
   `regulatory-legal`, `commercial-legal`, `legal-clinic`, and
   `legal-builder-hub` — **none of which touch this matter.** Leave them off.
3. ⚠ **The PRIME DIRECTIVE still governs.** These are litigation-shaped tools,
   which makes them *more* dangerous to this project than the transactional
   `legal` plugin, not less: output that looks like a case cite or a pinpoint is
   exactly what must never reach a filing unverified. **Nothing either plugin
   produces is a source.** Verify against the Official Reports, the statute, or
   the exhibit — every time.
