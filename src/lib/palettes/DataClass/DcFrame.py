"""
DcFrame.%class(
    frame_shape: any = PaFrameShape.%
    frame_shadow: any = PaFrameShadow.%
    line_width: int = %)
"""

from dataclasses import dataclass

from src.lib.palettes import *


@dataclass
class Base:

    frame_shape: any = PaFrameShape.NO
    frame_shadow: any = PaFrameShadow.PLAIN
    line_width: int = 0
    mid_line_width: int = 0
