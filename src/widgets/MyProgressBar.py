from .WgClass.MyQProgressBarStyle import Style
from src.lib.palettes import *


##################
##     BASE     ##
##################
class Base:
    def __init__(self, widget):
        self.widget = widget

    def Chargement(self):
        Style(
            widget=self.widget,

            border=DcBorder.Base(
                gen=(PaStyleBase.BORDER,) * 4,
                gen_rgb=PaRgb.TH3
            ),

            border_chunk=DcBorder.Base(
                radius=(3, 0, 3, 0)
            )
        )
