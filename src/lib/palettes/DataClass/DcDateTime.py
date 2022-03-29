"""
DcDateTime.%class(
    date: tuple = (%, %, %)
    time: tuple = (%, %, %))
"""
import datetime
from dataclasses import dataclass

from PySide6 import QtCore
@dataclass
class Base:

    d = datetime.datetime.now().strftime("%Y_%m_%d").split("_")
    y, m, d = int(d[0]), int(d[1]), int(d[2])

    date: tuple = QtCore.QDate(y, m, d)
    time: tuple = QtCore.QTime(0, 0, 0)
    date_time: tuple = QtCore.QDateTime(y, m, d, 0, 0, 0)
