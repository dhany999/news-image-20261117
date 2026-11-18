"""Entry program for make.fun news-image-20261117.

Copies the bundled image (entry.png, kept in this program's own
directory) to the output directory as entry.png. The output directory
comes from the MAKEFUN_OUTPUT_DIR environment variable and defaults to
/output when that variable is not set. Standard library only; the copy
is byte for byte, so two runs write identical files.
"""

import os
import shutil
import sys
from pathlib import Path


def main():
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    if not source.is_file():
        raise FileNotFoundError(
            "entry.png not found next to main.py: %s" % source
        )
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(source, target)
    # Guard the deterministic-output rule: the copy must be byte for
    # byte identical to the bundled image, so compare sizes and refuse
    # to report success when they differ.
    if target.stat().st_size != source.stat().st_size:
        raise IOError(
            "copied entry.png size %d != source size %d"
            % (target.stat().st_size, source.stat().st_size)
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
