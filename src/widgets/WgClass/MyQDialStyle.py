from .MyQDial import MyQDial
from src.lib.globals import v_wg
from src.lib.palettes import *


class Style(MyQDial):
    def __init__(
            self,
            widget,
            size_policy=v_wg.SIZE_POLICY,
            dim=v_wg.DIM_WG,
            font=v_wg.FONT,
            cursor=v_wg.CUR_ACTION,
            focus_policy=v_wg.FOCUS_POLICY,
            layout_direction=v_wg.LAYOUT_DIRECTION,

            value=DcValue.Base,

            wrapping=False,
            notch_target=3.7,
            notches_visible=False,
    ):
        super().__init__(widget,size_policy,dim,font,cursor,focus_policy,layout_direction,value,wrapping,notch_target,notches_visible)
