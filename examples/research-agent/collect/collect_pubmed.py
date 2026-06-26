#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PubMed 논문 수집 스크립트 (예시) — 표준 라이브러리만 사용 (설치 불필요).

검색어로 PubMed에서 논문을 찾아 초록·메타데이터를 papers/ 폴더에 저장한다.
NCBI E-utilities(esearch + efetch)를 쓰며 API 키는 필요 없다.

사용법:
  python3 collect_pubmed.py "검색어" [개수]
예:
  python3 collect_pubmed.py "metformin AND aging" 25
  python3 collect_pubmed.py "(insomnia) AND (cognition) AND review[pt]" 30

수업 팁:
  - Claude Code에게 "collect_pubmed.py 를 내 검색어로 실행해줘" 처럼 시키면 된다.
  - 저장된 논문 중 2~3개는 PMID 링크(https://pubmed.ncbi.nlm.nih.gov/PMID/)로 실제인지 확인할 것.
"""
import sys
import time
import os
import re
import json
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
# NCBI 권장: 요청에 도구명·이메일 표기 (가벼운 사용은 키 불필요)
TOOL = "wku-ai-agent-edu"
EMAIL = "student@example.com"   # 본인 이메일로 바꾸면 좋다
OUTDIR = "papers"


def _get(url):
    req = urllib.request.Request(url, headers={"User-Agent": TOOL})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def esearch(query, retmax):
    """검색어 → PMID 목록."""
    params = urllib.parse.urlencode({
        "db": "pubmed", "term": query, "retmax": retmax,
        "retmode": "json", "tool": TOOL, "email": EMAIL,
    })
    data = json.loads(_get(f"{EUTILS}/esearch.fcgi?{params}"))
    return data.get("esearchresult", {}).get("idlist", [])


def efetch(pmids):
    """PMID 목록 → 논문 상세(XML)."""
    params = urllib.parse.urlencode({
        "db": "pubmed", "id": ",".join(pmids), "retmode": "xml",
        "rettype": "abstract", "tool": TOOL, "email": EMAIL,
    })
    return _get(f"{EUTILS}/efetch.fcgi?{params}")


def text(el):
    return "".join(el.itertext()).strip() if el is not None else ""


def parse(xml_bytes):
    """XML → 논문 dict 목록."""
    root = ET.fromstring(xml_bytes)
    papers = []
    for art in root.findall(".//PubmedArticle"):
        pmid = text(art.find(".//PMID"))
        title = text(art.find(".//ArticleTitle"))
        # 초록은 여러 조각(Background/Methods/...)일 수 있다
        abstract = "\n".join(
            (f"{a.get('Label')+': ' if a.get('Label') else ''}{text(a)}")
            for a in art.findall(".//Abstract/AbstractText")
        ).strip()
        year = text(art.find(".//JournalIssue/PubDate/Year")) or \
            text(art.find(".//JournalIssue/PubDate/MedlineDate"))[:4]
        journal = text(art.find(".//Journal/Title"))
        authors = []
        for au in art.findall(".//AuthorList/Author"):
            last = text(au.find("LastName"))
            init = text(au.find("Initials"))
            if last:
                authors.append(f"{last} {init}".strip())
        papers.append({
            "pmid": pmid, "title": title, "year": year,
            "journal": journal, "authors": authors, "abstract": abstract,
        })
    return papers


def slug(s, n=40):
    s = re.sub(r"[^0-9A-Za-z가-힣]+", "-", s).strip("-").lower()
    return s[:n] or "paper"


def save(papers):
    os.makedirs(OUTDIR, exist_ok=True)
    saved = 0
    for i, p in enumerate(papers, 1):
        if not p["pmid"]:
            continue
        fn = f"{i:02d}-{slug(p['title'])}-{p['pmid']}.md"
        body = (
            f"# {p['title']}\n\n"
            f"- PMID: {p['pmid']}  (https://pubmed.ncbi.nlm.nih.gov/{p['pmid']}/)\n"
            f"- 저자: {', '.join(p['authors']) or 'N/A'}\n"
            f"- 연도: {p['year'] or 'N/A'}  · 저널: {p['journal'] or 'N/A'}\n\n"
            f"## 초록\n{p['abstract'] or '(초록 없음)'}\n"
        )
        with open(os.path.join(OUTDIR, fn), "w", encoding="utf-8") as f:
            f.write(body)
        saved += 1
    return saved


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    query = sys.argv[1]
    retmax = int(sys.argv[2]) if len(sys.argv) > 2 else 25
    print(f"[1/3] 검색: {query!r} (최대 {retmax}편)")
    pmids = esearch(query, retmax)
    print(f"      → PMID {len(pmids)}개")
    if not pmids:
        print("결과 없음. 검색어를 넓혀보세요.")
        return
    time.sleep(0.4)  # NCBI 예의상 간격
    print("[2/3] 상세 수집(초록)...")
    papers = parse(efetch(pmids))
    print(f"[3/3] 저장 → {OUTDIR}/")
    n = save(papers)
    print(f"완료: {n}편 저장. 2~3편은 PMID 링크로 실제 논문인지 확인하세요.")


if __name__ == "__main__":
    main()
