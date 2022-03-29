from .MyQCalendarWidget import MyQCalendarWidget
from src.lib.globals import v_wg
from ...lib.palettes import *


class Style(MyQCalendarWidget):
    def __init__(
            self,
            widget,
            size_policy=v_wg.SIZE_POLICY,
            dim=v_wg.DIM,
            font=v_wg.FONT,
            cursor=v_wg.CUR_ACTION,
            focus_policy=v_wg.FOCUS_POLICY,
            layout_direction=v_wg.LAYOUT_DIRECTION,

            date=DcDateTime.Base,
    ):
        super().__init__(widget,size_policy,dim,font,cursor,focus_policy,layout_direction,date)
