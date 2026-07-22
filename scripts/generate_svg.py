from pathlib import Path
import html

BASE = Path(__file__).resolve().parent.parent

ASCII_FILE = BASE / "assets" / "ascii.txt"
OUTPUT_DIR = BASE / "output"

OUTPUT_DIR.mkdir(exist_ok=True)

ascii_art = ASCII_FILE.read_text(encoding="utf-8")

lines = ascii_art.splitlines()

font_size = 8
line_height = 9

width = 1200
height = max(500, len(lines) * line_height + 60)


def build_svg(theme):
    if theme == "dark":
        bg = "#050816"
        text = "url(#asciiGradient)"
        border = "#00F5FF"
    else:
        bg = "#ffffff"
        text = "url(#asciiGradientLight)"
        border = "#3B82F6"

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg"
width="{width}"
height="{height}"
viewBox="0 0 {width} {height}">

<defs>

<linearGradient id="asciiGradient"
x1="0%"
y1="0%"
x2="100%"
y2="100%">

<stop offset="0%" stop-color="#00F5FF"/>

<stop offset="35%" stop-color="#00C8FF"/>

<stop offset="70%" stop-color="#7C3AED"/>

<stop offset="100%" stop-color="#FF00FF"/>

</linearGradient>

<linearGradient id="asciiGradientLight"
x1="0%"
y1="0%"
x2="100%"
y2="100%">

<stop offset="0%" stop-color="#2563EB"/>

<stop offset="50%" stop-color="#7C3AED"/>

<stop offset="100%" stop-color="#EC4899"/>

</linearGradient>

<filter id="glow">

<feGaussianBlur stdDeviation="2" result="coloredBlur"/>

<feMerge>

<feMergeNode in="coloredBlur"/>

<feMergeNode in="SourceGraphic"/>

</feMerge>

</filter>

</defs>

<rect width="100%" height="100%" fill="{bg}"/>

<rect
x="20"
y="20"
width="{width-40}"
height="{height-40}"
rx="15"
fill="none"
stroke="{border}"
stroke-width="2"/>

<text
x="40"
y="50"
font-family="Consolas, monospace"
font-size="{font_size}"
fill="{text}"
filter="url(#glow)">'''

    y = 0

    for line in lines:
        safe = html.escape(line)
        svg += f'<tspan x="40" dy="{line_height}">{safe}</tspan>'

    svg += """
</text>

</svg>
"""

    return svg


(OUTPUT_DIR / "dark.svg").write_text(
    build_svg("dark"),
    encoding="utf-8"
)

(OUTPUT_DIR / "light.svg").write_text(
    build_svg("light"),
    encoding="utf-8"
)

print("SVG generated successfully.")