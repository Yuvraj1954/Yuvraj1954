from datetime import date
from pathlib import Path
import re

START_DATE = date(2021, 12, 9)

ROOT = Path(__file__).resolve().parent.parent
SVG_FILE = ROOT / "assets" / "terminal.svg"
README_FILE = ROOT / "README.md"


def calculate_uptime(start: date, today: date) -> str:
    years = today.year - start.year
    months = today.month - start.month

    if today.day < start.day:
        months -= 1

    if months < 0:
        years -= 1
        months += 12

    return f"uptime {years}y {months}m"


today = date.today()
uptime = calculate_uptime(START_DATE, today)

# Update uptime in SVG
svg = SVG_FILE.read_text(encoding="utf-8")

pattern = r"2021-12-09 · uptime \d+y \d+m · still shipping"
replacement = f"2021-12-09 · {uptime} · still shipping"

updated_svg, count = re.subn(pattern, replacement, svg)

if count != 1:
    raise RuntimeError(
        f"Expected exactly one uptime line in terminal.svg, found {count}."
    )

SVG_FILE.write_text(updated_svg, encoding="utf-8")

# Update README cache-busting version
readme = README_FILE.read_text(encoding="utf-8")

cache_pattern = r"(assets/terminal\.svg\?v=)\d+"
cache_replacement = rf"\g<1>{today:%Y%m%d}"

updated_readme, cache_count = re.subn(
    cache_pattern,
    cache_replacement,
    readme,
)

if cache_count != 1:
    raise RuntimeError(
        f"Expected exactly one terminal.svg cache URL in README.md, "
        f"found {cache_count}."
    )

README_FILE.write_text(updated_readme, encoding="utf-8")

print(f"Updated terminal: 2021-12-09 · {uptime} · still shipping")
print(f"Updated README cache key: {today:%Y%m%d}")
