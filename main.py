#!/usr/bin/env python3
"""One Line of Earned Pride.

Writes a single line of text -- one quiet, earned moment of pride --
to /output/entry.txt. Exactly one line, no trailing newline.
"""

import os

LINE = (
    "Three summers he carried planks up the old oak after his shift, and "
    "tonight his daughter climbed the rope ladder alone, pushed open the "
    "trapdoor, and switched on the little lamp he had wired by hand."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> int:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # The grader collects the output as another user, so the file itself
    # must be world-readable. Never chmod the /output directory itself:
    # it is root-owned and merely writable, and chmod on it raises
    # PermissionError and fails the run.
    os.chmod(OUTPUT_PATH, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
