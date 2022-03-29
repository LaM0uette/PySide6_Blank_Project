from .MyQLCDNumber import MyQLCDNumber
from src.lib.globals import v_wg
from ...lib.palettes import *


class Style(MyQLCDNumber):
    def __init__(
            self,
            widget,
            size_policy=v_wg.SIZE_POLICY,
            dim=v_wg.DIM,
            font=v_wg.FONT,
            cursor=v_wg.CUR_ACTION,
            focus_policy=v_wg.FOCUS_POLICY,
            layout_direction=v_wg.LAYOUT_DIRECTION,

            frame=v_wg.FRAME,

            small_decimal_point=False,
            digit_count=5,
            digit_mode=PaDigitMode.DEC,
            segment_style=PaSegmentStyle.FLAT,
    ):
        super().__init__(widget, size_policy, dim, font, cursor, focus_policy, layout_direction, frame,small_decimal_point,digit_count,digit_mode,segment_style)
