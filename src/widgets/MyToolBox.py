from .WgClass.MyQToolBoxStyle import Style
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
            )
        )
    def Transparent(self):
        Style(
            widget=self.widget,
            dim=DcDim.Base(
                fixed_height=PaDim.H5
            )
        )
