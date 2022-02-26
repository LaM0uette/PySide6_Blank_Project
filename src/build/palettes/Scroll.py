from PySide6 import QtCore


class Scroll:

    def need(self): return QtCore.Qt.ScrollBarAsNeeded
    def on(self): return QtCore.Qt.ScrollBarAlwaysOn
    def off(self): return QtCore.Qt.ScrollBarAlwaysOff
