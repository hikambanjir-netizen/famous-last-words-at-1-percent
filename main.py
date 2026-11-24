"""Famous Last Words at 1 Percent — make.fun entry.

Writes the phone's last line to the grader's output file.
"""

import os

LINE = "Somebody tell my 6 a.m. alarm that all of last night's optimism was for nothing."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        pass
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
