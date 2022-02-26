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
            height_separator=5,
            curseur=Cur().souris_main(),

            # Couleurs BG
            bg=VBase.BG,
            bg_item=VBase.BG_ITEM,
            bg_item_checked=VBase.BG_ITEM_CHECKED,
            # Couleurs BG autres
            bg_separator=VBase.BG_SEPARATOR,
            # Couleurs FG
            fg=VBase.FG,
            fg_item=VBase.FG_ITEM,
            fg_item_checked=VBase.FG_ITEM_CHECKED,

            # Positions WG
            margin=((0, )*4),
            padding=((0, )*4),

            # Bordures
            border=VBase.WG_BORDER_WIDTH,
            border_style=VBase.WG_BORDER_STYLE,
            border_rgb=VBase.WG_BORDER_RGB,

            # Rayons
            radius=VBase.WG_RADIUS
    ):
        style = f"""
                /* MENU */
                QMenu {{
                background-color: rgba{bg};
                color: rgba{fg};
                }}
                
                /* SEPARATEUR */
                QMenu::separator{{
                height: {height_separator}px;
                background-color: rgba{bg_separator};
                }}
                
                /* ITEM */
                QMenu::item {{
                background-color: rgba{bg_item};
                color: rgba{fg_item};
                margin-top: {margin[0]}px;
                margin-bottom: {margin[1]}px;
                margin-right: {margin[2]}px;
                margin-left: {margin[3]}px;
                padding-top: {padding[0]}px;
                padding-bottom: {padding[1]}px;
                padding-right: {padding[2]}px;
                padding-left: {padding[3]}px;
                }}
                QMenu::item:selected {{
                background-color: rgba{bg_item_checked};
                color: rgba{fg_item_checked};
                }}
                
                /* BORDURES */
                .QMenu {{
                border-top: {border[0]}px {border_style} rgba{border_rgb};
                border-bottom: {border[1]}px {border_style} rgba{border_rgb};
                border-right: {border[2]}px {border_style} rgba{border_rgb};
                border-left: {border[3]}px {border_style} rgba{border_rgb};
                }}
                
                /* RAYONS */
                .QMenu {{
                border-top-right-radius: {radius[0]}px;
                border-top-left-radius: {radius[1]}px;
                border-bottom-right-radius: {radius[2]}px;
                border-bottom-left-radius: {radius[3]}px;
                }}"""

        for wg in wgs:
            wg.setStyleSheet(style)

            Fct(wg=wg, w=width, h=height).DIM()
            wg.setFont(Fct(font=font, font_size=font_size).FONT())

            wg.setCursor(Fct(cur=curseur).CUR())


##################
##     BASE     ##
##################
class Main(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            bg=Rgb().th1(),
            bg_item=Rgb().th1(),
            bg_item_checked=Rgb().th1(),
            fg=Rgb().th3(),
            fg_item=Rgb().th3(),
            fg_item_checked=Rgb().bn1(),
            border=((StyleBase().bd(), )*4),
            border_rgb=Rgb().th2(),
            height_separator=3,
            margin=(10, 10, 15, 15),
        )
