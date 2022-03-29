from PySide6 import QtCore, QtWidgets

from src import *
from src.gui.ui import rep_ui
from src.gui.events.Event import Event


class ResponseDlg(rep_ui.Ui_Rep, QtWidgets.QDialog):
    dragPos: QtCore.QPoint
    response = False

    def __init__(
            self,
            title,
            msg,
            ico,
            ico_rgb,
            txt_ok,
            txt_cancel,
            width,
            height,
            opacity,
    ):
        super(ResponseDlg, self).__init__()

        self.title = title
        self.msg = msg
        self.ico = ico
        self.ico_rgb = ico_rgb
        self.txt_ok = txt_ok
        self.txt_cancel = txt_cancel
        self.width = width
        self.height = height
        self.opacity = opacity

        self.INIT()

        ### CREATION DES EVENT ###
        self.evt = Event(self)
        self.mousePressEvent = self.evt.mousePressEvent
        self.mouseMoveEvent = self.evt.mouseMoveEvent

    ############################
    ##     INITIALISATION     ##
    ############################
    def IN_BASE(self):
        # Fenetre
        self.setWindowTitle(self.title)
        self.setFixedWidth(self.width)
        self.setFixedHeight(self.height)
        self.setWindowOpacity(self.opacity)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Tool)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setGraphicsEffect(PaShadow.OMBRE_PORTEE(self))
        self.setWindowModality(QtCore.Qt.ApplicationModal)
    def IN_SETUP_UI(self):
        ### Ui ###
        self.setupUi(self)
        self.glay_main.setContentsMargins(v_gb.MARGIN_APP, v_gb.MARGIN_APP, v_gb.MARGIN_APP, v_gb.MARGIN_APP)
    def IN_CLASSE(self):
        ### QFrame ###
        MyFrame.Menu(self.fr_menu_top).top()
        MyFrame.Cadre(self.fr_main).th2_fin()
        MyFrame.Dlg(self.fr_body).th(rgb=PaRgb.TH1)
        MyFrame.Menu(self.fr_rep_bottom).bottom_dlg()
        ### /QFrame ###


        ### QLabel ###
        MyLabel.Base(self.lb_mt_ico).ico_custom(img=self.ico, img_rgb=self.ico_rgb)
        MyLabel.Base(self.lb_mt_nom).Transparent(font=PaFont.HH3)
        MyLabel.Base(self.lb_rep_text).Transparent()
        ### /QLabel ###


        ### QPushButton ###
        MyPushButton.Dlg(self.pb_rep_ok).ok()
        MyPushButton.Dlg(self.pb_rep_annuler).nok_inv()
        MyPushButton.MenuTop(self.pb_mt_quitter).quitter()
        ### /QPushButton ###
    def IN_WG(self):
        # Base
        self.pb_mt_quitter.clicked.connect(lambda: self.close())

        # Frame menu_top
        self.fr_menu_top.setFixedHeight(PaDim.H9)

        # Menu_top
        self.lb_mt_nom.setText(self.title)

        # Message
        self.lb_rep_text.setText(self.msg)

        # pb dlg
        self.pb_rep_ok.setText(self.txt_ok)
        self.pb_rep_annuler.setText(self.txt_cancel)
        self.pb_rep_annuler.setDefault(True)
    def IN_CONNECTIONS(self):
        # Menu_top
        self.pb_mt_quitter.clicked.connect(lambda: self.close())

        # pb dlg
        self.pb_rep_ok.clicked.connect(lambda: self.f_ok())
        self.pb_rep_annuler.clicked.connect(lambda: self.close())
    def IN_ACT(self):
        pass
    def IN_WG_BASE(self):
        pass
    def INIT(self):
        self.IN_BASE()
        self.IN_SETUP_UI()
        self.IN_CLASSE()
        self.IN_WG()
        self.IN_CONNECTIONS()
        self.IN_ACT()
        self.IN_WG_BASE()
    ############################
    ##    /INITIALISATION     ##
    ############################


    #######################
    ##     FONCTIONS     ##
    #######################
    def f_ok(self):
        self.response = True
        self.close()
    #######################
    ##    /FONCTIONS     ##
    #######################
