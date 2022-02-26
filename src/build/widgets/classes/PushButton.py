from PySide6 import QtWidgets

from ....build import *
from ....build.widgets import VBase
from ....build.widgets.classes import ClassePb

class Style:
    def __init__(
            self,
            *wgs,
            wg_type=None,
            width=VBase.WG_WIDTH,
            height=VBase.WG_HEIGHT,
            font=VBase.FONT,
            font_size=VBase.FONT_SIZE,
            curseur=VBase.CUR,

            # Couleurs BG
            bg=VBase.BG,
            bg_hover=VBase.BG_HOVER,
            bg_checked=VBase.BG_CHECKED,
            bg_checked_hover=VBase.BG_CHECKED_HOVER,
            bg_pressed=VBase.BG_PRESSED,
            bg_checked_pressed=VBase.BG_CHECKED_PRESSED,
            # Couleurs FG
            fg=VBase.FG,
            fg_hover=VBase.FG_HOVER,
            fg_checked=VBase.FG_CHECKED,
            fg_checked_hover=VBase.FG_CHECKED_HOVER,
            fg_pressed=VBase.FG_PRESSED,
            fg_checked_pressed=VBase.FG_CHECKED_PRESSED,

            # Images
            img_uncheck=VBase.IMG_UNCHECK,
            img_uncheck_hover=VBase.IMG_UNCHECK_HOVER,
            img_check=VBase.IMG_CHECK,
            img_check_hover=VBase.IMG_CHECK_HOVER,
            img=VBase.IMG_UNROLL,
            img_hover=VBase.IMG_UNROLL_HOVER,
            # Images RGB
            img_uncheck_rgb=VBase.IMG_UNCHECK_RGB,
            img_uncheck_hover_rgb=VBase.IMG_UNCHECK_HOVER_RGB,
            img_check_rgb=VBase.IMG_CHECK_RGB,
            img_check_hover_rgb=VBase.IMG_CHECK_HOVER_RGB,
            img_rgb=VBase.IMG_UNROLL_RGB,
            img_hover_rgb=VBase.IMG_UNROLL_HOVER_RGB,
            # Images DIM
            img_height=VBase.img_height,
            IMG_HEIGHT=VBase.IMG_HEIGHT,

            # Bordures
            border=VBase.WG_BORDER_WIDTH,
            border_style=VBase.WG_BORDER_STYLE,
            border_rgb=VBase.WG_BORDER_RGB,
            # Bordures hover
            border_hover=VBase.WG_BORDER_WIDTH,
            border_hover_style=VBase.WG_BORDER_STYLE,
            border_hover_rgb=VBase.WG_BORDER_RGB,
            # Bordures checked
            border_checked=VBase.WG_BORDER_WIDTH,
            border_checked_style=VBase.WG_BORDER_STYLE,
            border_checked_rgb=VBase.WG_BORDER_RGB,
            # Bordures checked hover
            border_checked_hover=VBase.WG_BORDER_WIDTH,
            border_checked_hover_style=VBase.WG_BORDER_STYLE,
            border_checked_hover_rgb=VBase.WG_BORDER_RGB,

            # Rayons
            radius=VBase.WG_RADIUS
    ):
        style = f"""
                /* BUTTON */
                QPushButton {{
                background-color: rgba{bg};
                color: rgba{fg};
                }}
        
                QPushButton:hover {{
                background-color: rgba{bg_hover};
                color: rgba{fg_hover};
                }}
        
                QPushButton:checked {{
                background-color: rgba{bg_checked};
                color: rgba{fg_checked};
                }}
        
                QPushButton:checked:hover {{
                background-color: rgba{bg_checked_hover};
                color: rgba{fg_checked_hover};
                }}
        
                QPushButton:pressed {{
                background-color: rgba{bg_pressed};
                color: rgba{fg_pressed};
                }}
        
                QPushButton:checked:pressed {{
                background-color: rgba{bg_checked_pressed};
                color: rgba{fg_checked_pressed};
                }}
        
                /* BORDURES */
                .QPushButton {{
                border-top: {border[0]}px {border_style} rgba{border_rgb};
                border-bottom: {border[1]}px {border_style} rgba{border_rgb};
                border-right: {border[2]}px {border_style} rgba{border_rgb};
                border-left: {border[3]}px {border_style} rgba{border_rgb};
                }}
                .QPushButton:hover {{
                border-top: {border_hover[0]}px {border_hover_style} rgba{border_hover_rgb};
                border-bottom: {border_hover[1]}px {border_hover_style} rgba{border_hover_rgb};
                border-right: {border_hover[2]}px {border_hover_style} rgba{border_hover_rgb};
                border-left: {border_hover[3]}px {border_hover_style} rgba{border_hover_rgb};
                }}
                .QPushButton:checked {{
                border-top: {border_checked[0]}px {border_checked_style} rgba{border_checked_rgb};
                border-bottom: {border_checked[1]}px {border_checked_style} rgba{border_checked_rgb};
                border-right: {border_checked[2]}px {border_checked_style} rgba{border_checked_rgb};
                border-left: {border_checked[3]}px {border_checked_style} rgba{border_checked_rgb};
                }}
                .QPushButton:checked:hover {{
                border-top: {border_checked_hover[0]}px {border_checked_hover_style} rgba{border_checked_hover_rgb};
                border-bottom: {border_checked_hover[1]}px {border_checked_hover_style} rgba{border_checked_hover_rgb};
                border-right: {border_checked_hover[2]}px {border_checked_hover_style} rgba{border_checked_hover_rgb};
                border-left: {border_checked_hover[3]}px {border_checked_hover_style} rgba{border_checked_hover_rgb};
                }}
                
                /* RAYONS */
                .QPushButton {{
                border-top-right-radius: {radius[0]}px;
                border-top-left-radius: {radius[1]}px;
                border-bottom-right-radius: {radius[2]}px;
                border-bottom-left-radius: {radius[3]}px;
                }}"""

        for wg in wgs:
            wg.setStyleSheet(style)

            Fct(wg=wg, w=width, h=height).DIM()
            wg.setFont(Fct(font=font, font_size=font_size).FONT())

            wg.setFlat(True)
            wg.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

            wg.setCursor(Fct(cur=curseur).CUR())

            cls = ClassePb.ClassePb(
                wg=wg,
                dim_ico=img_height,
                DIM_ICO=IMG_HEIGHT,
                img=img,
                img_hover=img_hover,
                img_uncheck=img_uncheck,
                img_uncheck_hover=img_uncheck_hover,
                img_check=img_check,
                img_check_hover=img_check_hover,
                img_rgb=img_rgb,
                img_hover_rgb=img_hover_rgb,
                img_uncheck_rgb=img_uncheck_rgb,
                img_uncheck_hover_rgb=img_uncheck_hover_rgb,
                img_check_rgb=img_check_rgb,
                img_check_hover_rgb=img_check_hover_rgb,
            )


            if wg_type is not None:
                if wg_type == "check":
                    Fct(wg=wg, img=f"{img_uncheck}{img_uncheck_rgb}", dim=img_height).ICON()
                else:
                    Fct(wg=wg, img=f"{img}{img_rgb}", dim=img_height).ICON()

            if wg_type == "check":
                wg.enterEvent = cls.ENT_CHECK
                wg.leaveEvent = cls.LVE_CHECK
                wg.mousePressEvent = cls.MP_CHECK
            elif wg_type == "ico":
                wg.enterEvent = cls.ENT_ICO
                wg.leaveEvent = cls.LVE_ICO
                wg.mousePressEvent = cls.MP_ICO
            elif wg_type == "zoom":
                    wg.enterEvent = cls.ENT_ZOOM
                    wg.leaveEvent = cls.LVE_ZOOM


##################
##     BASE     ##
##################
class Base_th(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
        )
class Base_tr(Style):
    bg = Rgb().tr()

    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            bg=self.bg,
            bg_hover=self.bg,
            bg_checked=self.bg,
            bg_checked_hover=self.bg,
            bg_pressed=self.bg,
            bg_checked_pressed=self.bg,
            fg=Rgb().th3(),
            fg_checked=Rgb().bn1(),
    )
class menu_top:
    def __init__(self, *wgs):
        self.wgs = wgs

    def rtn(self,
            img=Img().main(),
            img_rgb="th2",
            ):
        Style(
            *self.wgs,
            wg_type="zoom",
            width=Dim().h9() * 1.2,
            curseur=Cur().souris_main(),

            bg=Rgb().tr(),
            bg_hover=Rgb().tr(),
            bg_checked=Rgb().tr(),
            bg_checked_hover=Rgb().tr(),
            bg_pressed=Rgb().tr(),
            fg_checked=Rgb().th3(),
            img=img,
            img_rgb=img_rgb,
        )

    def option(self):
        self.rtn(
            img=Img().option()
        )
    def reduire(self):
        self.rtn(
            img=Img().reduire(),
            img_rgb="bn1"
        )
    def agrandir(self):
        self.rtn(
            img=Img().agrandir(),
            img_rgb="th3"
        )
    def quitter(self):
        self.rtn(
            img=Img().quitter(),
            img_rgb="bn2"
        )


#################
##     TXT     ##
#################
class txt(Style):
    bd_gen = ((StyleBase().bd(),) * 4)
    bd_rgb = Rgb().th3()

    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            bg=Rgb().th1(),
            fg=Rgb().th3(),
            bg_hover=Rgb().th3(),
            fg_hover=Rgb().th1(),
            bg_pressed=Rgb().th3(),
            bg_checked=Rgb().th3(),
            fg_checked=Rgb().th1(),
            bg_checked_hover=Rgb().th1(),
            fg_checked_hover=Rgb().th3(),
            bg_checked_pressed=Rgb().th1(),
            border=self.bd_gen,
            border_hover=self.bd_gen,
            border_checked=self.bd_gen,
            border_checked_hover=self.bd_gen,
            border_rgb=self.bd_rgb,
            border_hover_rgb=self.bd_rgb,
            border_checked_rgb=self.bd_rgb,
            border_checked_hover_rgb=self.bd_rgb,
    )
class txt_inv(Style):
    bd_gen = ((StyleBase().bd(),) * 4)
    bd_rgb = Rgb().th3()
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            bg=Rgb().th3(),
            fg=Rgb().th1(),
            bg_hover=Rgb().th1(),
            fg_hover=Rgb().th3(),
            bg_pressed=Rgb().th1(),
            bg_checked=Rgb().th1(),
            fg_checked=Rgb().th3(),
            bg_checked_hover=Rgb().th3(),
            fg_checked_hover=Rgb().th1(),
            bg_checked_pressed=Rgb().th3(),
            border=self.bd_gen,
            border_hover=self.bd_gen,
            border_checked=self.bd_gen,
            border_checked_hover=self.bd_gen,
            border_rgb=self.bd_rgb,
            border_hover_rgb=self.bd_rgb,
            border_checked_rgb=self.bd_rgb,
            border_checked_hover_rgb=self.bd_rgb,
    )


#################
##     DLG     ##
#################
class dlg_ok(Style):
    bd_gen = ((StyleBase().bd(),) * 4)
    rgb_gen = Rgb().bn1()

    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            width=Dim().h6(),
            height=None,

            bg=Rgb().th1(),
            fg=self.rgb_gen,
            bg_hover=self.rgb_gen,
            fg_hover=Rgb().th1(),
            bg_pressed=self.rgb_gen,
            fg_pressed=Rgb().th1(),
            border=self.bd_gen,
            border_hover=self.bd_gen,
            border_checked=self.bd_gen,
            border_checked_hover=self.bd_gen,
            border_rgb=self.rgb_gen,
            border_hover_rgb=self.rgb_gen,
            border_checked_rgb=self.rgb_gen,
            border_checked_hover_rgb=self.rgb_gen,
    )
class dlg_ok_inv(Style):
    bd_gen = ((StyleBase().bd(),) * 4)
    rgb_gen = Rgb().bn1()

    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            width=Dim().h6(),
            height=None,

            bg=self.rgb_gen,
            fg=Rgb().th1(),
            bg_hover=Rgb().th1(),
            fg_hover=self.rgb_gen,
            bg_pressed=Rgb().th1(),
            fg_pressed=self.rgb_gen,
            border=self.bd_gen,
            border_hover=self.bd_gen,
            border_checked=self.bd_gen,
            border_checked_hover=self.bd_gen,
            border_rgb=self.rgb_gen,
            border_hover_rgb=self.rgb_gen,
            border_checked_rgb=self.rgb_gen,
            border_checked_hover_rgb=self.rgb_gen,
    )
class dlg_nok(Style):
    bd_gen = ((StyleBase().bd(),) * 4)
    rgb_gen = Rgb().bn2()

    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            width=Dim().h6(),
            height=None,

            bg=Rgb().th1(),
            fg=self.rgb_gen,
            bg_hover=self.rgb_gen,
            fg_hover=Rgb().th1(),
            bg_pressed=self.rgb_gen,
            fg_pressed=Rgb().th1(),
            border=self.bd_gen,
            border_hover=self.bd_gen,
            border_checked=self.bd_gen,
            border_checked_hover=self.bd_gen,
            border_rgb=self.rgb_gen,
            border_hover_rgb=self.rgb_gen,
            border_checked_rgb=self.rgb_gen,
            border_checked_hover_rgb=self.rgb_gen,
        )
class dlg_nok_inv(Style):
    bd_gen = ((StyleBase().bd(),) * 4)
    rgb_gen = Rgb().bn2()

    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            width=Dim().h6(),
            height=None,

            bg=self.rgb_gen,
            fg=Rgb().th1(),
            bg_hover=Rgb().th1(),
            fg_hover=self.rgb_gen,
            bg_pressed=Rgb().th1(),
            fg_pressed=self.rgb_gen,
            border=self.bd_gen,
            border_hover=self.bd_gen,
            border_checked=self.bd_gen,
            border_checked_hover=self.bd_gen,
            border_rgb=self.rgb_gen,
            border_hover_rgb=self.rgb_gen,
            border_checked_rgb=self.rgb_gen,
            border_checked_hover_rgb=self.rgb_gen,
        )
class plein:
    def __init__(self, *wgs):
        self.wgs = wgs

    def rtn(self,
            bg_gen=Rgb().tr(),
            fg_gen=Rgb().tr(),
            height=Dim().h5(),

            border_gen=((0, )*4),
            border_gen_rgb=Rgb().tr(),
            curseur=Cur().main()
            ):
        Style(
            *self.wgs,
            height=height,
            curseur=curseur,

            bg=bg_gen,
            bg_hover=bg_gen,
            bg_checked=bg_gen,
            bg_checked_hover=bg_gen,
            bg_pressed=bg_gen,
            bg_checked_pressed=bg_gen,
            fg=fg_gen,
            fg_hover=fg_gen,
            fg_checked=fg_gen,
            fg_checked_hover=fg_gen,
            fg_pressed=fg_gen,
            fg_checked_pressed=fg_gen,
            border=border_gen,
            border_hover=border_gen,
            border_checked=border_gen,
            border_checked_hover=border_gen,
            border_rgb=border_gen_rgb,
            border_hover_rgb=border_gen_rgb,
            border_checked_rgb=border_gen_rgb,
            border_checked_hover_rgb=border_gen_rgb,

            radius=((0, )*4)
        )

    def th1(self):
        self.rtn(
            bg_gen=Rgb().th1(),
            fg_gen=Rgb().th3(),
            border_gen=((StyleBase().bd(),) * 4),
            border_gen_rgb=Rgb().th2(),
        )
    def th2(self):
        self.rtn(
            bg_gen=Rgb().th2(),
            fg_gen=Rgb().th3(),
        )
    def th3(self):
        self.rtn(
            bg_gen=Rgb().th3(),
            fg_gen=Rgb().th1(),
        )
    def bn1(self):
        self.rtn(
            bg_gen=Rgb().bn1(),
            fg_gen=Rgb().th3(),
        )
    def bn2(self):
        self.rtn(
            bg_gen=Rgb().bn2(),
            fg_gen=Rgb().th3(),
        )


##################
##     DEMO     ##
##################
class Demo_bd(Style):
    bd_gen = ((StyleBase().bd(),) * 4)
    bd_rgb = Rgb().bn1()

    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            border=self.bd_gen,
            border_hover=self.bd_gen,
            border_checked=self.bd_gen,
            border_checked_hover=self.bd_gen,
            border_rgb=self.bd_rgb,
            border_hover_rgb=self.bd_rgb,
            border_checked_rgb=self.bd_rgb,
            border_checked_hover_rgb=self.bd_rgb,
    )
class Demo_rd(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            radius=((10, )*4)
    )
class ck_ico(Style):
    bg = Rgb().tr()

    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            wg_type="check",

            bg=self.bg,
            bg_hover=self.bg,
            bg_checked=self.bg,
            bg_checked_hover=self.bg,
            fg=Rgb().th3(),
    )
class zoom(Style):
    bg = Rgb().tr()

    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            wg_type="zoom",

            bg=self.bg,
            bg_hover=self.bg,
            bg_checked=self.bg,
            bg_checked_hover=self.bg,
            bg_pressed=self.bg,
            bg_checked_pressed=self.bg,
            img=Img().calendrier(),
            img_rgb="",
    )
