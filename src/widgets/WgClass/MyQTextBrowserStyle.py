from .MyQTextBrowser import MyQTextBrowser
from src.lib.globals import v_wg
from ...lib.palettes import *


class Style(MyQTextBrowser):
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

            scroll_policy=v_wg.SCROLL_POLICY,

            auto_formatting=PaAutoFormating.NONE,
            read_only=False,

            open_external_link=False,
            open_link=False,
    ):
        super().__init__(widget, size_policy, dim, font, cursor, focus_policy, layout_direction, frame, scroll_policy,auto_formatting,read_only,open_external_link,open_link)
