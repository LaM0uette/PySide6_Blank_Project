from .MyQWidget import MyQWidget


class MyQLineEdit(MyQWidget):
    def __init__(
            self,
            widget,
            size_policy,
            dim,
            font,
            cursor,
            focus_policy,
            layout_direction,

            input_mask,
            max_length,
            frame,
            echo_mode,
            align,
            drag_enabled,
            read_only,
            clear_button,
    ):
        super().__init__(widget,size_policy,dim,font,cursor,focus_policy,layout_direction)

        widget.setInputMask(input_mask)
        widget.setMaxLength(max_length)
        widget.setFrame(frame)
        widget.setEchoMode(echo_mode)
        widget.setAlignment(align.horizontal | align.vertical)
        widget.setDragEnabled(drag_enabled)
        widget.setReadOnly(read_only)
        widget.setClearButtonEnabled(clear_button)
