from PySide6 import QtCore, QtWidgets

from ....build import *
from ....build.widgets import VBase

class Style:
    def __init__(
            self,
            *wgs,
            wg_type=VBase.SB_BUTTONS_TYPE,
            width=VBase.WG_WIDTH,
            height=VBase.WG_HEIGHT,
            font=VBase.FONT,
            font_size=VBase.FONT_SIZE,
            no_focus=VBase.NO_FOCUS,
            value_min=VBase.VAL_MIN,
            value_max=VBase.VAL_MAX,
            value_step=VBase.VAL_STEP,
            align_horizontal=Align().h_center(),
            align_vertical=Align().v_center(),
            curseur=VBase.CUR,
            curseur_le=VBase.CUR_LE,

            # Couleurs BG
            bg=VBase.BG,
            bg_selection=VBase.BG_SELECTION,
            # Couleurs FG
            fg=VBase.FG,
            fg_selection=VBase.FG_SELECTION,

            # Images
            img_up=VBase.IMG_UP,
            img_down=VBase.IMG_DOWN,
            # Images RGB
            img_up_rgb=VBase.IMG_UP_RGB,
            img_down_rgb=VBase.IMG_DOWN_RGB,
            # Images DIM
            img_up_width=10,
            img_up_height=10,
            img_down_width=10,
            img_down_height=10,
            # Images positions
            img_up_dim=((0,) * 4),
            img_down_dim=((0,) * 4),


            # Bordures
            border=VBase.WG_BORDER_WIDTH,
            border_style=VBase.WG_BORDER_STYLE,
            border_rgb=VBase.WG_BORDER_RGB,
            # Bordures hover
            border_hover=VBase.WG_BORDER_WIDTH,
            border_hover_style=VBase.WG_BORDER_STYLE,
            border_hover_rgb=VBase.WG_BORDER_RGB,

            # Rayons
            radius=VBase.WG_RADIUS,
    ):
        style = f"""
                /* SPINBOX */
                QSpinBox, QDoubleSpinBox {{
                background-color: rgba{bg};
                color: rgba{fg};
                selection-background-color: rgba{bg_selection};
                selection-color: rgba{fg_selection}
                }}
        
                QSpinBox::up-button, QDoubleSpinBox::up-button  {{
                subcontrol-position: top right;
                top: {img_up_dim[0]}px;
                bottom: {img_up_dim[1]}px;
                right: {img_up_dim[2]}px;
                left: {img_up_dim[3]}px;
                image: url({f"{img_up}{img_up_rgb}.svg"});
                width: {img_up_width}px;
                height: {img_up_height}px;
                }}
        
                QSpinBox::down-button, QDoubleSpinBox::down-button  {{
                subcontrol-position: bottom right;
                top: {img_down_dim[0]}px;
                bottom: {img_down_dim[1]}px;
                right: {img_down_dim[2]}px;
                left: {img_down_dim[3]}px;
                image: url({f"{img_down}{img_down_rgb}.svg"});
                width: {img_down_width}px;
                height: {img_down_height}px;
                }}
        
                /* BORDURES */
                .QSpinBox, .QDoubleSpinBox {{
                border-top: {border[0]}px {border_style} rgba{border_rgb};
                border-bottom: {border[1]}px {border_style} rgba{border_rgb};
                border-right: {border[2]}px {border_style} rgba{border_rgb};
                border-left: {border[3]}px {border_style} rgba{border_rgb};
                }}
                .QSpinBox:hover, .QDoubleSpinBox:hover {{
                border-top: {border_hover[0]}px {border_hover_style} rgba{border_hover_rgb};
                border-bottom: {border_hover[1]}px {border_hover_style} rgba{border_hover_rgb};
                border-right: {border_hover[2]}px {border_hover_style} rgba{border_hover_rgb};
                border-left: {border_hover[3]}px {border_hover_style} rgba{border_hover_rgb};
                }}
                
                /* RAYONS */
                .QSpinBox, .QDoubleSpinBox {{
                border-top-right-radius: {radius[0]}px;
                border-top-left-radius: {radius[1]}px;
                border-bottom-right-radius: {radius[2]}px;
                border-bottom-left-radius: {radius[3]}px;
                }}"""

        for wg in wgs:
            wg.setStyleSheet(style)

            try: Fct(wg=wg, w=width, h=height).DIM()
            except: pass

            wg.setFont(Fct(font=font, font_size=font_size).FONT())

            wg.setAlignment(align_horizontal | align_vertical)

            wg.setMinimum(value_min)
            wg.setMaximum(value_max)
            wg.setSingleStep(value_step)

            wg.setFrame(QtWidgets.QFrame.NoFrame)
            wg.setButtonSymbols(wg_type)
            if no_focus: wg.setFocusPolicy(QtCore.Qt.NoFocus)

            wg.setCursor(Fct(cur=curseur).CUR())
            wg.lineEdit().setCursor(Fct(cur=curseur_le).CUR())


##################
##     BASE     ##
##################
class Plus_moins_th(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
        )
class Plus_moins_tr(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            no_focus=True,

            bg=Rgb().tr(),
            fg=Rgb().th3(),
    )
class Up_down_th(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            img_up=Img().fleche_top(),
            img_down=Img().fleche_bottom(),

    )
class Up_down_tr(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            no_focus=True,

            bg=Rgb().tr(),
            fg=Rgb().th3(),
            img_up=Img().fleche_top(),
            img_down=Img().fleche_bottom(),
    )

class rgb_bd_th3(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            value_max=255,

            border=((StyleBase().bd(),) * 4),
            border_hover=((StyleBase().bd(),) * 4),
            border_rgb=Rgb().th3(),
            border_hover_rgb=Rgb().th3(),
        )
class Plus_moins_bd_th3(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,

            border=((StyleBase().bd(),) * 4),
            border_hover=((StyleBase().bd(),) * 4),
            border_rgb=Rgb().th3(),
            border_hover_rgb=Rgb().th3(),
    )
class Plus_moins_inf_bd_th3(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            value_max=999999,

            border=((StyleBase().bd(),) * 4),
            border_hover=((StyleBase().bd(),) * 4),
            border_rgb=Rgb().th3(),
            border_hover_rgb=Rgb().th3(),
        )

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
