"""Entry for make.fun bounty "Have You Tried Turning It Off?".

Writes one funny tech-support line (97 chars, under the 200-char gate) to
$MAKEFUN_OUTPUT_DIR/entry.txt. Stdlib only; never writes into the repo.
"""

import os

LINE = "Your ticket has been escalated to our highest tier. That's me. I'm the highest tier. Please hold."

# Gate: entry.txt must be UTF-8 text of 1 to 199 characters, not only whitespace.
assert 1 <= len(LINE) <= 199 and LINE.strip(), "winning line fails the gate"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
