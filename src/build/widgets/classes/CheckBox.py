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
            curseur=Cur().souris_main(),

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

            # Positions WG
            spacing=10,

            # Images
            img_uncheck=VBase.IMG_UNCHECK,
            img_uncheck_hover=VBase.IMG_UNCHECK_HOVER,
            img_check=VBase.IMG_CHECK,
            img_check_hover=VBase.IMG_CHECK_HOVER,
            # Images RGB
            img_uncheck_rgb=VBase.IMG_UNCHECK_RGB,
            img_uncheck_hover_rgb=VBase.IMG_UNCHECK_HOVER_RGB,
            img_check_rgb=VBase.IMG_CHECK_RGB,
            img_check_hover_rgb=VBase.IMG_CHECK_HOVER_RGB,
            # Images DIM
            img_width=VBase.img_width,
            img_height=VBase.img_height,
            # Images positions
            img_margin=((0,) * 4),

            # Bordures
            border=VBase.WG_BORDER_WIDTH,
            border_style=VBase.WG_BORDER_STYLE,
            border_rgb=VBase.WG_BORDER_RGB,
            # Bordures hover
            border_hover=VBase.WG_BORDER_WIDTH,
            border_hover_style=VBase.WG_BORDER_STYLE,
            border_hover_rgb=VBase.WG_BORDER_RGB,
            # Bordures checked
            border_checked=VBase.WG_BORDER_WIDTH,
            border_checked_style=VBase.WG_BORDER_STYLE,
            border_checked_rgb=VBase.WG_BORDER_RGB,
            # Bordures checked hover
            border_checked_hover=VBase.WG_BORDER_WIDTH,
            border_checked_hover_style=VBase.WG_BORDER_STYLE,
            border_checked_hover_rgb=VBase.WG_BORDER_RGB,

            # Rayons
            radius=VBase.WG_RADIUS
    ):
        style = f"""
                /* CHECKBOX */
                QCheckBox {{
                background-color: rgba{bg};
                color: rgba{fg};
                spacing: {spacing}px;
                }}
                QCheckBox:hover {{
                background-color: rgba{bg_hover};
                color: rgba{fg_hover};
                }}
                QCheckBox:checked {{
                background-color: rgba{bg_checked};
                color: rgba{fg_checked};
                }}
                QCheckBox:checked:hover {{
                background-color: rgba{bg_checked_hover};
                color: rgba{fg_checked_hover};
                }}

                /* IMG */
                QCheckBox::indicator {{
                margin-top: {img_margin[0]}px;
                margin-bottom: {img_margin[1]}px;
                margin-right: {img_margin[2]}px;
                margin-left: {img_margin[3]}px;
                width: {img_width}px;
                height: {img_height}px;
                }}
                QCheckBox::indicator:unchecked {{
                image: url({f"{img_uncheck}{img_uncheck_rgb}.svg"});
                }}
                QCheckBox::indicator:hover {{
                image: url({f"{img_uncheck_hover}{img_uncheck_hover_rgb}.svg"});
                }}
                QCheckBox::indicator:checked {{
                image: url({f"{img_check}{img_check_rgb}.svg"});
                }}
                QCheckBox::indicator:checked:hover {{
                image: url({f"{img_check_hover}{img_check_hover_rgb}.svg"});
                }}

                /* BORDURES */
                .QCheckBox {{
                border-top: {border[0]}px {border_style} rgba{border_rgb};
                border-bottom: {border[1]}px {border_style} rgba{border_rgb};
                border-right: {border[2]}px {border_style} rgba{border_rgb};
                border-left: {border[3]}px {border_style} rgba{border_rgb};
                }}
                .QCheckBox:hover {{
                border-top: {border_hover[0]}px {border_hover_style} rgba{border_hover_rgb};
                border-bottom: {border_hover[1]}px {border_hover_style} rgba{border_hover_rgb};
                border-right: {border_hover[2]}px {border_hover_style} rgba{border_hover_rgb};
                border-left: {border_hover[3]}px {border_hover_style} rgba{border_hover_rgb};
                }}
                .QCheckBox:checked {{
                border-top: {border_checked[0]}px {border_checked_style} rgba{border_checked_rgb};
                border-bottom: {border_checked[1]}px {border_checked_style} rgba{border_checked_rgb};
                border-right: {border_checked[2]}px {border_checked_style} rgba{border_checked_rgb};
                border-left: {border_checked[3]}px {border_checked_style} rgba{border_checked_rgb};
                }}
                .QCheckBox:checked:hover {{
                border-top: {border_checked_hover[0]}px {border_checked_hover_style} rgba{border_checked_hover_rgb};
                border-bottom: {border_checked_hover[1]}px {border_checked_hover_style} rgba{border_checked_hover_rgb};
                border-right: {border_checked_hover[2]}px {border_checked_hover_style} rgba{border_checked_hover_rgb};
                border-left: {border_checked_hover[3]}px {border_checked_hover_style} rgba{border_checked_hover_rgb};
                }}
                
                /* RAYONS */
                .QCheckBox {{
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
class Base_th(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            img_margin=(0, 0, 0, (VBase.WG_HEIGHT - (VBase.WG_HEIGHT * StyleBase().x_ico())) / 2),
        )
class Base_tr(Style):
    bg = Rgb().tr()

    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            bg=self.bg,
            bg_hover=self.bg,
            bg_checked=self.bg,
            bg_checked_hover=self.bg,
            fg=Rgb().th3(),
            fg_checked=Rgb().th3(),
            img_margin=(0, 0, 0, (VBase.WG_HEIGHT - (VBase.WG_HEIGHT * StyleBase().x_ico())) / 2),
        )
