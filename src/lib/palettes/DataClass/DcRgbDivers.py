"""
DcRgbDivers.%class(
    tray_separator: tuple = PaRgb.%
    gridline: tuple = PaRgb.%
"""
from dataclasses import dataclass

from src.lib.palettes import *


@dataclass
class Base:

    tray_separator: tuple = PaRgb.BN1
    gridline: tuple = PaRgb.TH2
