from .MyQFrame import MyQFrame


class MyQStackedWidget(MyQFrame):
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
    ):
        super().__init__(widget, size_policy, dim, font, cursor, focus_policy, layout_direction, frame)
