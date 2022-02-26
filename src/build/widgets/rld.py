import importlib

from . import VBase
importlib.reload(VBase)

from .classes import CheckBox, ComboBox, DateEdit, Frame, Label, \
    ListWidget, ProgressBar, RadioButton, ScrollArea, Slider, \
    SpinBox, TableWidget, TextEdit, ToolBox, TrayIcon, TreeWidget, PushButton

importlib.reload(CheckBox)
importlib.reload(ComboBox)
importlib.reload(DateEdit)
importlib.reload(Frame)
importlib.reload(Label)
importlib.reload(ListWidget)
importlib.reload(ProgressBar)
importlib.reload(PushButton)
importlib.reload(RadioButton)
importlib.reload(ScrollArea)
importlib.reload(Slider)
importlib.reload(SpinBox)
importlib.reload(TableWidget)
importlib.reload(TextEdit)
importlib.reload(ToolBox)
importlib.reload(TrayIcon)
importlib.reload(TreeWidget)
