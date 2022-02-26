from ....build import *
from ....build.widgets import VBase

class Style:
    def __init__(
            self,
            *wgs,
            width=VBase.WG_WIDTH,
            height=VBase.WG_HEIGHT,
            font=VBase.FONT,
            font_size=VBase.FONT_SIZE,
            edit=VBase.EDIT,
            curseur=Cur().souris_main(),

            # Couleurs BG
            bg=VBase.BG,
            bg_hover=VBase.BG_HOVER,
            bg_selection=VBase.BG_SELECTION,
            bg_item=VBase.BG_ITEM,
            bg_item_hover=VBase.BG_ITEM_HOVER,
            # Couleurs FG
            fg=VBase.FG,
            fg_hover=VBase.FG_HOVER,
            fg_selection=VBase.FG_SELECTION,
            fg_item=VBase.FG_ITEM,
            fg_item_hover=VBase.FG_ITEM_HOVER,

            # Images
            img=VBase.IMG_UNROLL,
            img_hover=VBase.IMG_UNROLL_HOVER,
            # Images RGB
            img_rgb=VBase.IMG_UNROLL_RGB,
            img_hover_rgb=VBase.IMG_UNROLL_HOVER_RGB,
            # Images DIM
            img_width=VBase.img_width,
            img_height=VBase.img_height,

            # Bordures
            border=VBase.WG_BORDER_WIDTH,
            border_style=VBase.WG_BORDER_STYLE,
            border_rgb=VBase.WG_BORDER_RGB,
            # Bordures hover
            border_hover=VBase.WG_BORDER_WIDTH,
            border_hover_style=VBase.WG_BORDER_STYLE,
            border_hover_rgb=VBase.WG_BORDER_RGB,

            # Rayons
            radius=VBase.WG_RADIUS,

            # Scroll
            scroll_bg=VBase.SCROLL_BG,
            scroll_width=VBase.SCROLL_WIDTH,
            scroll_height=VBase.SCROLL_HEIGHT,
            scroll_handle_bg=VBase.SCROLL_HANDLE_BG,
            scroll_handle_bg_hover=VBase.SCROLL_HANDLE_BG_HOVER,
            scroll_handle_fg=VBase.SCROLL_HANDLE_FG,
            scroll_handle_fg_hover=VBase.SCROLL_HANDLE_FG_HOVER,
            scroll_handle_min_width=VBase.SCROLL_HANDLE_MIN_WIDTH,
            scroll_handle_min_height=VBase.SCROLL_HANDLE_MIN_HEIGHT,

    ):
        style = f"""
                /* COMBOBOX */
                QComboBox, QFontComboBox {{
                background-color: rgba{bg};
                color: rgba{fg};
                selection-background-color: rgba{bg_selection};
                selection-color: rgba{fg_selection};
                }}
                QComboBox:hover, QFontComboBox:hover {{
                background-color: rgba{bg_hover};
                color: rgba{fg_hover};
                }}

                /* BOUTON DE DEROULEMENT */
                QComboBox::drop-down, QFontComboBox::drop-down {{
                width: {height}px;
                border: none;
                }}

                /* IMAGE DU BOUTON DE DEROULEMENT */
                QComboBox::down-arrow, QFontComboBox::down-arrow {{
                image: url({f"{img}{img_rgb}.svg"});
                width: {img_width}px;
                height: {img_height}px;
                }}
                QComboBox::down-arrow:hover, QFontComboBox::down-arrow:hover {{
                image: url({f"{img_hover}{img_hover_rgb}.svg"});
                width: {img_width}px;
                height: {img_height}px;
                }}

                /* ELEMENTS DEROULEMENT */
                QComboBox QAbstractItemView::item, QFontComboBox QAbstractItemView::item {{
                background-color: rgba{bg_item};
                color: rgba{fg_item};
                }}
                QComboBox QAbstractItemView::item:hover, QFontComboBox QAbstractItemView::item:hover {{
                background-color: rgba{bg_item_hover};
                color: rgba{fg_item_hover};
                }}

                /* BORDURES */
                .QComboBox, .QFontComboBox {{
                border-top: {border[0]}px {border_style} rgba{border_rgb};
                border-bottom: {border[1]}px {border_style} rgba{border_rgb};
                border-right: {border[2]}px {border_style} rgba{border_rgb};
                border-left: {border[3]}px {border_style} rgba{border_rgb};
                }}
                .QComboBox:hover, .QFontComboBox:hover {{
                border-top: {border_hover[0]}px {border_hover_style} rgba{border_hover_rgb};
                border-bottom: {border_hover[1]}px {border_hover_style} rgba{border_hover_rgb};
                border-right: {border_hover[2]}px {border_hover_style} rgba{border_hover_rgb};
                border-left: {border_hover[3]}px {border_hover_style} rgba{border_hover_rgb};
                }}
                
                /* RAYONS */
                .QComboBox, .QFontComboBox {{
                border-top-right-radius: {radius[0]}px;
                border-top-left-radius: {radius[1]}px;
                border-bottom-right-radius: {radius[2]}px;
                border-bottom-left-radius: {radius[3]}px;
                }}
                
                /* SCROLL */
                QScrollBar {{
                background-color: rgba{scroll_bg};
                width: {scroll_width}px;
                height: {scroll_height}px;
                }}
                QScrollBar::handle:horizontal {{
                min-width: {scroll_handle_min_width}px;
                }}
                QScrollBar::handle:vertical {{
                min-height: {scroll_handle_min_height}px;
                }}
                QScrollBar::handle {{
                background-color: rgba{scroll_handle_fg};
                }}
                QScrollBar::handle:hover {{
                background-color: rgba{scroll_handle_fg_hover};
                }}
                
                QScrollBar::add-page, QScrollBar::sub-page {{
                background-color: rgba{scroll_handle_bg};
                border: none;
                }}
                QScrollBar::add-page:hover, QScrollBar::sub-page:hover {{
                background-color: rgba{scroll_handle_bg_hover};
                border: none;
                }}"""

        for wg in wgs:
            wg.setStyleSheet(style)

            Fct(wg=wg, w=width, h=height).DIM()
            wg.setFont(Fct(font=font, font_size=font_size).FONT())

            wg.setEditable(edit)

            wg.setCursor(Fct(cur=curseur).CUR())
            wg.view().setCursor(Fct(cur=Cur().souris_main()).CUR())
            if edit:
                wg.lineEdit().setFont(Fct(font_size=font_size).FONT())
                wg.lineEdit().setCursor(Fct(cur=Cur().IBeam()).CUR())


##################
##     BASE     ##
##################
class Base_th(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            curseur=Cur().main(),
    )
class Base_tr(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            edit=True,
            bg=Rgb().tr(),
            bg_hover=Rgb().tr(),
            fg=Rgb().th3(),
            bg_selection=Rgb().th3(),
            fg_selection=Rgb().th1(),
    )
