from .WgClass.MyQListViewStyle import Style
from src.lib.palettes import *


##################
##     BASE     ##
##################
class Base:
    def __init__(self, widget):
        self.widget = widget

    def Base(self):
        Style(
            widget=self.widget,
            border_item=DcBorder.Base(
                radius=(0,) * 4)
        )
    def Transparent(self):
        Style(
            widget=self.widget,
            background=DcRgbBg.Base(gen=PaRgb.TR),
            foreground_item=DcRgbBg.Base(
                base=PaRgb.TH3,
                checked=PaRgb.BN1,
            ),
            border_item=DcBorder.Base(
                radius=(0,)*4)
        )
