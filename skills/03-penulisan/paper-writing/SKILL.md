---
name: paper-writing
description: "Use when writing journal papers or IMRAD manuscripts."
version: 0.1.0
author: Mahdy, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [paper, imrad, writing, literature-matrix, publish]
    related_skills: [journal-scouting, indo-journal-scouting, thesis-proposal]
---

# Journal Paper Writing (IMRAD)

Turn a finished study (data + analysis in hand) into a submission-ready
manuscript, Indonesian or English, aimed at Garuda/SINTA/Scopus-indexed venues.
Do NOT use for proposal-stage work (see `thesis-proposal`) or paper discovery
(`journal-scouting`).

## When to Use
- Mahdy has results/data and says "bikin papernya", "tulis jadi jurnal", "draft manuskrip".
- Adjusting an existing draft to a target journal's IMRAD requirements.

## Paper types & structure
Standard original article = IMRAD: Introduction, Methods, Results, And Discussion,
plus Title / Abstract / Keywords / Conclusion / References / Supplementary.
Systematic review = PRISMA-compliant flow (diagram + checklist).

## WRITING order (not reading order)
1. Methods & Results — write as a pair (most objective first)
2. Introduction (final para) & Conclusion — write as a pair
3. Discussion
4. Introduction (beginning)
5. Abstract (250-350 words unless journal says otherwise)
6. Title — write LAST (10-15 words)
Consistency rules: Introduction objective MUST match Conclusion; each Methods
item MUST have a Results counterpart (1:1); Discussion claims must be supported
by Results data + literature references.

## Literature matrix
Before drafting, build matrix in 00_literature/literature-matrix.md:
columns = paper (T-A-J-I note), year, venue, method, context, findings, gap.
Source papers via journal-scouting (OpenAlex/Scopus/OKM). Every claim in Intro
and Discussion must trace to a matrix row — no phantom citations.

## IMRAD violations to avoid
1. Results in Methods; 2. Interpretation in Results; 3. References in Results
(compare only in Discussion); 4. New results in Discussion; 5. Result without
its Method; 6. Conclusion not matching Intro objective.

## Tense & voice
- Intro known facts: present. Specific studies: past. Methods/Results: past.
- Discussion (your results): past; general truths: present.
- Prefer active voice ("We analyzed...") unless journal wants passive.

## Project directory (one per paper)
{paper-slug}/ README.md (dashboard) · 00_literature/ (search-strategy,
literature-matrix, key-papers/) · 01_outline.md · sections/ (02_methods,
03_results, 04_introduction, 05_discussion, 06_conclusion, 07_abstract,
08_title) · tables/ · draft.docx via `docx` skill.

## Target journal selection (Garuda/SINTA/Scopus)
- Local: `indo-journal-scouting` skill — Garuda + SINTA (no API key), check
  SINTA accreditation rank (S1-S6) fits the paper's weight.
- International: Scopus journal targeting per quartile via fastmcp-browser
  (Scopus Sources CJR, 22 rows/page) or `journal-scouting` browser path.
- Before submitting, read the journal's Instructions for Authors: word limits,
  citation style, abstract format, figures/tables caps, AI-disclosure requirement.

## Pitfalls
- Never invent data/citations; every number must come from Mahdy's real results
  or a matrix row. Grounded-citations skill for verification.
- Don't write title/abstract before Methods+Results exist.
- Indonesian papers: keep technical terms in original (algorithm, regression),
  style per jurnal target (baku Bahasa Indonesia, bukan campur informal).
- Confirm with Mahdy before any submission/upload; delivery via google-workspace
  only after his OK.
