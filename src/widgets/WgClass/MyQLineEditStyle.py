from PySide6 import QtGui

from .MyQLineEdit import MyQLineEdit
from src.lib.globals import v_wg
from src.lib.palettes import *


class Style(MyQLineEdit):
    def __init__(
            self,
            widget,
            size_policy=v_wg.SIZE_POLICY,
            dim=v_wg.DIM_WG,
            font=v_wg.FONT,
            cursor=PaCur.IBEAM,
            focus_policy=PaFocusPolicy.STRONG,
            layout_direction=v_wg.LAYOUT_DIRECTION,

            input_mask=PaInputMask.NO,
            max_length=32767,
            frame=False,
            echo_mode=PaEchoMode.NORMAL,
            align=DcAlign.Base,
            drag_enabled=False,
            read_only=False,
            clear_button=False,

            background=v_wg.BACKGROUND,
            foreground=v_wg.FOREGROUND,
            border=v_wg.BORDER,
    ):
        super().__init__(widget,size_policy,dim,font,cursor,focus_policy,layout_direction,input_mask,max_length,frame,echo_mode,align,drag_enabled,read_only,clear_button)

        style = f"""
                /* WIDGET */
                QLineEdit {{
                background-color: rgba{background.base};
                selection-background-color: rgba{background.selection};
                selection-color: rgba{foreground.selection};
                }}

                /* BORDURES */
                QLineEdit {{
                border-top: {border.base[0]}px {border.base_style} rgba{border.base_rgb};
                border-bottom: {border.base[1]}px {border.base_style} rgba{border.base_rgb};
                border-right: {border.base[2]}px {border.base_style} rgba{border.base_rgb};
                border-left: {border.base[3]}px {border.base_style} rgba{border.base_rgb};
                }}
                QLineEdit:hover {{
                border-top: {border.hover[0]}px {border.hover_style} rgba{border.hover_rgb};
                border-bottom: {border.hover[1]}px {border.hover_style} rgba{border.hover_rgb};
                border-right: {border.hover[2]}px {border.hover_style} rgba{border.hover_rgb};
                border-left: {border.hover[3]}px {border.hover_style} rgba{border.hover_rgb};
                }}

                /* RAYONS */
                QLineEdit {{
                border-top-right-radius: {border.radius[0]}px;
                border-top-left-radius: {border.radius[1]}px;
                border-bottom-right-radius: {border.radius[2]}px;
                border-bottom-left-radius: {border.radius[3]}px;
                }}"""
        widget.setStyleSheet(style)

        palette_txt = QtGui.QPalette()
        palette_txt.setColor(QtGui.QPalette.Text, QtGui.QColor(*foreground.base))
        palette_txt.setColor(QtGui.QPalette.PlaceholderText, QtGui.QColor(*foreground.placeholder))
        widget.setPalette(palette_txt)

        widget.setFont(font)
