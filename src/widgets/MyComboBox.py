from .WgClass.MyQComboBoxStyle import Style
from src.lib.globals import v_wg
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

            editable=False,
            cursor=PaCur.SOURIS_MAIN,

            background=DcRgbBg.Base(
                base=PaRgb.TR,
                hover=PaRgb.TR,
                selection=PaRgb.TH3,
            ),

            foreground=DcRgbFg.Base(
                base=PaRgb.TH3,
                selection=PaRgb.TH1,
            )
        )
    def Font(self, font=v_wg.FONT):
        Style(
            widget=self.widget,
            font=font
        )
