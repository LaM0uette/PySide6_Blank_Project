"""
DcSizePolicy.%class(
    horizontal: PaSizePolicy.% \n
    vertical: PaSizePolicy.%)
"""

from dataclasses import dataclass

from src.lib.palettes import PaSizePolicy


@dataclass
class Base:

    horizontal: any = PaSizePolicy.PREFERED
    vertical: any = PaSizePolicy.PREFERED


class Expanding:

    horizontal: any = PaSizePolicy.EXPANDING
    vertical: any = PaSizePolicy.EXPANDING