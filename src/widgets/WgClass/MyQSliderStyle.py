from .MyQSlider import MyQSlider
from src.lib.globals import v_wg
from src.lib.palettes import *


class Style(MyQSlider):
    def __init__(
            self,
            widget,
            size_policy=v_wg.SIZE_POLICY,
            dim=v_wg.DIM_WG,
            font=v_wg.FONT,
            cursor=v_wg.CUR_ACTION,
            focus_policy=v_wg.FOCUS_POLICY,
            layout_direction=v_wg.LAYOUT_DIRECTION,

            value=v_wg.VALUE,

            tick_position=PaTickPosition.NO,
            tick_interval=0,
    ):
        super().__init__(widget,size_policy,dim,font,cursor,focus_policy,layout_direction,value,tick_position,tick_interval)
