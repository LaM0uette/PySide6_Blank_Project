import json

from src.config.config import Config


class PaRgb:

    @staticmethod
    def __get_rgb(val):
        with open(fr"theme/{Config.theme}.json", "r") as fichier:
            js = json.load(fichier)
            return tuple(js[val])

    @staticmethod
    def __rgb_to_hex(rgb):
        return "#" + "%02x%02x%02x" % rgb

    TH1 = __get_rgb(val="th1") + (255,)
    TH2 = __get_rgb(val="th2") + (255,)
    TH3 = __get_rgb(val="th3") + (255,)
    BN1 = __get_rgb(val="bn1") + (255,)
    BN2 = __get_rgb(val="bn2") + (255,)
    TR = 0, 0, 0, 0

    HX_TH1 = __rgb_to_hex(__get_rgb(val="th1"))
    HX_TH2 = __rgb_to_hex(__get_rgb(val="th2"))
    HX_TH3 = __rgb_to_hex(__get_rgb(val="th3"))
    HX_BN1 = __rgb_to_hex(__get_rgb(val="bn1"))
    HX_BN2 = __rgb_to_hex(__get_rgb(val="bn2"))
