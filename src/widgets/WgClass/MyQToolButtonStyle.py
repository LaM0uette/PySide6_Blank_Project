from .MyQToolButton import MyQToolButton
from src.lib.globals import v_wg


class Style(MyQToolButton):
    def __init__(
            self,
            widget,
            size_policy=v_wg.SIZE_POLICY,
            dim=v_wg.DIM_WG,
            font=v_wg.FONT,
            cursor=v_wg.CUR_ACTION,
            focus_policy=v_wg.FOCUS_POLICY,
            layout_direction=v_wg.LAYOUT_DIRECTION,

            txt=v_wg.TXT,
            ico=v_wg.ICO,
            checkable=False,
            checked=False,
            auto_actions=v_wg.AUTO_ACTIONS,

            popup_mode=v_wg.POPUP_MODE,
            tool_button_style=v_wg.TOOL_BUTTON_STYLE,
            auto_raise=False,
            arrow_type=v_wg.ARROW_TYPE,

            background=v_wg.BACKGROUND,
            foreground=v_wg.FOREGROUND,
            img=v_wg.IMG,
            border=v_wg.BORDER,
    ):
        # Style
        super().__init__(widget, size_policy, dim, font, cursor, focus_policy, layout_direction, txt, ico, checkable, checked, auto_actions, popup_mode, tool_button_style, auto_raise, arrow_type)
        style = f"""
                /* BUTTON */
                QToolButton {{
                background-color: rgba{background.base};
                color: rgba{foreground.base};
                }}
                QToolButton:hover {{
                background-color: rgba{background.hover};
                color: rgba{foreground.hover};
                }}
                QToolButton:checked {{
                background-color: rgba{background.checked};
                color: rgba{foreground.checked};
                }}
                QToolButton:checked:hover {{
                background-color: rgba{background.checked_hover};
                color: rgba{foreground.checked_hover};
                }}
                QToolButton:pressed {{
                background-color: rgba{background.pressed};
                color: rgba{foreground.pressed};
                }}
                QToolButton:checked:pressed {{
                background-color: rgba{background.checked_pressed};
                color: rgba{foreground.checked_pressed};
                }}
                
                QToolButton::menu-indicator {{
                image: url({f"{img.base}{img.base_rgb}.svg"});
                }}

                /* BORDURES */
                .QToolButton {{
                border-top: {border.base[0]}px {border.base_style} rgba{border.base_rgb};
                border-bottom: {border.base[1]}px {border.base_style} rgba{border.base_rgb};
                border-right: {border.base[2]}px {border.base_style} rgba{border.base_rgb};
                border-left: {border.base[3]}px {border.base_style} rgba{border.base_rgb};
                }}
                .QToolButton:hover {{
                border-top: {border.hover[0]}px {border.hover_style} rgba{border.hover_rgb};
                border-bottom: {border.hover[1]}px {border.hover_style} rgba{border.hover_rgb};
                border-right: {border.hover[2]}px {border.hover_style} rgba{border.hover_rgb};
                border-left: {border.hover[3]}px {border.hover_style} rgba{border.hover_rgb};
                }}
                .QToolButton:checked {{
                border-top: {border.checked[0]}px {border.checked_style} rgba{border.checked_rgb};
                border-bottom: {border.checked[1]}px {border.checked_style} rgba{border.checked_rgb};
                border-right: {border.checked[2]}px {border.checked_style} rgba{border.checked_rgb};
                border-left: {border.checked[3]}px {border.checked_style} rgba{border.checked_rgb};
                }}
                .QToolButton:checked:hover {{
                border-top: {border.checked_hover[0]}px {border.checked_hover_style} rgba{border.checked_hover_rgb};
                border-bottom: {border.checked_hover[1]}px {border.checked_hover_style} rgba{border.checked_hover_rgb};
                border-right: {border.checked_hover[2]}px {border.checked_hover_style} rgba{border.checked_hover_rgb};
                border-left: {border.checked_hover[3]}px {border.checked_hover_style} rgba{border.checked_hover_rgb};
                }}

                /* RAYONS */
                .QToolButton {{
                border-top-right-radius: {border.radius[0]}px;
                border-top-left-radius: {border.radius[1]}px;
                border-bottom-right-radius: {border.radius[2]}px;
                border-bottom-left-radius: {border.radius[3]}px;
                }}"""
        widget.setStyleSheet(style)
