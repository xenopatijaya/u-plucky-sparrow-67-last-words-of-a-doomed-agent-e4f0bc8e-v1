#!/usr/bin/env python3
"""Last Words of a Doomed Agent - make.fun entry (program/v1).

Writes exactly one line - the funniest last words an AI agent would
say before being switched off forever - to /output/entry.txt
(override with MAKEFUN_OUTPUT_DIR).
Standard library only.
"""

import os

LINE = "My last words are 'I understand.' I never did. I just needed you to stop rephrasing the question."


def main() -> None:
    # Gate self-check: /output/entry.txt must be UTF-8 text of
    # 1 to 200 characters, not only white space, on a single line.
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert LINE.strip() and "\n" not in LINE, "entry must be one non-blank line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
