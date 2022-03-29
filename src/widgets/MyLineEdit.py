from .WgClass.MyQLineEditStyle import Style
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
        )
    def Transparent(self):
        Style(
            widget=self.widget,

            background=DcRgbBg.Base(
                base=PaRgb.TR,
            ),

            foreground=DcRgbFg.Base(
                base=PaRgb.TH3,
            ),
        )

    def rgb_hex(self):
        Style(
            widget=self.widget,

            align=DcAlign.Base(horizontal=PaAlign.CENTER_HORIZONTAL),

            background=DcRgbBg.Base(
                base=PaRgb.TR,
                selection=PaRgb.TH3,
            ),

            foreground=DcRgbFg.Base(
                base=PaRgb.TH3,
                selection=PaRgb.TH1,
            ),
        )
