export const meta = {
  name: 'doc-review',
  description: 'Review one case document across four dimensions, adversarially verify findings, return confirmed issues',
  whenToUse: 'Before a draft in docs/ is considered done. args: path to the document to review.',
  phases: [
    { title: 'Review', detail: 'four parallel doc-reviewer lenses' },
    { title: 'Verify', detail: 'refute-or-confirm each finding' },
  ],
}

const FINDINGS_SCHEMA = {
  type: 'object',
  properties: {
    findings: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          severity: { type: 'string', enum: ['blocker', 'should-fix', 'nit'] },
          location: { type: 'string' },
          problem: { type: 'string' },
          evidence: { type: 'string' },
        },
        required: ['severity', 'location', 'problem', 'evidence'],
      },
    },
  },
  required: ['findings'],
}

const VERDICT_SCHEMA = {
  type: 'object',
  properties: {
    real: { type: 'boolean' },
    reason: { type: 'string' },
  },
  required: ['real', 'reason'],
}

const docPath = typeof args === 'string' ? args : args && args.path
if (!docPath) {
  return { error: 'Pass args as the path of the document to review, e.g. "docs/demand-letter.md".' }
}

const LENSES = [
  { key: 'facts', prompt: 'source verification: every date, mileage figure, RO number, dollar amount, and quotation must trace to CLAUDE.md verified tables or a file in materials/' },
  { key: 'legal', prompt: 'citation and legal sufficiency: statutory elements, deadlines, and every citation checked against the CLAUDE.md verified-citations table and its noted limits' },
  { key: 'consistency', prompt: 'internal consistency: dates and figures must agree with the timeline and with each other' },
  { key: 'tone', prompt: 'tone and risk: threats, emotional language, admissions against interest, overstated legal certainty' },
]

log(`Reviewing ${docPath} across ${LENSES.length} dimensions`)

const results = await pipeline(
  LENSES,
  lens =>
    agent(
      `Review the document at ${docPath} focusing ONLY on ${lens.prompt}. ` +
        'Report each problem with severity, exact location/quote, what is wrong, and which repo file (or absence of one) supports the finding.',
      { label: `review:${lens.key}`, phase: 'Review', schema: FINDINGS_SCHEMA, agentType: 'doc-reviewer' }
    ),
  (review, lens) =>
    parallel(
      review.findings.map(f => () =>
        agent(
          `Adversarially verify this review finding on ${docPath}. Re-read the document and the cited repo files ` +
            `and try to REFUTE it. Default to real=false if the document actually handles this correctly.\n\n` +
            JSON.stringify(f, null, 2),
          { label: `verify:${lens.key}`, phase: 'Verify', schema: VERDICT_SCHEMA, agentType: 'doc-reviewer' }
        ).then(v => ({ ...f, lens: lens.key, verdict: v }))
      )
    )
)

const all = results.filter(Boolean).flat().filter(Boolean)
const confirmed = all.filter(f => f.verdict && f.verdict.real)
const order = { blocker: 0, 'should-fix': 1, nit: 2 }
confirmed.sort((a, b) => (order[a.severity] ?? 3) - (order[b.severity] ?? 3))

log(`${confirmed.length} of ${all.length} findings confirmed`)
return { document: docPath, confirmed, dismissed: all.length - confirmed.length }
