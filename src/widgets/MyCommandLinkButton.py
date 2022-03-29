from .WgClass.MyQCommandLinkButtonStyle import Style
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

            background=DcRgbBg.Base(
                base=PaRgb.TH1,
                hover=PaRgb.TH1,
                checked=PaRgb.TH2,
                checked_hover=PaRgb.TH2,
                pressed=PaRgb.TH2,
                checked_pressed=PaRgb.TH1,
            ),

            foreground=DcRgbFg.Base(
                gen=PaRgb.TH3
            ),

            border=DcBorder.Base(
                base=(0, )*4,
                base_rgb=PaRgb.TR,
                hover=(2, )*4,
                hover_rgb=PaRgb.TH3,
                checked=(2, )*4,
                checked_rgb=PaRgb.TH3,
            )
        )
    def Transparent(self):
        Style(
            widget=self.widget,

            background=DcRgbBg.Base(gen=PaRgb.TR),
            foreground=DcRgbFg.Base(
                base=PaRgb.TH3,
                checked=PaRgb.BN1,
            ),
        )
