from .MyQTextEdit import MyQTextEdit


class MyQTextBrowser(MyQTextEdit):
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

            open_external_link,
            open_link,
    ):
        super().__init__(widget, size_policy, dim, font, cursor, focus_policy, layout_direction, frame, scroll_policy,auto_formatting,read_only)

        widget.setOpenExternalLinks(open_external_link)
        widget.setOpenLinks(open_link)
