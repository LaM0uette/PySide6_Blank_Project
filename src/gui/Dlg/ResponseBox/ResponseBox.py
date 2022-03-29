from functools import partial

from src import *
from src.gui.dlg.ResponseBox.ResponseDlg import ResponseDlg


class ResponseBox:

    @staticmethod
    def __rtn(title, msg, ico, ico_rgb, txt_ok, txt_cancel, width, height, opacity):
        reponse_dlg = ResponseDlg(
            title=title,
            msg=msg,
            ico=ico,
            ico_rgb=ico_rgb,
            txt_ok=txt_ok,
            txt_cancel=txt_cancel,
            width=width,
            height=height,
            opacity=opacity
        )
        reponse_dlg.exec()
        return reponse_dlg.response

    __WIDTH, __HEIGHT, __OPACITY = 650, 250, 1

    INFO = partial(__rtn, title="INFO", msg="", ico=PaImg.INFO, ico_rgb="th3", txt_ok="Ok", txt_cancel="Annuler", width=__WIDTH, height=__HEIGHT, opacity=__OPACITY)
    ALERTE = partial(__rtn, title="ALERTE", msg="", ico=PaImg.ALERTE, ico_rgb="th3", txt_ok="Valider", txt_cancel="Annuler", width=__WIDTH, height=__HEIGHT, opacity=__OPACITY)
    QUITTER = partial(__rtn, title="Quitter", msg="Voulez vous quitter cette application ?", ico=PaImg.QUITTER, ico_rgb="bn2", txt_ok="Quitter", txt_cancel="Annuler", width=__WIDTH, height=__HEIGHT, opacity=__OPACITY)
