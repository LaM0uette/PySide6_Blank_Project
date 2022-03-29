"""
DcRgbSlider.%class(
    groove_gen: tuple = %
    handle_gen: tuple = %

    groove: tuple = PaRgb.%
    groove_hover: tuple = PaRgb.%
    groove_pressed: tuple = PaRgb.%
    handle: tuple = PaRgb.%
    handle_hover: tuple = PaRgb.%
    handle_pressed: tuple = PaRgb.%
"""
from dataclasses import dataclass

from src.lib.palettes import *


@dataclass
class Base:
    groove_gen: tuple = None
    handle_gen: tuple = None

    groove: tuple = PaRgb.TH3
    groove_hover: tuple = PaRgb.TH3
    groove_pressed: tuple = PaRgb.TH3
    handle: tuple = PaRgb.TH2
    handle_hover: tuple = PaRgb.TH2
    handle_pressed: tuple = PaRgb.BN1


    def __post_init__(self):
        if self.groove_gen:
            self.groove = self.groove_gen
            self.groove_hover = self.groove_gen
            self.groove_pressed = self.groove_gen

        if self.handle_gen:
            self.handle = self.handle_gen
            self.handle_hover = self.handle_gen
            self.handle_pressed = self.handle_gen
