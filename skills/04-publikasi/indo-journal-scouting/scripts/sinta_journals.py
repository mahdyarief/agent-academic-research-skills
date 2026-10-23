"""SINTA (sinta.kemdiktisaintek.go.id) journal search -> JSON.

Usage:
  python sinta_journals.py "information system"
  python sinta_journals.py "sistem informasi" --rank S2 --pages 2 --json out.json

Requires: curl_cffi, beautifulsoup4 (system python).
Domain is kemdiktisaintek.go.id (NOT kemdikbud.go.id).
"""
import sys, re, json, time, argparse
from curl_cffi import requests as cffi_requests
from bs4 import BeautifulSoup

BASE = "https://sinta.kemdiktisaintek.go.id"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")

def norm(s):
    return re.sub(r"\s+", " ", (s or "")).strip()

def parse_items(html):
    soup = BeautifulSoup(html, "html.parser")
    out = []
    for it in soup.select("div.list-item"):
        d = {}
        name = it.select_one("div.affil-name a")
        if name:
            d["name"] = norm(name.get_text(" "))
            href = name.get("href", "")
            d["profile_url"] = href
        loc = it.select_one("div.affil-loc a")
        if loc:
            d["publisher"] = norm(loc.get_text(" "))
        pid = it.select_one("div.profile-id")
        if pid:
            txt = norm(pid.get_text(" "))
            p = re.search(r"P-ISSN\s*:\s*([\dXx]+)", txt)
            e = re.search(r"E-ISSN\s*:\s*([\dXx]+)", txt)
            if p: d["p_issn"] = p.group(1)
            if e: d["e_issn"] = e.group(1)
        acc = it.select_one("span.num-stat.accredited")
        if acc:
            m = re.search(r"(S[1-6])", acc.get_text(" "))
            d["rank"] = m.group(1) if m else norm(acc.get_text(" "))
        gar = it.select_one("span.num-stat.garuda-indexed")
        if gar:
            d["garuda_indexed"] = True
            a = gar.find_parent("a")
            if a and a.get("href"):
                d["garuda_url"] = a["href"]
        nums = [norm(n.get_text(" ")) for n in it.select("div.journal-list-stat div.pr-num")]
        labels = ["impact", "h5_index", "citations_5yr", "citations"]
        for lbl, val in zip(labels, nums):
            d[lbl] = val
        # abbreviated links (GS / website / editor)
        links = {}
        for a in it.select("div.affil-abbrev a[href]"):
            links[norm(a.get_text(" "))] = a["href"]
        if links:
            d["links"] = links
        if d.get("name"):
            out.append(d)
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query", nargs="?", default="")
    ap.add_argument("--rank", help="filter results to this SINTA rank (S1..S6)")
    ap.add_argument("--pages", type=int, default=1)
    ap.add_argument("--json")
    ap.add_argument("--delay", type=float, default=1.5)
    args = ap.parse_args()

    S = cffi_requests.Session(impersonate="chrome124")
    S.headers.update({"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9,id;q=0.8"})

    results = []
    for page in range(1, args.pages + 1):
        params = {}
        if args.query: params["q"] = args.query
        if page > 1: params["page"] = page
        r = S.get(f"{BASE}/journals", params=params, timeout=45)
        r.raise_for_status()
        results.extend(parse_items(r.text))
        if page < args.pages:
            time.sleep(args.delay)

    if args.rank:
        results = [d for d in results if d.get("rank") == args.rank.upper()]

    payload = {"query": args.query, "rank_filter": args.rank,
               "count": len(results), "journals": results}
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
