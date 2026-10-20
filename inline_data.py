#!/usr/bin/env python3
"""Inline swechat_data.js so each page works as a standalone file."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "swechat_data.js"
PAGES = ("aidev_rejection_pie.html", "aidev_rejection_pie_en.html")
BEGIN = "<!-- BEGIN INLINE SWECHAT DATA -->"
END = "<!-- END INLINE SWECHAT DATA -->"
SRC = re.compile(r'<script src="swechat_data\.js(?:\?[^"]*)?"></script>')


def main():
    block = f"{BEGIN}\n<script>\n{DATA.read_text(encoding='utf-8').rstrip()}\n</script>\n{END}"
    for name in PAGES:
        page = ROOT / name
        text = page.read_text(encoding="utf-8")
        if BEGIN in text:
            text = re.sub(
                re.escape(BEGIN) + r".*?" + re.escape(END),
                lambda _: block,
                text,
                count=1,
                flags=re.S,
            )
        else:
            text, count = SRC.subn(lambda _: block, text, count=1)
            if count != 1:
                raise SystemExit(f"{name}: swechat_data.js script tag not found")
        page.write_text(text, encoding="utf-8")
        print(f"inlined {name}")


if __name__ == "__main__":
    main()
