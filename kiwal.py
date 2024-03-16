#!/bin/env python3
"""kiwal.py - KiCAD colorscheme using pywal"""

from json import dumps, load # JSON library

WAL_PATH = "/home/air/.cache/wal/colors.json"
# THEME_PATH = "/home/air/.local/share/kicad/7.0/3rdparty/colors/kiwal.json"
THEME_PATH = "/home/air/.local/share/kicad/8.0/3rdparty/colors/kiwal.json"

def hex2rgb(arg_hex):
    """Convert Hex colors to RGB"""
    return tuple(int(arg_hex.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))

def brighten_rgb(arg_rgb, arg_factor):
    """Brighten an RGB color"""
    bright_rgb = []
    rgb = arg_rgb.split("(")[1].split(")")[0].split(",")
    for col in rgb:
        col = int(col)
        if col < 25:
            col = 25
        else:
            col = int(col * arg_factor)
        bright_rgb.append(col)
    return f"rgb{tuple(bright_rgb)}"

def rgb2rgba(arg_rgb, arg_alpha):
    """Convert RGB color to RGBA"""
    rgba = []
    rgb = arg_rgb.split("(")[1].split(")")[0].split(",")
    for col in rgb:
        col = int(col)
        rgba.append(col)
    rgba.append(float(arg_alpha))
    return f"rgba{tuple(rgba)}"

# Load pywal colors from the default colors.json file
with open(WAL_PATH, "r", encoding = "utf-8") as wal_json:
    wal = load(wal_json)
    # Close the file

# Get colors from colors.json
background = f"rgb{hex2rgb(wal['special']['background'])}"
foreground = f"rgb{hex2rgb(wal['special']['foreground'])}"
cursor = f"rgb{hex2rgb(wal['special']['cursor'])}"
color0 = f"rgb{hex2rgb(wal['colors']['color0'])}"
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
viewer = {
        'background_bottom': color8,
        'background_top': color7,
        'board': "rgba(51, 43, 23, 0.902)",
        'copper': "rgb(179, 156, 0)",
        'silkscreen_bottom': "rgb(230, 230, 230)",
        'silkscreen_top': "rgb(230, 230, 230)",
        'soldermask_bottom': "rgba(20, 51, 36, 0.831)",
        'soldermask_top': "rgba(20, 51, 36, 0.831)",
        'solderpaste': "rgb(128, 128, 128)",
        'use_board_stackup_colors': True
}

# PCBnew Color Scheme
board = {
        'anchor': color8,
        'aux_items': foreground,
        'b_adhes': brighten_rgb(color3, 1.1),
        'b_crtyd': color4,
        'b_fab': brighten_rgb(color8, 1.1),
        'b_mask': brighten_rgb(color3, 0.9),
        'b_paste': brighten_rgb(color3, 1.3),
        'b_silks': brighten_rgb(color6, 1.1),
        'background': background,
        'cmts_user': color7,
        'copper': {
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
            },
        'cursor': foreground,
        'drc': "rgb(45, 201, 55)",
        'drc_error': "rgb(231, 180, 22)",
        'drc_warning': "rgb(204, 50, 50)",
        'dwgs_user': color7,
        'eco1_user': brighten_rgb(color7, 0.8),
        'eco2_user': brighten_rgb(color7, 0.6),
        'edge_cuts': brighten_rgb(color7, 1.2),
        'f_adhes': brighten_rgb(color3, 1.1),
        'f_crtyd': color4,
        'f_fab': brighten_rgb(color8, 0.9),
        'f_mask': brighten_rgb(color2, 0.9),
        'f_paste': brighten_rgb(color2, 1.3),
        'f_silks': brighten_rgb(color2, 1.1),
        'footprint_text_back': brighten_rgb(color2, 1.1),
        'footprint_text_front': brighten_rgb(color6, 1.1),
        'footprint_text_invisible': brighten_rgb(background, 1.5),
        'grid': rgb2rgba(foreground, 0.5),
        'grid_axes': rgb2rgba(foreground, 0.65),
        'margin': rgb2rgba(foreground, 0.5),
        'microvia': color5,
        'no_connect': color1,
        'pad_front': color6,
        'pad_plated_hole': color6,
        'pad_through_hole': color6,
        'plated_hole': color6,
        'ratsnest': rgb2rgba(foreground, 0.65),
        'select_overlay': brighten_rgb(color1, 1.3),
        'through_via': color5,
        'user_1': brighten_rgb(color1, 0.65),
        'user_2': brighten_rgb(color2, 0.65),
        'user_3': brighten_rgb(color3, 0.65),
        'user_4': brighten_rgb(color4, 0.65),
        'user_5': brighten_rgb(color5, 0.65),
        'user_6': brighten_rgb(color6, 0.65),
        'user_7': brighten_rgb(color9, 0.65),
        'user_8': brighten_rgb(color10, 0.65),
        'user_9': brighten_rgb(color11, 0.65),
        'via_blind_buried': color5,
        'via_hole': background,
        'via_micro': color5,
        'via_through': color5,
        'worksheet': foreground
}

# Gerbview Colorscheme
gerbview = {
        'axes': rgb2rgba(foreground, 0.65),
        'background': background,
        'dcodes': foreground,
        'grid': rgb2rgba(foreground, 0.5),
        'layers': [
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
        ],
        'negative_objects': brighten_rgb(foreground, 0.9),
        'worksheet': foreground
}

# Theme Metadata
meta = {
        'name': "Kiwal",
        'version': 1
        }

# Theme Palette
palette = []
for color in wal['colors']:
    palette.append(f"rgb{hex2rgb(wal['colors'][color])}")

# EEschema Color Scheme
schematic = {
        'anchor': color6,
        'aux_items': color9,
        'background': background,
        'brightened': brighten_rgb(background, 1.1),
        'bus': brighten_rgb(foreground, 1.1),
        'bus_junction': brighten_rgb(foreground, 1.1),
        'component_body': brighten_rgb(background, 1.1),
        'component_outline': brighten_rgb(foreground, 1.1),
        'cursor': cursor,
        'erc_error': brighten_rgb(foreground, 1.1),
        'erc_exclusions': brighten_rgb(foreground, 1.1),
        'erc_warning': brighten_rgb(foreground, 1.1),
        'fields': foreground,
        'grid': rgb2rgba(foreground, 0.5),
        'grid_axes': rgb2rgba(brighten_rgb(foreground, 1.1), 0.65),
        'hidden': rgb2rgba(color12, 0.5),
        'highlighted': rgb2rgba(color1, 0.5),
        'hovered': rgb2rgba(color8, 0.25),
        'junction': foreground,
        'label_global': color2,
        'label_hier': color3,
        'label_local': color4,
        'no_connect': foreground,
        'note': color1,
        'override_item_colors': True,
        'pin': foreground,
        'pin_name': foreground,
        'pin_number': foreground,
        'reference': color10,
        'shadow': color8,
        'sheet': foreground,
        'sheet_background': brighten_rgb(background, 1.1),
        'sheet_fields': color13,
        'sheet_filename': color14,
        'sheet_label': color5,
        'sheet_name': color12,
        'value': color11,
        'wire': foreground,
        'worksheet': color7
        }

# Create the theme dict of dicts to hold the colorscheme
theme = {
        "meta": meta,
        "palette": palette,
        "schematic": schematic,
        "board": board,
        "3d_viewer": viewer,
        "gerbview": gerbview
        }

# Write the colors to the kiwal.json file
theme_str = dumps(theme, indent=2)
with open(THEME_PATH, "w", encoding = "utf-8") as theme_json:
    theme_json.write(theme_str)
    # Close the file
