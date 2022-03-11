from src.lib.palettes import *
from src.widgets import vb_wg
from src.widgets.TableWidget.Build import Build


##################
##     BASE     ##
##################
class Base:
    def __init__(self, *wgs):
        self.wgs = wgs

    def th(self):
        Build(
            *self.wgs,

            bg_corner=Rgb().th1(),

            border=(StyleBase().border(),) * 4,
            border_rgb=Rgb().th3(),
        )
    def tr(self):
        Build(
            *self.wgs,

            header_h=False,
            header_v=False,

            bg_corner=Rgb().th1(),
            bg=Rgb().tr(),
            bg_item=Rgb().tr(),
            bg_item_hover=Rgb().tr(),
            bg_item_checked=Rgb().th3(),
            bg_item_checked_hover=Rgb().th3(),
            fg_item=Rgb().th3(),
            fg_item_checked=Rgb().th1(),
        )


##################
##     DEMO     ##
##################
class Demo:
    def __init__(self, *wgs):
        self.wgs = wgs
    def th(self):
        bd_gen = ((1,) * 4)
        rgb_hd = Rgb().th1()
        rgb_item = Rgb().th2()

        Build(
            *self.wgs,

            height=Dim().h4(),

            bg_corner=Rgb().th1(),

            border=(StyleBase().border(),) * 4,
            border_rgb=Rgb().th3(),
            border_hd=bd_gen,
            border_hd_hover=bd_gen,
            border_hd_checked=bd_gen,
            border_hd_checked_hover=bd_gen,
            border_hd_rgb=rgb_hd,
            border_hd_hover_rgb=rgb_hd,
            border_hd_checked_rgb=rgb_hd,
            border_hd_checked_hover_rgb=rgb_hd,
            border_item=bd_gen,
            border_item_hover=bd_gen,
            border_item_checked=bd_gen,
            border_item_checked_hover=bd_gen,
            border_item_rgb=rgb_item,
            border_item_hover_rgb=rgb_item,
            border_item_checked_rgb=rgb_item,
            border_item_checked_hover_rgb=rgb_item,
        )
    def tr(self):
        Build(
            *self.wgs,

            height=Dim().h4(),
            header_h=False,
            header_v=False,

            bg_corner=Rgb().th1(),
            bg=Rgb().tr(),
            bg_item=Rgb().tr(),
            bg_item_hover=Rgb().tr(),
            bg_item_checked=Rgb().th3(),
            bg_item_checked_hover=Rgb().th3(),
            fg_item=Rgb().th3(),
            fg_item_checked=Rgb().th1(),
        )
