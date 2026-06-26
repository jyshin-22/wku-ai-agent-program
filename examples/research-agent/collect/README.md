# collect — 논문 수집 (PubMed)

Day 4 오전 '논문 수집' 단계용 예시. 검색어로 PubMed에서 초록·메타데이터를 모아
`papers/` 폴더에 저장합니다. 이 폴더가 팀의 **corpus**가 됩니다.

## 무엇이 들어 있나
- `collect_pubmed.py` — 동작하는 수집 스크립트 (표준 라이브러리만 · 설치 불필요 · API 키 불필요)

## 쓰는 법 (두 가지)
### A. 스크립트 직접 실행
```bash
python3 collect_pubmed.py "검색어" [개수]
# 예
python3 collect_pubmed.py "metformin AND aging" 25
python3 collect_pubmed.py "(insomnia) AND (cognition) AND review[pt]" 30
```
→ `papers/01-....md` … 형식으로 저장됩니다 (제목·PMID·저자·연도·초록).

### B. Claude Code로 (바이브코딩 권장)
실습에서는 스크립트를 직접 짜보는 게 핵심입니다. 예시 프롬프트:
```
PubMed에서 "[검색어]"로 논문 25편의 초록과 메타데이터(제목·저자·연도·PMID)를
받아 papers/ 폴더에 논문별 마크다운으로 저장하는 파이썬 스크립트를 만들고 실행해줘.
표준 라이브러리만 쓰고(설치 불필요), NCBI E-utilities를 사용해. 만든 뒤 실제로 실행해 동작을 확인해줘.
```
이 폴더의 `collect_pubmed.py` 를 참고 답안으로 보여줘도 됩니다.

## 검색어 팁 (PubMed)
- `AND` / `OR` / 괄호로 조합: `(drug A) AND (side effect)`
- 리뷰만: `review[pt]` · 최근 N년: `"last 5 years"[dp]`
- 너무 많으면 좁히고, 너무 적으면 넓혀 **재수집**

## ⚠ 꼭 확인
- **실제 논문인지**: 저장된 것 중 2~3편은 PMID 링크(`https://pubmed.ncbi.nlm.nih.gov/<PMID>/`)로 직접 확인.
  (Claude에게 그냥 "논문 찾아줘" 하면 가짜를 지어낼 수 있음 — 그래서 실제 API로 받는다.)
- **규모**: 20~30편이면 gap 찾기에 충분.
- `papers/` 는 팀마다 생성되는 산출물이라 git에 올리지 않습니다.

## 다음 단계
수집한 `papers/` 로 → 자료 파악 → gap 발견 → 가설 생성 (상위 폴더 `CLAUDE.md`·`README.md` 참고).
