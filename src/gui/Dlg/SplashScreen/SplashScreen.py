from PySide6 import QtCore, QtWidgets

from src import *
from src.gui.ui import splash_screen_ui


class SplashScreen(splash_screen_ui.Ui_SplashScreen, QtWidgets.QDialog):
    def __init__(self):
        super(SplashScreen, self).__init__()

        self.width = 600
        self.height = 400
        self.opacity = 1

        self.INIT()

    ############################
    ##     INITIALISATION     ##
    ############################
    def IN_BASE(self):
        ### Fenetre ###
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
        self.vlay_main.setContentsMargins(v_gb.MARGIN_APP, v_gb.MARGIN_APP, v_gb.MARGIN_APP, v_gb.MARGIN_APP)
    def IN_CLASSE(self):
        ### QFrame ###
        MyFrame.SplashScreen(self.fr_main)
        ### /QFrame ###


        ### QLabel ###
        MyLabel.Base(self.lb_ico).ico_splash()
        MyLabel.Base(self.lb_titre).Transparent(font=PaFont.HH3)
        for wg in [self.lb_description, self.lb_chargement]: MyLabel.Base(wg).Transparent(font=PaFont.TEXTE)
        ### /QLabel ###


        ### QProgressBar ###
        MyProgressBar.Base(self.pg_chargement).Chargement()
        ### /QProgressBar ###
    def IN_WG(self):
        ### Base ###
        self.setCursor(Functions().SET_CURSOR(cur=PaCur.SOURIS))

        ### Infos ###
        self.lb_titre.setText(Config.nom)
        self.lb_description.setText(Config.description)
    def IN_CONNECTIONS(self):
        pass
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
