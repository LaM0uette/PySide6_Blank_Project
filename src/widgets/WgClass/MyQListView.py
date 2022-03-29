from .MyQAbstractItemView import MyQAbstractItemView


class MyQListView(MyQAbstractItemView):
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

            movement,
            flow,
            items_spacing,
    ):
        super().__init__(widget, size_policy, dim, font, cursor, focus_policy, layout_direction, frame, scroll_policy, abstract_item_view, drag_drop, selection_mode, selection_behavior)

        widget.setMovement(movement)
        widget.setFlow(flow)
        widget.setSpacing(items_spacing)
