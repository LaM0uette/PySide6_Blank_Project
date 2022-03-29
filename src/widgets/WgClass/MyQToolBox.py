from .MyQFrame import MyQFrame


class MyQToolBox(MyQFrame):
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

            tab_spacing,
    ):
        super().__init__(widget, size_policy, dim, font, cursor, focus_policy, layout_direction, frame)

        widget.layout().setSpacing(tab_spacing)
