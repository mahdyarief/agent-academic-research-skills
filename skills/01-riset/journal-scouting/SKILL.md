---
name: journal-scouting
description: "Find academic papers and collect open-access download URLs."
version: 0.2.0
author: Mahdy, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [research, papers, openalex, open-access]
    related_skills: [arxiv, exa-web-research]
---

# Journal Scouting

Collect academic papers matching a topic, with metadata (title, authors, year, DOI, venue, citations) and working open-access download URLs. Primary source: **OpenAlex API** (free, no key, CAPTCHA-free). EXA (`exa-web-research` skill) is the complementary layer for grey literature, latest preprints, and non-scholarly web sources that OpenAlex does not index. The scispace skill was removed 2026-09-13 (search page retired by SciSpace, premium account hit CAPTCHA walls) — OpenAlex is now the sole paper-finding path. **Alternative browser path (verified 2026-09-26 via `fastmcp-browser-control`, profile `hermes`, bridge 127.0.0.1:9229): `https://www.scopus.com/sources` (signed in via campus session, 50,040 results, filter Subject area / Source type / quartile Q1-Q4 / top-10% / Open Access only, Download Source List + Export to Excel) for journal-target scouting per quartile, and `https://openknowledgemaps.org/` (free, BASE all-disciplines or PubMed, keyword -> GO visual literature map) for topic landscape before deep-dive. Browser path complements API discovery, never replaces mass discovery.**

## When to Use
- Mahdy asks to find journals/papers on a topic and wants download links.
- Building a literature list or collecting `oa_url` PDFs for a topic.
- Don't use for: arXiv-only searches (use `arxiv` skill), or semantic web searches
  for grey literature / non-academic sources (use `exa-web` / `exa-web-research`).

## Prerequisites
- Python stdlib only (`urllib.request`). No API key needed.
- Always add `mailto=<email>` to OpenAlex requests (polite pool).
- For delivering artifacts to Mahdy's Google Drive, see
  `references/gdrive-multi-account.md` (multi-account token registry + read/write split).

## API Key Policy (keyless-first + rotator)
- **Primary: keyless (mailto).** 100k credits/day — bigger budget than any free
  key. Always start here.
- **Fallback on HTTP 429 (keyless exhausted): key rotator.** Keys live in
  `openalex-keys.json` next to this SKILL.md, shape:
  `{"active_index": 0, "keys": [{"key": "...", "label": "mahdy-1", "added": "YYYY-MM-DD", "status": "active"}]}`
- Rotation rules (Mahdy's standing instruction):
  - Keyless first; a key is used ONLY after a 429.
  - Try keys in order (`active_index`); advance the pointer when one is also
    exhausted; never delete old keys — they reset daily at midnight UTC.
  - When Mahdy sends a new key: APPEND it to `openalex-keys.json` with a new
    label (`mahdy-2`, `mahdy-3`, ...); never overwrite or remove existing rows.
  - Verify a new key with `GET /rate-limit?api_key=<key>` before adding.
- **Check quota live via `/rate-limit`, never trust docs.** Measured with a real
  key: keyed accounts get ~10k credits/day (list=1, search=10 credits) plus a
  small daily dollar budget — NOT the 1M/day claimed in older blog posts. The
  numbers change; the endpoint is the source of truth.

## How to Run
Use `execute_code` with this query pattern:

```python
import json, urllib.request, urllib.parse
filt = 'title.search:"artificial intelligence" Indonesia business'
url = ("https://api.openalex.org/works?filter=" + urllib.parse.quote(filt)
       + "&per-page=100&sort=cited_by_count:desc&mailto=research@example.com"
       + "&select=display_name,publication_year,doi,primary_location,open_access,cited_by_count,authorships")
data = json.load(urllib.request.urlopen(url, timeout=30))
```

## Procedure
1. **Translate the topic into filter queries.** OpenAlex search is keyword-based:
   - Indonesian-language queries often return 0 results; rewrite in English.
   - Run 3-6 variants: `title.search:"<exact phrase>" <keyword>` combinations
     (e.g. `"artificial intelligence" Indonesia`, plus venue/topic words like
     `business`, `SME`, `banking`).
2. **Dedupe by DOI** across queries (they overlap heavily).
3. **Extract download URL per work, in priority order:**
   1. `open_access.oa_url`
   2. `primary_location.pdf_url`
   3. `primary_location.landing_page_url`
   4. Fallback: `https://doi.org/<doi>` (resolver, may be paywalled)
4. **Filter by relevance keywords** in the title when the topic implies a domain
   (e.g. business: sme, msme, umkm, bank, finance, marketing, firm, industry,
   productivity, performance, economy, tourism, entrepreneur).
5. **Sort by `cited_by_count` descending**, report top entries with one line each:
   title (year) | venue | DOI | download URL.
6. **Enrich each paper with its abstract** — the list alone is never the
   deliverable; Mahdy wants to know what each paper CONTAINS. Fetch
   `abstract_inverted_index` per DOI and rebuild the text:
   ```python
   def rebuild_abstract(inv):
       pos = {i: w for w, idxs in inv.items() for i in idxs}
       return " ".join(pos[i] for i in sorted(pos))
   ```
   Fetch one-by-one with a small sleep (~0.15s) — singleton fetches cost 1
   credit each, so 100 papers is cheap. Skip DOI prefixes `10.5281` (Zenodo)
   and `10.6084` (Figshare) — these are datasets with no abstract in OpenAlex.
6. **Save results to an isolated topic folder**, never loose in the workspace
   root. Scouting result location follows the SOURCE of the request (same rule
   as `workspace/kuliah/`):
   - Request from Mahdy's DM → `workspace/kuliah/pribadi/journal-scouting/<topic-slug>/`
   - Request from a course group chat → `workspace/kuliah/umum/journal-scouting/<topic-slug>/`
   `<topic-slug>` is kebab-case, e.g. `ai-adoption-indonesia-business`. Each
   topic folder holds `papers.json` plus all other artifacts (CSV/Excel,
   downloaded PDFs, notes) — nothing spills outside it.
7. **Present top picks BALANCED across domains, never from one keyword cluster.**
   A citation+keyword score surfaces whichever domain dominated the query terms
   (e.g. five SME-marketing papers) — Mahdy rejected such a list as
   one-note. Instead: group papers by domain via title keywords (sme/umkm,
   bank/finance, hr/employee, marketing, industry-specific, education,
   health), dedupe title duplicates (Zenodo/Figshare mirrors), then pick the
   strongest 1-2 per domain for the shortlist. Show the full domain grouping
   on request; never present a top-5 from a single cluster.
8. When presenting, explain what each pick CONTAINS from its abstract (method,
   finding, business relevance) — a bare title list is not acceptable.
   Present a short summary + top picks to Mahdy afterward.

## Browser path (complementary, via fastmcp-browser)
Bridge mechanics live in `fastmcp-browser-control` (WS 127.0.0.1:9229, scripts
in `<HERMES_HOME>/mcp-servers/fastmcp-browser/server/`). This section is
the DOMAIN procedure. Verified 2026-09-26, profile `hermes`.

### Scopus Sources — journal-target scouting (per quartile)
- Open `https://www.scopus.com/sources`; campus session shows "Signed in" —
  browser access, does NOT consume journal-scout API quota.
- 50,040 results, 22 table rows/page, metrics year selector (2025 current).
- Filters: Subject area, Source type (Journals / Conference Proceedings /
  Book Series / Trade Publications), quartile Q1-Q4 checkboxes, top-10%,
  Open Access only, min citations/documents, CiteScore.
- Read rows with `browser_evaluate` (works on Scopus, unlike Gmail):
  `Array.from(document.querySelectorAll("tbody tr"))...td.innerText` →
  title | CiteScore | percentile | citations | docs | publisher.
- Export: button "Download Scopus Source List", or tick rows -> "Export to
  Excel".
- Use case: pick target journals for Garuda/SINTA shortlist by quartile.
  Paper discovery stays on the API path above.

### Open Knowledge Maps — topic landscape before deep-dive
- Open `https://openknowledgemaps.org/`; `browser_evaluate` works.
- Form "Map a research topic (AI beta)": radio BASE (all disciplines) vs
  PubMed, keyword textbox -> GO; refine by time range. Result = visual
  cluster map of papers per sub-topic.
- Use case: see a topic's landscape in one screen before committing to a
  deep read; complementary to OpenAlex keyword lists.

### Session mechanics gotchas (verified)
- `bridge-run.mjs` is single-call: any tab-scoped method WITHOUT `browser_tabs`
  first in the same session returns `PERMISSION_DENIED` ("Tab N is not
  authorized"). For evaluate/click/fill use `bridge-act.mjs`
  (`TABID=<n> METHOD=<m> EXPR='...' node bridge-act.mjs`) — it authorizes
  tabs, snapshots, then runs the action.
- `bridge-act.mjs` parses `PARAMS || '{}'` and maps `EXPR`/`REF`/`URL` env
  vars into params; never pass an empty PARAMS (JSON.parse('') throws).
- Terminal output gets swallowed (`stdin is not a tty`) — re-run the identical
  command; long TABS lines eat `head -c` budget, grep them out (`grep -v '^TABS='`).

## Pitfalls
- OpenAlex does NOT host PDFs; `oa_url` points to the publisher/repo. Some links
  (DOI resolver, IEEE) land on paywalls — label them as such.
- `title.search:` returns nothing for long free-text queries; keep filters short.
- Related duplicate records (preprint + published, Figshare/Zenodo mirrors of the
  same paper) share titles — dedupe on title too when presenting.
- Rate limits (free): 100k credits/day, 100 req/s; list queries cost 10 credits.
  Never an issue for manual scouting batches.
- The removed `scispace` skill (2026-09-13) used to silently return `count: 0`
  because SciSpace's search page became an agentic chat UI with no scannable
  results — always go straight to OpenAlex; never fall back to SciSpace search.

## Verification
- Count deduped results vs. raw hits before presenting.
- Spot-check 2-3 download URLs actually resolve (HTTP 200 or a download page).
- File exists with one JSON object per paper, each containing `download_url`.

## Delivery to Drive (see references/gdrive-multi-account.md)
- Search/download = primary token (`google_token_mahdy.json`); upload runs under
  the dedicated upload account once registered. Folder Kuliah S2 must be shared
  (role `writer`) to the upload account before its first upload.
- Per-account token selection at call time: run `google_api.py` via subprocess
  with `HERMES_HOME=<profile>` and
  `GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE=google_token_<name>.json` — never mutate
  module constants (resolved at import).
- The installed `setup.py` has no `--services` flag (auth URL requests the full
  scope set) — don't probe for it; just run `--auth-url` / paste the returned
  `localhost:1` redirect URL back via `--auth-code`. A failed `localhost:1`
  load after consent is EXPECTED; the code lives in the browser address bar.
- Confirm with Mahdy before any upload or Drive share.
