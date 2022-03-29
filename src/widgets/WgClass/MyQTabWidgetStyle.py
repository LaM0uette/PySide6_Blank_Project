from .MyQTabWidget import MyQTabWidget
from src.lib.globals import v_wg
from src.lib.palettes import *


class Style(MyQTabWidget):
    def __init__(
            self,
            widget,
            size_policy=v_wg.SIZE_POLICY,
            dim=v_wg.DIM,
            font=v_wg.FONT,
            cursor=v_wg.CUR_ACTION,
            focus_policy=v_wg.FOCUS_POLICY,
            layout_direction=v_wg.LAYOUT_DIRECTION,

            tab_position=PaTabPosition.NORTH,
            uses_scroll_buttons=False,
            document_mode=False,
            tabs_closable=False,
            tabs_movable=False,
    ):
        super().__init__(widget,size_policy,dim,font,cursor,focus_policy,layout_direction,tab_position,uses_scroll_buttons,document_mode,tabs_closable,tabs_movable)
