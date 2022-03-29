from .MyQAbstractButton import MyQAbstractButton


class MyQToolButton(MyQAbstractButton):
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

            popup_mode,
            tool_button_style,
            auto_raise,
            arrow_type,
    ):
        super().__init__(widget,size_policy,dim,font,cursor,focus_policy,layout_direction,txt,ico,checkable,checked,auto_actions)

        # Default
        widget.setPopupMode(popup_mode)
        widget.setToolButtonStyle(tool_button_style)
        widget.setAutoRaise(auto_raise)
        widget.setArrowType(arrow_type)
