"""
DcDragDrop.%class(
    drag_enabled: bool = %
    drag_drop_mode: any = PaDragDropMode.%
    drop_action: any = PaDropAction.%)
"""

from dataclasses import dataclass

from src.lib.palettes import *


@dataclass
class Base:

    drag_enabled: bool = False
    drag_drop_mode: any = PaDragDropMode.NO
    drop_action: any = PaDropAction.MOVE
