from .MyQTreeWidget import MyQTreeWidget
from src.lib.globals import v_wg
from src.lib.palettes import *


class Style(MyQTreeWidget):
    def __init__(
            self,
            widget,
            size_policy=DcSizePolicy.Expanding,
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

            uniform_row_height=False,
            items_expandable=True,
            sorting=False,
            animate=False,
            header_hidden=False,

            column_count=1
    ):
        super().__init__(widget, size_policy, dim, font, cursor, focus_policy, layout_direction, frame, scroll_policy, abstract_item_view, drag_drop, selection_mode, selection_behavior, uniform_row_height,items_expandable,sorting,animate,header_hidden, column_count)
