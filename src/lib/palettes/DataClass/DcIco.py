"""
DcIco.%class(
    ico: str = PaImg.% \n
    ico_rgb: str = "%" \n
    ico_width: int = PaDim.% \n
    ico_height: int = PaDim.%)
"""

from dataclasses import dataclass


@dataclass
class Base:

    ico: str = None
    ico_rgb: str = ""
    ico_width: int = None
    ico_height: int = None
