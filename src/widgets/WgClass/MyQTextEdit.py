from .MyQAbstractScrollArea import MyQAbstractScrollArea


class MyQTextEdit(MyQAbstractScrollArea):
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

            auto_formatting,
            read_only,
    ):
        super().__init__(widget, size_policy, dim, font, cursor, focus_policy, layout_direction, frame, scroll_policy)

        widget.setAutoFormatting(auto_formatting)
        widget.setReadOnly(read_only)
