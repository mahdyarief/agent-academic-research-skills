"""Garuda (garuda.kemdiktisaintek.go.id) article search -> JSON.

Usage:
  python garuda_search.py "artificial intelligence" --pages 1
  python garuda_search.py "umkm adopsi ai" --pages 2 --json out.json

Requires: curl_cffi, beautifulsoup4 (system python).
No API key. Domain is kemdiktisaintek.go.id (NOT kemdikbud.go.id).
"""
import sys, re, json, time, argparse
from curl_cffi import requests as cffi_requests
from bs4 import BeautifulSoup

BASE = "https://garuda.kemdiktisaintek.go.id"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")

def norm(s):
    return re.sub(r"\s+", " ", (s or "")).strip()

def parse_items(html):
    soup = BeautifulSoup(html, "html.parser")
    out = []
    for it in soup.select("div.article-item"):
        d = {}
        t = it.select_one("a.title-article")
        if t:
            d["title"] = norm(t.get_text(" "))
            href = t.get("href", "")
            d["detail_url"] = BASE + href if href.startswith("/") else href
        d["authors"] = [norm(a.get_text(" ")) for a in it.select("a.author-article")]
        subs = it.select("xmp.subtitle-article")
        if subs:
            d["venue"] = norm(subs[0].get_text(" "))
        if len(subs) > 1:
            d["publisher"] = norm(subs[1].get_text(" "))
        act = it.select_one("p.action-article")
        if act:
            for a in act.select("a[href]"):
                href = a.get("href", "")
                if "/article/download/" in href:
                    d["pdf_url"] = href
                elif "/article/view/" in href:
                    d.setdefault("source_url", href)
                elif href.startswith("https://doi.org/"):
                    d["doi"] = href.replace("https://doi.org/", "")
        ab = it.select_one("div.article-abstract xmp.abstract-article")
        if ab:
            d["abstract"] = norm(ab.get_text(" "))
        if d.get("title"):
            out.append(d)
    return out

def find_total(html):
    m = re.search(r"Found\s+([\d,\.]+)\s+documents", html)
    return int(re.sub(r"[.,]", "", m.group(1))) if m else None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query")
    ap.add_argument("--pages", type=int, default=1)
    ap.add_argument("--json", help="write results to this file")
    ap.add_argument("--delay", type=float, default=1.5)
    args = ap.parse_args()

    S = cffi_requests.Session(impersonate="chrome124")
    S.headers.update({"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9,id;q=0.8"})

    results, total = [], None
    for page in range(1, args.pages + 1):
        url = f"{BASE}/documents"
        params = {"q": args.query}
        if page > 1:
            params["page"] = page
        r = S.get(url, params=params, timeout=45)
        r.raise_for_status()
        if total is None:
            total = find_total(r.text)
        items = parse_items(r.text)
        results.extend(items)
        if page < args.pages:
            time.sleep(args.delay)

    # dedupe by doi, else normalized title
    seen, dedup = set(), []
    for d in results:
        key = d.get("doi") or d.get("title", "").lower()
        if key in seen:
            continue
        seen.add(key)
        dedup.append(d)

    payload = {"query": args.query, "total_found": total,
               "count": len(dedup), "articles": dedup}
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
