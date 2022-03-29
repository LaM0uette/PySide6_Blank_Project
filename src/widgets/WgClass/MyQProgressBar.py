from .MyQWidget import MyQWidget


class MyQProgressBar(MyQWidget):
    def __init__(
            self,
            widget,
            size_policy,
            dim,
            font,
            cursor,
            focus_policy,
            layout_direction,

            value,
            align,
            text_visible,
            progress_format,
    ):
        super().__init__(widget,size_policy,dim,font,cursor,focus_policy,layout_direction)

        widget.setMinimum(value.min)
        widget.setMaximum(value.max)
        widget.setAlignment(align.horizontal | align.vertical)
        widget.setTextVisible(text_visible)
        widget.setFormat(progress_format)
