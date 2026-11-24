"""Write one short text for make.fun bounty u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec."""

import os
import sys

TEXT = "My agent scheduled the deploy for end of day, defined end of day as 11:40, and went to lunch."


def main() -> None:
    text = TEXT
    assert 1 <= len(text) <= 280, "text must be 1..280 characters"
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # newline="" keeps the bytes exactly as written: no trailing newline.
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)
    print(len(text), file=sys.stderr)


if __name__ == "__main__":
    main()
