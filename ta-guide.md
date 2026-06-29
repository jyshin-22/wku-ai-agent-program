# 조교(TA) 가이드 — 신약 개발을 위한 AI Agent 특강

> **이 문서의 사용법: 조교는 수업 전, 학생이 실습할 전 과정을 직접 한 번 끝까지 수행(리허설)한다.**
> 그래야 막히는 지점·소요 시간·흔한 함정을 미리 체득하고, 수업 중 학생을 정확히 지원할 수 있습니다.
> 대상 수강생: **약학 대학생(비전공)** · 핵심 도구: **Claude Code** · 실습 자료: `examples/`.

---

## 1. 실습 전체 흐름

| 일자·세션 | 유형 | 실습 |
|-----------|------|------|
| Day 2 오후1 | 설치 | Python + Claude Code |
| Day 2 오후2 | 설정 | 주요 설정 + oh-my-claudecode 플러그인 |
| Day 3 오전·오후1 | 개인 | 미니 프로젝트 기획 → 개발 |
| Day 3 오후2 | 팀 | 리서치 방법론·쟁점 → 팀 구성·기획 |
| Day 4 오전 | 팀 | **논문 수집(PubMed)** |
| Day 4 오후1 | 팀 | **자료 파악 & gap 발견** |
| Day 4 오후2 | 팀 | **가설 생성 & 평가** |
| Day 5 오전 | 팀 | 버퍼 / 보완 |
| Day 5 오후1 | 팀 | 가설 제안서·발표자료 (AI 활용) |
| Day 5 오후2 | 발표 | 팀별 발표 |

Day 4가 실습의 핵심이자 가장 손이 많이 가는 구간입니다.

---

## 2. 리허설 사전 준비

- [ ] Windows·macOS **양쪽** 환경 확보(가능하면). 학생 OS는 둘 중 하나입니다.
- [ ] `examples/` 최신 상태로 clone/pull.
- [ ] Claude Code 계정/로그인 방식 확인(구독 또는 Anthropic Console).
- [ ] 인터넷 연결(논문 수집에 필요).
- [ ] 리허설 소요: 환경 제외하고 전 과정 **약 1.5~2시간**(처음 1회). 여유를 두고 잡으세요.

---

# 3. 전 과정 리허설 (조교가 직접 수행)

각 단계: **무엇을 한다 · 입력(명령/프롬프트) · 봐야 할 결과 · 확인 포인트 · 흔한 함정**.
프롬프트는 그대로 따라 해도 되고, `examples/prompts/research-prompts.md`의 것을 써도 됩니다.

## 리허설 0 — 환경 설치 (Day 2 체험)

**Python**
- Windows: python.org 설치 파일 → 첫 화면 **'Add python.exe to PATH' 체크** → `python --version`
- macOS: .pkg 설치 → **'Install Certificates.command' 실행** → `python3 --version`

**Node.js 24**
- nodejs.org에서 Node.js 24 설치(Windows .msi / macOS .pkg 또는 `brew install node@24`) → `node --version`(v24.x)·`npm --version`
- Claude Code의 npm 설치와 oh-my-claudecode 등 일부 도구가 Node를 사용.

**Claude Code**
- Windows(PowerShell): `irm https://claude.ai/install.ps1 | iex`
- macOS: `curl -fsSL https://claude.ai/install.sh | bash` (또는 `brew install --cask claude-code`)
- 로그인: `claude` 실행 → 브라우저 OAuth(안 열리면 `c`로 URL 복사)

**동작 확인 (이게 되면 설치 완료)**
```
cd examples/mini-project/sandbox
claude
```
프롬프트 예: `이 폴더에 어떤 파일이 있고 각각 무슨 내용인지 알려줘`
→ 이어서: `expenses.csv를 항목별로 합산하고 총합도 알려줘`
- **확인 포인트**: 합계가 식비 44,500 · 총합 98,500로 나오면 정상(정답이 정해진 데이터).
- 함정: `python` vs `python3`(Mac), PATH 미설정(Win), 브라우저 로그인.

**플러그인**
```
/plugin marketplace add https://github.com/Yeachan-Heo/oh-my-claudecode
/plugin install oh-my-claudecode
/omc-setup
```
- 확인 포인트: `/help`에 플러그인 명령이 보이거나 `/omc-setup` 완료.
- 함정: 경로 오타, team 기능엔 tmux 필요.

## 리허설 1 — 개인 미니 프로젝트 (Day 3 체험)

- 무엇을: 기획서 한 장 → 동작하는 작은 결과물(바이브코딩).
- 입력: `examples/mini-project/project-plan-template.md`를 간단히 채운 뒤, 작업 폴더에서
  `이 기획서대로 작은 프로그램을 만들고 실제로 실행해서 결과를 보여줘`
- 봐야 할 결과: 실행되는 결과물 + 한두 번의 수정 요청에 반영.
- 확인 포인트: "됐다"가 아니라 **실제 실행 결과**를 눈으로 확인했는가.
- 함정: 주제를 너무 크게 잡음 → "한 세션에 끝낼 범위"로 좁히게 지도하는 감을 익혀 두기.

## 리허설 2 — 팀 프로젝트 전 과정 (Day 4~5 체험) ★핵심

작업 폴더를 하나 만들어 `research-agent`를 복사해 쓰면 편합니다.
```
cp -r examples/research-agent ~/ta-rehearsal
cd ~/ta-rehearsal
```
> 네트워크 없이 리허설하려면 제공된 `sources/`(가상 수면 corpus 6편)를 그대로 corpus로 써도 됩니다.
> PubMed까지 리허설하려면 아래 2-1을 수행해 `papers/`를 만듭니다.

### 2-1. 논문 수집 (Day 4 오전)
```
cd collect
python3 collect_pubmed.py "metformin AND aging" 20
```
- 봐야 할 결과: `papers/`에 논문별 .md 파일(제목·PMID·초록).
- 확인 포인트: **2~3편을 PMID 링크(`https://pubmed.ncbi.nlm.nih.gov/<PMID>/`)로 열어 실재 확인.**
- 함정: 에이전트에게 "논문 찾아줘"만 시키면 **가짜 논문을 지어낼 수 있음** → 실제 API/스크립트로 받기.
- 백업: 수업 당일 PubMed 지연 대비, 리허설에서 만든 `papers/`를 **백업으로 보관**.

### 2-2. 자료 파악 (Day 4 오후1)
`research-agent`(또는 ta-rehearsal) 폴더에서 `claude` 실행 후:
```
papers/ (없으면 sources/)의 각 논문을 같은 틀로 정리해줘 —
각 논문의 핵심 주장·방법·근거·한계를 표로 만들어줘.
```
- 봐야 할 결과: 논문별 한 행짜리 표. → `worksheets/1-literature-matrix.md` 형식으로 정리.
- 확인 포인트: 모든 논문이 같은 열로 채워지고, 주장이 엇갈리는 행이 보이는가.
- 함정: 정리 없이 바로 gap을 찾으려 함 → **정리(정규화)가 먼저**.

### 2-3. gap 발견 (Day 4 오후1)
```
정리한 자료에서 충돌·미검증·빠진 관점(gap)을 찾고,
각 gap이 어느 논문에서 비롯됐는지 근거를 달아줘.
```
- 봐야 할 결과: 근거가 달린 gap 목록 → `worksheets/2-gap-list.md`.
- 확인 포인트: 각 gap에 근거 논문이 있는가(근거 없는 gap은 제외).
- (sources/ 사용 시) 예상 gap: 권장 수면 7–9h vs 6h 충돌, 낮잠 경계 불명확 등.

### 2-4. 가설 생성 (Day 4 오후2)
```
각 gap에서 검증 가능한 새 가설을 8개 만들고, 어느 gap·논문에서 나왔는지 근거를 달아줘.
이어서 논문들의 핵심 아이디어 3~5개를 뽑아 배경과 조합한 가설도 만들어줘.
```
- 봐야 할 결과: '~한 조건에서 ~할 것이다' 형태의 가설 다수, 각자 근거 태그.
- 확인 포인트: 근거 없는 가설(환각)이 섞이지 않았는가.

### 2-5. 평가·우선순위 (Day 4 오후2)
```
위 가설들을 근거·새로움·중요성·검증 가능성으로 평가해 순위를 매기고,
상위 2개를 추천해줘. 왜 그렇게 매겼는지 근거도 함께.
```
- 봐야 할 결과: 평가표 + 상위 1~2개 → `worksheets/3-hypothesis-eval.md`.
- 확인 포인트: 한 가설에만 의존하지 않고 후보군을 남겼는가. 사람 검토를 거쳤는가.

### 2-6. 제안서·발표자료 (Day 5)
```
상위 가설로 output/report-template.md 형식의 가설 제안서 초안을 만들어줘.
각 항목에 근거(gap·논문)를 달고, 한계도 적어줘.
```
- 봐야 할 결과: 제안서 초안. **완성 모습은 `output/SAMPLE-hypothesis-proposal.md`와 비교.**
- 확인 포인트: **사실·출처·rationale을 사람이 검토**했는가(AI 초안 ≠ 최종본).

### 리허설을 마치면
- 전 과정에서 **막힌 지점·소요 시간·자주 나올 질문**을 메모해 둡니다(아래 9장 양식).
- 백업 `papers/` 1개 확보. SAMPLE과 본인 결과를 비교해 "좋은 산출물"의 감을 잡습니다.

---

## 4. 환경 트러블슈팅 (Day 2 집중, 이후 상시)

| 증상 | 해결 |
|------|------|
| `python` 못 찾음 (Win) | 설치 관리자 'Modify'에서 PATH 추가 → 터미널 재시작 |
| `python`이 아니라 `python3`만 (Mac) | macOS는 `python3`·`pip3` 사용 |
| SSL/인증서 오류 (Mac) | 'Install Certificates.command' 실행 |
| `claude` 못 찾음 | 터미널 재시작 / `claude doctor` |
| 설치 스크립트 오류·HTML | Win은 PowerShell `irm`, Mac은 `curl`/Homebrew |
| 로그인 브라우저 안 열림 | 터미널에서 `c`로 URL 복사 → 직접 붙여넣기 |
| PubMed 지연/오류 | 개수 5~10으로 축소, 또는 백업 `papers/` 사용 |

---

## 5. 공통 지도 원칙

- **대신 해주지 말 것** — 답이 아니라 "에이전트에게 어떻게 물을지"를 코칭. 학생 역할은 방향 제시 + 검증.
- **검증을 습관화** — "됐다"가 아니라 "직접 실행해 확인했나요?"를 반복.
- **AI 출력은 반드시 사람이 검증** — 논문(가짜 주의)·수치·인용. 일관된 핵심 메시지.
- **작게·반복** — 큰 한 번보다 작은 단위로.
- **진척 편차 흡수** — 빠른 팀은 심화, 느린 팀은 개별 지원.

---

## 6. 세션 종료 시 점검(학생 산출물)

- Day 2: 전원 설치·로그인 완료
- Day 3: 개인 동작물 + 팀 기획서(`research-plan-template.md`)
- Day 4 오전: `papers/`에 실재 논문 20~30편
- Day 4 오후1: 논문 정리표 + 근거 달린 gap 목록
- Day 4 오후2: 가설 평가표 + 상위 가설 1~2개
- Day 5: 검토를 거친 제안서·발표자료

---

## 7. examples 폴더 빠른 지도

| 경로 | 쓰는 시점 |
|------|-----------|
| `claude-setup/` | Day 2 오후2 (설정) |
| `mini-project/project-plan-template.md` | Day 3 오전 |
| `mini-project/sandbox/` | Day 2~3 동작 확인 |
| `prompts/research-prompts.md` | Day 4 단계별 프롬프트 |
| `research-agent/CLAUDE.md` | Day 4 에이전트 규칙 |
| `research-agent/research-plan-template.md` | Day 3 오후2 팀 기획 |
| `research-agent/collect/collect_pubmed.py` | Day 4 오전 수집 |
| `research-agent/sources/` | (네트워크 없이) 연습용 corpus |
| `research-agent/worksheets/1~3` | Day 4 오후 (정리표·gap·평가표) |
| `research-agent/output/report-template.md` | Day 5 제안서 |
| `research-agent/output/SAMPLE-hypothesis-proposal.md` | 완성 예시(목표 모습) |

---

## 8. 자주 나오는 학생 질문 (FAQ)

- "에이전트가 만든 논문이 진짜인가요?" → PMID/링크로 확인. 실제 API로 받은 것만 신뢰.
- "가설을 몇 개 만들어야?" → 생성은 많이(6~10개), 제안은 1~2개로 추림.
- "질문에 답 정리하는 거 아닌가요?" → 아닙니다. 목표는 **새 가설 제안**(Q&A 보고서 아님).
- "코드가 에러나요." → 에러 메시지를 그대로 에이전트에 붙여 "이 에러 고쳐줘".
- "어디까지 하면 끝?" → 6장의 산출물 기준으로 안내.

---

## 9. 리허설 기록 (조교용 메모 양식)

각 조교가 리허설 후 채워 공유하면 수업 운영에 큰 도움이 됩니다.

```
- 환경(OS):
- 전 과정 소요 시간:
- 막혔던 지점 / 해결:
- 학생이 자주 물을 것 같은 질문:
- 백업 papers/ 확보 여부:
- 개선 제안(자료·프롬프트):
```
