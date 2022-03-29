from PySide6 import QtGui

from .MyQFrame import MyQFrame


class MyQLabel(MyQFrame):
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

            text_format,
            pixmap,
            pixmap_rgb,
            scaled_contents,
            align,
            word_wrap,
            indent,
            open_external_link,
    ):
        super().__init__(widget, size_policy, dim, font, cursor, focus_policy, layout_direction, frame)

        widget.setTextFormat(text_format)
        if pixmap is not None:
            widget.setPixmap(QtGui.QPixmap(f"{pixmap}{pixmap_rgb}.svg"))
            widget.setScaledContents(scaled_contents)
        widget.setAlignment(align.horizontal | align.vertical)
        widget.setWordWrap(word_wrap)
        widget.setFocusPolicy(focus_policy)
        widget.setIndent(indent)
        widget.setOpenExternalLinks(open_external_link)
