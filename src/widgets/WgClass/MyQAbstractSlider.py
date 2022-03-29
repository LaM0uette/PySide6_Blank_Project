from .MyQWidget import MyQWidget


class MyQAbstractSlider(MyQWidget):
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
    ):
        super().__init__(widget,size_policy,dim,font,cursor,focus_policy,layout_direction)

        widget.setMinimum(value.min)
        widget.setMaximum(value.max)
        widget.setSingleStep(value.step)
        widget.setPageStep(value.page_step)
