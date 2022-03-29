import json
import os

from src.config.config import Config


class PaCur:

    @staticmethod
    def __cursor(img, xy):
        return [f"assets/cursor/{Config.cur}/{img}.cur", xy[0], xy[1]]

    with open(f"{os.path.dirname(f'assets/cursor/{Config.cur}/_data.json')}/_data.json", "r", encoding="utf-8") as fichier:
        cur = json.load(fichier)

    _souris = cur["_souris"]
    _centre = cur["_centre"]
    _crayon = cur["_crayon"]
    _fleche_top = cur["_fleche_top"]

    AGRANDIR = __cursor("agrandir", _souris)
    COPIER = __cursor("copier", _souris)
    CRAYON = __cursor("crayon", _crayon)
    CROIX = __cursor("croix", _centre)
    FLECHE_NESW = __cursor("fleche_nesw", _centre)
    FLECHE_NS = __cursor("fleche_ns", _centre)
    FLECHE_NWSE = __cursor("fleche_nwse", _centre)
    FLECHE_TOP = __cursor("fleche_top", _fleche_top)
    FLECHE_MOVE = __cursor("fleche_move", _centre)
    FLECHE_WE = __cursor("fleche_we", _centre)
    IBEAM = __cursor("ibeam", _centre)
    INFOS = __cursor("infos", _souris)
    MAIN = __cursor("main", _souris)
    NON = __cursor("non", _centre)
    RETOUR = __cursor("retour", _souris)
    SOURIS = __cursor("souris", _souris)
    SOURIS_MAIN = __cursor("souris_main", _souris)
    SOURIS_NON = __cursor("souris_non", _souris)
