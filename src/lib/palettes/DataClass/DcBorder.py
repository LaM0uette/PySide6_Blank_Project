"""
DcBorder.%class(
    gen: tuple = %
    gen_style: tuple = %
    gen_rgb: tuple = %

    base: tuple = (%, %, %, %)
    base_style: str = "%"
    base_rgb: str = PaRgb.%
    hover: tuple = (%, %, %, %)
    hover_style: str = "%"
    hover_rgb: str = PaRgb.%
    checked: tuple = (%, %, %, %)
    checked_style: str = "%"
    checked_rgb: str = PaRgb.%
    checked_hover: tuple = (%, %, %, %)
    checked_hover_style: str = "%"
    checked_hover_rgb: str = PaRgb.%

    radius: tuple = (%, %, %, %))
"""

from dataclasses import dataclass

from src.lib.palettes import PaRgb


@dataclass
class Base:
    gen: tuple = None
    gen_style: tuple = None
    gen_rgb: tuple = None

    base: tuple = (0,)*4
    base_style: str = "solid"
    base_rgb: str = PaRgb.TR
    hover: tuple = base
    hover_style: str = base_style
    hover_rgb: str = base_rgb
    indeterminate: tuple = base
    indeterminate_style: str = base_style
    indeterminate_rgb: str = base_rgb
    indeterminate_hover: tuple = base
    indeterminate_hover_style: str = base_style
    indeterminate_hover_rgb: str = base_rgb
    checked: tuple = base
    checked_style: str = base_style
    checked_rgb: str = base_rgb
    checked_hover: tuple = base
    checked_hover_style: str = base_style
    checked_hover_rgb: str = base_rgb

    radius: tuple = (3,)*4

    def __post_init__(self):
        if self.gen:
            self.base = self.gen
            self.hover = self.gen
            self.indeterminate = self.gen
            self.indeterminate_hover = self.gen
            self.checked = self.gen
            self.checked_hover = self.gen

        if self.gen_style:
            self.base_style = self.gen_style
            self.hover_style = self.gen_style
            self.indeterminate_style = self.gen_style
            self.indeterminate_hover_style = self.gen_style
            self.checked_style = self.gen_style
            self.checked_hover_style = self.gen_style

        if self.gen_rgb:
            self.base_rgb = self.gen_rgb
            self.hover_rgb = self.gen_rgb
            self.indeterminate_rgb = self.gen_rgb
            self.indeterminate_hover_rgb = self.gen_rgb
            self.checked_rgb = self.gen_rgb
            self.checked_hover_rgb = self.gen_rgb
