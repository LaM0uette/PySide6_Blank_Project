from functools import partial

from src import *
from src.gui.dlg.MsgBox.MsgDlg import MsgDlg


class MsgBox:

    @staticmethod
    def __rtn(title, msg, ico, ico_rgb, txt_ok, width, height, opacity):
        msg_dlg = MsgDlg(
            title=title,
            msg=msg,
            ico=ico,
            ico_rgb=ico_rgb,
            txt_ok=txt_ok,
            width=width,
            height=height,
            opacity=opacity
        )
        msg_dlg.exec()


    __WIDTH, __HEIGHT, __OPACITY = 650, 250, 1

    INFO = partial(__rtn, title="INFO", msg="", ico=PaImg.INFO, ico_rgb="th3", txt_ok="Ok", width=__WIDTH, height=__HEIGHT, opacity=__OPACITY)
    ALERTE = partial(__rtn, title="ALERTE", msg="", ico=PaImg.INFO, ico_rgb="th3", txt_ok="Ok", width=__WIDTH, height=__HEIGHT, opacity=__OPACITY, )
