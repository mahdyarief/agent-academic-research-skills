---
name: literature-mapping
description: "Use when mapping a research landscape to build gap evidence."
version: 0.1.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [research, literature-mapping, gap-scouting, browser]
    related_skills: [blocked-page-recovery]
---

# Literature Mapping

Map a research landscape with citation-graph / visualization tools
(Inciteful, Litmaps, Open Knowledge Maps) and bank the raw evidence before
any gap claim. Procedure first, synthesis last.

## When to Use

- Scouting where a defensible gap might sit across a paper cluster.
- Complementing API keyword sweeps with citation-neighborhood views.
- Don't use for: mass paper collection with download URLs (API sweep path),
  or single-paper deep reads.

For biomedical, health-informatics, or claims-data topics, PubMed covers
venues the other paths miss, keyless. Read `references/pubmed-eutilities.md` for
the esearch/esummary/efetch recipe, the hyphenation and vocabulary pitfalls,
and how to turn a zero-hit intersection into a reproducible gap claim.

## Procedure

1. **Open a record file first.** Create `<topic>/DATA-AWAL-SCOUT.md` with a
   raw-only header before touching any mapping tool.
2. **Seed the graph at the boundary, not the core.** Paste one seed DOI at
   the edge of the target area so link-prediction pulls cross-boundary
   neighbors; read the Similar / Most Important tables row by row
   (author-year, venue, similarity, cites).
3. **Run a narrow keyword map second.** One tight intersection query
   (e.g. `"apparent losses" billing "data quality"`) beats a broad term;
   note the hit count (`1-20 of N`) verbatim.
4. **Run a visual landscape map third.** Build the map, loosen the abstract
   filter when a strict default returns ~1 resource, and read clusters via
   `document.body.innerText`.
5. **Append each tool's output MENTAH as it arrives** — query used, counts,
   author-year rows, map URLs. Label every observation raw / not-a-conclusion.
6. **Conclude only on explicit go-ahead.** Premature synthesis mid-scout is
   the failure this rule prevents.

## Pitfalls

- **Watch for duplicate publications when citing recovered PDFs.** The same
  manuscript can ship under two journal titles/DOIs (same publisher,
  adjacent years). Cite ONE version only; flag the duplication to the user
  so a careful reviewer cannot accuse you of double-counting evidence.
- **Strip `target="_blank"` before programmatic `form.submit()`.** A blank-target
  POST under automation is popup-blocked and silently no-ops — the page stays
  put with no new tab; remove the attribute first, then submit.
- **Verify navigation by URL, never by action echo.** A JS-run receipt only
  proves code executed; follow every submit with a wait plus a `location.href`
  read proving the page actually changed (expect `/map/<hash>`).
- **Re-authorize tabs after navigation or idle.** A `tabId` that worked calls
  ago can return `PERMISSION_DENIED` again — re-list tabs and retry.
- **Set framework-controlled inputs via the native prototype setter** plus a
  bubbling `input` event; bare `.value = x` leaves framework state empty.
- **Read rendered result cards via `innerText`, not selectors.** Custom card
  components match no plain `li/div/article` selector and return `[]`.
- **Loosen strict abstract-length filters before trusting a near-empty map.**
  A length threshold can collapse a real landscape to one resource; re-run
  unfiltered and record both counts.
- **For API novelty sweeps use the `title_and_abstract.search:"<phrase>" <keyword>`
  filter form.** The bare `title_and_abstract:` field form is rejected by
  OpenAlex, and broad `search=` counts (thousands of hits) are noise — only
  tight-filter counts prove a gap is empty; record the exact filter string
  next to every count.
- **Write multi-query sweeps to a script file and run it, never inline.**
  Inline f-strings and shell pipes mangle quoted phrases; a file survives
  retries and edits when a network error cuts the turn mid-sweep.
- **Paginate OpenAlex with `page=`, never `cursor=`, for free bulk pulls.**
  Cursor paging beyond the first page returns HTTP 401 "API key required";
  `page=` with `per_page=200` stays free — loop until `len(results) < per_page`
  or you reach `meta.count`. Symptom to recognize: a sweep where only the
  large queries "error" and small ones succeed is a paging bug, not a bad
  filter — reach for `page=` before rewriting the query.
- **Do not expect Indonesian-language literature in OpenAlex.** `language:id`
  filters to 0 hits on most business/education topics; local coverage must
  come from Garuda/SINTA as a separate source, not from filtering OpenAlex.
- **Sweep every source the protocol names, not just the keyless one.** If
  Scopus/SINTA/Garuda are in the protocol, pull them too — an OpenAlex-only
  result set looks complete but leaves the reviewer's coverage question open.
- **Run a Scopus search from a crafted results URL when the live session is
  signed in.** Navigate straight to
  `scopus.com/results/results.uri?src=s&sot=aut&sdt=aut&sl=86&s=TITLE-ABS-KEY(<query>)%20AND%20PUBYEAR%20%3E%20YYYY`
  and read the count from `document.body.innerText` ("N documents found") —
  faster and more robust than filling the form. The results page also renders
  abstracts for screening (the MCP Scopus search returns them null).
- **A page count is not an extraction.** "74 documents found" read off the
  page is the source total, not the rows you collected — pull the records and
  re-count against that number before reporting the sweep finished, or say the
  pull is still pending.

## Verification

- Record file holds one dated section per tool with query, counts, and rows.
- Every map/graph URL in the file resolves when reopened.
- File contains zero gap verdicts, rankings, or recommendations.
