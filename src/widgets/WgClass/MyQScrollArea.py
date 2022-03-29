from .MyQAbstractScrollArea import MyQAbstractScrollArea


class MyQScrollArea(MyQAbstractScrollArea):
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

            resizable
    ):
        super().__init__(widget, size_policy, dim, font, cursor, focus_policy, layout_direction, frame, scroll_policy)

        widget.setWidgetResizable(resizable)
