from ....build import *
from ....build.widgets import VBase

class Style:
    def __init__(
            self,
            *wgs,
            width=VBase.WIDTH,
            height=VBase.HEIGHT,
            value_min=VBase.VAL_MIN,
            value_max=VBase.VAL_MAX,
            value_step=VBase.VAL_STEP,
            curseur=VBase.CUR,

            # Couleurs BG
            bg=VBase.BG,
            bg_groove=VBase.BG_GROOVE,
            bg_groove_2=None,
            bg_groove_hover=VBase.BG_GROOVE_HOVER,
            bg_groove_hover_2=None,
            bg_groove_pressed=VBase.BG_GROOVE_PRESSED,
            bg_groove_pressed_2=None,
            bg_handle=VBase.BG_HANDLE,
            bg_handle_hover=VBase.BG_HANDLE_HOVER,
            bg_handle_pressed=VBase.BG_HANDLE_PRESSED,
            gradient=((0, )*4),

            # Dimensions WG
            width_groove=Dim().h9(),
            height_groove=Dim().h9(),
            width_handle_h=Dim().h9(),
            height_handle_h=Dim().h9(),
            width_handle_v=Dim().h9(),
            height_handle_v=Dim().h9(),

            # Positions WG
            margin_handle_h=((0, )*4),
            margin_handle_v=((0, )*4),

            # Bordures
            border=VBase.WG_BORDER_WIDTH,
            border_style=VBase.WG_BORDER_STYLE,
            border_rgb=VBase.WG_BORDER_RGB,
            # Bordures hover
            border_hover=VBase.WG_BORDER_WIDTH,
            border_hover_style=VBase.WG_BORDER_STYLE,
            border_hover_rgb=VBase.WG_BORDER_RGB,
            # Bordures slider h
            border_handle_h=VBase.WG_BORDER_WIDTH,
            border_handle_h_style=VBase.WG_BORDER_STYLE,
            border_handle_h_rgb=VBase.WG_BORDER_RGB,
            # Bordures slider v
            border_handle_v=VBase.WG_BORDER_WIDTH,
            border_handle_v_style=VBase.WG_BORDER_STYLE,
            border_handle_v_rgb=VBase.WG_BORDER_RGB,

            # Rayons
            radius=VBase.WG_RADIUS,
            radius_groove_h=VBase.WG_RADIUS,
            radius_groove_v=VBase.WG_RADIUS,
            radius_handle_h=VBase.WG_RADIUS,
            radius_handle_v=VBase.WG_RADIUS,
    ):
        style = f"""
                /* SLIDER  */
                QSlider {{
                background-color: rgba{bg};
                }}
        
                /* BARRE_H */
                QSlider::groove:horizontal {{
                background-color: qlineargradient(spread:pad, x1:{gradient[0]}, y1:{gradient[1]}, x2:{gradient[2]}, y2:{gradient[3]}, stop:0 rgba{bg_groove}, stop:1 rgba{bg_groove_2});
                height: {height_groove}px;
                border-top-right-radius: {radius_groove_h[0]}px;
                border-top-left-radius: {radius_groove_h[1]}px;
                border-bottom-right-radius: {radius_groove_h[2]}px;
                border-bottom-left-radius: {radius_groove_h[3]}px;
                }}
                QSlider::groove:horizontal:hover {{
                background-color: qlineargradient(spread:pad, x1:{gradient[0]}, y1:{gradient[1]}, x2:{gradient[2]}, y2:{gradient[3]}, stop:0 rgba{bg_groove_hover}, stop:1 rgba{bg_groove_hover_2});
                }}
                QSlider::groove:horizontal:pressed {{
                background-color: qlineargradient(spread:pad, x1:{gradient[0]}, y1:{gradient[1]}, x2:{gradient[2]}, y2:{gradient[3]}, stop:0 rgba{bg_groove_pressed}, stop:1 rgba{bg_groove_pressed_2});
                }}

                /* CURSEUR_H */
                QSlider::handle:horizontal {{
                background-color: rgba{bg_handle};
                width: {width_handle_h}px;
                height: {height_handle_h}px;
                border-top-right-radius: {radius_handle_h[0]}px;
                border-top-left-radius: {radius_handle_h[1]}px;
                border-bottom-right-radius: {radius_handle_h[2]}px;
                border-bottom-left-radius: {radius_handle_h[3]}px;
                margin-top: {margin_handle_h[0]}px;
                margin-bottom: {margin_handle_h[1]}px;
                margin-right: {margin_handle_h[2]}px;
                margin-left: {margin_handle_h[3]}px;
                border-top: {border_handle_h[0]}px {border_handle_h_style} rgba{border_handle_h_rgb};
                border-bottom: {border_handle_h[1]}px {border_handle_h_style} rgba{border_handle_h_rgb};
                border-right: {border_handle_h[2]}px {border_handle_h_style} rgba{border_handle_h_rgb};
                border-left: {border_handle_h[3]}px {border_handle_h_style} rgba{border_handle_h_rgb};
                }}
                QSlider::handle:horizontal:hover {{
                background-color: rgba{bg_handle_hover};
                }}
                QSlider::handle:horizontal:pressed {{
                background-color: rgba{bg_handle_pressed};
                }}
        
                /* BARRE_V */
                QSlider::groove:vertical {{
                background-color: qlineargradient(spread:pad, x1:{gradient[0]}, y1:{gradient[1]}, x2:{gradient[2]}, y2:{gradient[3]}, stop:0 rgba{bg_groove}, stop:1 rgba{bg_groove_2});
                width: {width_groove}px;
                border-top-right-radius: {radius_groove_v[0]}px;
                border-top-left-radius: {radius_groove_v[1]}px;
                border-bottom-right-radius: {radius_groove_v[2]}px;
                border-bottom-left-radius: {radius_groove_v[3]}px;
                }}
                QSlider::groove:vertical:hover {{
                background-color: qlineargradient(spread:pad, x1:{gradient[0]}, y1:{gradient[1]}, x2:{gradient[2]}, y2:{gradient[3]}, stop:0 rgba{bg_groove_hover}, stop:1 rgba{bg_groove_hover_2});
                }}
                QSlider::groove:vertical:pressed {{
                background-color: qlineargradient(spread:pad, x1:{gradient[0]}, y1:{gradient[1]}, x2:{gradient[2]}, y2:{gradient[3]}, stop:0 rgba{bg_groove_pressed}, stop:1 rgba{bg_groove_pressed_2});
                }}
        
                /* CURSEUR_V */
                QSlider::handle:vertical {{
                background-color: rgba{bg_handle};
                width: {width_handle_v}px;
                height: {height_handle_v}px;
                border-top-right-radius: {radius_handle_v[0]}px;
                border-top-left-radius: {radius_handle_v[1]}px;
                border-bottom-right-radius: {radius_handle_v[2]}px;
                border-bottom-left-radius: {radius_handle_v[3]}px;
                margin-top: {margin_handle_v[0]}px;
                margin-bottom: {margin_handle_v[1]}px;
                margin-right: {margin_handle_v[2]}px;
                margin-left: {margin_handle_v[3]}px;
                border-top: {border_handle_v[0]}px {border_handle_v_style} rgba{border_handle_v_rgb};
                border-bottom: {border_handle_v[1]}px {border_handle_v_style} rgba{border_handle_v_rgb};
                border-right: {border_handle_v[2]}px {border_handle_v_style} rgba{border_handle_v_rgb};
                border-left: {border_handle_v[3]}px {border_handle_v_style} rgba{border_handle_v_rgb};
                }}
                QSlider::handle:vertical:hover {{
                background-color: rgba{bg_handle_hover};
                }}
                QSlider::handle:vertical:pressed {{
                background-color: rgba{bg_handle_pressed};
                }}
        
                /* BORDURES */
                .QSlider {{
                border-top: {border[0]}px {border_style} rgba{border_rgb};
                border-bottom: {border[1]}px {border_style} rgba{border_rgb};
                border-right: {border[2]}px {border_style} rgba{border_rgb};
                border-left: {border[3]}px {border_style} rgba{border_rgb};
                }}
                .QSlider:hover {{
                border-top: {border_hover[0]}px {border_hover_style} rgba{border_hover_rgb};
                border-bottom: {border_hover[1]}px {border_hover_style} rgba{border_hover_rgb};
                border-right: {border_hover[2]}px {border_hover_style} rgba{border_hover_rgb};
                border-left: {border_hover[3]}px {border_hover_style} rgba{border_hover_rgb};
                }}
                
                /* RAYONS */
                .QSlider {{
                border-top-right-radius: {radius[0]}px;
                border-top-left-radius: {radius[1]}px;
                border-bottom-right-radius: {radius[2]}px;
                border-bottom-left-radius: {radius[3]}px;
                }}"""

        for wg in wgs:
            wg.setStyleSheet(style)

            Fct(wg=wg, w=width, h=height).DIM()

            wg.setMinimum(value_min)
            wg.setMaximum(value_max)
            wg.setSingleStep(value_step)

            wg.setCursor(Fct(cur=curseur).CUR())


##################
##     BASE     ##
##################
class Base_th(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
        )
class Base_rond(Style):
    def __init__(self, *wgs):
        super().__init__(
            *wgs,
            width=200,
            height=200,

            bg=Rgb().th1(),
            bg_handle=Rgb().th3(),
            bg_handle_hover = Rgb().th3(),
            bg_handle_pressed = Rgb().th3(),

            height_groove=12,
            width_groove=12,
            width_handle_h=10,
            height_handle_h=4,
            width_handle_v=4,
            height_handle_v=10,

            margin_handle_h=(-3, -3, 0, 0),
            margin_handle_v=(0, 0, -3, -3),

            border_handle_h=((3, )*4),
            border_handle_h_rgb=Rgb().th2(),
            border_handle_v=((3, )*4),
            border_handle_v_rgb=Rgb().th2(),

            radius_groove_h=((3, )*4),
            radius_groove_v=((3, )*4),
            radius_handle_h=((6, )*4),
            radius_handle_v=((6, )*4),
        )
class rgb(Style):
    def __init__(self,
                 *wgs,
                 rgb=None,
                 rgb_1=None,
                 rgb_2=None,
                 ):
        super().__init__(
            *wgs,
            height=Dim().h8(),
            value_max=255,

            bg=Rgb().th1(),
            bg_handle=rgb,
            bg_handle_hover=rgb,
            bg_handle_pressed=rgb,

            bg_groove=rgb_1,
            bg_groove_2=rgb_2,
            bg_groove_hover=rgb_1,
            bg_groove_hover_2=rgb_2,
            bg_groove_pressed=rgb_1,
            bg_groove_pressed_2=rgb_2,
            gradient=(0, 0, 1, 0),

            height_groove=12,
            width_groove=12,
            width_handle_h=12,
            height_handle_h=4,
            width_handle_v=4,
            height_handle_v=12,

            margin_handle_h=(-5, -5, 0, 0),
            margin_handle_v=(0, 0, -5, -5),

            border_handle_h=((3, )*4),
            border_handle_h_rgb=rgb,
            border_handle_v=((3, )*4),
            border_handle_v_rgb=rgb,

            radius_groove_h=((3, )*4),
            radius_groove_v=((3, )*4),
            radius_handle_h=((4, )*4),
            radius_handle_v=((4, )*4),
        )
