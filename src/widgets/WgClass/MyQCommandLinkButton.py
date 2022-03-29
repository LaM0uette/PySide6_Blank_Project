from .MyQPushButton import MyQPushButton


class MyQCommandLinkButton(MyQPushButton):
    def __init__(
            self,
            widget,
            size_policy,
            dim,
            font,
            cursor,
            focus_policy,
            layout_direction,

            txt,
            ico,
            checkable,
            checked,
            auto_actions,

            auto_default,
            default,
            flat,

            description
    ):

        # Default
        super().__init__(widget, size_policy, dim, font, cursor, focus_policy, layout_direction, txt, ico, checkable, checked, auto_actions, auto_default, default, flat)

        widget.setAutoDefault(auto_default)
        widget.setDefault(default)
        widget.setFlat(flat)
        if description: widget.setDescription(description)
