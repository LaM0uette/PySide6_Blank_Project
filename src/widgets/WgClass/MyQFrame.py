from .MyQWidget import MyQWidget


class MyQFrame(MyQWidget):
    def __init__(
            self,
            widget,
            size_policy,
            dim,
            font,
            cursor,
            focus_policy,
            layout_direction,

            frame,
    ):
        super().__init__(widget,size_policy,dim,font,cursor,focus_policy,layout_direction)

        widget.setFrameShape(frame.frame_shape)
        widget.setFrameShadow(frame.frame_shadow)
        widget.setLineWidth(frame.line_width)
        widget.setMidLineWidth(frame.mid_line_width)

        # if shadow: widget.setGraphicsEffect(shadow)
