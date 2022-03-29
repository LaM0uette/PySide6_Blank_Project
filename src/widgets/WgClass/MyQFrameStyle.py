from .MyQFrame import MyQFrame
from src.lib.globals import v_wg
from src.lib.palettes import *


class Style(MyQFrame):
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

            background=DcRgbBg.Base(gen=PaRgb.TH3),
            border=v_wg.BORDER
    ):
        # Style
        super().__init__(widget, size_policy, dim, font, cursor, focus_policy, layout_direction, frame)

        style = f"""
                /* FRAME */
                .QFrame {{
                background-color: rgba{background.base};
                }}
                .QFrame:hover {{
                background-color: rgba{background.hover};
                }}

                /* BORDURES */
                .QFrame {{
                border-top: {border.base[0]}px {border.base_style} rgba{border.base_rgb};
                border-bottom: {border.base[1]}px {border.base_style} rgba{border.base_rgb};
                border-right: {border.base[2]}px {border.base_style} rgba{border.base_rgb};
                border-left: {border.base[3]}px {border.base_style} rgba{border.base_rgb};
                }}
                .QFrame:hover {{
                border-top: {border.hover[0]}px {border.hover_style} rgba{border.hover_rgb};
                border-bottom: {border.hover[1]}px {border.hover_style} rgba{border.hover_rgb};
                border-right: {border.hover[2]}px {border.hover_style} rgba{border.hover_rgb};
                border-left: {border.hover[3]}px {border.hover_style} rgba{border.hover_rgb};
                }}

                /* RAYONS */
                .QFrame {{
                border-top-right-radius: {border.radius[0]}px;
                border-top-left-radius: {border.radius[1]}px;
                border-bottom-right-radius: {border.radius[2]}px;
                border-bottom-left-radius: {border.radius[3]}px;
                }}"""
        widget.setStyleSheet(style)
