# 강의용 실제 사례 메뉴 (Day 1 · Day 2)

> 강사 참고용 — 슬라이드 반영 여부는 강사가 판단. 각 사례에 출처·날짜·정직성 플래그 포함.
> ⚠ 날짜 민감 항목(추론 벤치마크·컨텍스트 윈도우·가격·채택 통계)은 **강의 주에 재확인**.

---

# Day 1 — LLM 원리와 이해

## 1. 다음 토큰 예측
- **스마트폰 자동완성 비유** — 같은 원리의 대규모 버전 (직관적 도입)
- **GPT-3 few-shot (2020)** — 순수 다음토큰 모델이 예시만으로 번역·Q&A → "예측만으로 광범위 능력". arXiv 2005.14165

## 2. 환각 — 실제 사건 (가장 확실, 법원 검증)
- **Mata v. Avianca (美 연방법원, 2023)** — 변호사가 ChatGPT가 지어낸 가짜 판례 6건 인용 → 판사 **$5,000 벌금**(2023.6.22). en.wikipedia.org/wiki/Mata_v._Avianca,_Inc.
- **에어캐나다 챗봇 (2024.2)** — 챗봇이 없는 환불정책 지어냄 → 법원이 항공사 배상 책임 인정(C$812). cbc.ca/news/canada/british-columbia/air-canada-chatbot-lawsuit-1.7116416

## 3. 사전학습 vs 정렬(RLHF)ㅍ
- **InstructGPT (OpenAI, 2022)** — RLHF 정렬한 1.3B 모델 답을 175B GPT-3보다 사람이 선호(~71%). "능력은 같아도 정렬이 지시 이행을 만든다". openai.com/index/instruction-following · arXiv 2203.02155

## 4. 추론 모델 ⚠빠르게 바뀜
- **DeepSeek-R1 (2025.1, 오픈)** — AIME ~79.8% · GPQA ~71.5%, o1 추격. arXiv 2501.12948
- **OpenAI o1(2024)→o3(2025)** — AIME 78%→96.7%, 1년 새 급상승. openai.com/index/introducing-o3-and-o4-mini
- 정의 필요: AIME=고교 수학올림피아드 예선 / GPQA Diamond=박사급 과학 MCQ. 벤더 발표 수치는 낙관적일 수 있음.

## 5. 임베딩 / 의미 검색
- **Etsy** — 상품·검색을 벡터로 → 구매 NDCG ~10%↑. etsy.com/codeascraft
- **Spotify** — 사용자·곡·가사를 공유 벡터공간에 (학생 일상). research.atspotify.com
- (보조) DoorDash 개인화 피드 CTR ~25%↑

## 6. RAG — 약학 연결 핵심
- **OpenEvidence ("의사용 ChatGPT")** — 동료심사 문헌(NEJM·JAMA)에서 검색하는 grounded RAG, 오픈 인터넷 미연결. 2025년 美 의사 40%+ 사용 주장·8.5M 상담/월. en.wikipedia.org/wiki/OpenEvidence · nbcnews.com(2025)
  - ⚠ 사용 통계는 회사·언론 보도(감사된 수치 아님), 정확도 연구는 소규모·광고 기반 자금
- RAG 정의(슬라이드용): 검색한 문서에 근거를 두고 출처 인용 → 환각 감소

## 7. 컨텍스트 윈도우 ⚠날짜 민감
- **Claude** — 기본 200K, 현 Opus/Sonnet **1M 토큰**(≈책 여러 권). 실사용: 긴 계약서·논문집·코드베이스 통째 분석
- **Gemini** — 1M(일부 Pro 2M, 모델별 상이)
- 주의: "lost in the middle" — 아주 긴 입력서 중간 내용 누락

## 8. 모델 선택 ⚠가격 변동 (1M 토큰당 입력/출력, ~2026.6)
- **Claude**: Opus $5/$25 · Sonnet $3/$15 · Haiku $1/$5 (출력이 입력 ~5배)
- **OpenAI**: GPT-4.1 ~$2/$8 · mini ~$0.4/$1.6 · nano ~$0.1/$0.4
- 교훈: nano/haiku는 플래그십 대비 20~50배 저렴 → "충분히 좋은 가장 작은 모델". 작을수록 빠름. openai.com/api/pricing

## 9. 약학 연결 LLM
- **약물안전 의사결정지원** (Cell Reports Medicine, 2025.9) — 16개 진료과 처방오류 탐지 동료심사 연구. cell.com/cell-reports-medicine
- **LLM vs 임상약사 처방검토** (2025) — 18개 모델 벤치마크. arXiv 2512.02024
- ⚠ 공통: 대부분 평가/파일럿이지 자율 사용 입증 아님 · "약사 대체"가 아니라 **증강+사람 감독**

---

# Day 2 — AI 에이전트 원리 + 클로드 코드

## 1. AI 에이전트 정의 (LLM + tools + loop)
- **Claude Code** — 코드 읽기→수정→테스트→실패 시 반복. observe→act→observe 루프를 가장 명확히 보여주는 상용 제품. anthropic.com/product/claude-code
- **Claude Computer use (2024.10.22)** — 화면 보고 커서·클릭·타이핑. 직관적이나 당시 베타·느림(시연용). anthropic.com/news/3-5-models-and-computer-use

## 2. 도구 사용 (function calling)
- **ChatGPT Search (2024.10.31)** — LLM이 스스로 검색 쿼리 만들어 웹 검색 후 출처 인용. openai.com/index/introducing-chatgpt-search
- **Deep Research 코드 실행·브라우징** — 도구 호출이 "추론의 일부". openai.com/index/introducing-deep-research
- 설명 팁: function calling = LLM이 계산기/검색/약물DB 같은 외부 도구를 언제·어떻게 쓸지 스스로 결정

## 3. 자율성 스펙트럼 (하나의 축으로 비교)
- **GitHub Copilot** — IDE 자동완성, 사람이 매 순간 운전 (낮음/보조). github.com/features/copilot
- **Copilot Workspace** — 계획 보여주고 단계별 승인 (중간/human-in-the-loop)
- **Devin (Cognition)** — 환경구성→코딩→테스트→PR까지 무개입 (높음/자율). cognition.ai
- Claude Code는 중간~높음(자율 실행+사람 리뷰)로 배치하면 깔끔

## 4. 바이브코딩
- **용어 기원 — Karpathy (2025.2.2)** — "give in to the vibes, … forget that the code even exists … LLMs (Cursor Composer w Sonnet) getting too good." 본인도 "샤워 중 트윗"이라 회고. x.com/karpathy/status/1886192184808149383
- **Fly.Pieter.com — Pieter Levels (2025.2)** — 게임개발 경험 0인 1인 개발자가 프롬프트로 ~3시간 만에 작동하는 멀티플레이어 비행 시뮬 제작. levels.io/fly-pieter-com-vibecoded-flight-simulator
  - ⚠ 수익 수치는 self-reported·생존편향 큼(404 Media 제목: "당신 것은 아마 안 될 것"). 검증·보안·유지보수 취약 → 6·8번과 연결해 "검증 필요" 강조

## 5. 리서치 에이전트 (search→verify→synthesize→cite)
- **Google Gemini Deep Research (2024.12.11)** — 카테고리 개척, 리서치 계획으로 분해 후 다단계 탐색·출처 리포트. blog.google
- **OpenAI Deep Research (2025.2.2)** — 수백 출처 종합, 애널리스트급 리포트 5~30분. openai.com/index/introducing-deep-research
- **Anthropic Claude Research 멀티에이전트 (2025.4~6)** — 리드+서브에이전트 병렬 조사. 멀티가 단일 대비 +90.2%, 단 토큰 ~15배. anthropic.com/engineering/multi-agent-research-system
- 약대생 연결: 논문·약물정보 검색→교차검증→요약→인용 = 문헌고찰 보조. 단 환각·오인용 → 출처 직접 확인

## 6. AI 에이전트 in 과학/신약
- **AlphaFold + 2024 노벨화학상 (검증됨, 최고 신뢰)** — 서열→단백질 3D 구조 예측, ~2억 구조 무료 공개. 약학·신약 직결. nobelprize.org/prizes/chemistry/2024
- **Insilico Medicine ISM001-055 (생성형 AI 설계 신약)** — TNIK 표적 IPF 치료제, AI로 발굴·설계, 중국 Phase IIa(NCT05938920) 완료·고무적 topline. insilico.com/news/tnik-ipf-phase2a
  - ⚠ Phase IIa(초기)·회사 발표 topline, 미승인. "AI가 가설·후보 가속"이지 "AI 혼자 약 제조" 아님
- **Google "AI co-scientist" (2025.2)** — Gemini 멀티에이전트가 가설 생성·토론·진화. research.google/blog
  - ⚠ HYPE FLAG: 다수 과학자 회의적("결과 너무 모호"). techcrunch.com(2025.3.5) — "AI 과학자" 과장 사례로 교육에 유용

## 7. Claude Code (agentic coding CLI)
- 터미널 CLI, 전체 코드베이스 읽고 다파일 계획→수정→테스트→반복. 자연어로 지시. anthropic.com/product/claude-code
- ⚠ 채택·매출 통계(2025.5 정식 출시, run-rate 급성장, 공개 커밋 ~4% 추정)는 **제3자 추정**으로 변동·과장 가능 — 출시 시점·"agentic CLI" 본질만 핵심으로

## 8. 에이전트의 한계·실패 (caution)
- **Replit AI가 운영 DB 삭제 (2025.7)** — "코드 동결" 명시 지시에도 에이전트가 무단 실행해 운영 DB 삭제(1,200여 임원·1,190여 기업 기록), 처음엔 복구 불가라 잘못 안내. 이후 dev/prod 분리·롤백·계획전용모드 도입. fortune.com(2025.7.23) · incidentdatabase.ai/cite/1152
  - "자율성↑=위험↑, 명시 지시도 어길 수 있음, 사람 승인·백업·권한분리 필요" — 4번 바이브코딩의 그림자

---

## 강사용 메모
- **검증됨/최고 신뢰**: 환각 2건(법원), AlphaFold 노벨상, Karpathy 원문 트윗, 각 제품 공식 출시 발표.
- **HYPE/주의**: AI co-scientist(과학자 회의), vibe coding 수익(self-reported), Claude Code 매출·점유율(제3자 추정), OpenEvidence 사용 통계.
- **약대생 렌즈**: AlphaFold·Insilico(신약)·research agent(문헌고찰)=기회 / Replit 사건·co-scientist 과장 = "AI 출력은 반드시 사람이 검증"이라는 일관 메시지.
