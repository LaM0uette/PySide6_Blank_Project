from src.lib.palettes import *


#####################
##     QWidget     ##
#####################
SIZE_POLICY = DcSizePolicy.Base
DIM = DcDim.Base
DIM_WG = DcDim.Base(fixed_height=PaDim.H9)
FONT = PaFont.BASE
CUR = PaCur.SOURIS
CUR_ACTION = PaCur.MAIN
FOCUS_POLICY = PaFocusPolicy.NO
LAYOUT_DIRECTION = PaLayoutDirection.LEFT_TO_RIGHT
#####################
##    /QWidget     ##
#####################


#############################
##     QAbstractButton     ##
#############################
TXT = None
ICO = DcIco.Base
AUTO_ACTIONS = DcAutoActions.Base
AUTO_ACTIONS_EXCLUSIVE = DcAutoActions.Base
#############################
##    /QAbstractButton     ##
#############################


#############################
##     QToolButton     ##
#############################
POPUP_MODE = PaPopupMode.DELAYED
TOOL_BUTTON_STYLE = PaToolButtonStyle.ICON_ONLY
ARROW_TYPE = PaArrowType.NO
#############################
##    /QAbstractButton     ##
#############################


####################
##     QFrame     ##
####################
FRAME = DcFrame.Base
####################
##    /QFrame     ##
####################


#################################
##     QAbstractScrollArea     ##
#################################
SCROLL_POLICY = DcScrollPolicy.Base
#################################
##    /QAbstractScrollArea     ##
#################################


###############################################
##     QAbstractSpinBox / QAbstractSlider    ##
###############################################
VALUE = DcValue.Base
###############################################
##    /QAbstractSpinBox / QAbstractSlider    ##
###############################################


###################
##     STYLE     ##
###################
BACKGROUND = DcRgbBg.Base
FOREGROUND = DcRgbFg.Base
BACKGROUND_ITEM = DcRgbBg.Base
FOREGROUND_ITEM = DcRgbFg.Base
IMG = DcImg.Base
BORDER = DcBorder.Base
SCROLL = DcScroll.Base
HEADER_H = True
HEADER_V = True
###################
##    /STYLE     ##
###################
