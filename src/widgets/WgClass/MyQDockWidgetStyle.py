from .MyQDockWidget import MyQDockWidget
from src.lib.globals import v_wg
from src.lib.palettes import *


class Style(MyQDockWidget):
    def __init__(
            self,
            widget,
            size_policy=v_wg.SIZE_POLICY,
            dim=v_wg.DIM,
            font=v_wg.FONT,
            cursor=v_wg.CUR_ACTION,
            focus_policy=v_wg.FOCUS_POLICY,
            layout_direction=v_wg.LAYOUT_DIRECTION,

            floating=False,
    ):
        super().__init__(widget,size_policy,dim,font,cursor,focus_policy,layout_direction,floating)
