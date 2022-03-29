from .MyQAbstractItemView import MyQAbstractItemView


class MyQTableView(MyQAbstractItemView):
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

            show_grid,
            grid_style,
            sorting,
            corner_button_enabled,
    ):
        super().__init__(widget, size_policy, dim, font, cursor, focus_policy, layout_direction, frame, scroll_policy, abstract_item_view, drag_drop, selection_mode, selection_behavior)

        widget.setShowGrid(show_grid)
        widget.setGridStyle(grid_style)
        widget.setSortingEnabled(sorting)
        widget.setCornerButtonEnabled(corner_button_enabled)
