from PySide6 import QtWidgets


class SelectionBehavior:

    def item(self): return QtWidgets.QAbstractItemView.SelectItems
    def row(self): return QtWidgets.QAbstractItemView.SelectRows
    def column(self): return QtWidgets.QAbstractItemView.SelectColumns
