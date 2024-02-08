#!/bin/env python3
"""kiwal.py - KiCAD colorscheme using pywal"""

from json import dumps, load # JSON library

WAL_PATH = "/home/air/.cache/wal/colors.json"
THEME_PATH = "/home/air/.local/share/kicad/7.0/3rdparty/colors/kiwal.json"

def hex2rgb(arg_hex):
    """Convert Hex colors to RGB"""
    return tuple(int(arg_hex.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))

def brighten_rgb(rgb, factor):
    """Brighten an RGB color"""
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
with open(WAL_PATH, "r", encoding = "utf-8") as wal_json:
    wal = load(wal_json)
    # Close the file

# REFACTOR: Can the dicts be assembled individually and then combined afterwards?
# Create the theme dict of dicts to hold the colorscheme
theme = {
    "meta": {},
    "palette": {},
    "schematic": {},
    "board": {},
    "gerbview": {},
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

# PCBnew Color Scheme
theme['board']['anchor'] = color8
theme['board']['aux_items'] = foreground
theme['board']['b_adhes'] = brighten_rgb(color3, 1.1)
theme['board']['b_crtyd'] = color4
theme['board']['b_fab'] = brighten_rgb(color8, 1.1)
theme['board']['b_mask'] = brighten_rgb(color3, 0.9)
theme['board']['b_paste'] = brighten_rgb(color3, 1.3)
theme['board']['b_silks'] = brighten_rgb(color6, 1.1)
theme['board']['background'] = background
theme['board']['cmts_user'] = color7
theme['board']['copper'] = {
      "b": color3,
      "f": color2,
      "in1": color5,
      "in2": color6,
      "in3": color1,
      "in4": color4,
      "in5": brighten_rgb(color3, 0.8),
      "in6": brighten_rgb(color2, 0.8),
      "in7": brighten_rgb(color5, 0.8),
      "in8": brighten_rgb(color6, 0.8),
      "in9": brighten_rgb(color1, 0.8),
      "in10": brighten_rgb(color4, 0.8),
      "in11": brighten_rgb(color3, 1.2),
      "in12": brighten_rgb(color2, 1.2),
      "in13": brighten_rgb(color5, 1.2),
      "in14": brighten_rgb(color6, 1.2),
      "in15": brighten_rgb(color1, 1.2),
      "in16": brighten_rgb(color4, 1.2),
      "in17": brighten_rgb(color3, 0.6),
      "in18": brighten_rgb(color2, 0.6),
      "in19": brighten_rgb(color5, 0.6),
      "in20": brighten_rgb(color6, 0.6),
      "in21": brighten_rgb(color1, 0.6),
      "in22": brighten_rgb(color4, 0.6),
      "in23": brighten_rgb(color3, 1.4),
      "in24": brighten_rgb(color2, 1.4),
      "in25": brighten_rgb(color5, 1.4),
      "in26": brighten_rgb(color6, 1.4),
      "in27": brighten_rgb(color1, 1.4),
      "in28": brighten_rgb(color4, 1.4),
      "in29": brighten_rgb(color7, 1.2),
      "in30": brighten_rgb(color7, 0.8)
    }
theme['board']['cursor'] = foreground
theme['board']['drc'] = "rgb(45, 201, 55)"
theme['board']['drc_error'] = "rgb(231, 180, 22)"
theme['board']['drc_warning'] = "rgb(204, 50, 50)"
theme['board']['dwgs_user'] = color7
theme['board']['eco1_user'] = brighten_rgb(color7, 0.8)
theme['board']['eco2_user'] = brighten_rgb(color7, 0.6)
theme['board']['edge_cuts'] = brighten_rgb(color7, 1.2)
theme['board']['f_adhes'] = brighten_rgb(color3, 1.1)
theme['board']['f_crtyd'] = color4
theme['board']['f_fab'] = brighten_rgb(color8, 0.9)
theme['board']['f_mask'] = brighten_rgb(color2, 0.9)
theme['board']['f_paste'] = brighten_rgb(color2, 1.3)
theme['board']['f_silks'] = brighten_rgb(color2, 1.1)
theme['board']['footprint_text_back'] = theme['board']['b_silks']
theme['board']['footprint_text_front'] = theme['board']['f_silks']
theme['board']['footprint_text_invisible'] = brighten_rgb(background, 1.5)
theme['board']['grid'] = rgb2rgba(foreground, 0.5)
theme['board']['grid_axes'] = rgb2rgba(foreground, 0.65)
theme['board']['margin'] = rgb2rgba(foreground, 0.5)
theme['board']['microvia'] = color5
theme['board']['no_connect'] = color1
theme['board']['pad_front'] = color6
theme['board']['pad_plated_hole'] = color6
theme['board']['pad_through_hole'] = color6
theme['board']['plated_hole'] = color6
theme['board']['ratsnest'] = rgb2rgba(foreground, 0.65)
theme['board']['select_overlay'] = brighten_rgb(color1, 1.3)
theme['board']['through_via'] = color5
theme['board']['user_1'] = brighten_rgb(color1, 0.65)
theme['board']['user_2'] = brighten_rgb(color2, 0.65)
theme['board']['user_3'] = brighten_rgb(color3, 0.65)
theme['board']['user_4'] = brighten_rgb(color4, 0.65)
theme['board']['user_5'] = brighten_rgb(color5, 0.65)
theme['board']['user_6'] = brighten_rgb(color6, 0.65)
theme['board']['user_7'] = brighten_rgb(color9, 0.65)
theme['board']['user_8'] = brighten_rgb(color10, 0.65)
theme['board']['user_9'] = brighten_rgb(color11, 0.65)
theme['board']['via_blind_buried'] = color5
theme['board']['via_hole'] = background
theme['board']['via_micro'] = color5
theme['board']['via_through'] = color5
theme['board']['worksheet'] = foreground

# Gerbview Colorscheme
theme['gerbview']['axes'] = rgb2rgba(foreground, 0.65)
theme['gerbview']['background'] = background
theme['gerbview']['dcodes'] = foreground
theme['gerbview']['grid'] = rgb2rgba(foreground, 0.5)
theme['gerbview']['layers'] = [
      "rgb(132, 0, 0)",
      "rgb(194, 194, 0)",
      "rgb(194, 0, 194)",
      "rgb(194, 0, 0)",
      "rgb(0, 132, 132)",
      "rgb(0, 132, 0)",
      "rgb(0, 0, 132)",
      "rgb(132, 132, 132)",
      "rgb(132, 0, 132)",
      "rgb(194, 194, 194)",
      "rgb(132, 0, 132)",
      "rgb(132, 0, 0)",
      "rgb(132, 132, 0)",
      "rgb(194, 194, 194)",
      "rgb(0, 0, 132)",
      "rgb(0, 132, 0)",
      "rgb(132, 0, 0)",
      "rgb(194, 194, 0)",
      "rgb(194, 0, 194)",
      "rgb(194, 0, 0)",
      "rgb(0, 132, 132)",
      "rgb(0, 132, 0)",
      "rgb(0, 0, 132)",
      "rgb(132, 132, 132)",
      "rgb(132, 0, 132)",
      "rgb(194, 194, 194)",
      "rgb(132, 0, 132)",
      "rgb(132, 0, 0)",
      "rgb(132, 132, 0)",
      "rgb(194, 194, 194)",
      "rgb(0, 0, 132)",
      "rgb(0, 132, 0)",
      "rgb(132, 0, 0)",
      "rgb(194, 194, 0)",
      "rgb(194, 0, 194)",
      "rgb(194, 0, 0)",
      "rgb(0, 132, 132)",
      "rgb(0, 132, 0)",
      "rgb(0, 0, 132)",
      "rgb(132, 132, 132)",
      "rgb(132, 0, 132)",
      "rgb(194, 194, 194)",
      "rgb(132, 0, 132)",
      "rgb(132, 0, 0)",
      "rgb(132, 132, 0)",
      "rgb(194, 194, 194)",
      "rgb(0, 0, 132)",
      "rgb(0, 132, 0)",
      "rgb(132, 0, 0)",
      "rgb(194, 194, 0)",
      "rgb(194, 0, 194)",
      "rgb(194, 0, 0)",
      "rgb(0, 132, 132)",
      "rgb(0, 132, 0)",
      "rgb(0, 0, 132)",
      "rgb(132, 132, 132)",
      "rgb(132, 0, 132)",
      "rgb(194, 194, 194)",
      "rgb(132, 0, 132)",
      "rgb(132, 0, 0)"
    ]
theme['gerbview']['negative_objects'] = brighten_rgb(foreground, 0.9)
theme['gerbview']['worksheet'] = foreground

# Theme Metadata
theme['meta']['name'] = "Kiwal"
theme['meta']['version'] = 1

# Theme Palette
palette = []
for color in wal['colors']:
    palette.append(f"rgb{hex2rgb(wal['colors'][color])}")
theme['palette'] = palette

# EEschema Color Scheme
theme['schematic']['anchor'] = color6
theme['schematic']['aux_items'] = color9
theme['schematic']['background'] = background
theme['schematic']['brightened'] = brighten_rgb(background, 1.1)
theme['schematic']['bus'] = brighten_rgb(foreground, 1.1)
theme['schematic']['bus_junction'] = brighten_rgb(foreground, 1.1)
theme['schematic']['component_body'] = brighten_rgb(background, 1.1)
theme['schematic']['component_outline'] = brighten_rgb(foreground, 1.1)
theme['schematic']['cursor'] = cursor
theme['schematic']['erc_error'] = brighten_rgb(foreground, 1.1)
theme['schematic']['erc_exclusions'] = brighten_rgb(foreground, 1.1)
theme['schematic']['erc_warning'] = brighten_rgb(foreground, 1.1)
theme['schematic']['fields'] = foreground
theme['schematic']['grid'] = rgb2rgba(foreground, 0.5)
theme['schematic']['grid_axes'] = rgb2rgba(brighten_rgb(foreground, 1.1), 0.65)
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
theme['schematic']['sheet_background'] = brighten_rgb(background, 1.1)
theme['schematic']['sheet_fields'] = color13
theme['schematic']['sheet_filename'] = color14
theme['schematic']['sheet_label'] = color5
theme['schematic']['sheet_name'] = color12
theme['schematic']['value'] = color11
theme['schematic']['wire'] = foreground
theme['schematic']['worksheet'] = color7

# Write the colors to the kiwal.json file
theme_str = dumps(theme, indent=2)
with open(THEME_PATH, "w", encoding = "utf-8") as theme_json:
    theme_json.write(theme_str)
    # Close the file
