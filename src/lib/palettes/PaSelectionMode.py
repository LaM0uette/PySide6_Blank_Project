from PySide6.QtWidgets import QAbstractItemView


class PaSelectionMode:

    NO = QAbstractItemView.NoSelection
    SINGLE = QAbstractItemView.SingleSelection
    MULTI = QAbstractItemView.MultiSelection
    EXTENDED = QAbstractItemView.ExtendedSelection
    CONTIGUOUS = QAbstractItemView.ContiguousSelection
