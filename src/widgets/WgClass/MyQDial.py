from .MyQAbstractSlider import MyQAbstractSlider


class MyQDial(MyQAbstractSlider):
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

            wrapping,
            notch_target,
            notches_visible,
    ):
        super().__init__(widget,size_policy,dim,font,cursor,focus_policy,layout_direction,value)

        widget.setWrapping(wrapping)
        widget.setNotchTarget(notch_target)
        widget.setNotchesVisible(notches_visible)
