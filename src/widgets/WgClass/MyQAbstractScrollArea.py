from .MyQFrame import MyQFrame


class MyQAbstractScrollArea(MyQFrame):
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
    ):
        super().__init__(widget, size_policy, dim, font, cursor, focus_policy, layout_direction, frame)

        widget.setHorizontalScrollBarPolicy(scroll_policy.horizontal)
        widget.setVerticalScrollBarPolicy(scroll_policy.vertical)
        widget.setSizeAdjustPolicy(scroll_policy.size_adjust)
