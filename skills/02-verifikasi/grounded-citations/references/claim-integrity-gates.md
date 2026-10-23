# Claim-Integrity Gates (I-D-A-K)

Adapted for empirical social-science / business research (interview, survey,
case study) from the failure-mode taxonomy in **Lu et al. (2026), _Towards
end-to-end automation of AI research_, Nature 651:914-919** (DOI
`10.1038/s41586-026-10265-5`), as catalogued in the `academic-research-skills`
project. The original modes are framed around code experiments; the mapping
below re-points each one at a non-technical empirical study. Source-lineage
and counterexample gates are adapted from the `hermes-researcher-agent`
project's evidence gate.

The point of the gates: **these failures look like competent work.** A draft
with an invented percentage reads exactly like a draft with a real one. A
miscited reference reads like a correct one. You cannot catch them by reading
more carefully — you catch them by checking the claim against its source file.

Run the gates before a deliverable is called done, not after a reviewer finds
the problem.

---

## The four gates

| Gate | Question it answers | Modes it covers |
|---|---|---|
| **I — Identitas** | Does every reference exist and say what we claim? | Citation integrity |
| **D — Data** | Is every number/quote traceable to its source file, right denominator? | Analysis slip, invented result |
| **A — Argumen** | Is the causal story supported by the design, not a proxy? | Proxy reliance, artifact-as-insight |
| **K — Kerangka** | Does the method text match what was done, and the framing match the question? | Method fabrication, frame-lock |

Mnemonic: **I-D-A-K** (reads like "tidak") — Identitas, Data, Argumen, Kerangka.

---

## The modes, adapted

### I — Identitas

**M1. Hallucinated citation.** A reference that does not exist, is miscited
(wrong year/venue/authors), or is attributed a finding it does not make.
- Every reference in the draft resolves to a real record (DOI/arXiv id) in the
  source file it came from — checked live, not from memory.
- The cited source actually contains the sentence the claim depends on; open
  the `_fulltext.txt` / extracted page and quote it.
- Sample counts and effect figures are quoted with the source's own wording,
  not a paraphrase that shifts the meaning.
- Corpus-scale evidence that this is not paranoia: Zhao et al. (2026) estimate
  ~146,932 hallucinated citations for 2025 alone across arXiv/bioRxiv/SSRN/PMC.

### D — Data

**M2. Analysis slip passing self-review.** A miscount, wrong denominator,
wrong cell, or dropped row that produces a plausible but wrong figure.
- For every number in the draft: which file/script produced it? If no saved
  artefact, flag it.
- Suspiciously round or suspiciously clean values (exactly 50%, zero variance,
  identical counts across subgroups) are the classic tell of a broken pipeline
  or a copy error — re-derive them.
- A subgroup count is anchored to ITS OWN base, never the full sample.

**M3. Invented result / quote.** A finding, quote, or percentage that no
participant actually produced — written to fit the narrative.
- Every participant quote is verbatim from the transcript, with an ID
  (P07) and a line you can re-open.
- Every percentage has its numerator and denominator recoverable in the data.
- "We ran N interviews" matches the number of transcripts in the folder.

### A — Argumen

**M4. Proxy / shortcut reliance.** The reported effect is real but driven by a
surrogate, not the mechanism claimed (the colour-biased-MNIST failure in
domain terms: a cost finding driven by something that only correlates with
cost).
- Is there a rival explanation that the design rules out? If not, the causal
  claim is not supported by this study.
- The claim's evidence measures the construct itself, not something merely
  correlated with it.
- For cost claims: the measure is an actual usage-based charge (API, credits,
  execution), not a self-reported impression standing in for it.

**M5. Artefact reframed as insight.** An unexpected result caused by a coding
error, a misclassified theme, or a data-entry glitch gets narrated as a novel
finding.
- Every "surprisingly", "unexpectedly", "counterintuitively" claim: could a
  literature reference have predicted the opposite? If not, re-check the data.
- First-pass surprises are higher risk than surprises that survive re-coding.

### K — Kerangka

**M6. Method fabrication.** The Methods section describes procedures,
sampling, or instruments that were not what was actually done.
- Every method detail (N, sampling frame, instrument, period, analysis steps)
  appears in the actual protocol/notes, not reconstructed from what a
  reasonable study *would* have done.
- No preprocessing or step the author cannot point to.

**M7. Frame-lock.** An early commitment (research question, construct choice,
analysis lens) that the study can no longer back out of.
- If you knew at the start what you know now, would the question or construct
  change?
- "In hindsight" / "we later realised" in the discussion are the tells.
- If flagged, the honest move is to return to the framing step, not to push
  the paper through.

---

## Outcomes per mode

For each mode, record one of three states so the gate is auditable:

- **CLEAR** — evidence rules the mode out; record the evidence briefly.
- **SUSPECTED** — a detection question returned a concerning answer; surface it.
- **INSUFFICIENT EVIDENCE** — cannot rule in or out without inputs not yet
  provided; surface and block the draft until resolved.

Modes **I, D-2, D-3 and K-6** are hard blocks: if they are not CLEAR, the
deliverable does not ship. The rest may ship flagged, with the caveat visible.

---

## Source lineage (independence, not volume)

Three articles reporting the same announcement are ONE piece of evidence.
- Corroboration requires sources with independent origins; a press-release
  reprint, a mirror, and an aggregator post count as one lineage.
- When all sources share one origin, say so and downgrade confidence rather
  than letting repetition read as replication.
- Same for figures: if two sources report the same number, check whether the
  second is quoting the first.

## Counterexample gate

Before a decision-relevant claim ships, look for evidence AGAINST it. If none
is found, record that explicitly ("no contrary source found in this sweep") —
a one-sided sweep is a coverage gap, not a confirmation.

---

## Route selection (research depth)

Pick the depth before collecting, so the effort matches the stake:

- **Quick fact** — one lookup, one source; no deliverable.
- **Deep research** — multi-source synthesis with a grounded deliverable;
  register every source in the ledger.
- **Repo / tool check** — GitHub API metadata + README + release history;
  never judge a repository by star count alone.
- **Community pain** — what practitioners report (Reddit, forums, issues);
  label it sentiment, not measurement.
- **Comparison / decision brief** — end in a recommendation with the trade-off
  and the coverage gap stated, never a raw link dump.
