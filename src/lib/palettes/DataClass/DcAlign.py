"""
DcAlign.%class(
    horizontal: any = PaAlign.%
    vertical: any = PaAlign.%)
"""

from dataclasses import dataclass

from src.lib.palettes import PaAlign


@dataclass
class Base:

    horizontal: any = PaAlign.CENTER_HORIZONTAL
    vertical: any = PaAlign.CENTER_VERTICAL
