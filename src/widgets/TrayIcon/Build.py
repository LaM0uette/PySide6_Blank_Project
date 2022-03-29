from src.config import Config
from src.build.mods import Functions
from src.lib.palettes import *


class Build:
    def __init__(
            self,
            *wgs,

            # Dimensions
            width=None,
            height=PaDim.H9,
            height_separator=5,

            # Police
            font=Config.font,
            font_size=PaFont.H4,

            # Paramètres
            focus_policy=PaFocusPolicy.STRONG,

            # Curseur
            cursor=PaCur.SOURIS_MAIN,

            # Couleurs BG
            bg=PaRgb.TH3,
            bg_item=PaRgb.TH3,
            bg_item_checked=PaRgb.TH1,
            # Couleurs BG autres
            bg_separator=PaRgb.BN1,
            # Couleurs FG
            fg=PaRgb.TH1,
            fg_item=PaRgb.TH1,
            fg_item_checked=PaRgb.TH3,

            # Positions WG
            margin=(0,) * 4,
            padding=(0,) * 4,

            # Bordures
            border=(0,) * 4,
            border_style="solid",
            border_rgb=PaRgb.TR,
            # Bordures item
            border_item=(0,) * 4,
            border_item_style="solid",
            border_item_rgb=PaRgb.TR,
            # Bordures item checked
            border_item_checked=(0,) * 4,
            border_item_checked_style="solid",
            border_item_checked_rgb=PaRgb.TR,

            # Rayons
            radius=(3,) * 4,
            radius_item=(3,) * 4,
    ):
        """
        *Border_Style: str() : dashed | dot-dash | dot-dot-dash | dotted | double | groove | inset | outset | ridge | solid | none \n
        *PaCur: list() : PaCur().%nomCurseur() \n
        *PaDim: int() : PaDim().%nomDim() \n
        *PaFocusPolicy: QtCore.Qt : PaFocusPolicy().%nomFocus \n
        *PaFont: int() : PaFont().%nomFont() \n
        *RgbBox: tuple() : RgbBox().%nomCouleur() \n
        *Tuple: tuple() : (int(), int(), int(), int()) == (Top, Bottom, Right, Left) | (TopRight, TopLeft, BottomRight, BottomLeft) \n

        :param wgs:
        :param width: *PaDim
        :param height: *PaDim
        :param height_separator: int()
        :param font: str()
        :param font_size: *PaFont
        :param focus_policy: *PaFocusPolicy
        :param cursor: *PaCur
        :param bg: *RgbBox
        :param bg_item: *RgbBox
        :param bg_item_checked: *RgbBox
        :param bg_separator: *RgbBox
        :param fg: *RgbBox
        :param fg_item: *RgbBox
        :param fg_item_checked: *RgbBox
        :param margin: *Tuple
        :param padding: *Tuple
        :param border: *Tuple
        :param border_style: *Border_Style
        :param border_rgb: *RgbBox
        :param border_item: *Tuple
        :param border_item_style: *Border_Style
        :param border_item_rgb: *RgbBox
        :param border_item_checked: *Tuple
        :param border_item_checked_style: *Border_Style
        :param border_item_checked_rgb: *RgbBox
        :param radius: *Tuple
        :param radius_item: *Tuple
        """

        style = f"""
                /* MENU */
                QMenu {{
                background-color: rgba{bg};
                color: rgba{fg};
                }}

                /* SEPARATEUR */
                QMenu::separator{{
                height: {height_separator}px;
                background-color: rgba{bg_separator};
                }}

                /* ITEM */
                QMenu::item {{
                background-color: rgba{bg_item};
                color: rgba{fg_item};
                margin-top: {margin[0]}px;
                margin-bottom: {margin[1]}px;
                margin-right: {margin[2]}px;
                margin-left: {margin[3]}px;
                padding-top: {padding[0]}px;
                padding-bottom: {padding[1]}px;
                padding-right: {padding[2]}px;
                padding-left: {padding[3]}px;
                border-top: {border_item[0]}px {border_item_style} rgba{border_item_rgb};
                border-bottom: {border_item[1]}px {border_item_style} rgba{border_item_rgb};
                border-right: {border_item[2]}px {border_item_style} rgba{border_item_rgb};
                border-left: {border_item[3]}px {border_item_style} rgba{border_item_rgb};
                border-top-right-radius: {radius_item[0]}px;
                border-top-left-radius: {radius_item[1]}px;
                border-bottom-right-radius: {radius_item[2]}px;
                border-bottom-left-radius: {radius_item[3]}px;
                }}
                QMenu::item:selected {{
                background-color: rgba{bg_item_checked};
                color: rgba{fg_item_checked};
                border-top: {border_item_checked[0]}px {border_item_checked_style} rgba{border_item_checked_rgb};
                border-bottom: {border_item_checked[1]}px {border_item_checked_style} rgba{border_item_checked_rgb};
                border-right: {border_item_checked[2]}px {border_item_checked_style} rgba{border_item_checked_rgb};
                border-left: {border_item_checked[3]}px {border_item_checked_style} rgba{border_item_checked_rgb};
                }}

                /* BORDURES */
                .QMenu {{
                border-top: {border[0]}px {border_style} rgba{border_rgb};
                border-bottom: {border[1]}px {border_style} rgba{border_rgb};
                border-right: {border[2]}px {border_style} rgba{border_rgb};
                border-left: {border[3]}px {border_style} rgba{border_rgb};
                }}

                /* RAYONS */
                .QMenu {{
                border-top-right-radius: {radius[0]}px;
                border-top-left-radius: {radius[1]}px;
                border-bottom-right-radius: {radius[2]}px;
                border-bottom-left-radius: {radius[3]}px;
                }}"""
        for wg in wgs:
            # Dimensions
            Functions().SET_DIM(wg, width=width, height=height)

            # Police
            Functions().SET_FONT(wg, font=font, font_size=font_size)

            # Paramètres
            wg.setFocusPolicy(focus_policy)

            # Curseur
            wg.setCursor(Functions().SET_CURSOR(cursor))

            # Style
            wg.setStyleSheet(style)
