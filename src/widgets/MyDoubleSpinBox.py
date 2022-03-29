from .WgClass.MyQDoubleSpinBoxStyle import Style
from src.lib.palettes import *


##################
##     BASE     ##
##################
class PlusMinus:
    def __init__(self, widget):
        self.widget = widget

    def Base(self):
        Style(
            widget=self.widget,
        )
    def Transparent(self):
        Style(
            widget=self.widget,

            focus_policy=PaFocusPolicy.NO,

            background=DcRgbBg.Base(
                base=PaRgb.TR
            ),

            foreground=DcRgbBg.Base(
                base=PaRgb.TH3
            ),
        )
class UpDown:
    def __init__(self, widget):
        self.widget = widget

    def Base(self):
        Style(
            widget=self.widget,

            img=DcImg.Base(
                up=PaImg.FLECHE_TOP,
                down=PaImg.FLECHE_BOTTOM,
                up_hover=PaImg.FLECHE_TOP,
                down_hover=PaImg.FLECHE_BOTTOM,
            )
        )

    def Transparent(self):
        Style(
            widget=self.widget,

            focus_policy=PaFocusPolicy.NO,

            background=DcRgbBg.Base(
                base=PaRgb.TR
            ),

            foreground=DcRgbFg.Base(
                base=PaRgb.TH3
            ),

            img=DcImg.Base(
                up=PaImg.FLECHE_TOP,
                down=PaImg.FLECHE_BOTTOM,
                up_hover=PaImg.FLECHE_TOP,
                down_hover=PaImg.FLECHE_BOTTOM,
            )
        )


##################
##     DLG      ##
##################
class Dlg:
    def __init__(self, widget):
        self.widget = widget

    def rtn(self, value_max):
        Style(
            widget=self.widget,

            dim=DcDim.Base(
                fixed_width=PaDim.H7
            ),

            value=DcValue.Base(
                max=value_max
            ),
        )


    def th(self): self.rtn(value_max=100)
    def rgb(self): self.rtn(value_max=255)
    def inf(self): self.rtn(value_max=99999999)
