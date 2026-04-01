#!/usr/bin/env python3
"""
Generate an animated SVG of a ship sailing across the GitHub contribution graph.
The ship leaves a wake trail and the ocean has gentle waves.
Contribution cells become ocean depth — darker green = deeper water.
"""

import json
import os
import requests
from datetime import datetime, timedelta

# ── CONFIG ──
CELL_SIZE = 13
CELL_GAP = 3
CELL_RADIUS = 2
COLS = 53  # weeks
ROWS = 7   # days
MARGIN_LEFT = 40
MARGIN_TOP = 30
WIDTH = MARGIN_LEFT + COLS * (CELL_SIZE + CELL_GAP) + 40
HEIGHT = MARGIN_TOP + ROWS * (CELL_SIZE + CELL_GAP) + 60

# Ocean palette (dark theme, maritime)
COLORS = {
    0: "#0d1117",      # deep ocean (no contributions)
    1: "#0e4429",      # shallow water
    2: "#006d32",      # medium depth
    3: "#26a641",      # reef
    4: "#39d353",      # surface glow
}

DAY_LABELS = ["", "Mon", "", "Wed", "", "Fri", ""]
MONTH_LABELS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def fetch_contributions(username: str, token: str) -> list[list[int]]:
    """Fetch contribution data from GitHub GraphQL API."""
    query = """
    query($username: String!) {
      user(login: $username) {
        contributionsCollection {
          contributionCalendar {
            weeks {
              contributionDays {
                contributionCount
                date
              }
            }
          }
        }
      }
    }
    """
    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.post(
        "https://api.github.com/graphql",
        json={"query": query, "variables": {"username": username}},
        headers=headers,
    )
    data = resp.json()
    weeks = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]

    grid = []
    for week in weeks:
        col = []
        for day in week["contributionDays"]:
            count = day["contributionCount"]
            if count == 0:
                level = 0
            elif count <= 3:
                level = 1
            elif count <= 7:
                level = 2
            elif count <= 12:
                level = 3
            else:
                level = 4
            col.append(level)
        grid.append(col)
    return grid


def generate_fallback_grid() -> list[list[int]]:
    """Generate a sample grid if API fails."""
    import random
    random.seed(42)
    grid = []
    for _ in range(COLS):
        col = [random.choice([0, 0, 0, 1, 1, 2, 3, 4]) for _ in range(ROWS)]
        grid.append(col)
    return grid


def ship_svg() -> str:
    """SVG path for a cargo vessel silhouette."""
    return """
    <g id="ship">
      <!-- Hull -->
      <path d="M0,18 L4,24 L56,24 L60,18 L54,18 L52,20 L8,20 L6,18 Z"
            fill="#c8ccd0" stroke="#8b9298" stroke-width="0.5"/>
      <!-- Deck -->
      <rect x="10" y="12" width="40" height="6" rx="1"
            fill="#6e7681" stroke="#8b9298" stroke-width="0.5"/>
      <!-- Superstructure -->
      <rect x="14" y="4" width="14" height="8" rx="1"
            fill="#8b9298" stroke="#6e7681" stroke-width="0.5"/>
      <!-- Bridge windows -->
      <rect x="16" y="6" width="3" height="2" rx="0.5" fill="#58a6ff" opacity="0.8"/>
      <rect x="20" y="6" width="3" height="2" rx="0.5" fill="#58a6ff" opacity="0.8"/>
      <rect x="24" y="6" width="3" height="2" rx="0.5" fill="#58a6ff" opacity="0.8"/>
      <!-- Mast -->
      <line x1="21" y1="0" x2="21" y2="4" stroke="#8b9298" stroke-width="1.5"/>
      <!-- Funnel -->
      <rect x="36" y="6" width="8" height="6" rx="1"
            fill="#da3633" stroke="#8b9298" stroke-width="0.5"/>
      <!-- Funnel stripe -->
      <rect x="36" y="8" width="8" height="2" fill="#f0f6fc" opacity="0.3"/>
      <!-- Smoke -->
      <circle cx="40" cy="3" r="2" fill="#6e7681" opacity="0.4">
        <animate attributeName="cy" values="3;-2;-8" dur="3s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="0.4;0.2;0" dur="3s" repeatCount="indefinite"/>
        <animate attributeName="r" values="2;3;4" dur="3s" repeatCount="indefinite"/>
      </circle>
      <circle cx="42" cy="5" r="1.5" fill="#6e7681" opacity="0.3">
        <animate attributeName="cy" values="5;0;-6" dur="3.5s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="0.3;0.15;0" dur="3.5s" repeatCount="indefinite"/>
        <animate attributeName="r" values="1.5;2.5;3.5" dur="3.5s" repeatCount="indefinite"/>
      </circle>
      <!-- Cargo containers -->
      <rect x="10" y="13" width="4" height="4" rx="0.5" fill="#1f6feb" opacity="0.7"/>
      <rect x="15" y="13" width="4" height="4" rx="0.5" fill="#da3633" opacity="0.7"/>
      <rect x="30" y="13" width="4" height="4" rx="0.5" fill="#2ea043" opacity="0.7"/>
      <rect x="35" y="13" width="4" height="4" rx="0.5" fill="#1f6feb" opacity="0.7"/>
      <rect x="44" y="13" width="4" height="4" rx="0.5" fill="#da3633" opacity="0.7"/>
    </g>
    """


def wake_trail_svg() -> str:
    """Animated wake/foam behind the ship."""
    return """
    <g id="wake" opacity="0.3">
      <line x1="-5" y1="22" x2="-40" y2="28" stroke="#58a6ff" stroke-width="1"
            stroke-dasharray="3,5">
        <animate attributeName="stroke-dashoffset" values="0;-16" dur="1s" repeatCount="indefinite"/>
      </line>
      <line x1="-5" y1="20" x2="-50" y2="26" stroke="#58a6ff" stroke-width="0.8"
            stroke-dasharray="2,6">
        <animate attributeName="stroke-dashoffset" values="0;-16" dur="1.3s" repeatCount="indefinite"/>
      </line>
    </g>
    """


def wave_pattern_svg() -> str:
    """Subtle animated wave overlay."""
    return """
    <defs>
      <pattern id="waves" x="0" y="0" width="120" height="20"
               patternUnits="userSpaceOnUse">
        <path d="M0,10 Q15,5 30,10 Q45,15 60,10 Q75,5 90,10 Q105,15 120,10"
              fill="none" stroke="#58a6ff" stroke-width="0.5" opacity="0.08">
          <animateTransform attributeName="transform" type="translate"
                            values="0,0;-120,0" dur="8s" repeatCount="indefinite"/>
        </path>
      </pattern>
    </defs>
    """


def generate_svg(grid: list[list[int]]) -> str:
    """Generate the complete animated SVG."""
    total_width = MARGIN_LEFT + COLS * (CELL_SIZE + CELL_GAP)
    anim_duration = "20s"

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}"',
        f'     viewBox="0 0 {WIDTH} {HEIGHT}">',
        "",
        "<!-- Background -->",
        f'<rect width="{WIDTH}" height="{HEIGHT}" rx="6" fill="#0d1117"/>',
        "",
        wave_pattern_svg(),
        f'<rect width="{WIDTH}" height="{HEIGHT}" fill="url(#waves)" rx="6"/>',
        "",
        "<!-- Day labels -->",
    ]

    # Day labels
    for row in range(ROWS):
        if DAY_LABELS[row]:
            y = MARGIN_TOP + row * (CELL_SIZE + CELL_GAP) + CELL_SIZE * 0.75
            parts.append(
                f'<text x="{MARGIN_LEFT - 8}" y="{y}" '
                f'fill="#8b9298" font-size="10" font-family="system-ui,-apple-system,sans-serif" '
                f'text-anchor="end">{DAY_LABELS[row]}</text>'
            )

    # Month labels
    parts.append("")
    parts.append("<!-- Month labels -->")
    month_positions = {}
    for col_idx, col_data in enumerate(grid):
        if col_data:
            # First day of each week — check if it's a new month
            pass
    # Simplified: place month labels evenly
    for i, month in enumerate(MONTH_LABELS):
        x = MARGIN_LEFT + (i * COLS // 12) * (CELL_SIZE + CELL_GAP) + 4
        parts.append(
            f'<text x="{x}" y="{MARGIN_TOP - 8}" '
            f'fill="#8b9298" font-size="10" font-family="system-ui,-apple-system,sans-serif">'
            f'{month}</text>'
        )

    # Contribution cells
    parts.append("")
    parts.append("<!-- Contribution cells (ocean) -->")
    for col_idx, col_data in enumerate(grid):
        for row_idx, level in enumerate(col_data):
            x = MARGIN_LEFT + col_idx * (CELL_SIZE + CELL_GAP)
            y = MARGIN_TOP + row_idx * (CELL_SIZE + CELL_GAP)
            color = COLORS[level]
            parts.append(
                f'<rect x="{x}" y="{y}" width="{CELL_SIZE}" height="{CELL_SIZE}" '
                f'rx="{CELL_RADIUS}" fill="{color}" stroke="#21262d" stroke-width="0.5"/>'
            )

    # Ship animation
    start_x = -70
    end_x = total_width + 20
    ship_y = MARGIN_TOP + 2 * (CELL_SIZE + CELL_GAP) - 4  # Sail at row 2-3

    parts.append("")
    parts.append("<!-- Animated ship -->")
    parts.append(f'<g transform="translate({start_x},{ship_y}) scale(0.9)">')
    parts.append(f'  <animateTransform attributeName="transform" type="translate"')
    parts.append(f'    values="{start_x},{ship_y};{end_x},{ship_y}"')
    parts.append(f'    dur="{anim_duration}" repeatCount="indefinite"')
    parts.append(f'    additive="replace"/>')
    # Gentle bobbing
    parts.append(f'  <animateTransform attributeName="transform" type="translate"')
    parts.append(f'    values="0,0;0,-1.5;0,0;0,1.5;0,0"')
    parts.append(f'    dur="2.5s" repeatCount="indefinite"')
    parts.append(f'    additive="sum"/>')
    parts.append(wake_trail_svg())
    parts.append(ship_svg())
    parts.append("</g>")

    # Title
    parts.append("")
    parts.append("<!-- Title -->")
    parts.append(
        f'<text x="{WIDTH - 20}" y="{HEIGHT - 15}" '
        f'fill="#484f58" font-size="10" font-family="system-ui,-apple-system,sans-serif" '
        f'text-anchor="end" font-style="italic">'
        f'github.com/ORTODOX1</text>'
    )

    parts.append("")
    parts.append("</svg>")

    return "\n".join(parts)


def main():
    username = "ORTODOX1"
    token = os.environ.get("GITHUB_TOKEN", "")

    if token:
        try:
            grid = fetch_contributions(username, token)
            print(f"Fetched {len(grid)} weeks of contribution data")
        except Exception as e:
            print(f"API fetch failed: {e}, using fallback")
            grid = generate_fallback_grid()
    else:
        print("No GITHUB_TOKEN, using fallback grid")
        grid = generate_fallback_grid()

    svg = generate_svg(grid)

    os.makedirs("dist", exist_ok=True)
    with open("dist/ship-animation.svg", "w") as f:
        f.write(svg)

    # Also generate dark variant
    with open("dist/ship-animation-dark.svg", "w") as f:
        f.write(svg)

    print(f"Generated SVG: {len(svg)} bytes")
    print("Output: dist/ship-animation.svg")


if __name__ == "__main__":
    main()
