from src.build.mods import Functions


class MyQWidget:
    def __init__(
            self,
            widget,
            size_policy,
            dim,
            font,
            cursor,
            focus_policy,
            layout_direction,
    ):
        """
        :param widget: Widget
        :param size_policy: dc_size_policy.%class(*arguments)
        :param dim: dc_dim.%class(*arguments)
        :param font: PaFont.%
        :param cursor: PaCur.%
        :param focus_policy: PaFocusPolicy.%
        :param layout_direction: PaLayoutDirection.%
        """

        # PaSizePolicy
        widget.setSizePolicy(size_policy.horizontal, size_policy.vertical)

        # Dimmensions
        if dim.minimum_width: widget.setMinimumWidth(dim.minimum_width)
        if dim.minimum_height: widget.setMinimumHeight(dim.minimum_height)
        if dim.maximum_width: widget.setMaximumWidth(dim.maximum_width)
        if dim.maximum_height: widget.setMaximumHeight(dim.maximum_height)

        # PaFont
        widget.setFont(font)

        # Curseur
        widget.setCursor(Functions().SET_CURSOR(cursor))

        # PaFocusPolicy
        widget.setFocusPolicy(focus_policy)

        # PaLayoutDirection
        widget.setLayoutDirection(layout_direction)
