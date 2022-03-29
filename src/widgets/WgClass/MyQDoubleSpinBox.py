from .MyQAbstractSpinBox import MyQAbstractSpinBox


class MyQDoubleSpinBox(MyQAbstractSpinBox):
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
            decimals,
            value,
    ):
        super().__init__(widget,size_policy,dim,font,cursor,focus_policy,layout_direction,wrapping,frame,align,read_only,button_symbols,accelerated)

        widget.setSuffix(suffix)
        widget.setPrefix(prefix)
        widget.setDecimals(decimals)
        widget.setMinimum(value.min)
        widget.setMaximum(value.max)
        widget.setSingleStep(value.step)
