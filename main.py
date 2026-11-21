"""Entry for make.fun's news-image-20261121 bounty.

The artwork (art.jpg, a newspaper front page summing up 21 November
2026's world news) ships inside this repository. Running this program
copies it, byte for byte, to /output/entry.png, which is the file the
bounty grades. The copy is a pure file transfer, so two runs always
produce identical bytes.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "art.jpg")
OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.png")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT_FILE)
    print(f"wrote {OUTPUT_FILE} from {SOURCE}")


if __name__ == "__main__":
    main()
