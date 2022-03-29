from .MyQAbstractButton import MyQAbstractButton


class MyQCheckBox(MyQAbstractButton):
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

            tristate,
    ):
        super().__init__(widget,size_policy,dim,font,cursor,focus_policy,layout_direction,txt,ico,checkable,checked,auto_actions)

        # Default
        widget.setTristate(tristate)
