#!/bin/env python3
"""kiwal.py - KiCAD colorscheme using pywal"""

from json import dumps, load # JSON library

WAL_PATH = "/home/air/.cache/wal/colors.json"
THEME_PATH = "/home/air/.local/share/kicad/7.0/3rdparty/colors/kiwal.json"

def hex2rgb(arg_hex):
    """Convert Hex colors to RGB"""
    return tuple(int(arg_hex.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))

def brighten_rgb(rgb):
    """Brighten an RGB color"""
    factor = 1.1
    bright_rgb = []
    rgb = rgb.split("(")[1].split(")")[0].split(",")
    for col in rgb:
        col = int(col)
        if col < 25:
            col = 25
        else:
            col = int(col * factor)
        bright_rgb.append(col)
    return f"rgb{tuple(bright_rgb)}"

def rgb2rgba(rgb, alpha):
    """Convert RGB color to RGBA"""
    rgba = []
    rgb = rgb.split("(")[1].split(")")[0].split(",")
    for col in rgb:
        col = int(col)
        rgba.append(col)
    rgba.append(float(alpha))
    return f"rgba{tuple(rgba)}"

# Load pywal colors from the default colors.json file
with open(WAL_PATH, "r") as wal_json:
    wal = load(wal_json)
    # Close the file

# Create the theme dict of dicts to hold the colorscheme
theme = {
    "meta": {},
    "palette": {},
    "schematic": {},
    "3d_viewer": {},
}

# Get colors from colors.json
background = f"rgb{hex2rgb(wal['special']['background'])}"
foreground = f"rgb{hex2rgb(wal['special']['foreground'])}"
cursor = f"rgb{hex2rgb(wal['special']['cursor'])}"
color1 = f"rgb{hex2rgb(wal['colors']['color1'])}"
color2 = f"rgb{hex2rgb(wal['colors']['color2'])}"
color3 = f"rgb{hex2rgb(wal['colors']['color3'])}"
color4 = f"rgb{hex2rgb(wal['colors']['color4'])}"
color5 = f"rgb{hex2rgb(wal['colors']['color5'])}"
color6 = f"rgb{hex2rgb(wal['colors']['color6'])}"
color7 = f"rgb{hex2rgb(wal['colors']['color7'])}"
color8 = f"rgb{hex2rgb(wal['colors']['color8'])}"
color9 = f"rgb{hex2rgb(wal['colors']['color9'])}"
color10 = f"rgb{hex2rgb(wal['colors']['color10'])}"
color11 = f"rgb{hex2rgb(wal['colors']['color11'])}"
color12 = f"rgb{hex2rgb(wal['colors']['color12'])}"
color13 = f"rgb{hex2rgb(wal['colors']['color13'])}"
color14 = f"rgb{hex2rgb(wal['colors']['color14'])}"
color15 = f"rgb{hex2rgb(wal['colors']['color15'])}"

# 3D Viewer Color Scheme
theme['3d_viewer']['background_bottom'] = color8
theme['3d_viewer']['background_top'] = color7
theme['3d_viewer']['board'] = "rgba(51, 43, 23, 0.902)"
theme['3d_viewer']['copper'] = "rgb(179, 156, 0)"
theme['3d_viewer']['silkscreen_bottom'] = "rgb(230, 230, 230)"
theme['3d_viewer']['silkscreen_top'] = "rgb(230, 230, 230)"
theme['3d_viewer']['soldermask_bottom'] = "rgba(20, 51, 36, 0.831)"
theme['3d_viewer']['soldermask_top'] = "rgba(20, 51, 36, 0.831)"
theme['3d_viewer']['solderpaste'] = "rgb(128, 128, 128)"
theme['3d_viewer']['use_board_stackup_colors'] = True

# Theme Metadata
theme['meta']['name'] = "Kiwal"
theme['meta']['version'] = 1

# Theme Palette
palette = []
for color in wal['colors']:
    palette.append(f"rgb{hex2rgb(wal['colors'][color])}")
theme['palette'] = palette

# Schematic Color Scheme
theme['schematic']['anchor'] = color6
theme['schematic']['aux_items'] = color9
theme['schematic']['background'] = background
theme['schematic']['brightened'] = brighten_rgb(background)
theme['schematic']['bus'] = brighten_rgb(foreground)
theme['schematic']['bus_junction'] = brighten_rgb(foreground)
theme['schematic']['component_body'] = brighten_rgb(background)
theme['schematic']['component_outline'] = brighten_rgb(foreground)
theme['schematic']['cursor'] = cursor
theme['schematic']['erc_error'] = brighten_rgb(foreground)
theme['schematic']['erc_exclusions'] = brighten_rgb(foreground)
theme['schematic']['erc_warning'] = brighten_rgb(foreground)
theme['schematic']['fields'] = foreground
theme['schematic']['grid'] = rgb2rgba(foreground, 0.25)
theme['schematic']['grid_axes'] = rgb2rgba(brighten_rgb(foreground), 0.5)
theme['schematic']['hidden'] = rgb2rgba(color12, 0.5)
theme['schematic']['highlighted'] = rgb2rgba(color1, 0.5)
theme['schematic']['hovered'] = rgb2rgba(color8, 0.25)
theme['schematic']['junction'] = foreground
theme['schematic']['label_global'] = color2
theme['schematic']['label_hier'] = color3
theme['schematic']['label_local'] = color4
theme['schematic']['no_connect'] = foreground
theme['schematic']['note'] = color1
theme['schematic']['override_item_colors'] = True
theme['schematic']['pin'] = foreground
theme['schematic']['pin_name'] = foreground
theme['schematic']['pin_number'] = foreground
theme['schematic']['reference'] = color10
theme['schematic']['shadow'] = color8
theme['schematic']['sheet'] = foreground
theme['schematic']['sheet_background'] = brighten_rgb(background)
theme['schematic']['sheet_fields'] = color13
theme['schematic']['sheet_filename'] = color14
theme['schematic']['sheet_label'] = color5
theme['schematic']['sheet_name'] = color12
theme['schematic']['value'] = color11
theme['schematic']['wire'] = foreground
theme['schematic']['worksheet'] = color7

# Write the colors to the kiwal.json file
theme_str = dumps(theme, indent=2)
with open(THEME_PATH, "w") as theme_json:
    theme_json.write(theme_str)
    # Close the file
