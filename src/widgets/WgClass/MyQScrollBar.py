from .MyQAbstractSlider import MyQAbstractSlider


class MyQScrollBar(MyQAbstractSlider):
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
        super().__init__(widget,size_policy,dim,font,cursor,focus_policy,layout_direction,value)
