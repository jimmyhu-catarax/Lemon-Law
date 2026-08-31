export const meta = {
  name: 'case-research',
  description: 'Fan out lemon-law research questions to parallel researchers, verify key claims, synthesize a cited memo',
  whenToUse: 'When several independent legal research questions need answering. args: array of research-question strings.',
  phases: [
    { title: 'Research', detail: 'one case-researcher agent per question' },
    { title: 'Verify', detail: 'adversarial check of each key claim' },
    { title: 'Synthesize', detail: 'merge confirmed findings into one memo' },
  ],
}

const FINDINGS_SCHEMA = {
  type: 'object',
  properties: {
    question: { type: 'string' },
    findings: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          claim: { type: 'string' },
          source: { type: 'string' },
          jurisdiction: { type: 'string' },
          verified: { type: 'boolean' },
        },
        required: ['claim', 'source', 'jurisdiction', 'verified'],
      },
    },
  },
  required: ['question', 'findings'],
}

const VERDICT_SCHEMA = {
  type: 'object',
  properties: {
    holds: { type: 'boolean' },
    reason: { type: 'string' },
  },
  required: ['holds', 'reason'],
}

const questions = Array.isArray(args) ? args : [args].filter(Boolean)
if (!questions.length) {
  return { error: 'Pass args as an array of research-question strings.' }
}

log(`Researching ${questions.length} question(s)`)

const researched = await pipeline(
  questions,
  (q, _item, i) =>
    agent(
      `Research this question for the Lemon-Law case (see CLAUDE.md for case context): ${q}\n` +
        'Check CLAUDE.md and materials/_extracted/ first, then search the web for primary sources. ' +
        'Return each finding as a claim + source URL + jurisdiction, and mark verified=false ' +
        'for anything not confirmed in a primary source.',
      { label: `research:q${i + 1}`, phase: 'Research', schema: FINDINGS_SCHEMA, agentType: 'case-researcher' }
    ),
  (result, q) =>
    parallel(
      result.findings.map(f => () =>
        agent(
          `Adversarially verify this legal-research claim. Try to refute it by checking the cited source ` +
            `and at least one independent primary source.\n\nClaim: ${f.claim}\nCited source: ${f.source}\n` +
            `Jurisdiction: ${f.jurisdiction}\n\nDefault to holds=false if the source does not clearly support the claim.`,
          { label: `verify:${f.claim.slice(0, 40)}`, phase: 'Verify', schema: VERDICT_SCHEMA, agentType: 'case-researcher' }
        ).then(v => ({ ...f, question: q, verdict: v }))
      )
    )
)

const all = researched.filter(Boolean).flat().filter(Boolean)
const confirmed = all.filter(f => f.verdict && f.verdict.holds)
const rejected = all.filter(f => !f.verdict || !f.verdict.holds)
log(`${confirmed.length} claims confirmed, ${rejected.length} refuted or unverifiable`)

phase('Synthesize')
const memo = await agent(
  'Write a research memo in markdown for the Lemon-Law repo synthesizing these CONFIRMED findings, ' +
    'grouped by question, with source URLs cited inline and jurisdiction noted per rule. ' +
    'List refuted/unverifiable claims in a final "Not confirmed" section so they are not silently dropped. ' +
    'Return only the memo markdown.\n\nConfirmed:\n' +
    JSON.stringify(confirmed, null, 2) +
    '\n\nRefuted or unverifiable:\n' +
    JSON.stringify(rejected.map(({ verdict, ...f }) => ({ ...f, reason: verdict && verdict.reason })), null, 2),
  { label: 'synthesize-memo', phase: 'Synthesize' }
)

return { memo, confirmed: confirmed.length, rejected: rejected.length }
