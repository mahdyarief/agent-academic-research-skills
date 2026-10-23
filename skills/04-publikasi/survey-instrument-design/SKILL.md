---
name: survey-instrument-design
description: "Use when writing or revising survey questionnaire items."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [survey, questionnaire, instrument, research-methods, wording, bias]
    related_skills: [google-forms, thesis-proposal, dosen-ready-academic-prose]
---

# Survey / Questionnaire Instrument Design

Craft and revise the items a **respondent** actually reads (Google Form, Qualtrics,
paper): labels, wording, explanations, and how much to explain. Mechanics of
building the form (Forms API, branching) live in `google-forms`.

## When to Use

- Writing or revising items for a respondent-facing survey or questionnaire.
- Deciding how much explanation, example, or illustration to attach to an item.
- Turning an academic construct into a label real (non-expert) people will read.

## Rules

1. **Keep the internal construct name separate from the respondent-facing label.**
   The construct in the thesis/matrix/paper keeps its standard term (e.g. "net
   benefit", DeLone & McLean). The form label is written for the respondent. They do
   not have to match — do not let thesis terminology leak into the form verbatim.
2. **When a literal translation of a standard term reads oddly to a lay reader,
   surface the original term in the label** — e.g. `Manfaat Bersih (Net Benefit)`.
   The parenthetical makes it read as deliberate terminology, not a clumsy
   translation. A bare literal calque (just "manfaat bersih") reads as an error to a
   non-expert and will get flagged.
3. **No ALL-CAPS for emphasis in respondent-facing text.** A shouted word ("SETELAH")
   reads as unnatural to lay readers. Write normal sentences.
4. **Examples/illustrations in an item are a bias trade-off, not a free win.** They
   aid comprehension but anchor answers (respondents gravitate toward the example)
   and invite socially-desirable responses. For harmless items a worked example is
   fine; for sensitive items (complaining, counterproductive behaviour, anything
   socially undesirable) prefer ONE neutral instruction at the section head —
   "Jawab sesuai kebiasaan Anda yang sebenarnya, bukan yang ideal. Tidak ada jawaban
   benar atau salah." — instead of concrete per-item examples.
5. **Flag the trade-off, do not decide it silently.** When adding an example, anchor,
   or scale descriptor, state the cost (anchoring / social desirability) in the reply
   and offer the neutral alternative.
6. **A wording change touches every artifact that quotes the item — sync them all in one
   change.** Not just the master markdown and the live form: also the build script (if it
   keys sections/items by display title), the analysis matrices, and the RQ / rumusan-
   masalah docs. After a change, grep the whole project for the removed text (a
   distinctive number or phrase) and fix every hit. Divergence stays invisible until a
   rebuild silently reverts the live form or a matrix contradicts the instrument.
7. **Verify the rendered text, not just a 200.** After an update, GET the item back
   and read the description/label as the respondent would.
8. **No meta-label preamble in an item's help text.** Do not open a clarification with
   "Maksudnya:", "Catatan:", "Penjelasan:". Write it as a plain sentence that continues
   from the item, so the help reads as part of the question, not as an attached
   researcher note. (This user rejects the label outright — it makes the text feel like
   a separate block.)
9. **For a numeric item, the worked example must NOT terminate in the answer value.**
   An example ending "...jadi tulis 1,5" hands respondents the number to copy: the
   unsure ones write it verbatim, the sure ones anchor near it, so the distribution
   spikes on one value and the item's variance collapses — worst when that item feeds a
   derived variable (e.g. net = A − B). Keep the mechanics (unit, direction, sign, a
   scenario) but state only that the *difference* is what gets submitted; the
   illustration teaches how to compute, not what to enter. Scenario inputs still anchor
   weakly — pick non-round numbers and check for a single-value spike at pilot (n≈30).
   When the item has a companion/paired item that carries no example at all, drop the
   example entirely (definition + unit + sign rule only) rather than keeping a scenario:
   that makes the two items' measurement quality symmetric. A worked scenario also
   implies a kind of work (e.g. report-writing) that other occupations cannot map onto.

10. **Do not ask respondents to compare groups — derive the group, compare the outcome at
    analysis.** A between-subjects question ("is X better than Y?") never belongs on the
    form; a self-reported comparison is subjective, not a test. Instead: one discriminator
    item marks the group (a depth/usage choice whose top option is the interest group), a
    short follow-up verifies membership for the rare arm, and a common outcome block is
    filled by BOTH groups. The comparison is a group-difference test run later. Plan to
    over-sample the rare arm or the test will be underpowered.

11. **Screening gates: one criterion per question; enumerate the eligible options.** A
    combined eligibility item ("bekerja AND berdomisili di X?") is double-barreled —
    someone meeting only one half cannot answer honestly. Split each criterion into its
    own question. A region/geography gate should be a radio that ENUMERATES the
    sub-regions (Kota X, Kabupaten Y, … "Di luar …") with out-of-scope options routed to
    a closing section: you get a sample-composition column for reporting instead of a
    bare Ya/Tidak, and the options themselves word the inclusion definition for the
    respondent. Remember the gate's limit: an anonymous open-link survey cannot verify
    location — the distribution channel is the real control. When the user asks how to
    guarantee respondents are from region X, answer with the three layers: screen (gate),
    distribute (channel), verify (column).

## Working with this user

- He reviews at **construct level, not language level** — present terminology options
  with a clear recommendation and let him pick, rather than silently rewriting.
- He reads as a layperson and rejects jargon that "rasanya aneh" when read cold.
  Run a lay-readability pass before calling wording final.
- Technical/academic terms stay; the *form* is what gets made plain.
