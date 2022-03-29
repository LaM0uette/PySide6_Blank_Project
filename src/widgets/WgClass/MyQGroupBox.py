from .MyQWidget import MyQWidget


class MyQGroupBox(MyQWidget):
    def __init__(
            self,
            widget,
            size_policy,
            dim,
            font,
            cursor,
            focus_policy,
            layout_direction,

            align,
            flat,
            checkable,
            checked,
    ):
        super().__init__(widget,size_policy,dim,font,cursor,focus_policy,layout_direction)

        widget.setAlignment(align.horizontal | align.vertical)
        widget.setFlat(flat)
        widget.setCheckable(checkable)
        widget.setChecked(checked)
