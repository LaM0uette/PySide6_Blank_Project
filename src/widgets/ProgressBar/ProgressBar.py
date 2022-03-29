from src.lib.palettes import *
from src.widgets import vb_wg
from src.widgets.ProgressBar.Build import Build


##################
##     BASE     ##
##################
class Base:
    def __init__(self, *wgs):
        self.wgs = wgs

    def Chargement(self):
        Build(
            *self.wgs,

            border=(PaStyleBase.BORDER,) * 4,
            border_hover=(PaStyleBase.BORDER,) * 4,
            border_rgb=PaRgb.TH3,
            border_hover_rgb=PaRgb.TH3,

            radius_chunk=(3, 0, 3, 0)
        )
