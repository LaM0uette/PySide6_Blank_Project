from .MyQAbstractScrollArea import MyQAbstractScrollArea


class MyQAbstractItemView(MyQAbstractScrollArea):
    def __init__(
            self,
            widget,
            size_policy,
            dim,
            font,
            cursor,
            focus_policy,
            layout_direction,

            frame,

            scroll_policy,

            abstract_item_view,
            drag_drop,
            selection_mode,
            selection_behavior,
    ):
        super().__init__(widget, size_policy, dim, font, cursor, focus_policy, layout_direction, frame, scroll_policy)

        widget.setAutoScroll(abstract_item_view.auto_scroll)
        widget.setAutoScrollMargin(abstract_item_view.auto_scroll_margin)
        widget.setTabKeyNavigation(abstract_item_view.tab_navigation)
        widget.setDragEnabled(drag_drop.drag_enabled)
        widget.setDragDropMode(drag_drop.drag_drop_mode)
        widget.setDefaultDropAction(drag_drop.drop_action)
        widget.setAlternatingRowColors(abstract_item_view.alternative_row_colors)
        widget.setSelectionMode(selection_mode)
        widget.setSelectionBehavior(selection_behavior)
