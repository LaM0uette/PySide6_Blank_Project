"""
DcImg.%class(
    base: str = PaImg.%
    uncheck: str = PaImg.%
    uncheck_hover: str = PaImg.%
    check: str = PaImg.%
    check_hover: str = PaImg.%
    indeterminate: str = PaImg.%
    indeterminate_hover: str = PaImg.%
    unroll: str = PaImg.%
    unroll_hover: str = PaImg.%
    up: str = PaImg.%
    up_hover: str = PaImg.%
    down: str = PaImg.%
    down_hover: str = PaImg.%
    right: str = PaImg.%
    right_hover: str = PaImg.%
    left: str = PaImg.%
    left_hover: str = PaImg.%

    base_rgb: str = "%"
    uncheck_rgb: str = "%"
    uncheck_hover_rgb: str = "%"
    check_rgb: str = "%"
    check_hover_rgb: str = "%"
    indeterminate_rgb: str = "%"
    indeterminate_hover_rgb: str = "%"
    unroll_rgb: str = "%"
    unroll_hover_rgb: str = "%"
    up_rgb: str = "%"
    up_hover_rgb: str = "%"
    down_rgb: str = "%"
    down_hover_rgb: str = "%"
    right_rgb: str = "%"
    right_hover_rgb: str = "%"
    left_rgb: str = "%"
    left_hover_rgb: str = "%")
"""

from dataclasses import dataclass

from src.lib.palettes import PaImg


@dataclass
class Base:
    width: int = 16
    height: int = 16
    margin: tuple = (0, )*4

    base: str = PaImg.MAIN
    base_hover: str = base
    uncheck: str = PaImg.CHECK0
    uncheck_hover: str = uncheck
    check: str = PaImg.CHECK2
    check_hover: str = check
    indeterminate: str = PaImg.CHECK1
    indeterminate_hover: str = indeterminate
    unroll: str = PaImg.FLECHE_BOTTOM
    unroll_hover: str = unroll
    up: str = PaImg.PLUS
    up_hover: str = up
    down: str = PaImg.MOINS
    down_hover: str = down
    right: str = PaImg.FLECHE_RIGHT
    right_hover: str = right
    left: str = PaImg.FLECHE_LEFT
    left_hover: str = left

    base_rgb: str = "th2"
    base_hover_rgb: str = "th3"
    uncheck_rgb: str = "th2"
    uncheck_hover_rgb: str = "bn1"
    check_rgb: str = "th2"
    check_hover_rgb: str = "bn1"
    indeterminate_rgb: str = "th3"
    indeterminate_hover_rgb: str = "th1"
    unroll_rgb: str = "th2"
    unroll_hover_rgb: str = "bn1"
    up_rgb: str = "th2"
    up_hover_rgb: str = "bn1"
    down_rgb: str = "th2"
    down_hover_rgb: str = "bn1"
    right_rgb: str = "th3"
    right_hover_rgb: str = "bn1"
    left_rgb: str = "th3"
    left_hover_rgb: str = "bn1"
