# Competitor Questionnaire Scouting: Google Forms (viewform)

When scouting whether a competitor/proposed study already exists, researchers
often share a Google Form link (preprint-stage instrument). The `viewform`
page is JS-rendered, but ALL questions, scales, and options ship in one
embedded JSON blob. Never drive a browser for this.

## Recipe

1. Fetch the HTML with curl (plain UA suffices, no auth):
   `curl -sL -m 60 -A "Mozilla/5.0" "<viewform-url>" -o gform.html`
2. Extract the page-state blob via regex + `json.loads`:
   `FB_PUBLIC_LOAD_DATA_\s*=\s*(\[.*?\]);` (DOTALL)
3. Walk `data[1][1]` — a list of sections. Strings nest arbitrarily deep,
   so collect with a recursive `flat_text(x)` gathering every non-empty
   string from nested lists, dedupe per section preserving order.
4. Print section index + FULL strings (no truncation) — recover titles,
   Likert scale labels (5=SS..1=STS), and options. Also print the raw
   HTML `<p><strong>X...</strong></p>` blocks for complete item wording.
5. Record findings in the topic's `reading/` folder as a competitor note
   (structure, methodological flaws, overlap vs our construct, action).

## Pitfalls

- Section entries are NOT uniform question objects: headings, consent items,
  identity fields, and Likert items share the same nesting. Treat every
  section as text first; do not assume `sec[1]` is a question array
  (blind indexing raises IndexError on headers).
- `web_extract` returns only title + preamble (~1KB), never the items.
  Go straight to curl + embedded JSON.
- Quick-preview prints cut item text at ~120 chars — the full strings
  require the deduped per-section dump, not the first-pass preview.
- Verify the competitor title against web search before treating it as
  a threat: an instrument circulating does not mean a paper has shipped.

## After the instrument: check for a published twin in the same cluster

- A circulating form is often the SECOND entrant: sweep Garuda (national)
  and web search with the form's exact title keywords before scoring threat.
  A published paper with a near-identical title + DV pair in the same
  population means the cluster is already occupied — score the PUBLISHED
  paper as the real threat, the form as a second mover.
- When sweeping, run both academic angles (Garuda/SINTA for worker or
  student populations) and the agentic/industry angle (vendor blogs, policy
  notes, Work Trend Index / Hopes & Fears style reports). Zero empirical
  hits on the agentic/harness side is itself evidence — record it as moat,
  not as absence of data.
- National student-population hits (thesis, learning-outcome studies) are
  context, not direct competitors to a worker-population design — file them
  as landscape, never as foundation citations.

## Reading the threat (novelty overlap)

- Map the competitor instrument to YOUR construct dimensions explicitly
  (adoption spectrum? intensity? DV = intention vs behaviour vs perceived
  performance?) — overlap is almost always partial.
- Score threat on four explicit axes, not gut feel: (1) research question
  class (causal-attributive X→Y vs descriptive-distributional), (2) technology
  scope (chatbot-only vs chatbot+harness ladder), (3) population (programmer /
  student subset vs cross-sector knowledge workers), (4) measurement form
  (agreement-with-benefit Likert vs frequency/proportion/delegation counts).
  Threat is LOW when all four differ even if keywords match; it rises only if
  your design also claims the competitor's DV (e.g. performance gain).
- Industry reports (adoption percentages, daily/agentic-use rates) are
  symptom-background material for a problem statement, never competitor
  literature — keep them in a separate section of the note.

## Reserve-file rule (user preference)

- When the user asks to keep competitor/landscape intel "just in case",
  write ONE reserve note under the topic's `reading/` folder (bibliography +
  results + threat score + reuse-as-material list) and LEAVE the main draft
  untouched. Offer the draft-insert as a follow-up question; never auto-edit
  the problem statement from a landscape sweep.
- A form is never bibliography: cite a published twin formally; mention a
  live form only as "a running study (public questionnaire, year)" with no
  reference-list entry.
