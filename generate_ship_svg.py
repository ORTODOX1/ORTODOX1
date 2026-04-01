#!/usr/bin/env python3
"""
Generate an animated SVG of a ship sailing across the GitHub contribution graph.
The ship navigates between contribution "reefs" — weaving around dense areas
and finding the clearest water path through the graph.
"""

import json
import math
import os
import requests

CELL_SIZE = 13
CELL_GAP = 3
CELL_STRIDE = CELL_SIZE + CELL_GAP
COLS = 53
ROWS = 7
MARGIN_LEFT = 40
MARGIN_TOP = 30
WIDTH = MARGIN_LEFT + COLS * CELL_STRIDE + 40
HEIGHT = MARGIN_TOP + ROWS * CELL_STRIDE + 60

COLORS = {
    0: "#0d1117",
    1: "#0e4429",
    2: "#006d32",
    3: "#26a641",
    4: "#39d353",
}

DAY_LABELS = ["", "Mon", "", "Wed", "", "Fri", ""]
MONTH_LABELS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def fetch_contributions(username, token):
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
    resp = requests.post(
        "https://api.github.com/graphql",
        json={"query": query, "variables": {"username": username}},
        headers={"Authorization": f"Bearer {token}"},
    )
    data = resp.json()
    weeks = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
    grid = []
    for week in weeks:
        col = []
        for day in week["contributionDays"]:
            c = day["contributionCount"]
            level = 0 if c == 0 else 1 if c <= 3 else 2 if c <= 7 else 3 if c <= 12 else 4
            col.append(level)
        grid.append(col)
    return grid


def generate_fallback_grid():
    import random
    random.seed(42)
    return [[random.choice([0, 0, 0, 1, 1, 2, 3, 4]) for _ in range(ROWS)] for _ in range(COLS)]


def find_ship_path(grid):
    """
    Find a path for the ship that weaves between dense contribution areas.
    The ship moves left-to-right, choosing the row with least 'reef' density
    at each column, with smooth transitions (max 1 row change per 2 columns).
    """
    # Calculate density: for each column, how heavy is each row
    density = []
    for col_idx in range(len(grid)):
        col_density = []
        for row in range(ROWS):
            # Look at this cell + neighbors for smoothing
            total = 0
            for dc in range(-1, 2):
                ci = col_idx + dc
                if 0 <= ci < len(grid):
                    if row < len(grid[ci]):
                        total += grid[ci][row]
            col_density.append(total)
        density.append(col_density)

    # Find path: greedy with smoothing
    # Start from the row with least density in first columns
    path = []
    current_row = 3  # Start middle

    for col in range(len(grid)):
        # Consider staying or moving +-1 row
        best_row = current_row
        best_score = float('inf')

        for candidate in range(max(0, current_row - 1), min(ROWS, current_row + 2)):
            score = density[col][candidate] if col < len(density) else 0
            # Penalty for being at edges
            if candidate == 0 or candidate == ROWS - 1:
                score += 1
            # Bonus for smooth path (prefer not changing)
            if candidate == current_row:
                score -= 0.3
            if score < best_score:
                best_score = score
                best_row = candidate

        # Only change row every 2-3 columns for smooth sailing
        if col % 2 == 0:
            current_row = best_row

        path.append(current_row)

    return path


def path_to_svg_bezier(path):
    """Convert row-path to smooth SVG bezier curve coordinates."""
    points = []
    for col, row in enumerate(path):
        x = MARGIN_LEFT + col * CELL_STRIDE + CELL_SIZE / 2
        y = MARGIN_TOP + row * CELL_STRIDE + CELL_SIZE / 2
        points.append((x, y))

    if len(points) < 2:
        return ""

    # Build smooth cubic bezier path
    d = f"M {points[0][0]},{points[0][1]}"
    for i in range(1, len(points)):
        # Control points for smooth curve
        prev = points[i - 1]
        curr = points[i]
        cp1x = prev[0] + (curr[0] - prev[0]) * 0.5
        cp1y = prev[1]
        cp2x = prev[0] + (curr[0] - prev[0]) * 0.5
        cp2y = curr[1]
        d += f" C {cp1x},{cp1y} {cp2x},{cp2y} {curr[0]},{curr[1]}"

    return d, points


def ship_svg():
    """Large cargo vessel SVG — scaled up 1.8x from original."""
    return """
    <g id="ship">
      <!-- Hull -->
      <path d="M0,28 L6,38 L90,38 L96,28 L86,28 L83,32 L13,32 L10,28 Z"
            fill="#c8ccd0" stroke="#8b9298" stroke-width="0.7"/>
      <!-- Waterline stripe -->
      <path d="M8,32 L88,32 L86,36 L10,36 Z"
            fill="#8b4c4c" opacity="0.5"/>
      <!-- Deck -->
      <rect x="14" y="18" width="66" height="10" rx="1.5"
            fill="#6e7681" stroke="#8b9298" stroke-width="0.5"/>
      <!-- Superstructure -->
      <rect x="20" y="5" width="24" height="13" rx="1.5"
            fill="#8b9298" stroke="#6e7681" stroke-width="0.7"/>
      <!-- Bridge windows -->
      <rect x="23" y="8" width="5" height="3.5" rx="0.7" fill="#58a6ff" opacity="0.9"/>
      <rect x="30" y="8" width="5" height="3.5" rx="0.7" fill="#58a6ff" opacity="0.9"/>
      <rect x="37" y="8" width="5" height="3.5" rx="0.7" fill="#58a6ff" opacity="0.9"/>
      <!-- Bridge top -->
      <rect x="22" y="2" width="20" height="3" rx="1" fill="#6e7681"/>
      <!-- Mast -->
      <line x1="32" y1="-6" x2="32" y2="2" stroke="#8b9298" stroke-width="2"/>
      <!-- Mast cross -->
      <line x1="27" y1="-3" x2="37" y2="-3" stroke="#8b9298" stroke-width="1"/>
      <!-- Navigation light -->
      <circle cx="32" cy="-6" r="1.5" fill="#da3633" opacity="0.8">
        <animate attributeName="opacity" values="0.8;0.3;0.8" dur="2s" repeatCount="indefinite"/>
      </circle>
      <!-- Funnel -->
      <rect x="56" y="8" width="14" height="10" rx="1.5"
            fill="#da3633" stroke="#8b9298" stroke-width="0.7"/>
      <!-- Funnel stripe -->
      <rect x="56" y="12" width="14" height="3" fill="#f0f6fc" opacity="0.3"/>
      <!-- Funnel top -->
      <rect x="55" y="6" width="16" height="2" rx="1" fill="#4a1010"/>
      <!-- Smoke puffs -->
      <circle cx="63" cy="2" r="3" fill="#6e7681" opacity="0.35">
        <animate attributeName="cy" values="2;-6;-16" dur="4s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="0.35;0.15;0" dur="4s" repeatCount="indefinite"/>
        <animate attributeName="r" values="3;5;7" dur="4s" repeatCount="indefinite"/>
      </circle>
      <circle cx="66" cy="4" r="2.5" fill="#6e7681" opacity="0.25">
        <animate attributeName="cy" values="4;-4;-14" dur="4.5s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="0.25;0.1;0" dur="4.5s" repeatCount="indefinite"/>
        <animate attributeName="r" values="2.5;4;6" dur="4.5s" repeatCount="indefinite"/>
      </circle>
      <circle cx="60" cy="3" r="2" fill="#6e7681" opacity="0.2">
        <animate attributeName="cy" values="3;-5;-13" dur="5s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="0.2;0.08;0" dur="5s" repeatCount="indefinite"/>
        <animate attributeName="r" values="2;3.5;5" dur="5s" repeatCount="indefinite"/>
      </circle>
      <!-- Cargo containers row 1 -->
      <rect x="15" y="19" width="7" height="7" rx="0.7" fill="#1f6feb" opacity="0.8"/>
      <rect x="23" y="19" width="7" height="7" rx="0.7" fill="#da3633" opacity="0.8"/>
      <rect x="46" y="19" width="7" height="7" rx="0.7" fill="#2ea043" opacity="0.8"/>
      <rect x="54" y="19" width="7" height="7" rx="0.7" fill="#1f6feb" opacity="0.8"/>
      <rect x="66" y="19" width="7" height="7" rx="0.7" fill="#da3633" opacity="0.8"/>
      <rect x="74" y="19" width="7" height="7" rx="0.7" fill="#e3b341" opacity="0.8"/>
      <!-- Bow shape -->
      <path d="M86,28 L96,28 L93,33 L88,36 L86,32 Z"
            fill="#adb5bd" stroke="#8b9298" stroke-width="0.5"/>
    </g>
    """


def wake_trail_svg():
    return """
    <g id="wake" opacity="0.25">
      <line x1="-8" y1="34" x2="-60" y2="42" stroke="#58a6ff" stroke-width="1.2"
            stroke-dasharray="4,7">
        <animate attributeName="stroke-dashoffset" values="0;-22" dur="1.2s" repeatCount="indefinite"/>
      </line>
      <line x1="-8" y1="30" x2="-70" y2="38" stroke="#58a6ff" stroke-width="0.8"
            stroke-dasharray="3,8">
        <animate attributeName="stroke-dashoffset" values="0;-22" dur="1.5s" repeatCount="indefinite"/>
      </line>
      <line x1="-8" y1="36" x2="-50" y2="44" stroke="#58a6ff" stroke-width="0.6"
            stroke-dasharray="2,9">
        <animate attributeName="stroke-dashoffset" values="0;-22" dur="1.8s" repeatCount="indefinite"/>
      </line>
    </g>
    """


def bow_wave_svg():
    """Wave at the bow of the ship."""
    return """
    <g id="bowwave" opacity="0.3">
      <path d="M94,36 Q100,30 98,24" fill="none" stroke="#58a6ff" stroke-width="1">
        <animate attributeName="d"
          values="M94,36 Q100,30 98,24;M94,36 Q102,28 96,22;M94,36 Q100,30 98,24"
          dur="2s" repeatCount="indefinite"/>
      </path>
      <path d="M96,38 Q104,32 100,26" fill="none" stroke="#58a6ff" stroke-width="0.6" opacity="0.5">
        <animate attributeName="d"
          values="M96,38 Q104,32 100,26;M96,38 Q106,30 98,24;M96,38 Q104,32 100,26"
          dur="2.3s" repeatCount="indefinite"/>
      </path>
    </g>
    """


def wave_pattern_svg():
    return """
    <defs>
      <pattern id="waves" x="0" y="0" width="200" height="20"
               patternUnits="userSpaceOnUse">
        <path d="M0,10 Q25,6 50,10 Q75,14 100,10 Q125,6 150,10 Q175,14 200,10"
              fill="none" stroke="#58a6ff" stroke-width="0.4" opacity="0.06">
          <animateTransform attributeName="transform" type="translate"
                            values="0,0;-200,0" dur="12s" repeatCount="indefinite"/>
        </path>
      </pattern>
    </defs>
    """


def generate_svg(grid):
    # Find navigation path
    ship_path = find_ship_path(grid)
    path_data, path_points = path_to_svg_bezier(ship_path)

    # Animation duration
    anim_duration = "25s"
    total_path_length = sum(
        math.sqrt((path_points[i][0] - path_points[i-1][0])**2 +
                  (path_points[i][1] - path_points[i-1][1])**2)
        for i in range(1, len(path_points))
    )

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}"',
        f'     viewBox="0 0 {WIDTH} {HEIGHT}">',
        "",
        f'<rect width="{WIDTH}" height="{HEIGHT}" rx="6" fill="#0d1117"/>',
        "",
        wave_pattern_svg(),
        f'<rect width="{WIDTH}" height="{HEIGHT}" fill="url(#waves)" rx="6"/>',
        "",
        "<!-- Navigation path (invisible) -->",
        f'<path id="shipRoute" d="{path_data}" fill="none" stroke="none"/>',
        "",
    ]

    # Day labels
    for row in range(ROWS):
        if DAY_LABELS[row]:
            y = MARGIN_TOP + row * CELL_STRIDE + CELL_SIZE * 0.75
            parts.append(
                f'<text x="{MARGIN_LEFT - 8}" y="{y}" '
                f'fill="#8b9298" font-size="10" font-family="system-ui,sans-serif" '
                f'text-anchor="end">{DAY_LABELS[row]}</text>'
            )

    # Month labels
    for i, month in enumerate(MONTH_LABELS):
        x = MARGIN_LEFT + (i * COLS // 12) * CELL_STRIDE + 4
        parts.append(
            f'<text x="{x}" y="{MARGIN_TOP - 8}" '
            f'fill="#8b9298" font-size="10" font-family="system-ui,sans-serif">'
            f'{month}</text>'
        )

    # Contribution cells
    parts.append("")
    for col_idx, col_data in enumerate(grid):
        for row_idx, level in enumerate(col_data):
            x = MARGIN_LEFT + col_idx * CELL_STRIDE
            y = MARGIN_TOP + row_idx * CELL_STRIDE
            parts.append(
                f'<rect x="{x}" y="{y}" width="{CELL_SIZE}" height="{CELL_SIZE}" '
                f'rx="2" fill="{COLORS[level]}" stroke="#21262d" stroke-width="0.5"/>'
            )

    # Ship following the path with animateMotion
    ship_offset_x = -48  # Center the ship on the path point
    ship_offset_y = -20

    parts.append("")
    parts.append("<!-- Ship sailing along reef-avoiding path -->")
    parts.append(f'<g transform="translate({ship_offset_x},{ship_offset_y}) scale(0.85)">')
    parts.append(f'  <animateMotion dur="{anim_duration}" repeatCount="indefinite"')
    parts.append(f'    rotate="auto" keyPoints="0;1" keyTimes="0;1" calcMode="linear">')
    parts.append(f'    <mpath href="#shipRoute"/>')
    parts.append(f'  </animateMotion>')
    # Bobbing
    parts.append(f'  <animateTransform attributeName="transform" type="translate"')
    parts.append(f'    values="0,0;0,-2;0,0;0,2;0,0"')
    parts.append(f'    dur="3s" repeatCount="indefinite" additive="sum"/>')
    parts.append(wake_trail_svg())
    parts.append(bow_wave_svg())
    parts.append(ship_svg())
    parts.append("</g>")

    # Watermark
    parts.append(
        f'<text x="{WIDTH - 20}" y="{HEIGHT - 15}" '
        f'fill="#484f58" font-size="10" font-family="system-ui,sans-serif" '
        f'text-anchor="end" font-style="italic">github.com/ORTODOX1</text>'
    )
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
            print(f"API failed: {e}, using fallback")
            grid = generate_fallback_grid()
    else:
        print("No GITHUB_TOKEN, using fallback grid")
        grid = generate_fallback_grid()

    svg = generate_svg(grid)
    os.makedirs("dist", exist_ok=True)
    for name in ["ship-animation.svg", "ship-animation-dark.svg"]:
        with open(f"dist/{name}", "w") as f:
            f.write(svg)
    print(f"Generated SVG: {len(svg)} bytes")


if __name__ == "__main__":
    main()
