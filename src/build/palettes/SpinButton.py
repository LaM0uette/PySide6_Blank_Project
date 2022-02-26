from PySide6 import QtWidgets


class SpinButton:

    def no_button(self): return QtWidgets.QAbstractSpinBox.NoButtons
    def plus_minus(self): return QtWidgets.QAbstractSpinBox.PlusMinus
    def up_down(self): return QtWidgets.QAbstractSpinBox.UpDownArrows
