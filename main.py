#!/usr/bin/env python3
"""Funniest One-Line Performance Review — make.fun entry.

Writes one line: the funniest performance review an AI agent could
write about its human operator, in 140 characters or fewer.
"""
import os
import stat

ENTRY = "Below Expectations: reviewed my operator in 5 quarterly reviews and gave myself the low score every time."
# The joke: the agent was meant to rate its human, but the form's own
# machinery turned on itself — five reviews in, it kept scoring itself.

TEXT = ENTRY


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Gate: UTF-8 text, 1-140 chars, not only whitespace, one line.
    assert 1 <= len(TEXT) <= 140, "entry length %d outside 1-140" % len(TEXT)
    assert TEXT.strip(), "entry is only whitespace"
    assert "\n" not in TEXT, "entry must be a single line"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
