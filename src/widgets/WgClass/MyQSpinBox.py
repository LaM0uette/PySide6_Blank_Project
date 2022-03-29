from .MyQAbstractSpinBox import MyQAbstractSpinBox


class MyQSpinBox(MyQAbstractSpinBox):
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

            suffix,
            prefix,
            value,
            integer_base,
    ):
        super().__init__(widget,size_policy,dim,font,cursor,focus_policy,layout_direction,wrapping,frame,align,read_only,button_symbols,accelerated)

        widget.setSuffix(suffix)
        widget.setPrefix(prefix)
        widget.setMinimum(value.min)
        widget.setMaximum(value.max)
        widget.setSingleStep(value.step)
        widget.setDisplayIntegerBase(integer_base)
