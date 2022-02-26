from PySide6 import QtWidgets, QtCore

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
            font_size_hd=VBase.FONT_SIZE_HD,
            scroll_h=VBase.SCROLL_H,
            scroll_v=VBase.SCROLL_V,
            header_h=VBase.HEADER_H,
            header_v=VBase.HEADER_V,
            curseur=Cur().croix(),

            # Couleurs BG
            bg=VBase.BG,
            bg_item=VBase.BG_ITEM,
            bg_item_hover=VBase.BG_ITEM_HOVER,
            bg_item_checked=VBase.BG_ITEM_CHECKED,
            bg_item_checked_hover=VBase.BG_ITEM_CHECKED_HOVER,
            bg_corner=VBase.BG,
            bg_header=Rgb().th2(),
            bg_header_hover=Rgb().th2(),
            bg_header_checked=Rgb().th3(),
            bg_header_checked_hover=Rgb().th3(),
            # Couleurs FG
            fg=VBase.FG,
            fg_item=VBase.FG_ITEM,
            fg_item_hover=VBase.FG_ITEM_HOVER,
            fg_item_checked=VBase.FG_ITEM_CHECKED,
            fg_item_checked_hover=VBase.FG_ITEM_CHECKED_HOVER,
            fg_header=Rgb().th1(),
            fg_header_hover=Rgb().bn1(),
            fg_header_checked=Rgb().bn1(),
            fg_header_checked_hover=Rgb().bn2(),
            # couleurs autres
            gridline=VBase.GRIDLINE,

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
            # Bordures item
            border_item=VBase.WG_BORDER_WIDTH,
            border_item_style=VBase.WG_BORDER_STYLE,
            border_item_rgb=VBase.WG_BORDER_RGB,
            # Bordures item hover
            border_item_hover=VBase.WG_BORDER_WIDTH,
            border_item_hover_style=VBase.WG_BORDER_STYLE,
            border_item_hover_rgb=VBase.WG_BORDER_RGB,
            # Bordures item checked
            border_item_checked=VBase.WG_BORDER_WIDTH,
            border_item_checked_style=VBase.WG_BORDER_STYLE,
            border_item_checked_rgb=VBase.WG_BORDER_RGB,
            # Bordures item checked hover
            border_item_checked_hover=VBase.WG_BORDER_WIDTH,
            border_item_checked_hover_style=VBase.WG_BORDER_STYLE,
            border_item_checked_hover_rgb=VBase.WG_BORDER_RGB,

            # Rayons
            radius=VBase.WG_RADIUS,
            radius_item=VBase.WG_RADIUS,
            radius_hd=VBase.WG_RADIUS,

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
                /* CORNER */
                QTableCornerButton::section {{
                background-color: rgba{bg_corner};
                }}
        
                /* TABLE_WIDGET */
                QTableWidget, QTableView {{
                background-color: rgba{bg};
                gridline-color: rgba{gridline};
                color: rgba{fg};
                }}
        
                /* ITEM */
                QTableWidget::item, QTableView::item {{
                background-color: rgba{bg_item};
                color: rgba{fg_item};
                border-top: {border_item[0]}px {border_item_style} rgba{border_item_rgb};
                border-bottom: {border_item[1]}px {border_item_style} rgba{border_item_rgb};
                border-right: {border_item[2]}px {border_item_style} rgba{border_item_rgb};
                border-left: {border_item[3]}px {border_item_style} rgba{border_item_rgb};
                border-top-right-radius: {radius_item[0]}px;
                border-top-left-radius: {radius_item[1]}px;
                border-bottom-right-radius: {radius_item[2]}px;
                border-bottom-left-radius: {radius_item[3]}px;
                }}
                QTableWidget::item:hover, QTableView::item:hover {{
                background-color: rgba{bg_item_hover};
                color: rgba{fg_item_hover};
                border-top: {border_item_hover[0]}px {border_item_hover_style} rgba{border_item_hover_rgb};
                border-bottom: {border_item_hover[1]}px {border_item_hover_style} rgba{border_item_hover_rgb};
                border-right: {border_item_hover[2]}px {border_item_hover_style} rgba{border_item_hover_rgb};
                border-left: {border_item_hover[3]}px {border_item_hover_style} rgba{border_item_hover_rgb};
                }}
                QTableWidget::item:selected, QTableView::item:selected {{
                background-color: rgba{bg_item_checked};
                color: rgba{fg_item_checked};
                border-top: {border_item_checked[0]}px {border_item_checked_style} rgba{border_item_checked_rgb};
                border-bottom: {border_item_checked[1]}px {border_item_checked_style} rgba{border_item_checked_rgb};
                border-right: {border_item_checked[2]}px {border_item_checked_style} rgba{border_item_checked_rgb};
                border-left: {border_item_checked[3]}px {border_item_checked_style} rgba{border_item_checked_rgb};
                }}
                QTableWidget::item:selected:hover, QTableView::item:selected:hover {{
                background-color: rgba{bg_item_checked_hover};
                color: rgba{fg_item_checked_hover};
                border-top: {border_item_checked_hover[0]}px {border_item_checked_hover_style} rgba{border_item_checked_hover_rgb};
                border-bottom: {border_item_checked_hover[1]}px {border_item_checked_hover_style} rgba{border_item_checked_hover_rgb};
                border-right: {border_item_checked_hover[2]}px {border_item_checked_hover_style} rgba{border_item_checked_hover_rgb};
                border-left: {border_item_checked_hover[3]}px {border_item_checked_hover_style} rgba{border_item_checked_hover_rgb};
                }}
        
                /* BORDURES */
                .QTableWidget, .QTableView {{
                border-top: {border[0]}px {border_style} rgba{border_rgb};
                border-bottom: {border[1]}px {border_style} rgba{border_rgb};
                border-right: {border[2]}px {border_style} rgba{border_rgb};
                border-left: {border[3]}px {border_style} rgba{border_rgb};
                }}
                .QTableWidget:hover, .QTableView:hover {{
                border-top: {border_hover[0]}px {border_hover_style} rgba{border_hover_rgb};
                border-bottom: {border_hover[1]}px {border_hover_style} rgba{border_hover_rgb};
                border-right: {border_hover[2]}px {border_hover_style} rgba{border_hover_rgb};
                border-left: {border_hover[3]}px {border_hover_style} rgba{border_hover_rgb};
                }}
                
                /* HEADER */
                QHeaderView::section {{
                background-color: rgba{bg_header};
                color: rgba{fg_header};
                border-top: {border_hd[0]}px {border_hd_style} rgba{border_hd_rgb};
                border-bottom: {border_hd[1]}px {border_hd_style} rgba{border_hd_rgb};
                border-right: {border_hd[2]}px {border_hd_style} rgba{border_hd_rgb};
                border-left: {border_hd[3]}px {border_hd_style} rgba{border_hd_rgb};
                border-top-right-radius: {radius_hd[0]}px;
                border-top-left-radius: {radius_hd[1]}px;
                border-bottom-right-radius: {radius_hd[2]}px;
                border-bottom-left-radius: {radius_hd[3]}px;
                }}
                QHeaderView::section:hover {{
                background-color: rgba{bg_header_hover};
                color: rgba{fg_header_hover};
                border-top: {border_hd_hover[0]}px {border_hd_hover_style} rgba{border_hd_hover_rgb};
                border-bottom: {border_hd_hover[1]}px {border_hd_hover_style} rgba{border_hd_hover_rgb};
                border-right: {border_hd_hover[2]}px {border_hd_hover_style} rgba{border_hd_hover_rgb};
                border-left: {border_hd_hover[3]}px {border_hd_hover_style} rgba{border_hd_hover_rgb};
                }}
                QHeaderView::section:checked {{
                background-color: rgba{bg_header_checked};
                color: rgba{fg_header_checked};
                border-top: {border_hd_checked[0]}px {border_hd_checked_style} rgba{border_hd_checked_rgb};
                border-bottom: {border_hd_checked[1]}px {border_hd_checked_style} rgba{border_hd_checked_rgb};
                border-right: {border_hd_checked[2]}px {border_hd_checked_style} rgba{border_hd_checked_rgb};
                border-left: {border_hd_checked[3]}px {border_hd_checked_style} rgba{border_hd_checked_rgb};
                }}
                QHeaderView::section:checked:hover {{
                background-color: rgba{bg_header_checked_hover};
                color: rgba{fg_header_checked_hover};
                border-top: {border_hd_checked_hover[0]}px {border_hd_checked_hover_style} rgba{border_hd_checked_hover_rgb};
                border-bottom: {border_hd_checked_hover[1]}px {border_hd_checked_hover_style} rgba{border_hd_checked_hover_rgb};
                border-right: {border_hd_checked_hover[2]}px {border_hd_checked_hover_style} rgba{border_hd_checked_hover_rgb};
                border-left: {border_hd_checked_hover[3]}px {border_hd_checked_hover_style} rgba{border_hd_checked_hover_rgb};
                }}
                
                /* RAYONS */
                .QTableWidget, .QTableView {{
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
            wg.horizontalHeader().setStyleSheet(style)
            wg.verticalHeader().setStyleSheet(style)

            Fct(wg=wg, w=width, h=height).DIM()
            wg.setFont(Fct(font=font, font_size=font_size).FONT())
            wg.horizontalHeader().setFont(Fct(font_size=font_size_hd).FONT())
            wg.verticalHeader().setFont(Fct(font_size=font_size_hd).FONT())

            wg.setHorizontalScrollBarPolicy(scroll_h)
            wg.setVerticalScrollBarPolicy(scroll_v)
            wg.horizontalHeader().setVisible(header_h)
            wg.verticalHeader().setVisible(header_v)

            wg.setCursor(Fct(cur=curseur).CUR())
            wg.viewport().setCursor(Fct(cur=curseur).CUR())

            wg.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
            wg.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)
            wg.verticalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)
            wg.setFrameShape(QtWidgets.QFrame.NoFrame)

            wg.resizeColumnsToContents()

            wg.setFocusPolicy(QtCore.Qt.NoFocus)


##################
##     BASE     ##
##################
class Base_th(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            bg_corner=Rgb().th1(),

            border=((StyleBase().bd(),) * 4),
            border_rgb=Rgb().th3(),
        )
class Base_tr(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            header_h=False,
            header_v=False,

            bg_corner=Rgb().th1(),
            bg=Rgb().tr(),
            bg_item=Rgb().tr(),
            bg_item_hover=Rgb().tr(),
            bg_item_checked=Rgb().th3(),
            bg_item_checked_hover=Rgb().th3(),
            fg_item=Rgb().th3(),
            fg_item_checked=Rgb().th1(),
    )
