from functools import partial

from src import *
from src.gui.dlg.OptionBox.OptionDlg import OptionDlg


class OptionBox:

    @staticmethod
    def __rtn(fen_main, title, msg, ico, ico_rgb, txt_apply, txt_ok, width, height, opacity):
        opt = OptionDlg(
            fen_main=fen_main,
            title=title,
            msg=msg,
            ico=ico,
            ico_rgb=ico_rgb,
            txt_apply=txt_apply,
            txt_ok=txt_ok,
            width=width,
            height=height,
            opacity=opacity
        )
        opt.exec()

    __WIDTH, __HEIGHT, __OPACITY = 850, 600, 1

    MAIN = partial(__rtn, title="OPTION", msg="", ico=PaImg.INFO, ico_rgb="th3", txt_apply="Appliquer", txt_ok="Ok", width=__WIDTH, height=__HEIGHT, opacity=__OPACITY)
