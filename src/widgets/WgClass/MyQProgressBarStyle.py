from .MyQProgressBar import MyQProgressBar
from src.lib.globals import v_wg
from src.lib.palettes import *


class Style(MyQProgressBar):
    def __init__(
            self,
            widget,
            size_policy=v_wg.SIZE_POLICY,
            dim=v_wg.DIM_WG,
            font=v_wg.FONT,
            cursor=v_wg.CUR_ACTION,
            focus_policy=v_wg.FOCUS_POLICY,
            layout_direction=v_wg.LAYOUT_DIRECTION,

            value=DcValue.Base,
            align=DcAlign.Base,
            text_visible=True,
            progress_format=PaProgressFormat.VALUE,

            background=v_wg.BACKGROUND,
            background_progress=DcRgbProgress.Base,
            foreground=v_wg.FOREGROUND,
            padding=(0,) * 4,
            border=v_wg.BORDER,
            border_chunk=v_wg.BORDER
    ):
        super().__init__(widget,size_policy,dim,font,cursor,focus_policy,layout_direction,value,align,text_visible,progress_format)

        style = f"""
                /* PROGRESSBAR */
                QProgressBar {{
                background-color: rgba{background.base};
                color: rgba{foreground.base};
                }}

                /* PROGRESS */
                QProgressBar::chunk {{
                background-color: rgba{background_progress.chunk};
                border-top-right-radius: {border_chunk.radius[0]}px;
                border-top-left-radius: {border_chunk.radius[1]}px;
                border-bottom-right-radius: {border_chunk.radius[2]}px;
                border-bottom-left-radius: {border_chunk.radius[3]}px;
                }}
                QProgressBar::chunk:hover {{
                background-color: rgba{background_progress.chunk_hover};
                }}

                /* BORDURES */
                .QProgressBar {{
                border-top: {border.base[0]}px {border.base_style} rgba{border.base_rgb};
                border-bottom: {border.base[1]}px {border.base_style} rgba{border.base_rgb};
                border-right: {border.base[2]}px {border.base_style} rgba{border.base_rgb};
                border-left: {border.base[3]}px {border.base_style} rgba{border.base_rgb};
                padding-top: {padding[0]}px;
                padding-bottom: {padding[1]}px;
                padding-right: {padding[2]}px;
                padding-left: {padding[3]}px;
                }}
                .QProgressBar:hover {{
                border-top: {border.hover[0]}px {border.hover_style} rgba{border.hover_rgb};
                border-bottom: {border.hover[1]}px {border.hover_style} rgba{border.hover_rgb};
                border-right: {border.hover[2]}px {border.hover_style} rgba{border.hover_rgb};
                border-left: {border.hover[3]}px {border.hover_style} rgba{border.hover_rgb};
                }}

                /* RAYONS */
                .QProgressBar {{
                border-top-right-radius: {border.radius[0]}px;
                border-top-left-radius: {border.radius[1]}px;
                border-bottom-right-radius: {border.radius[2]}px;
                border-bottom-left-radius: {border.radius[3]}px;
                }}"""
        widget.setStyleSheet(style)