# 신약 개발을 위한 AI Agent 특강 — 자료 저장소

약학 대학생 대상 5일 특강의 슬라이드·실습 자료·운영 문서 모음입니다.

## 무엇이 들어 있나

| 경로 | 내용 |
|------|------|
| `slides/day1–5.pptx` (+ `.pdf`) | 5일치 강의 슬라이드 (생성 산출물) |
| `slides_content.py` | 슬라이드 콘텐츠(데이터). **여기를 고친다.** |
| `build_slides.py` | 슬라이드 생성기 (python-pptx) |
| `examples/` | 실습·프로젝트용 예제·템플릿·작업 시트 |
| `ta-guide.md` | **조교 가이드** — 학생 실습 전 과정을 조교가 먼저 리허설 |
| `live-demos.md` | 강의 중 라이브 데모 기획 (강사용) |
| `cases.md` | 슬라이드에 쓸 실제 사례 출처 모음 |
| `research_project_open_questions.md` | 리서치 방법론·쟁점(생성 vs 선별)과 권고 |

## 일자 구성 (담당 강사 세션)

- **Day 1** LLM의 원리와 이해 (강의)
- **Day 2** AI 에이전트 원리 + Claude Code 설치·설정 (강의+실습)
- **Day 3** 미니 프로젝트 + 리서치 방법론·쟁점 + 팀 구성
- **Day 4** 팀 리서치 에이전트 — 논문 수집 → 자료 파악·gap → 가설 생성·평가
- **Day 5** 가설 제안서·발표자료(AI 활용) + 발표

> '제약 산업에서의 AI'(월 오전·오후1)는 별도 강사 담당으로 본 자료에서 제외.

## 슬라이드 빌드

```bash
pip install --break-system-packages python-pptx     # 최초 1회
python3 build_slides.py                              # slides/day1–5.pptx 생성
# PDF: LibreOffice 필요
for d in 1 2 3 4 5; do soffice --headless --convert-to pdf --outdir slides slides/day$d.pptx; done
```
- 한글 렌더링에는 나눔/Noto CJK 폰트 필요(`fonts-nanum`, `fonts-noto-cjk`).
- 콘텐츠 수정은 `slides_content.py`, 레이아웃/디자인은 `build_slides.py`.

## 실습 자료 진입점

- 조교는 먼저 **`ta-guide.md`의 리허설**을 끝까지 수행하세요.
- 실습 파일 지도는 `examples/README.md` 참고.
