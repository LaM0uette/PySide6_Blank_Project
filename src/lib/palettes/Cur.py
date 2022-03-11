import json
import os

from src.config import config


class Cur:
    with open(f"{os.path.dirname(f'src/assets/cursor/{config.cur}/_data.json')}/_data.json", "r", encoding="utf-8") as fichier:
        cur = json.load(fichier)

    _souris = cur["_souris"]
    _centre = cur["_centre"]
    _crayon = cur["_crayon"]
    _fleche_top = cur["_fleche_top"]

    def CUR(self, img, xy): return [f"src/assets/cursor/{config.cur}/{img}.cur", xy[0], xy[1]]

    def agrandir(self): return self.CUR(img="agrandir", xy=self._souris)
    def copier(self): return self.CUR(img="copier", xy=self._souris)
    def crayon(self): return self.CUR(img="crayon", xy=self._crayon)
    def croix(self): return self.CUR(img="croix", xy=self._centre)
    def fleche_nesw(self): return self.CUR(img="fleche_nesw", xy=self._centre)
    def fleche_ns(self): return self.CUR(img="fleche_ns", xy=self._centre)
    def fleche_nwse(self): return self.CUR(img="fleche_nwse", xy=self._centre)
    def fleche_top(self): return self.CUR(img="fleche_top", xy=self._fleche_top)
    def fleche_tout(self): return self.CUR(img="fleche_tout", xy=self._centre)
    def fleche_we(self): return self.CUR(img="fleche_we", xy=self._centre)
    def ibeam(self): return self.CUR(img="ibeam", xy=self._centre)
    def infos(self): return self.CUR(img="infos", xy=self._souris)
    def main(self): return self.CUR(img="main", xy=self._souris)
    def non(self): return self.CUR(img="non", xy=self._centre)
    def retour(self): return self.CUR(img="retour", xy=self._souris)
    def souris(self): return self.CUR(img="souris", xy=self._souris)
    def souris_main(self): return self.CUR(img="souris_main", xy=self._souris)
    def souris_non(self): return self.CUR(img="souris_non", xy=self._souris)
