from .MyQColumnView import MyQColumnView
from src.lib.globals import v_wg
from src.lib.palettes import *


class Style(MyQColumnView):
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

            abstract_item_view=DcAbstractItemView.Base,
            drag_drop=DcDragDrop.Base,
            selection_mode=PaSelectionMode.SINGLE,
            selection_behavior=PaSelectionBehavior.ROW,

            resize_grips_visible=True,
    ):
        super().__init__(widget, size_policy, dim, font, cursor, focus_policy, layout_direction, frame, scroll_policy, abstract_item_view,drag_drop,selection_mode,selection_behavior, resize_grips_visible)
