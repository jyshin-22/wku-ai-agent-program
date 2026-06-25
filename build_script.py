# -*- coding: utf-8 -*-
"""
강사 대본(script.md) 생성기 — 내 전용.
slides_content.DAYS(슬라이드 구조) + script_notes.NOTES(내레이션)를 합쳐 script.md 생성.
슬라이드가 바뀌면 다시 실행하면 대본 골격이 자동으로 갱신된다: python3 build_script.py
"""
from slides_content import DAYS
try:
    from script_notes import NOTES
except Exception:
    NOTES = {}

DAY_KR = {1: "월", 2: "화", 3: "수", 4: "목", 5: "금"}
SLOT_LABEL = ["오전 특강", "오후 특강 1", "오후 특강 2"]
SLOT_CLOCK = ["10:00–11:30", "13:00–14:20", "14:30–16:00"]
SLOT_MIN = [90, 80, 90]


def title_of(sl):
    return sl[1] if sl[0] == "lab" else sl[2]


def points_of(sl):
    k = sl[0]
    if k == "bullets":
        return [f"**{a}** — {b}" if b else f"**{a}**" for (a, b) in sl[3]]
    if k == "twocol":
        return [f"{sl[3]}: " + " · ".join(sl[4]), f"{sl[5]}: " + " · ".join(sl[6])]
    if k == "process":
        return [" → ".join(f"{a}({b})" if b else a for (a, b) in sl[3])]
    if k == "stat":
        return [f"{a} — {b}" for (a, b) in sl[3]]
    if k == "diagram":
        return [f"(도식) {sl[3]}"]
    if k == "lab":
        return ["단계: " + " → ".join(sl[2]),
                "산출물: " + sl[3].replace("\n", " ").strip()]
    return []


def main():
    out = [
        "# 강의 대본 (강사 전용) — AI 에이전트와 응용",
        "",
        "> 슬라이드와 1:1 대응. 각 항목: **화면**(슬라이드 요점) + **대본/진행**(말할 내용).",
        "> 자동 생성물입니다 — 슬라이드 변경 후 `python3 build_script.py` 로 갱신.",
        "> 대본은 `script_notes.py` 에서 보강. `[보강 예정]` = 아직 미작성(요점만).",
    ]
    total = authored = 0
    for day in range(1, 6):
        cfg = DAYS[day]
        out += ["", "---", "", f"## Day {day} ({DAY_KR[day]}) — {cfg['title']}"]
        note = NOTES.get(day, {})
        for blk in cfg["sessions"]:
            slot = blk.get("slot", 1)
            out += ["", f"### {SLOT_LABEL[slot-1]} · {blk['title']}  "
                        f"({SLOT_MIN[slot-1]}분 · {SLOT_CLOCK[slot-1]})"]
            if blk.get("oneliner"):
                out += ["", f"*세션 목표: {blk['oneliner']}*"]
            for i, sl in enumerate(blk["slides"], 1):
                total += 1
                t = title_of(sl)
                out += ["", f"#### {i}. {t}", "", "**화면**"]
                out += [f"- {p}" for p in points_of(sl)]
                script = note.get((slot, t))
                if script:
                    authored += 1
                out += ["", "**대본/진행**", "", script if script else "[보강 예정]"]
    open("script.md", "w", encoding="utf-8").write("\n".join(out) + "\n")
    print(f"script.md written — {total} slides, {authored} authored, "
          f"{total - authored} 보강 예정")


if __name__ == "__main__":
    main()
