from src.lib.palettes import *
from src.widgets.TrayIcon.Build import Build


##################
##     BASE     ##
##################
class Main(Build):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,

            bg=PaRgb.TH1,
            bg_item=PaRgb.TH1,
            bg_item_checked=PaRgb.TH1,
            fg=PaRgb.TH3,
            fg_item=PaRgb.TH3,
            fg_item_checked=PaRgb.BN1,

            border=(PaStyleBase.BORDER,) * 4,
            border_rgb=PaRgb.TH2,

            border_item=(0, PaStyleBase.BORDER, 0, 0),
            border_item_checked=(0, PaStyleBase.BORDER, 0, 0),
            border_item_rgb=PaRgb.TH1,
            border_item_checked_rgb=PaRgb.TH2,
            radius_item=(0, )*4,

            height_separator=3,
            margin=(2, 2, 15, 15),
        )
