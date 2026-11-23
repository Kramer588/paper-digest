# -*- coding: utf-8 -*-
"""paper-digest 1.3.0 workspace checker. Usage: python check_workspace.py <workspace>"""
import io, os, re, sys


def read(p):
    return io.open(p, encoding="utf-8").read() if os.path.exists(p) else ""


def main(ws):
    ok = True
    checks = []

    def req(rel, label, min_len=1):
        nonlocal ok
        t = read(os.path.join(ws, rel))
        good = len(t.strip()) >= min_len
        ok = ok and good
        checks.append((label, rel, good, len(t)))

    # core state
    for rel, label in [("RESEARCH-AGENDA.md", "项目议程"), ("LEARNER-PROFILE.md", "学习者画像"),
                       ("PLAN.md", "学习计划"), ("RESOURCES.md", "文献库"),
                       ("review/QUEUE.md", "复习队列"), ("MASTERY.md", "掌握矩阵")]:
        req(rel, label)

    # assets
    for a in ("assets/lesson.css", "assets/quiz.js"):
        req(a, "资产")

    # digests: HTML primary, md legacy
    ddir = os.path.join(ws, "digests")
    if os.path.isdir(ddir):
        for fn in sorted(os.listdir(ddir)):
            p = os.path.join(ddir, fn)
            if fn.endswith(".md"):
                print("  legacy digest（.md，重读时迁移为 HTML）：", fn)
                continue
            if not fn.endswith(".html"):
                continue
            t = read(p)
            need = {
                "digest-head": 'class="digest-head"' in t,
                "toc": 'class="toc"' in t,
                "claim-table": 'class="claim-table"' in t,
                "teachback": 'id="teachback"' in t,
                "quiz>=2": len(re.findall(r"data-quiz", t)) >= 2,
                "details>=5": t.count("<details") >= 5,
                "writing-qa": 'id="writing-qa"' in t and len(re.findall(r"data-write", t)) >= 3,
                "assets": "../assets/lesson.css" in t and "../assets/quiz.js" in t,
            }
            miss = [k for k, v in need.items() if not v]
            good = not miss
            ok = ok and good
            checks.append(("digest HTML 结构", fn, good, len(t)))
            if miss:
                print("  digest 缺：", fn, miss)

    # lessons
    ldir = os.path.join(ws, "lessons")
    if os.path.isdir(ldir):
        for fn in sorted(os.listdir(ldir)):
            if fn.endswith(".html"):
                t = read(os.path.join(ldir, fn))
                good = ("data-quiz" in t or "data-recall" in t) and ("lesson.css" in t or "quiz.js" in t)
                ok = ok and good
                checks.append(("lesson 结构", fn, good, len(t)))

    print("\n== paper-digest 1.3.0 workspace check ==")
    for label, rel, good, n in checks:
        print(("PASS" if good else "FAIL"), label, rel, n)
    print("\nRESULT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else os.getcwd()))
