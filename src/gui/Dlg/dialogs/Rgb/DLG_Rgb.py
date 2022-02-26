from .RgbApp import RgbApp
from .....build import *


class DLG_Rgb:
    def __init__(self,
                 width=700,
                 height=500,
                 opacity=1
    ):
        self.width = width
        self.height = height
        self.opacity = opacity

    def _rtn(self, titre, rgb, ico, tm, txt_pb_ok, txt_pb_annuler):
        rgb = RgbApp(
            titre=titre,
            rgb=rgb,
            ico=ico,
            tm=tm,
            txt_pb_ok=txt_pb_ok,
            txt_pb_annuler=txt_pb_annuler,
            width=self.width,
            height=self.height,
            opacity=self.opacity
        )
        rgb.exec()

        return rgb.rep, rgb.rgb_rtn


    def GET(self, titre="RGB", rgb=None, ico=Img().info(), tm="th3", txt_pb_ok="Ok", txt_pb_annuler="Annuler"):
        if rgb is None: rgb = (0, 0, 0)

        return self._rtn(
            titre=titre,
            rgb=rgb,
            ico=ico,
            tm=tm,
            txt_pb_ok=txt_pb_ok,
            txt_pb_annuler=txt_pb_annuler
        )
