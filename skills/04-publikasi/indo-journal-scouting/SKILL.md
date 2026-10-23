---
name: indo-journal-scouting
description: "Scout Indonesian journals: Garuda + SINTA (no API key)."
version: 0.1.0
author: Mahdy, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [research, journals, garuda, sinta, indonesia]
    related_skills: [journal-scouting, arxiv]
---

# Indo Journal Scouting

Scout **Indonesian** scholarly sources in two layers, both scraped from official
Kemdiktisaintek portals (no API key, no Cloudflare):

- **Garuda** (`garuda.kemdiktisaintek.go.id`) — article/document search. This is
  the Indonesian national journal portal: full metadata per article (title,
  authors, journal+volume+year, publisher, DOI, direct PDF link) AND the abstract
  is already inline on the results page (no second request needed).
- **SINTA** (`sinta.kemdiktisaintek.go.id`) — journal ranking/profiling. Use when
  Mahdy needs to CHOOSE a publish target: SINTA rank (S1–S6), impact, H5-index,
  citations, publisher, ISSN.

Pair with the `journal-scouting` skill (OpenAlex, international) — together they
cover international + national in one pass.

## When to Use
- Run `scripts/garuda_search.py` and `scripts/sinta_journals.py` directly; do NOT hand-roll a scraper. They already handle UA headers, pagination, rank filter, and JSON output.
- Mahdy wants Indonesian-language journals, or a publish target at SINTA level.
- Searching for local-context research (UMKM, adopsi teknologi AI di Indonesia).
- Checking "has anyone published on this topic in Indonesia already?"
- Don't use for: international/paywalled literature (use `journal-scouting` /
  OpenAlex), or arXiv preprints (use `arxiv`).

## CRITICAL: Domain moved to kemdiktisaintek.go.id (2026)
Kemdikbud was split into **Kemdiktisaintek**. The old domains are DEAD in DNS
(NXDOMAIN from every resolver, including 1.1.1.1):
- `garuda.kemdikbud.go.id` → **`garuda.kemdiktisaintek.go.id`**
- `sinta.kemdikbud.go.id` → **`sinta.kemdiktisaintek.go.id`**

If a fetch fails with "could not resolve host", it is the domain rename, NOT
local DNS or a block. Always use the `kemdiktisaintek.go.id` domains.

## CRITICAL: run with the SYSTEM python, not the execute_code sandbox
`curl_cffi` and `beautifulsoup4` are installed in the system Python only. The
`execute_code` sandbox uses a different interpreter and raises ModuleNotFoundError.
Workflow: write the script to `workspace/tmp/` (inside the profile), then run it
via `terminal()` with `python <path>`. Do NOT try `import curl_cffi` inside
`execute_code`.

Also: run scripts from `<HERMES_HOME>/...`, never
from `C:\Users\<user>\AppData\Local\Temp` — that scratch dir is outside the
profile and Mahdy has corrected this.

## How to Run
Use the bundled scripts (both take a query and print JSON):

```bash
cd "<HERMES_HOME>"
python skills/research/indo-journal-scouting/scripts/garuda_search.py "artificial intelligence" --pages 1
python skills/research/indo-journal-scouting/scripts/sinta_journals.py "information system" --rank S2
```

Both scripts use `curl_cffi` with `impersonate="chrome124"` and a polite delay
between page requests.

## Procedure
1. **Garuda search** for the topic → per-article: title, authors, journal line
   (venue + vol + year), publisher, doi, pdf_url, source_url, detail_url,
   abstract. Filter `pdf_url` non-null for downloadable-only when needed.
2. **Dedupe** by DOI (falls back to normalized title when DOI is absent).
3. **SINTA lookup** for candidate journals → rank (S1–S6), impact, H5-index,
   citations, publisher, ISSN, profile_url. Use this to pick a publish target.
4. **Save to an isolated topic folder** inside the profile (same rule as
   `journal-scouting`):
   - DM request → `workspace/kuliah/pribadi/journal-scouting/<topic-slug>/`
   - course-group request → `workspace/kuliah/umum/journal-scouting/<topic-slug>/`
   File: `garuda.json` / `sinta.json` alongside any `papers.json` from OpenAlex.
5. **Present with abstracts** — Mahdy wants to know what each paper CONTAINS, not
   a bare title list. Abstract is inline in Garuda results, so include it.
6. **Pairing rule:** when the topic is Indonesian-context, query BOTH Garuda and
   OpenAlex; Garuda gives local journals, OpenAlex gives the international
   framing/citations. Never present Garuda-only without saying so.

## Selectors (verified 2026-09-14 — re-verify if a script returns 0 rows)
Garuda results page `/documents?q=<kw>`: each hit is `div.article-item`
(10 per page):
- `a.title-article` → title + `href=/documents/detail/<id>` (detail_url)
- `a.author-article` → one per author, joined by `;`
- `xmp.subtitle-article` (1st) → `Jurnal X Vol N No M (YYYY): ...` (venue/year)
- `xmp.subtitle-article` (2nd, after `Publisher :`) → publisher
- `p.action-article a[href*="/article/download/"]` → direct PDF (`pdf_url`)
- `p.action-article a[href*="article/view/"]` → landing (`source_url`)
- `p.action-article a[href^="https://doi.org/"]` → DOI
- `div.article-abstract xmp.abstract-article` → full abstract (inline!)

SINTA journals page `/journals?q=<kw>`: each hit is `div.list-item` (10/page):
- `div.affil-name a` → journal name + `href=/journals/profile/<id>`
- `div.affil-loc a` → publisher institution (affiliation)
- `div.profile-id` → `P-ISSN : ... | E-ISSN : ...`
- `span.num-stat.accredited` → **SINTA rank text (S1–S6)**
- `span.num-stat.garuda-indexed` → Garuda-indexed flag + garuda journal id
- `div.journal-list-stat div.pr-num` (ordered) → Impact, H5-index, Citations 5yr, Citations
- `div.affil-abbrev a` → Google Scholar / Website / Editor URLs
Both sites are server-rendered HTML — there is NO public JSON API. Parsing is
inherently brittle; if layout changes, selectors break and the script returns 0
rows (check that first, don't assume the site is down).

## Querying Garuda effectively (gap-testing topics)
Garuda matches query terms against title+abstract as full-text keywords, NOT an
exact phrase. Consequences:
- Long translated phrases (e.g. "biaya penggunaan kecerdasan buatan") return 0
  results. Query with SHORT natural keyword pairs instead ("kecerdasan buatan biaya",
  "adopsi teknologi kecerdasan buatan"). A 0 count often means the phrasing is
  wrong, not that the field is empty — always retry with simpler synonyms before
  declaring a gap.
- Indonesian journals rarely use technical loanwords the way practitioners do
  (e.g. "token" in the AI-cost sense). Translate the CONCEPT to jurnal-ese
  ("biaya operasional", "ekonomi teknologi") or the search misses everything.
- Gap-testing workflow: run several short keyword variants per topic, compare
  `total_found`, then read the fetched titles/abstracts — totals are noisy and
  abstract-level relevance is the real signal.

## Mentor workflow for Mahdy (how to present results)
- Present direct per-paper PDF links (from `pdf_url`) plus the Garuda detail URL —
  Mahdy reads the papers himself; do NOT summarize/paraphrase abstracts for him.
  He reads Indonesian journals first to learn the patterns, then English ones.
- Teach the T-A-J-I reading method (abstrak → struktur → bagian kunci → rujukan)
  and the 5-column literature matrix (Author(year) | Metode | Temuan | Gap |
  Catatan) — he practices by writing one matrix row per paper himself, agent only
  corrects.
- The correct research order is literature-first (L-U-P-A: Lihat lanskap → Uji
  gap → Pilih → Ajukan), NOT problem-first. Never revive the topic-brainstorm-
  first sequence; a brainstormed topic is a hypothesis to be gap-tested, not a
  paper plan.

## Pitfalls
- **HTML scraping, not an API** — unlike OpenAlex, a layout change silently
  breaks selectors. If results are 0, dump one container with `.prettify()` and
  re-derive selectors before concluding anything else.
- **Be polite.** Government portals may rate-limit or IP-ban under aggressive
  traffic. Keep the inter-page delay (~1.5s), no parallelism for bulk runs.
- **`xmp` tags** — Garuda wraps title/abstract/venue in `<xmp>` (renders verbatim
  text). `BeautifulSoup.get_text()` handles it, but be aware values may contain
  raw entities/whitespace; normalize with `re.sub(r'\s+', ' ', s)`.
- **Abstract text has words glued** (e.g. `diIndonesia`) in some Garuda records —
  that's the source data, not a parsing bug.
- **SINTA rank is not the same as Scopus quartile.** S2 = SINTA-2 (national),
  NOT Q2. Use `is Scopus` filter on SINTA to find Scopus-indexed journals.
- **OpenLibrary Telkom is NOT automatable** (Cloudflare Turnstile, "protect
  everything", cf_clearance bound to browser profile). Don't attempt it; see
  `blocked-page-recovery` skill for the general rule.

## Verification
- Script exits 0 and prints a non-empty JSON array.
- Spot-check 1-2 `pdf_url` resolve (HTTP 200).
- For SINTA, confirm `rank` matches the `span.num-stat.accredited` text on-page.
