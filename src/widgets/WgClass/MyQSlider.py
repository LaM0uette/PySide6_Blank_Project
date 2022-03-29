from .MyQAbstractSlider import MyQAbstractSlider


class MyQSlider(MyQAbstractSlider):
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

            tick_position,
            tick_interval,
    ):
        super().__init__(widget,size_policy,dim,font,cursor,focus_policy,layout_direction,value)

        widget.setTickPosition(tick_position)
        widget.setTickInterval(tick_interval)
