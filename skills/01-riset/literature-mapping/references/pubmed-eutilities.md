# PubMed via E-utilities (no API key)

Use for biomedical, health-informatics, clinical, and claims-data topics. PubMed
indexes venues OpenAlex and Scopus surface poorly, and abstracts are free.

## Procedure

1. Write one scan script into `analysis/` that loops a dict of named queries and
dumps JSON. Never run twenty curls by hand: you lose the query-to-result
mapping and cannot then report a defensible gap.
2. Search: `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi` with
   `db=pubmed`, `term=<query>`, `retmax=30` or `40`, `retmode=json`,
   `sort=relevance`. Read `esearchresult.count` (total) and `idlist` (fetched).
3. Summarize: `esummary.fcgi` with `id=<comma ids>`, `retmode=json`, chunks of
   100. Gives title, `fulljournalname`, `pubdate`, and DOI inside `articleids`.
4. Read abstracts before deciding anything: `efetch.fcgi` with
   `rettype=abstract&retmode=text`. One call handles a dozen PMIDs and prints
   journal, volume, pages, DOI, PMID, and the structured abstract. Cheap enough
   for every shortlisted record; skip full text until a record is clearly a
   competitor.
5. `time.sleep(0.4)` between calls (3 requests per second, keyless limit).

## Pitfalls

- Field tag `[tiab]` restricts to title and abstract. Without it, common words
  match MeSH expansions and the set floods with noise.
- Run every hyphenation and derivation variant: `undercoding`, `under-coding`,
  `undercoded`, `underreporting`. They return different sets; one spelling
  silently hides half the competitors.
- Do not trust a coined phrasing. `"missing procedure"` returns zero records;
  the literature says under-coding, under-reporting, uncoded, and incomplete
  recording. Zero hits on a natural-sounding phrase is a vocabulary problem,
  not a gap.
- `sort=relevance` beats date sorting: the canonical anchors of a field are
  usually a decade old, and newest-first buries them.
- Report `count` next to `fetched`. A 779-hit query read at retmax 40 supports
  "checked the top 40 by relevance", never "nothing exists".
- A negative result becomes gap evidence only when you also state the query and
  the filter. Record hits per query, then title-filter by domain keywords, then
  the surviving count. That chain is what an examiner can reproduce.
- Take journal, year, and DOI from the efetch header, not from a summary call,
  before writing a reference-list entry.
- Scope the claim to the index. PubMed covers biomedicine and health
  informatics; information systems, management, and accounting literature on
  data quality and governance sits outside it, so "absent from PubMed" is not
  "absent from the literature".

## Reading the result as a landscape, not a list

Group the hits by the object they act on, not by method. For a detection task
the split that matters is: work that estimates how much is missing, work that
flags which specific items are missing, and work that only concedes the premise
while training a model. The second group is the real competitor even when it
has fewer citations, because it is closer to the claim being made. Then check
what comparison channel each of them uses; a channel produced by the same
process under measurement is not independent and cannot separate competing
causes of the same observed pattern.
