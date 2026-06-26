# examples — 실습·프로젝트용 예제/템플릿 모음

수업 중 실습·프로젝트에서 바로 쓰는 예제 파일과 템플릿입니다.
모든 데이터/출처는 **교육용 가상 자료(fictional)** 이며 실제가 아닙니다.

## 폴더 구성
| 폴더 | 용도 | 사용 시점 |
|------|------|-----------|
| `prompts/` | 프롬프트 템플릿 (일반·리서치·보고서) | 전 과정 |
| `claude-setup/` | `settings.json` · `CLAUDE.md` 예시 | Day 2 오후2 (설정) |
| `mini-project/` | 개인 미니 프로젝트 기획서 + **에이전트 동작 확인용 샌드박스** | Day 2~3 |
| `research-agent/` | **가설 생성 에이전트 템플릿** (규칙·기획서·가상 corpus·제안서 양식) | Day 3~5 |
| `research-agent/collect/` | **PubMed 논문 수집 스크립트** (`collect_pubmed.py`) | Day 4 오전 (수집) |

## 빠른 시작
1. Claude Code를 프로젝트 폴더에서 실행: `cd <폴더> && claude`
2. 동작 확인: `mini-project/sandbox/` 에서 "이 폴더에 뭐가 있는지 알려줘"
3. 논문 수집(Day 4): `research-agent/collect/`의 `collect_pubmed.py`로 PubMed corpus 구축
4. 가설 생성 실습: `research-agent/`를 복사해 팀 작업 폴더로 사용 (자료파악→gap→가설생성→평가)

## 사용 팁
- 템플릿의 `[ ... ]` 부분을 자기 내용으로 채우세요.
- 가상 자료(`research-agent/sources/`)는 실제 출처가 아니므로, 실제 프로젝트에선 진짜 자료로 교체하세요.
