from .MyQWidget import MyQWidget
from src.build.mods import Functions


class MyQAbstractButton(MyQWidget):
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
    ):
        super().__init__(widget,size_policy,dim,font,cursor,focus_policy,layout_direction)

        # Txt
        if txt: widget.setText(txt)

        # Ico
        if ico.ico:
            widget.setIcon(Functions().SET_ICON(ico=ico.ico, rgb=ico.ico_rgb))

            if not ico.ico_width: ico.ico_width = widget.height()
            if not ico.ico_height: ico.ico_height = widget.height()
            widget.setIconSize(Functions().SET_ICON_DIM(width=ico.ico_width, height=ico.ico_height))

        # Actions
        widget.setCheckable(checkable)
        widget.setChecked(checked)
        widget.setAutoRepeat(auto_actions.auto_repeat)
        widget.setAutoExclusive(auto_actions.auto_exclusive)
        widget.setAutoRepeatDelay(auto_actions.auto_repeat_delay)
        widget.setAutoRepeatDelay(auto_actions.auto_repeat_interval)
