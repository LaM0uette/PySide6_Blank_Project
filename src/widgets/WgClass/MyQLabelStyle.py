from .MyQLabel import MyQLabel
from src.lib.globals import v_wg
from ...lib.palettes import *


class Style(MyQLabel):
    def __init__(
            self,
            widget,
            size_policy=v_wg.SIZE_POLICY,
            dim=v_wg.DIM,
            font=v_wg.FONT,
            cursor=v_wg.CUR,
            focus_policy=v_wg.FOCUS_POLICY,
            layout_direction=v_wg.LAYOUT_DIRECTION,

            frame=v_wg.FRAME,

            text_format=PaTextFormat.PLAIN,
            pixmap=None,
            pixmap_rgb="",
            scaled_contents=True,
            align=DcAlign.Base(horizontal=PaAlign.LEFT),
            word_wrap=True,
            indent=0,
            open_external_link=False,

            background=v_wg.BACKGROUND,
            foreground=v_wg.FOREGROUND,
            margin=(0,) * 4,
            padding=(0,) * 4,
            border=v_wg.BORDER,
    ):
        super().__init__(widget, size_policy, dim, font, cursor, focus_policy, layout_direction, frame,text_format,pixmap,pixmap_rgb,scaled_contents,align,word_wrap,indent,open_external_link)

        style = f"""
                /* LABEL */
                .QLabel {{
                background-color: rgba{background.base};
                color: rgba{foreground.base};
                margin-top: {margin[0]}px;
                margin-bottom: {margin[1]}px;
                margin-right: {margin[2]}px;
                margin-left: {margin[3]}px;
                padding-top: {padding[0]}px;
                padding-bottom: {padding[1]}px;
                padding-right: {padding[2]}px;
                padding-left: {padding[3]}px;
                }}
                .QLabel:hover {{
                background-color: rgba{background.hover};
                color: rgba{foreground.hover};
                }}

                /* BORDURES */
                .QLabel {{
                border-top: {border.base[0]}px {border.base_style} rgba{border.base_rgb};
                border-bottom: {border.base[1]}px {border.base_style} rgba{border.base_rgb};
                border-right: {border.base[2]}px {border.base_style} rgba{border.base_rgb};
                border-left: {border.base[3]}px {border.base_style} rgba{border.base_rgb};
                }}
                .QLabel:hover {{
                border-top: {border.hover[0]}px {border.hover_style} rgba{border.hover_rgb};
                border-bottom: {border.hover[1]}px {border.hover_style} rgba{border.hover_rgb}
                border-right: {border.hover[2]}px {border.hover_style} rgba{border.hover_rgb};
                border-left: {border.hover[3]}px {border.hover_style} rgba{border.hover_rgb};
                }}

                /* RAYONS */
                .QLabel {{
                border-top-right-radius: {border.radius[0]}px;
                border-top-left-radius: {border.radius[1]}px;
                border-bottom-right-radius: {border.radius[2]}px;
                border-bottom-left-radius: {border.radius[3]}px;
                }}"""
        widget.setStyleSheet(style)

        widget.setFont(font)