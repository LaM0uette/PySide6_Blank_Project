from .MyQSpinBox import MyQSpinBox
from src.lib.globals import v_wg
from src.lib.palettes import *


class Style(MyQSpinBox):
    def __init__(
            self,
            widget,
            size_policy=v_wg.SIZE_POLICY,
            dim=v_wg.DIM_WG,
            font=v_wg.FONT,
            cursor=v_wg.CUR_ACTION,
            focus_policy=v_wg.FOCUS_POLICY,
            layout_direction=v_wg.LAYOUT_DIRECTION,

            wrapping=False,
            frame=False,
            align=DcAlign.Base,
            read_only=False,
            button_symbols=PaButtonSymbols.PLUS_MINUS,
            accelerated=True,

            suffix="",
            prefix="",
            value=v_wg.VALUE,
            integer_base=10,

            background=v_wg.BACKGROUND,
            foreground=v_wg.FOREGROUND,
            img=v_wg.IMG,
            img_up_pos=(3, 0, 3, 0),
            img_down_pos=(0, 3, 3, 0),
            border=v_wg.BORDER,
    ):
        super().__init__(widget,size_policy,dim,font,cursor,focus_policy,layout_direction,wrapping,frame,align,read_only,button_symbols,accelerated,suffix,prefix,value,integer_base)

        style = f"""
                        /* SPINBOX */
                        QSpinBox {{
                        background-color: rgba{background.base};
                        color: rgba{foreground.base};
                        selection-background-color: rgba{background.selection};
                        selection-color: rgba{foreground.selection}
                        }}

                        QSpinBox::up-button {{
                        subcontrol-position: top right;
                        top: {img_up_pos[0]}px;
                        bottom: {img_up_pos[1]}px;
                        right: {img_up_pos[2]}px;
                        left: {img_up_pos[3]}px;
                        image: url({f"{img.up}{img.up_rgb}.svg"});
                        width: {img.width/2}px;
                        height: {img.height/2}px;
                        }}
                        QSpinBox::up-button:hover {{
                        image: url({f"{img.up_hover}{img.up_hover_rgb}.svg"});
                        }}

                        QSpinBox::down-button {{
                        subcontrol-position: bottom right;
                        top: {img_down_pos[0]}px;
                        bottom: {img_down_pos[1]}px;
                        right: {img_down_pos[2]}px;
                        left: {img_down_pos[3]}px;
                        image: url({f"{img.down}{img.down_rgb}.svg"});
                        width: {img.width/2}px;
                        height: {img.height/2}px;
                        }}
                        QSpinBox::down-button:hover {{
                        image: url({f"{img.down_hover}{img.down_hover_rgb}.svg"});
                        }}

                        /* BORDURES */
                        .QSpinBox {{
                        border-top: {border.base[0]}px {border.base_style} rgba{border.base_rgb};
                        border-bottom: {border.base[1]}px {border.base_style} rgba{border.base_rgb};
                        border-right: {border.base[2]}px {border.base_style} rgba{border.base_rgb};
                        border-left: {border.base[3]}px {border.base_style} rgba{border.base_rgb};
                        }}
                        .QSpinBox:hover {{
                        border-top: {border.hover[0]}px {border.hover_style} rgba{border.hover_rgb};
                        border-bottom: {border.hover[1]}px {border.hover_style} rgba{border.hover_rgb};
                        border-right: {border.hover[2]}px {border.hover_style} rgba{border.hover_rgb};
                        border-left: {border.hover[3]}px {border.hover_style} rgba{border.hover_rgb};
                        }}

                        /* RAYONS */
                        .QSpinBox {{
                        border-top-right-radius: {border.radius[0]}px;
                        border-top-left-radius: {border.radius[1]}px;
                        border-bottom-right-radius: {border.radius[2]}px;
                        border-bottom-left-radius: {border.radius[3]}px;
                        }}"""
        widget.setStyleSheet(style)
"""
"lr":
QSpinBox::up-button, QDoubleSpinBox::up-button  {{
subcontrol-origin: margin;
subcontrol-position: center right;
right: {(dim_h - (dim_h  * P_style().x_ico())) / 2}px;
image: url({pb_up + tm + ".svg"});
height: {dim_h * P_style().x_ico() / 1.6}px;
width: {dim_h * P_style().x_ico() / 1.6}px;
}}

QSpinBox::down-button, QDoubleSpinBox::down-button  {{
subcontrol-origin: margin;
subcontrol-position: center left;
left: {(dim_h - (dim_h  * P_style().x_ico())) / 2}px;
image: url({pb_down + tm + ".svg"});
height: {dim_h * P_style().x_ico() / 1.6}px;
width: {dim_h * P_style().x_ico() / 1.6}px;
}}
"""