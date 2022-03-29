import glob
import os
import pathlib
import shutil

from PySide6 import QtGui, QtCore

from src.config.config import Config
from src.lib.palettes import *


class Functions:

    def SET_CURSOR(self, cur):
        return QtGui.QCursor(QtGui.QPixmap(cur[0]), cur[1], cur[2])
    def SET_ICON(self, ico, rgb):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f"{ico}{rgb}.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        return icon
    def SET_ICON_DIM(self, width, height):
        icon_dim = QtCore.QSize(width, height)
        return icon_dim



    def ADD_QACTION(self, tray, ico=None, ico_rgb=None, txt="", shortcut_txt="", status_tip="", size=None, fct=None, sht_1=None, sht_2=None, sht_3=None):
        if size is None: size=12

        shortcut = int()
        if sht_1 is not None: shortcut += sht_1
        if sht_2 is not None: shortcut += sht_2
        if sht_3 is not None: shortcut += sht_3

        action = QtGui.QAction(self)
        action.setIcon(QtGui.QPixmap(f"{ico}{ico_rgb}.svg").scaledToHeight(size))
        action.setText(txt)
        action.setShortcut(shortcut_txt)
        action.setStatusTip(status_tip)
        action.triggered.connect(fct)

        tray.addAction(action)
        QtGui.QShortcut(QtGui.QKeySequence(shortcut), self).activated.connect(fct)

    def GEN_SVG(self):
        hx1, hx2, hx3, hxbn1, hxbn2 = PaRgb.HX_TH1, PaRgb.HX_TH2, PaRgb.HX_TH3, PaRgb.HX_BN1, PaRgb.HX_BN2
        ls_couleurs = [
            {"rgb_base": "#1D1D1B", "rgb_rep_th1": hx1, "rgb_rep_th2": hx2, "rgb_rep_th3": hx3, "rgb_rep_bn1": hxbn1, "rgb_rep_bn2": hxbn2},
            {"rgb_base": "#3C3C3B", "rgb_rep_th1": hx2, "rgb_rep_th2": hx1, "rgb_rep_th3": hx1, "rgb_rep_bn1": hx2, "rgb_rep_bn2": hx2},
            {"rgb_base": "#575756", "rgb_rep_th1": hx3, "rgb_rep_th2": hx3, "rgb_rep_th3": hx2, "rgb_rep_bn1": hx3, "rgb_rep_bn2": hx3},
            {"rgb_base": "#E30613", "rgb_rep_th1": hxbn1, "rgb_rep_th2": hxbn1, "rgb_rep_th3": hxbn1, "rgb_rep_bn1": hxbn1, "rgb_rep_bn2": hxbn1},
            {"rgb_base": "#00983A", "rgb_rep_th1": hxbn2, "rgb_rep_th2": hxbn2, "rgb_rep_th3": hxbn2, "rgb_rep_bn1": hxbn2, "rgb_rep_bn2": hxbn2}
        ]
        dct_rep_th = {
            "th1": "rgb_rep_th1",
            "th2": "rgb_rep_th2",
            "th3": "rgb_rep_th3",
            "bn1": "rgb_rep_bn1",
            "bn2": "rgb_rep_bn2"
        }

        liens_img = os.listdir("assets/img/")
        for lien_img in liens_img:
            lien = f"assets/img/{lien_img}/"
            lien_rgb = f"{lien}rgb"

            if not os.path.exists(lien_rgb):
                os.makedirs(lien_rgb)
            else:
                try:
                    fichiers = glob.glob(f"{lien_rgb}/*")
                    for fichier in fichiers:
                        os.remove(fichier)
                except: pass

            for svg in glob.glob(f"{lien}*.svg"):
                if "thc" not in svg:
                    for rep in dct_rep_th:
                        img_rgb_svg = f"{pathlib.Path(svg).stem}{rep}.svg"
                        shutil.copyfile(svg, f"{lien_rgb}/{img_rgb_svg}")

                        for couleur in ls_couleurs:
                            with open(f"{lien_rgb}/{img_rgb_svg}", "r+") as svgMod:
                                data = svgMod.read()

                                data = data.replace(couleur["rgb_base"], couleur[dct_rep_th[rep]])
                                svgMod.seek(0)
                                svgMod.write(data)
                else:
                    shutil.copyfile(svg, f"{lien_rgb}/{pathlib.Path(svg).stem[:-4]}.svg")
    def RGB_HEX(self, rgb):
        return "#" + "%02x%02x%02x" % rgb
    def HEX_RGB(self, hex_colors):
        rgb = hex_colors.lstrip('#')
        lv = len(rgb)
        return tuple(int(rgb[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))



    # A SUPPR
    def SET_ICON_A_SUPPR(self, wg, img, dim):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f"{img}.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        wg.setIcon(icon)
        wg.setIconSize(QtCore.QSize(dim, dim))
    def SET_DIM(self, *args, width=None, height=None):
        for wg in args:
            if width is not None: wg.setFixedWidth(width)
            if height is not None: wg.setFixedHeight(height)
    def SET_FONT(self, *args, font=Config.font, font_size=None, rtn=False):
        if not font_size: return

        ft = QtGui.QFont()
        ft.setFamily(font)
        ft.setPointSize(font_size)

        if rtn: return ft

        for wg in args:
            wg.setFont(ft)