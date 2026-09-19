from datetime import date
from pathlib import Path

START_DATE = date(2021, 12, 9)

ROOT = Path(__file__).resolve().parent.parent
SVG_FILE = ROOT / "assets" / "terminal.svg"

today = date.today()

years = today.year - START_DATE.year
months = today.month - START_DATE.month

if today.day < START_DATE.day:
    months -= 1

if months < 0:
    years -= 1
    months += 12

uptime = f"uptime {years}y {months}m"

svg = SVG_FILE.read_text(encoding="utf-8")

# Replace the previous generated line.
import re

svg = re.sub(
    r'\d{4}-\d{2}-\d{2} · uptime \d+y \d+m · still shipping',
    f'2021-12-09 · {uptime} · still shipping',
    svg
)

SVG_FILE.write_text(svg, encoding="utf-8")

print(f"Updated terminal: 2021-12-09 · {uptime} · still shipping")
