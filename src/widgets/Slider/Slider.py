from src.lib.palettes import *
from src.widgets import vb_wg
from src.widgets.Slider.Build import Build


##################
##     BASE     ##
##################
class Base:
    def __init__(self, *wgs):
        self.wgs = wgs

    def th(self):
        Build(
            *self.wgs,

            bg=PaRgb.TH1,

            height_groove=12,
            width_groove=12,
            width_handle_h=20,
            height_handle_h=10,
            width_handle_v=10,
            height_handle_v=20,

            margin_handle_h=(-3, -3, 0, 0),
            margin_handle_v=(0, 0, -3, -3),
        )
    def rond(self):
        Build(
            *self.wgs,

            width=200,
            height=200,

            bg=PaRgb.TH1,
            bg_handle=PaRgb.TH3,
            bg_handle_hover=PaRgb.TH3,
            bg_handle_pressed=PaRgb.TH3,

            height_groove=12,
            width_groove=12,
            width_handle_h=10,
            height_handle_h=4,
            width_handle_v=4,
            height_handle_v=10,

            margin_handle_h=(-3, -3, 0, 0),
            margin_handle_v=(0, 0, -3, -3),

            border_handle_h=(3,) * 4,
            border_handle_h_rgb=PaRgb.TH2,
            border_handle_v=(3,) * 4,
            border_handle_v_rgb=PaRgb.TH2,

            radius_groove_h=(3,) * 4,
            radius_groove_v=(3,) * 4,
            radius_handle_h=(6,) * 4,
            radius_handle_v=(6,) * 4,
        )
    def rgb(self, rgb=None, rgb_1=None, rgb_2=None):
        Build(
            *self.wgs,

            height=PaDim.H8,

            value_max=255,

            bg=PaRgb.TH1,
            bg_handle=rgb,
            bg_handle_hover=rgb,
            bg_handle_pressed=rgb,
            bg_groove=rgb_1,
            bg_groove_2=rgb_2,
            bg_groove_hover=rgb_1,
            bg_groove_hover_2=rgb_2,
            bg_groove_pressed=rgb_1,
            bg_groove_pressed_2=rgb_2,
            gradient=(0, 0, 1, 0),

            height_groove=12,
            width_groove=12,
            width_handle_h=18,
            height_handle_h=4,
            width_handle_v=4,
            height_handle_v=18,

            margin_handle_h=(-5, -5, 0, 0),
            margin_handle_v=(0, 0, -5, -5),

            border_groove=(1,) * 4,
            border_groove_rgb=PaRgb.TH3,
            border_handle_h=(2,) * 4,
            border_handle_h_rgb=PaRgb.TH3,
            border_handle_v=(2,) * 4,
            border_handle_v_rgb=PaRgb.TH3,

            radius_groove_h=(2,) * 4,
            radius_groove_v=(2,) * 4,
            radius_handle_h=(8,) * 4,
            radius_handle_v=(8,) * 4,
        )
