from .WgClass.MyQTreeViewStyle import Style
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

            background_header=DcRgbBg.Base(
                base=PaRgb.TH3
            ),

            foreground_header=DcRgbBg.Base(
                base=PaRgb.TH1
            ),

            border=DcBorder.Base(
                radius=(0,) * 4
            ),
            border_item=DcBorder.Base(
                radius=(0,) * 4
            )
        )
    def Transparent(self):
        Style(
            widget=self.widget,

            scroll_policy=DcScrollPolicy.Base(
                horizontal=PaScrollPolicy.OFF,
                vertical=PaScrollPolicy.OFF
            ),

            background=DcRgbBg.Base(
                gen=PaRgb.TR
            ),
            background_item=DcRgbBg.Base(
                gen=PaRgb.TR
            ),

            foreground_item=DcRgbBg.Base(
                base=PaRgb.TH3,
                checked=PaRgb.BN1
            ),

            border_item=DcBorder.Base(
                gen=(0, 0, 0, 2),
                base_rgb=PaRgb.TH2,
                hover_rgb=PaRgb.TH3,
                checked_rgb=PaRgb.BN1,
                checked_hover_rgb=PaRgb.BN1,
                radius=(0,) * 4
            )
        )
    def Option(self):
        Style(
            widget=self.widget,
            dim=DcDim.Base(
                fixed_width=PaDim.H5
            ),
            header_hidden=True,

            scroll_policy=DcScrollPolicy.Base(
                horizontal=PaScrollPolicy.OFF,
                vertical=PaScrollPolicy.OFF
            ),

            background=DcRgbBg.Base(
                gen=PaRgb.TR
            ),
            background_header=DcRgbBg.Base(
                base=PaRgb.TR
            ),
            background_item=DcRgbBg.Base(
                gen=PaRgb.TR
            ),

            foreground_header=DcRgbFg.Base(
                base=PaRgb.TH1,
            ),
            foreground_item=DcRgbFg.Base(
                base=PaRgb.TH3,
                checked=PaRgb.BN1
            ),

            border=DcBorder.Base(
                gen=(0, 0, 2, 0),
                gen_rgb=PaRgb.TH2,
                radius=(0,) * 4
            ),
            border_item=DcBorder.Base(
                gen=(0, 0, 0, 2),
                base_rgb=PaRgb.TH2,
                hover_rgb=PaRgb.TH3,
                checked_rgb=PaRgb.BN1,
                checked_hover_rgb=PaRgb.BN1,
                radius=(0,) * 4
            )
        )


##################
##     DEMO     ##
##################
class Demo:
    def __init__(self, widget):
        self.widget = widget

    def Base(self):
        Style(
            widget=self.widget,
            dim=DcDim.Base(
                fixed_height=PaDim.H5
            ),

            background_header=DcRgbBg.Base(
                base=PaRgb.TH3
            ),

            foreground_header=DcRgbBg.Base(
                base=PaRgb.TH1
            )
        )
    def Transparent(self):
        Style(
            widget=self.widget,

            scroll_policy=DcScrollPolicy.Base(
                horizontal=PaScrollPolicy.OFF,
                vertical=PaScrollPolicy.OFF
            ),

            background=DcRgbBg.Base(
                gen=PaRgb.TR
            ),
            background_item=DcRgbBg.Base(
                gen=PaRgb.TR
            ),

            foreground_item=DcRgbBg.Base(
                base=PaRgb.TH3,
                checked=PaRgb.BN1
            ),

            border_item=DcBorder.Base(
                gen=(0, 0, 0, 2),
                base=PaRgb.TH2,
                hover=PaRgb.TH3,
                checked=PaRgb.BN1,
                checked_hover=PaRgb.BN1,
                radius=(0,) * 4
            )
        )
