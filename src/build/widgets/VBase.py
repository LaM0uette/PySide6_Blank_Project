from ...build import *
from ...config import *


######################
##     COULEURS     ##
######################
# BG
BG = Rgb().th3()
BG_HOVER = Rgb().th3()
BG_CHECKED = Rgb().th1()
BG_CHECKED_HOVER = Rgb().th1()
BG_PRESSED = Rgb().th3()
BG_CHECKED_PRESSED = Rgb().th1()
BG_SELECTION = Rgb().th1()
# BG item
BG_ITEM = Rgb().th3()
BG_ITEM_HOVER = Rgb().th3()
BG_ITEM_CHECKED = Rgb().th1()
BG_ITEM_CHECKED_HOVER = Rgb().th1()
# BG Autres
BG_CHUNK = Rgb().th2()
BG_CHUNK_HOVER = Rgb().bn1()
BG_GROOVE = Rgb().th3()
BG_GROOVE_HOVER = Rgb().th3()
BG_GROOVE_PRESSED = Rgb().th3()
BG_HANDLE = Rgb().th2()
BG_HANDLE_HOVER = Rgb().th2()
BG_HANDLE_PRESSED = Rgb().bn1()
BG_SEPARATOR = Rgb().bn1()

# FG
FG = Rgb().th1()
FG_HOVER = Rgb().bn1()
FG_CHECKED = Rgb().th3()
FG_CHECKED_HOVER = Rgb().bn1()
FG_PRESSED = Rgb().bn1()
FG_CHECKED_PRESSED = Rgb().bn2()
FG_SELECTION = Rgb().th3()
FG_PLACEHOLDER = Rgb().th2()
# FG item
FG_ITEM = Rgb().th1()
FG_ITEM_HOVER = Rgb().bn1()
FG_ITEM_CHECKED = Rgb().th3()
FG_ITEM_CHECKED_HOVER = Rgb().bn1()

# Autres
GRIDLINE = Rgb().th2()


########################
##     DIMENSIONS     ##
########################
WIDTH = None
HEIGHT = None
WG_WIDTH = None
WG_HEIGHT = Dim().h9()


####################
##     IMAGES     ##
####################
# Check
IMG_UNCHECK = Img().check()
IMG_UNCHECK_HOVER = Img().check()
IMG_CHECK = Img().valider()
IMG_CHECK_HOVER = Img().valider()
IMG_UNROLL = Img().fleche_bottom()
IMG_UNROLL_HOVER = Img().fleche_bottom()
# Check RGB
IMG_UNCHECK_RGB = "th2"
IMG_UNCHECK_HOVER_RGB = "bn1"
IMG_CHECK_RGB = "th2"
IMG_CHECK_HOVER_RGB = "bn1"
IMG_UNROLL_RGB = "th2"
IMG_UNROLL_HOVER_RGB = "bn1"

# Fleches
IMG_UP = Img().plus()
IMG_DOWN = Img().moins()
IMG_RIGHT = Img().fleche_droite()
IMG_LEFT = Img().fleche_gauche()
# Fleches RGB
IMG_UP_RGB = "th2"
IMG_DOWN_RGB = "th2"
IMG_RIGHT_RGB = "th3"
IMG_LEFT_RGB = "th3"

# img dim
img_width = WG_HEIGHT * StyleBase().x_ico()
IMG_WIDTH = WG_HEIGHT * StyleBase().X_ICO()
img_height = WG_HEIGHT * StyleBase().x_ico()
IMG_HEIGHT = WG_HEIGHT * StyleBase().X_ICO()


#####################
##     BORDURE     ##
#####################
BORDER_WIDTH = ((0, )*4)
BORDER_STYLE = "solid"
BORDER_RGB = Rgb().tr()
WG_BORDER_WIDTH = ((0, )*4)
WG_BORDER_STYLE = "solid"
WG_BORDER_RGB = Rgb().tr()


###################
##     RAYON     ##
###################
RADIUS = 3
WG_RADIUS = ((3, )*4)


####################
##     SCROLL     ##
####################
SCROLL_BG = Rgb().th1()
SCROLL_WIDTH = 6
SCROLL_HEIGHT = 6

SCROLL_HANDLE_BG = Rgb().th3()
SCROLL_HANDLE_BG_HOVER = Rgb().th3()
SCROLL_HANDLE_FG = Rgb().th2()
SCROLL_HANDLE_FG_HOVER = Rgb().bn1()
SCROLL_HANDLE_MIN_WIDTH = 20
SCROLL_HANDLE_MIN_HEIGHT = 20

SCROLL_H = Scroll().need()
SCROLL_V = Scroll().need()
HEADER_H = True
HEADER_V = True


####################
##     POLICE     ##
####################
FONT = config.font
FONT_SIZE = Font().h4()
FONT_SIZE_HD = Font().h3()


########################
##     PARAMETRES     ##
########################
EDIT = False
NO_FOCUS = False
SB_BUTTONS_TYPE = SpinButton().plus_minus()
TEXT_VISIBLE = True
VAL_MIN = 0
VAL_MAX = 100
VAL_STEP = 1
SELECTION_BEHAVIOR = SelectionBehavior().row()
WORD_WRAP = True


#####################
##     CURSEUR     ##
#####################
CUR = Cur().souris()
CUR_LE = Cur().IBeam()
