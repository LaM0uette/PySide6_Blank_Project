from PySide6 import QtWidgets

from ....build import *
from ....build.widgets import VBase

class Style:
    def __init__(
            self,
            *wgs,
            width=VBase.WIDTH,
            height=VBase.HEIGHT,
            font=VBase.FONT,
            font_size=VBase.FONT_SIZE,
            curseur=VBase.CUR,

            # Couleurs BG
            bg=VBase.BG,
            bg_hover=VBase.BG_HOVER,
            bg_checked=VBase.BG_CHECKED,
            bg_checked_hover=VBase.BG_CHECKED_HOVER,
            # Couleurs FG
            fg=VBase.FG,
            fg_hover=VBase.FG_HOVER,
            fg_checked=VBase.FG_CHECKED,
            fg_checked_hover=VBase.FG_CHECKED_HOVER,

            # Bordures
            border=VBase.WG_BORDER_WIDTH,
            border_style=VBase.WG_BORDER_STYLE,
            border_rgb=VBase.WG_BORDER_RGB,
            # Bordures hover
            border_hover=VBase.WG_BORDER_WIDTH,
            border_hover_style=VBase.WG_BORDER_STYLE,
            border_hover_rgb=VBase.WG_BORDER_RGB,
            # Bordures HD
            border_hd=VBase.WG_BORDER_WIDTH,
            border_hd_style=VBase.WG_BORDER_STYLE,
            border_hd_rgb=VBase.WG_BORDER_RGB,
            # Bordures HD hover
            border_hd_hover=VBase.WG_BORDER_WIDTH,
            border_hd_hover_style=VBase.WG_BORDER_STYLE,
            border_hd_hover_rgb=VBase.WG_BORDER_RGB,
            # Bordures HD checked
            border_hd_checked=VBase.WG_BORDER_WIDTH,
            border_hd_checked_style=VBase.WG_BORDER_STYLE,
            border_hd_checked_rgb=VBase.WG_BORDER_RGB,
            # Bordures HD checked hover
            border_hd_checked_hover=VBase.WG_BORDER_WIDTH,
            border_hd_checked_hover_style=VBase.WG_BORDER_STYLE,
            border_hd_checked_hover_rgb=VBase.WG_BORDER_RGB,

            # Rayons
            radius=VBase.WG_RADIUS,
            radius_tab=VBase.WG_RADIUS,

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
                /* TOOLBOX */
                QToolBox::tab {{
                background-color: rgba{bg};
                color: rgba{fg};
                border-top: {border_hd[0]}px {border_hd_style} rgba{border_hd_rgb};
                border-bottom: {border_hd[1]}px {border_hd_style} rgba{border_hd_rgb};
                border-right: {border_hd[2]}px {border_hd_style} rgba{border_hd_rgb};
                border-left: {border_hd[3]}px {border_hd_style} rgba{border_hd_rgb};
                border-top-right-radius: {radius_tab[0]}px;
                border-top-left-radius: {radius_tab[1]}px;
                border-bottom-right-radius: {radius_tab[2]}px;
                border-bottom-left-radius: {radius_tab[3]}px;
                }}
        
                QToolBox::tab:hover {{
                background-color: rgba{bg_hover};
                color: rgba{fg_hover};
                border-top: {border_hd_hover[0]}px {border_hd_hover_style} rgba{border_hd_hover_rgb};
                border-bottom: {border_hd_hover[1]}px {border_hd_hover_style} rgba{border_hd_hover_rgb};
                border-right: {border_hd_hover[2]}px {border_hd_hover_style} rgba{border_hd_hover_rgb};
                border-left: {border_hd_hover[3]}px {border_hd_hover_style} rgba{border_hd_hover_rgb};
                }}
        
                QToolBox::tab:selected {{
                background-color: rgba{bg_checked};
                color: rgba{fg_checked};
                border-top: {border_hd_checked[0]}px {border_hd_checked_style} rgba{border_hd_checked_rgb};
                border-bottom: {border_hd_checked[1]}px {border_hd_checked_style} rgba{border_hd_checked_rgb};
                border-right: {border_hd_checked[2]}px {border_hd_checked_style} rgba{border_hd_checked_rgb};
                border-left: {border_hd_checked[3]}px {border_hd_checked_style} rgba{border_hd_checked_rgb};
                }}
        
                QToolBox::tab:selected:hover {{
                background-color: rgba{bg_checked_hover};
                color: rgba{fg_checked_hover};
                border-top: {border_hd_checked_hover[0]}px {border_hd_checked_hover_style} rgba{border_hd_checked_hover_rgb};
                border-bottom: {border_hd_checked_hover[1]}px {border_hd_checked_hover_style} rgba{border_hd_checked_hover_rgb};
                border-right: {border_hd_checked_hover[2]}px {border_hd_checked_hover_style} rgba{border_hd_checked_hover_rgb};
                border-left: {border_hd_checked_hover[3]}px {border_hd_checked_hover_style} rgba{border_hd_checked_hover_rgb};
                }}
        
                /* BORDURES */
                .QToolBox {{
                border-top: {border[0]}px {border_style} rgba{border_rgb};
                border-bottom: {border[1]}px {border_style} rgba{border_rgb};
                border-right: {border[2]}px {border_style} rgba{border_rgb};
                border-left: {border[3]}px {border_style} rgba{border_rgb};
                }}
                .QToolBox:hover {{
                border-top: {border_hover[0]}px {border_hover_style} rgba{border_hover_rgb};
                border-bottom: {border_hover[1]}px {border_hover_style} rgba{border_hover_rgb};
                border-right: {border_hover[2]}px {border_hover_style} rgba{border_hover_rgb};
                border-left: {border_hover[3]}px {border_hover_style} rgba{border_hover_rgb};
                }}
                
                /* RAYONS */
                .QToolBox {{
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

            wg.setFrameShape(QtWidgets.QFrame.NoFrame)

            wg.setCursor(Fct(cur=curseur).CUR())


##################
##     BASE     ##
##################
class Base_th(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
        )
class Base_tr(Style):
    bd_hd = (0, StyleBase().bd(), 0, 0)
    rgb_hb = Rgb().bn1()

    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            bg=Rgb().tr(),
            bg_hover=Rgb().tr(),
            fg=Rgb().th3(),
            border_hd=self.bd_hd,
            border_hd_hover=self.bd_hd,
            border_hd_checked=self.bd_hd,
            border_hd_checked_hover=self.bd_hd,
            border_hd_rgb=self.rgb_hb,
            border_hd_hover_rgb=self.rgb_hb,
            border_hd_checked_rgb=self.rgb_hb,
            border_hd_checked_hover_rgb=self.rgb_hb,
            border=((StyleBase().bd(), )*4),
            border_hover=((StyleBase().bd(), )*4),
            border_rgb=Rgb().th3(),
            border_hover_rgb=Rgb().th3(),
            radius_tab=((0, )*4)
    )
