from .RepApp import RepApp
from .....build import *


class DLG_Rep:
    def __init__(self,
                 width=600,
                 height=200,
                 opacity=1
    ):
        self.width = width
        self.height = height
        self.opacity = opacity

    def _rtn(self, titre, msg, ico, tm, txt_pb_ok, txt_pb_annuler):
        rep = RepApp(
            titre=titre,
            msg=msg,
            ico=ico,
            tm=tm,
            txt_pb_ok=txt_pb_ok,
            txt_pb_annuler=txt_pb_annuler,
            width=self.width,
            height=self.height,
            opacity=self.opacity
        )
        rep.exec()

        return rep.rep


    def INFO(self, titre="INFO", msg="", ico=Img().info(), tm="th3", txt_pb_ok="Ok", txt_pb_annuler="Annuler"):
        return self._rtn(
            titre=titre,
            msg=msg,
            ico=ico,
            tm=tm,
            txt_pb_ok=txt_pb_ok,
            txt_pb_annuler=txt_pb_annuler
        )
    def ALERTE(self, titre="ALERTE", msg="", ico=Img().alerte(), tm="th3", txt_pb_ok="Valider", txt_pb_annuler="Annuler"):
        return self._rtn(
            titre=titre,
            msg=msg,
            ico=ico,
            tm=tm,
            txt_pb_ok=txt_pb_ok,
            txt_pb_annuler=txt_pb_annuler
        )
    def QUITTER(self, titre="Quitter", msg="Voulez vous quitter cette application ?", ico=Img().quitter(), tm="bn2", txt_pb_ok="Quitter", txt_pb_annuler="Annuler"):
        return self._rtn(
            titre=titre,
            msg=msg,
            ico=ico,
            tm=tm,
            txt_pb_ok=txt_pb_ok,
            txt_pb_annuler=txt_pb_annuler
        )
