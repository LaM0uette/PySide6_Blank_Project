from .WgClass.MyQFrameStyle import Style
from src.lib.palettes import *


##################
##     BASE     ##
##################
class Base:
    def __init__(self, widget):
        self.widget = widget

    def Base(self, rgb=PaRgb.TH3):
        Style(
            widget=self.widget,
            background=DcRgbBg.Base(gen=rgb)
        )
    def Base_no_radius(self, rgb=PaRgb.TH3):
        Style(
            widget=self.widget,
            background=DcRgbBg.Base(gen=rgb),

            border=DcBorder.Base(radius=(0, )*4)
        )
    def Transparent(self, rgb=PaRgb.TR):
        Style(
            widget=self.widget,
            background=DcRgbBg.Base(gen=rgb)
        )


##################
##     MENU     ##
##################
class Menu:
    def __init__(self, widget):
        self.widget = widget

    def top(self):
        Style(
            self.widget,

            dim=DcDim.Base(fixed_height=PaDim.H9),

            background=DcRgbBg.Base(gen=PaRgb.TH1),
            border=DcBorder.Base(radius=(3, 3, 0, 0))
        )
    def bottom(self):
        Style(
            self.widget,

            dim=DcDim.Base(fixed_height=PaDim.H10),

            background=DcRgbBg.Base(gen=PaRgb.TH2),
            border=DcBorder.Base(radius=(0, 0, 3, 3))
        )
    def bottom_dlg(self):
        Style(
            self.widget,

            dim=DcDim.Base(fixed_height=PaDim.H9),

            background=DcRgbBg.Base(gen=PaRgb.TH2),
            border=DcBorder.Base(radius=(0, 0, 3, 3))
        )


####################
##     CADRES     ##
####################
class Cadre:
    def __init__(self, widget):
        self.widget = widget

    def rtn(self, rgb, bd=(PaStyleBase.BORDER,) * 4):
        Style(
            self.widget,

            background=DcRgbBg.Base(gen=PaRgb.TR),
            border=DcBorder.Base(
                gen=bd,
                gen_rgb=rgb,
                radius=(5, )*4
            )
        )

    def th1(self): self.rtn(rgb=PaRgb.TH1)
    def th2(self): self.rtn(rgb=PaRgb.TH2)
    def th3(self): self.rtn(rgb=PaRgb.TH3)
    def bn1(self): self.rtn(rgb=PaRgb.BN1)
    def bn2(self): self.rtn(rgb=PaRgb.BN2)

    def th1_fin(self): self.rtn(rgb=PaRgb.TH1, bd=(1,) * 4)
    def th2_fin(self): self.rtn(rgb=PaRgb.TH2, bd=(1,) * 4)
    def th3_fin(self): self.rtn(rgb=PaRgb.TH3, bd=(1,) * 4)
    def bn1_fin(self): self.rtn(rgb=PaRgb.BN1, bd=(1,) * 4)
    def bn2_fin(self): self.rtn(rgb=PaRgb.BN2, bd=(1,) * 4)


#################
##     DLG     ##
#################
class Dlg:
    def __init__(self, widget):
        self.widget = widget

    def th(self, rgb=PaRgb.TH3):
        Style(
            widget=self.widget,
            background=DcRgbBg.Base(gen=rgb),
            border=DcBorder.Base(radius=(0, )*4)
        )
    def tr(self, rgb=PaRgb.TH3):
        Style(
            widget=self.widget,
            background=DcRgbBg.Base(gen=rgb),
            border=DcBorder.Base(radius=(0, )*4)
        )


####################
##     AUTRES     ##
####################
class palette_rgb:
    def __init__(self, widget, rgb):
        self.widget = widget

        Style(
            widget=self.widget,
            background=DcRgbBg.Base(gen=rgb),
            border=DcBorder.Base(radius=(40, )*4)
        )
class SplashScreen:
    def __init__(self, widget):
        self.widget = widget

        Style(
            widget=self.widget,
            background=DcRgbBg.Base(gen=PaRgb.TH1),
            border=DcBorder.Base(
                gen=(PaStyleBase.BORDER,) * 4,
                gen_rgb=PaRgb.TH3,
                radius=(3, )*4
            )
        )
class ToolBox:
    def __init__(self, widget):
        self.widget = widget

        Style(
            widget=self.widget,
            background=DcRgbBg.Base(gen=PaRgb.TH1),
            border=DcBorder.Base(
                gen=(PaStyleBase.BORDER,) * 4,
                gen_rgb=PaRgb.TH3,
                radius=(3, )*4
            )
        )
