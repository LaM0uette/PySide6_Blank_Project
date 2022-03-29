from .MyQAbstractScrollArea import MyQAbstractScrollArea


class MyQPlainTextEdit(MyQAbstractScrollArea):
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

            read_only,
    ):
        super().__init__(widget, size_policy, dim, font, cursor, focus_policy, layout_direction, frame, scroll_policy)

        widget.setReadOnly(read_only)
