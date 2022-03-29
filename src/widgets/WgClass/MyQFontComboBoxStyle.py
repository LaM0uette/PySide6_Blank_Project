from .MyQFontComboBox import MyQFontComboBox
from src.build.mods import Functions
from src.lib.globals import v_wg
from src.lib.palettes import *


class Style(MyQFontComboBox):
    def __init__(
            self,
            widget,
            size_policy=v_wg.SIZE_POLICY,
            dim=v_wg.DIM_WG,
            font=v_wg.FONT,
            cursor=v_wg.CUR_ACTION,
            focus_policy=v_wg.FOCUS_POLICY,
            layout_direction=v_wg.LAYOUT_DIRECTION,

            editable=True,
            max_visible_items=10,
            insert_policy=PaInsertPolicy.NO,
            set_frame=False,

            current_font=PaFont.BASE,

            background=v_wg.BACKGROUND,
            background_item=v_wg.BACKGROUND,
            foreground=v_wg.FOREGROUND,
            foreground_item=v_wg.FOREGROUND,
            img=v_wg.IMG,
            margin=(0, 0, 5, 0),
            border=v_wg.BORDER,
            scroll=v_wg.SCROLL,
    ):
        super().__init__(widget,size_policy,dim,font,cursor,focus_policy,layout_direction,editable,max_visible_items,insert_policy,set_frame,current_font)

        style = f"""
        /* COMBOBOX */
        QFontComboBox {{
        background-color: rgba{background.base};
        color: rgba{foreground.base};
        selection-background-color: rgba{background.selection};
        selection-color: rgba{foreground.selection};
        }}
        QFontComboBox:hover {{
        background-color: rgba{background.hover};
        color: rgba{foreground.hover};
        }}

        /* BOUTON DE DEROULEMENT */
        QFontComboBox::drop-down {{
        width: {img.height}px;
        margin-top: {margin[0]}px;
        margin-bottom: {margin[1]}px;
        margin-right: {margin[2]}px;
        margin-left: {margin[3]}px;
        border: none;
        }}

        /* IMAGE DU BOUTON DE DEROULEMENT */
        QFontComboBox::down-arrow {{
        image: url({f"{img.unroll}{img.unroll_rgb}.svg"});
        width: {img.width}px;
        height: {img.height}px;
        }}
        QFontComboBox::down-arrow:hover {{
        image: url({f"{img.unroll_hover}{img.unroll_hover_rgb}.svg"});
        width: {img.width}px;
        height: {img.height}px;
        }}

        /* ELEMENTS DEROULEMENT */
        QFontComboBox QAbstractItemView {{
        background-color: rgba{background.base};
        color: rgba{foreground.base};
        }}
        QFontComboBox QAbstractItemView::item {{
        background-color: rgba{background_item.base};
        color: rgba{foreground_item.base};
        }}
        QFontComboBox QAbstractItemView::item:hover {{
        background-color: rgba{background_item.hover};
        color: rgba{foreground_item.hover};
        }}

        /* BORDURES */
        .QFontComboBox {{
        border-top: {border.base[0]}px {border.base_style} rgba{border.base_rgb};
        border-bottom: {border.base[1]}px {border.base_style} rgba{border.base_rgb};
        border-right: {border.base[2]}px {border.base_style} rgba{border.base_rgb};
        border-left: {border.base[3]}px {border.base_style} rgba{border.base_rgb};
        }}
        .QFontComboBox:hover {{
        border-top: {border.hover[0]}px {border.hover_style} rgba{border.hover_rgb};
        border-bottom: {border.hover[1]}px {border.hover_style} rgba{border.hover_rgb};
        border-right: {border.hover[2]}px {border.hover_style} rgba{border.hover_rgb};
        border-left: {border.hover[3]}px {border.hover_style} rgba{border.hover_rgb};
        }}

        /* RAYONS */
        .QFontComboBox {{
        border-top-right-radius: {border.radius[0]}px;
        border-top-left-radius: {border.radius[1]}px;
        border-bottom-right-radius: {border.radius[2]}px;
        border-bottom-left-radius: {border.radius[3]}px;
        }}

        /* SCROLL */
        QScrollBar {{
        background-color: rgba{scroll.bg};
        width: {scroll.width}px;
        height: {scroll.height}px;
        }}
        QScrollBar::handle:horizontal {{
        min-width: {scroll.min_width_handle}px;
        }}
        QScrollBar::handle:vertical {{
        min-height: {scroll.min_height_min_handle}px;
        }}
        QScrollBar::handle {{
        background-color: rgba{scroll.handle_fg};
        }}
        QScrollBar::handle:hover {{
        background-color: rgba{scroll.handle_fg_hover};
        }}

        QScrollBar::add-page, QScrollBar::sub-page {{
        background-color: rgba{scroll.handle_bg};
        border: none;
        }}
        QScrollBar::add-page:hover, QScrollBar::sub-page:hover {{
        background-color: rgba{scroll.handle_bg_hover};
        border: none;
        }}"""
        widget.setStyleSheet(style)
        widget.setFont(font)

        if editable:
            widget.lineEdit().setFont(font)
            widget.lineEdit().setCursor(Functions().SET_CURSOR(PaCur.IBEAM))
