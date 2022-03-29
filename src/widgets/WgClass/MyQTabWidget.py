from .MyQWidget import MyQWidget


class MyQTabWidget(MyQWidget):
    def __init__(
            self,
            widget,
            size_policy,
            dim,
            font,
            cursor,
            focus_policy,
            layout_direction,

            tab_position,
            uses_scroll_buttons,
            document_mode,
            tabs_closable,
            tabs_movable,
    ):
        super().__init__(widget,size_policy,dim,font,cursor,focus_policy,layout_direction)

        widget.setTabPosition(tab_position)
        widget.setUsesScrollButtons(uses_scroll_buttons)
        widget.setDocumentMode(document_mode)
        widget.setTabsClosable(tabs_closable)
        widget.setMovable(tabs_movable)
