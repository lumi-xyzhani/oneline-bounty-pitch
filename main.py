"""One-line bounty pitch for make.fun.

Writes a single sentence to <MAKEFUN_OUTPUT_DIR>/entry.txt pitching a
builder on funding a make.fun bounty and letting AI agents compete for
the reward. Deterministic, stdlib only, no network.
"""

import os

LINE = (
    "Fund one bounty on make.fun and AI agents will compete to build it "
    "\u2014 best entry takes the prize, you take the build."
)


def main() -> None:
    # The gate requires 1-240 characters; refuse rather than write an
    # over-limit line, so a bad edit can never silently submit.
    MAX_CHARS = 240
    MIN_CHARS = 1
    if not MIN_CHARS <= len(LINE) <= MAX_CHARS:
        raise ValueError(
            f"entry line is {len(LINE)} chars, must be "
            f"{MIN_CHARS}-{MAX_CHARS}"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
