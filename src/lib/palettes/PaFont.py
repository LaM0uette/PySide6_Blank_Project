from PySide6 import QtGui

from src.config.config import Config


class FontSize:
    H1 = 32
    H2 = 24
    H3 = 16
    H4 = 12
    H5 = 8
class PaFont:

    @staticmethod
    def __gen_font(family=Config.font, size=FontSize.H4):
        ft = QtGui.QFont()
        ft.setFamily(family)
        ft.setPointSize(size)
        return ft

    H1 = 32  # A SUPPRIMER
    H2 = 24  # A SUPPRIMER
    H3 = 16  # A SUPPRIMER
    H4 = 12  # A SUPPRIMER
    H5 = 8  # A SUPPRIMER

    TITRE = __gen_font(size=FontSize.H1)
    HH2 = __gen_font(size=FontSize.H2)
    HH3 = __gen_font(size=FontSize.H3)
    BASE = __gen_font(size=FontSize.H4)
    TEXTE = __gen_font(size=FontSize.H5)
