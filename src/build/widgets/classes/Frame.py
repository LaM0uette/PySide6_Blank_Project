from PySide6 import QtWidgets

from ....build import *
from ....build.widgets import VBase

class Style:
    def __init__(
            self,
            *wgs,
            width=VBase.WIDTH,
            height=VBase.HEIGHT,
            curseur=Cur().souris(),

            # Couleurs BG
            bg=VBase.BG,

            # Bordures
            border=VBase.WG_BORDER_WIDTH,
            border_style=VBase.WG_BORDER_STYLE,
            border_rgb=VBase.WG_BORDER_RGB,
            # Bordures hover
            border_hover=VBase.WG_BORDER_WIDTH,
            border_hover_style=VBase.WG_BORDER_STYLE,
            border_hover_rgb=VBase.WG_BORDER_RGB,

            # Rayons
            radius=(0, 0, 0, 0),
    ):
        style = f"""
                /* FRAME */
                .QFrame {{
                background-color: rgba{bg};
                }}
        
                /* BORDURES */
                .QFrame {{
                border-top: {border[0]}px {border_style} rgba{border_rgb};
                border-bottom: {border[1]}px {border_style} rgba{border_rgb};
                border-right: {border[2]}px {border_style} rgba{border_rgb};
                border-left: {border[3]}px {border_style} rgba{border_rgb};
                }}
                .QFrame:hover {{
                border-top: {border_hover[0]}px {border_hover_style} rgba{border_hover_rgb};
                border-bottom: {border_hover[1]}px {border_hover_style} rgba{border_hover_rgb};
                border-right: {border_hover[2]}px {border_hover_style} rgba{border_hover_rgb};
                border-left: {border_hover[3]}px {border_hover_style} rgba{border_hover_rgb};
                }}
                
                /* RAYONS */
                .QFrame {{
                border-top-right-radius: {radius[0]}px;
                border-top-left-radius: {radius[1]}px;
                border-bottom-right-radius: {radius[2]}px;
                border-bottom-left-radius: {radius[3]}px;
                }}"""

        for wg in wgs:
            wg.setStyleSheet(style)

            Fct(wg=wg, w=width, h=height).DIM()

            wg.setCursor(Fct(cur=curseur).CUR())

            wg.setFrameShape(QtWidgets.QFrame.NoFrame)


##################
##     BASE     ##
##################
class Base_th(Style):
    def __init__(self, *wgs, rgb=Rgb().th1()):
        super().__init__(
            *wgs,
            bg=rgb,
        )
class Base_tr(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            bg=Rgb().tr()
    )


##################
##     MENU     ##
##################
class Menu_top(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            height=Dim().h9(),

            bg=Rgb().th1(),
            radius=(VBase.RADIUS, VBase.RADIUS, 0, 0)
    )
class Menu_bottom(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            height=Dim().h10(),

            bg=Rgb().th2(),
            radius=(0, 0, VBase.RADIUS-1, VBase.RADIUS-1)
    )
class Menu_bottom_dlg(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            height=Dim().h9(),

            bg=Rgb().th2(),
            radius=(0, 0, VBase.RADIUS-1, VBase.RADIUS-1)
    )


####################
##     AUTRES     ##
####################
class Cadre:
    def __init__(self, *wgs):
        self.wgs = wgs

    def rtn(self, rgb):
        Style(
            *self.wgs,
            bg=Rgb().tr(),
            border=((StyleBase().bd(),) * 4),
            border_rgb=rgb,
            border_hover=((StyleBase().bd(),) * 4),
            border_hover_rgb=rgb,
            radius = ((VBase.RADIUS+1, )*4)
        )

    def th1(self): self.rtn(rgb=Rgb().th1())
    def th2(self): self.rtn(rgb=Rgb().th2())
    def th3(self): self.rtn(rgb=Rgb().th3())
    def bn1(self): self.rtn(rgb=Rgb().bn1())
    def bn2(self): self.rtn(rgb=Rgb().bn2())
class palette_rgb(Style):
    def __init__(self, *wgs, rgb):
        super().__init__(
            *wgs,
            bg=rgb,
            radius=((40, )*4),
    )


##################
##     DEMO     ##
##################
class Demo_hover(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            bg=Rgb().tr(),
            border=((StyleBase().bd(),) * 4),
            border_rgb=Rgb().bn1(),
            border_hover=((StyleBase().bd(),) * 4),
            border_hover_style="dashed",
            border_hover_rgb=Rgb().bn1(),
            radius = ((VBase.RADIUS+1, )*4)
    )
