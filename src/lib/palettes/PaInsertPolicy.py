from PySide6 import QtWidgets


class PaInsertPolicy:

    NO = QtWidgets.QComboBox.NoInsert
    TOP = QtWidgets.QComboBox.InsertAtTop
    BOTTOM = QtWidgets.QComboBox.InsertAtBottom
    CURRENT = QtWidgets.QComboBox.InsertAtCurrent
    AFTER_CURRENT = QtWidgets.QComboBox.InsertAfterCurrent
    BEFORE_CURRENT = QtWidgets.QComboBox.InsertBeforeCurrent
    ALPHABETICALLY = QtWidgets.QComboBox.InsertAlphabetically
