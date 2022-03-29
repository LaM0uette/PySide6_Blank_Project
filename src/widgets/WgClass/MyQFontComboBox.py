from .MyQComboBox import MyQComboBox


class MyQFontComboBox(MyQComboBox):
    def __init__(
            self,
            widget,
            size_policy,
            dim,
            font,
            cursor,
            focus_policy,
            layout_direction,

            editable,
            max_visible_items,
            insert_policy,
            set_frame,

            current_font,
    ):
        super().__init__(widget,size_policy,dim,font,cursor,focus_policy,layout_direction,editable,max_visible_items,insert_policy,set_frame)

        widget.setCurrentFont(current_font)
