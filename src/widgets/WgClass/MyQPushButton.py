from .MyQAbstractButton import MyQAbstractButton


class MyQPushButton(MyQAbstractButton):
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
            flat
    ):
        super().__init__(widget,size_policy,dim,font,cursor,focus_policy,layout_direction,txt,ico,checkable,checked,auto_actions)

        # Default
        widget.setAutoDefault(auto_default)
        widget.setDefault(default)
        widget.setFlat(flat)
