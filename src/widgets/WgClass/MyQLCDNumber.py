from .MyQFrame import MyQFrame


class MyQLCDNumber(MyQFrame):
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

            small_decimal_point,
            digit_count,
            digit_mode,
            segment_style,
    ):
        super().__init__(widget, size_policy, dim, font, cursor, focus_policy, layout_direction, frame)

        widget.setSmallDecimalPoint(small_decimal_point)
        widget.setDigitCount(digit_count)
        widget.setMode(digit_mode)
        widget.setSegmentStyle(segment_style)
