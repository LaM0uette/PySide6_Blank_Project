from src.lib.palettes import *
from src.widgets import vb_wg
from src.widgets.TextEdit.Build import Build


##################
##     BASE     ##
##################
class Base:
    def __init__(self, *wgs):
        self.wgs = wgs

    def th(self):
        Build(
            *self.wgs,
        )
    def tr(self):
        Build(
            *self.wgs,

            bg=PaRgb.TR,
            fg=PaRgb.TH3
        )


##################
##     DEMO     ##
##################
class Demo:
    def __init__(self, *wgs):
        self.wgs = wgs

    def th(self):
        Build(
            *self.wgs,

            height=PaDim.H5
        )
    def tr(self):
        Build(
            *self.wgs,

            height=PaDim.H5,

            bg=PaRgb.TR,
            fg=PaRgb.TH3
        )
