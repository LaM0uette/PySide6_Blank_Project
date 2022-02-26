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
            text_visible=VBase.TEXT_VISIBLE,
            align_horizontal=Align().h_center(),
            align_vertical=Align().v_center(),
            curseur=Cur().souris(),

            # Couleurs BG
            bg=VBase.BG,
            bg_chunk=VBase.BG_CHUNK,
            bg_chunk_hover=VBase.BG_CHUNK_HOVER,
            # Couleurs FG
            fg=VBase.FG,

            # Positions WG
            padding=((0, )*4),

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
            radius_chunk=VBase.WG_RADIUS
    ):
        style = f"""
                /* PROGRESSBAR */
                QProgressBar {{
                background-color: rgba{bg};
                color: rgba{fg};
                }}
        
                /* PROGRESS */
                QProgressBar::chunk {{
                background-color: rgba{bg_chunk};
                border-top-right-radius: {radius_chunk[0]}px;
                border-top-left-radius: {radius_chunk[1]}px;
                border-bottom-right-radius: {radius_chunk[2]}px;
                border-bottom-left-radius: {radius_chunk[3]}px;
                }}
                QProgressBar::chunk:hover {{
                background-color: rgba{bg_chunk_hover};
                }}
        
                /* BORDURES */
                .QProgressBar {{
                border-top: {border[0]}px {border_style} rgba{border_rgb};
                border-bottom: {border[1]}px {border_style} rgba{border_rgb};
                border-right: {border[2]}px {border_style} rgba{border_rgb};
                border-left: {border[3]}px {border_style} rgba{border_rgb};
                padding-top={padding[0]}px;
                padding-bottom={padding[1]}px;
                padding-right={padding[2]}px;
                padding-left={padding[3]}px;
                }}
                .QProgressBar:hover {{
                border-top: {border_hover[0]}px {border_hover_style} rgba{border_hover_rgb};
                border-bottom: {border_hover[1]}px {border_hover_style} rgba{border_hover_rgb};
                border-right: {border_hover[2]}px {border_hover_style} rgba{border_hover_rgb};
                border-left: {border_hover[3]}px {border_hover_style} rgba{border_hover_rgb};
                }}
                
                /* RAYONS */
                .QProgressBar {{
                border-top-right-radius: {radius[0]}px;
                border-top-left-radius: {radius[1]}px;
                border-bottom-right-radius: {radius[2]}px;
                border-bottom-left-radius: {radius[3]}px;
                }}"""

        for wg in wgs:
            wg.setStyleSheet(style)

            Fct(wg=wg, w=width, h=height).DIM()
            wg.setFont(Fct(font=font, font_size=font_size).FONT())

            wg.setAlignment(align_horizontal | align_vertical)
            wg.setTextVisible(text_visible)

            wg.setCursor(Fct(cur=curseur).CUR())


##################
##     BASE     ##
##################
class Base_th(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,

            border=((StyleBase().bd(), )*4),
            border_hover=((StyleBase().bd(), )*4),
            border_rgb=Rgb().th3(),
            border_hover_rgb=Rgb().th3(),
        )
class Base_tr(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            text_visible=False,

            bg=Rgb().tr(),

            border=((StyleBase().bd(), )*4),
            border_hover=((StyleBase().bd(), )*4),
            border_rgb=Rgb().th3(),
            border_hover_rgb=Rgb().th3(),
    )
