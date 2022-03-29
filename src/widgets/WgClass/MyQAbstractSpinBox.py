from .MyQWidget import MyQWidget


class MyQAbstractSpinBox(MyQWidget):
    def __init__(
            self,
            widget,
            size_policy,
            dim,
            font,
            cursor,
            focus_policy,
            layout_direction,

            wrapping,
            frame,
            align,
            read_only,
            button_symbols,
            accelerated,
    ):
        super().__init__(widget,size_policy,dim,font,cursor,focus_policy,layout_direction)

        widget.setWrapping(wrapping)
        widget.setFrame(frame)
        widget.setAlignment(align.horizontal | align.vertical)
        widget.setReadOnly(read_only)
        widget.setButtonSymbols(button_symbols)
        widget.setAccelerated(accelerated)
