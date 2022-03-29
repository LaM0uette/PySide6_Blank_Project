from .MyQPushButton import MyQPushButton
from .ClassePb import ClassePb
from src.build.mods import Functions
from src.lib.globals import v_wg
from src.lib.palettes import *


class Style(MyQPushButton):
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

            auto_default=False,
            default=False,
            flat=True,

            pb_type=None,
            background=v_wg.BACKGROUND,
            foreground=v_wg.FOREGROUND,
            img=v_wg.IMG,
            border=v_wg.BORDER
    ):
        super().__init__(widget,size_policy,dim,font,cursor,focus_policy,layout_direction,txt,ico,checkable,checked,auto_actions,auto_default,default,flat)

        # Style
        style = f"""
                /* BUTTON */
                QPushButton {{
                background-color: rgba{background.base};
                color: rgba{foreground.base};
                }}
                QPushButton:hover {{
                background-color: rgba{background.hover};
                color: rgba{foreground.hover};
                }}
                QPushButton:checked {{
                background-color: rgba{background.checked};
                color: rgba{foreground.checked};
                }}
                QPushButton:checked:hover {{
                background-color: rgba{background.checked_hover};
                color: rgba{foreground.checked_hover};
                }}
                QPushButton:pressed {{
                background-color: rgba{background.pressed};
                color: rgba{foreground.pressed};
                }}
                QPushButton:checked:pressed {{
                background-color: rgba{background.checked_pressed};
                color: rgba{foreground.checked_pressed};
                }}

                /* BORDURES */
                .QPushButton {{
                border-top: {border.base[0]}px {border.base_style} rgba{border.base_rgb};
                border-bottom: {border.base[1]}px {border.base_style} rgba{border.base_rgb};
                border-right: {border.base[2]}px {border.base_style} rgba{border.base_rgb};
                border-left: {border.base[3]}px {border.base_style} rgba{border.base_rgb};
                }}
                .QPushButton:hover {{
                border-top: {border.hover[0]}px {border.hover_style} rgba{border.hover_rgb};
                border-bottom: {border.hover[1]}px {border.hover_style} rgba{border.hover_rgb};
                border-right: {border.hover[2]}px {border.hover_style} rgba{border.hover_rgb};
                border-left: {border.hover[3]}px {border.hover_style} rgba{border.hover_rgb};
                }}
                .QPushButton:checked {{
                border-top: {border.checked[0]}px {border.checked_style} rgba{border.checked_rgb};
                border-bottom: {border.checked[1]}px {border.checked_style} rgba{border.checked_rgb};
                border-right: {border.checked[2]}px {border.checked_style} rgba{border.checked_rgb};
                border-left: {border.checked[3]}px {border.checked_style} rgba{border.checked_rgb};
                }}
                .QPushButton:checked:hover {{
                border-top: {border.checked_hover[0]}px {border.checked_hover_style} rgba{border.checked_hover_rgb};
                border-bottom: {border.checked_hover[1]}px {border.checked_hover_style} rgba{border.checked_hover_rgb};
                border-right: {border.checked_hover[2]}px {border.checked_hover_style} rgba{border.checked_hover_rgb};
                border-left: {border.checked_hover[3]}px {border.checked_hover_style} rgba{border.checked_hover_rgb};
                }}

                /* RAYONS */
                .QPushButton {{
                border-top-right-radius: {border.radius[0]}px;
                border-top-left-radius: {border.radius[1]}px;
                border-bottom-right-radius: {border.radius[2]}px;
                border-bottom-left-radius: {border.radius[3]}px;
                }}"""
        widget.setStyleSheet(style)

        # Classes PB
        ht = dim.fixed_height or widget.height()
        img_height = ht * PaStyleBase.x_ico
        IMG_HEIGHT = ht * PaStyleBase.X_ICO

        cls = ClassePb(
            widget=widget,
            dim_ico=img_height,
            DIM_ICO=IMG_HEIGHT,
            img=img.base,
            img_hover=img.base_hover,
            img_uncheck=img.uncheck,
            img_uncheck_hover=img.uncheck_hover,
            img_check=img.check,
            img_check_hover=img.check_hover,
            img_rgb=img.base_rgb,
            img_hover_rgb=img.base_hover_rgb,
            img_uncheck_rgb=img.uncheck_rgb,
            img_uncheck_hover_rgb=img.uncheck_hover_rgb,
            img_check_rgb=img.check_rgb,
            img_check_hover_rgb=img.check_hover_rgb,
        )

        if pb_type is not None:
            if pb_type == "check":
                widget.setIcon(Functions().SET_ICON(ico=img.uncheck, rgb=img.uncheck_rgb))
            else:
                widget.setIcon(Functions().SET_ICON(ico=img.base, rgb=img.base_rgb))

            widget.setIconSize(Functions().SET_ICON_DIM(width=img_height, height=img_height))

        if pb_type == "check":
            widget.enterEvent = cls.ENT_CHECK
            widget.leaveEvent = cls.LVE_CHECK
            widget.mousePressEvent = cls.MP_CHECK
        elif pb_type == "ico":
            widget.enterEvent = cls.ENT_ICO
            widget.leaveEvent = cls.LVE_ICO
            widget.mousePressEvent = cls.MP_ICO
        elif pb_type == "zoom":
            widget.enterEvent = cls.ENT_ZOOM
            widget.leaveEvent = cls.LVE_ZOOM
