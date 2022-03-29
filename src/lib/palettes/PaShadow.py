from functools import partial

from PySide6 import QtWidgets, QtGui


class PaShadow:

    @staticmethod
    def __get_shadow(wg, blur_radius: int, rgba: tuple, offset: list):
        shadow = QtWidgets.QGraphicsDropShadowEffect(wg)
        shadow.setBlurRadius(blur_radius)
        shadow.setColor(QtGui.QColor(*rgba))
        shadow.setOffset(offset[0], offset[1])
        return shadow

    __R, __G, __B = 0, 0, 0

    GLOW = partial(__get_shadow, blur_radius=8, rgba=(__R, __G, __B, 255), offset=[0, 0])
    PRESPECTIVE = partial(__get_shadow, blur_radius=6, rgba=(__R, __G, __B, 150), offset=[3, 3])
    OMBRE_PORTEE = partial(__get_shadow, blur_radius=12, rgba=(__R, __G, __B, 150), offset=[0, 0])
