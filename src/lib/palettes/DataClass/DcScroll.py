"""
DcScroll.%class(
    width: int = %
    height: int = %
    min_width_handle: int = %
    min_height_min_handle: int = %

    bg: tuple = PaRgb.%
    handle_bg: tuple = PaRgb.%
    handle_bg_hover: tuple = PaRgb.%
    handle_fg: tuple = PaRgb.%
    handle_fg_hover: tuple = PaRgb.%)
"""

from dataclasses import dataclass

from src.lib.palettes import *


@dataclass
class Base:

    width: int = 10
    height: int = 10
    min_width_handle: int = 20
    min_height_min_handle: int = 20

    bg: tuple = PaRgb.TH1
    handle_bg: tuple = PaRgb.TH3
    handle_bg_hover: tuple = PaRgb.TH3
    handle_fg: tuple = PaRgb.TH2
    handle_fg_hover: tuple = PaRgb.BN1
