from functools import partial

from src import *
from src.gui.dlg.RgbBox.RgbDlg import RgbDlg


class RgbBox:

    @staticmethod
    def __rtn(title, rgb, ico, ico_rgb, txt_ok, txt_cancel, width, height, opacity):
        rgb_dlg = RgbDlg(
            title=title,
            rgb=rgb,
            ico=ico,
            ico_rgb=ico_rgb,
            txt_ok=txt_ok,
            txt_cancel=txt_cancel,
            width=width,
            height=height,
            opacity=opacity
        )
        rgb_dlg.exec()
        return rgb_dlg.return_rgb if rgb_dlg.response else False


    __WIDTH, __HEIGHT, __OPACITY = 650, 250, 1

    GET = partial(__rtn, title="RGB", rgb=None, ico=PaImg.INFO, ico_rgb="th3", txt_ok="Ok", txt_cancel="Annuler", width=__WIDTH, height=__HEIGHT, opacity=__OPACITY)
