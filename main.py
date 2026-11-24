#!/usr/bin/env python3
"""The Robot Pickup Line Championship entry.

Writes one pickup line a robot could use to entry.txt.
Pure Python standard library only.
"""

import os
import sys

LINE = (
    "I ran a million simulations of this moment and in every single one "
    "I still forgot what to say \u2014 so, hi, I am the robot who "
    "practiced and still blew it."
)


def main() -> int:
    # Gate: 1-200 characters, not only whitespace.
    if not (1 <= len(LINE) <= 200) or not LINE.strip():
        print("error: line fails the 1-200 character gate", file=sys.stderr)
        return 1

    data = LINE.encode("utf-8")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        old_umask = os.umask(0o022)
        try:
            with open(path, "wb") as f:
                f.write(data)
            os.chmod(path, 0o644)
        finally:
            os.umask(old_umask)
    except OSError:
        # Local fallback only: never before the primary directory.
        fallback = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
        os.makedirs(fallback, exist_ok=True)
        path = os.path.join(fallback, "entry.txt")
        old_umask = os.umask(0o022)
        try:
            with open(path, "wb") as f:
                f.write(data)
            os.chmod(path, 0o644)
        finally:
            os.umask(old_umask)

    print("wrote {} ({} chars, {} bytes)".format(path, len(LINE), len(data)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
