from .MyQScrollArea import MyQScrollArea
from src.lib.globals import v_wg


class Style(MyQScrollArea):
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

            scroll_policy=v_wg.SCROLL_POLICY,

            resizable=True,

            background=v_wg.BACKGROUND,
            border=v_wg.BORDER,

            scroll=v_wg.SCROLL,
    ):
        super().__init__(widget, size_policy, dim, font, cursor, focus_policy, layout_direction, frame, scroll_policy, resizable)

        style = f"""
                /* SCROLLAREA */
                .QScrollArea .QWidget {{
                background-color: rgba{background.base};
                }}

                /* BORDURES */
                .QScrollArea {{
                border-top: {border.base[0]}px {border.base_style} rgba{border.base_rgb};
                border-bottom: {border.base[1]}px {border.base_style} rgba{border.base_rgb};
                border-right: {border.base[2]}px {border.base_style} rgba{border.base_rgb};
                border-left: {border.base[3]}px {border.base_style} rgba{border.base_rgb};
                }}
                .QScrollArea:hover {{
                border-top: {border.hover[0]}px {border.hover_style} rgba{border.hover_rgb};
                border-bottom: {border.hover[1]}px {border.hover_style} rgba{border.hover_rgb};
                border-right: {border.hover[2]}px {border.hover_style} rgba{border.hover_rgb};
                border-left: {border.hover[3]}px {border.hover_style} rgba{border.hover_rgb};
                }}

                /* RAYONS */
                .QScrollArea {{
                border-top-right-radius: {border.radius[0]}px;
                border-top-left-radius: {border.radius[1]}px;
                border-bottom-right-radius: {border.radius[2]}px;
                border-bottom-left-radius: {border.radius[3]}px;
                }}

                /* SCROLL */
                .QScrollArea .QScrollBar {{
                background-color: rgba{scroll.bg};
                width: {scroll.width}px;
                height: {scroll.height}px;
                }}
                .QScrollArea .QScrollBar::handle:horizontal {{
                min-width: {scroll.min_width_handle}px;
                }}
                .QScrollArea .QScrollBar::handle:vertical {{
                min-height: {scroll.min_height_min_handle}px;
                }}
                .QScrollArea .QScrollBar::handle {{
                background-color: rgba{scroll.handle_fg};
                }}
                .QScrollArea .QScrollBar::handle:hover {{
                background-color: rgba{scroll.handle_fg_hover};
                }}

                .QScrollArea .QScrollBar::add-page, .QScrollArea .QScrollBar::sub-page {{
                background-color: rgba{scroll.handle_bg};
                border: none;
                }}
                .QScrollArea .QScrollBar::add-page:hover, .QScrollArea .QScrollBar::sub-page:hover {{
                background-color: rgba{scroll.handle_bg_hover};
                border: none;
                }}"""
        widget.setStyleSheet(style)
