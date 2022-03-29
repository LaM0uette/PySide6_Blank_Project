from .MyQTableView import MyQTableView


class MyQTableWidget(MyQTableView):
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

            row_count,
            column_count,
    ):
        super().__init__(widget, size_policy, dim, font, cursor, focus_policy, layout_direction, frame, scroll_policy, abstract_item_view, drag_drop, selection_mode, selection_behavior, show_grid,grid_style,sorting,corner_button_enabled)

        widget.setRowCount(row_count)
        widget.setColumnCount(column_count)
