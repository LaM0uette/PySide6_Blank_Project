from PySide6.QtWidgets import QAbstractScrollArea


class PaSizeAdjustPolicy:

    IGNORED = QAbstractScrollArea.AdjustIgnored
    TO_CONTENTS_ON_FIRST_SHOW = QAbstractScrollArea.AdjustToContentsOnFirstShow
    TO_CONTENTS = QAbstractScrollArea.AdjustToContents
