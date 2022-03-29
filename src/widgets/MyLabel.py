from .WgClass.MyQLabelStyle import Style
from src.lib.palettes import *


##################
##     BASE     ##
##################
class Base:
    def __init__(self, widget):
        self.widget = widget

    def ico_main(self):
        Style(
            widget=self.widget,

            dim=DcDim.Base(
                fixed_width=PaDim.H9,
                fixed_height=PaDim.H9,
            ),

            focus_policy=PaFocusPolicy.NO,

            background=DcRgbBg.Base(
                base=PaRgb.TR,
                hover=PaRgb.TR,
            ),

            pixmap=PaImg.MAIN,
            pixmap_rgb="th3",

            scaled_contents=True,
        )
    def ico_splash(self):
        Style(
            widget=self.widget,

            dim=DcDim.Base(
                fixed_width=PaDim.H5,
                fixed_height=PaDim.H5,
            ),

            focus_policy=PaFocusPolicy.NO,

            background=DcRgbBg.Base(
                base=PaRgb.TR,
                hover=PaRgb.TR,
            ),

            pixmap=PaImg.MAIN,
            pixmap_rgb="th3",

            scaled_contents=True,
        )
    def ico_custom(self, img=PaImg.MAIN, img_rgb="th3"):
        Style(
            widget=self.widget,

            dim=DcDim.Base(
                fixed_width=PaDim.H9,
                fixed_height=PaDim.H9,
            ),

            focus_policy=PaFocusPolicy.NO,

            background=DcRgbBg.Base(
                base=PaRgb.TR,
                hover=PaRgb.TR,
            ),

            pixmap=img,
            pixmap_rgb=img_rgb,

            scaled_contents=True,
        )

    def Base(self, font=PaFont.BASE):
        Style(
            widget=self.widget,

            focus_policy=PaFocusPolicy.NO,
            font=font
        )
    def Transparent(self, font=PaFont.BASE):
        Style(
            widget=self.widget,

            background=DcRgbBg.Base(
                base=PaRgb.TR,
                hover=PaRgb.TR,
            ),

            foreground=DcRgbFg.Base(
                base=PaRgb.TH3,
                hover=PaRgb.TH3,
            ),

            focus_policy=PaFocusPolicy.NO,
            font=font
        )
    def Title(self, font=PaFont.BASE):
        Style(
            widget=self.widget,

            background=DcRgbBg.Base(
                base=PaRgb.TR,
                hover=PaRgb.TR,
            ),

            foreground=DcRgbFg.Base(
                base=PaRgb.TH3,
                hover=PaRgb.TH3,
            ),

            focus_policy=PaFocusPolicy.NO,

            align=DcAlign.Base(horizontal=PaAlign.CENTER_HORIZONTAL),
            font=font
        )
