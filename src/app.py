import sys

from PySide6 import QtCore, QtWidgets, QtGui

from .gui import *
from .build import *
from .config import *
from .In_classe import In_classe


class main(main_ui.Ui_main, QtWidgets.QWidget):
    dragPos: QtCore.QPoint

    def __init__(self):
        super(main, self).__init__()

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.sizegrip = QtWidgets.QSizeGrip(self)
        self.win_state = QtCore.Qt.WindowNoState

        self.tray = QtWidgets.QSystemTrayIcon(QtGui.QPixmap(ICO_MAIN), self)
        self.tray_menu = QtWidgets.QMenu()
        self.tray_menu.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.setupUi(self)
        self.INIT()

    ############################
    ##     INITIALISATION     ##
    ############################
    def IN_BASE(self):
        # Fenetre
        self.setWindowTitle(config.nom)
        self.setWindowOpacity(config.opacity)
        self._resize()
    def IN_CLASSE(self):
        ### QCheckBox ###
        ### /QCheckBox ###


        ### QComboBox ###
        ### /QComboBox ###


        ### QDateEdit ###
        ### /QDateEdit ###


        ### QFrame ###
        Frame.Base_th(self.fr_body)
        Frame.Menu_bottom(self.fr_menu_bottom)
        ### /QFrame ###


        ### QLabel ###
        Label.Base_tr(self.lb_mb_version)
        ### /QLabel ###


        ### QListWidget ###
        ### /QListWidget ###


        ### QProgressBar ###
        ### /QProgressBar ###


        ### QPushButton ###
        PushButton.menu_top(self.pb_mt_option).option()
        PushButton.menu_top(self.pb_mt_reduire).reduire()
        PushButton.menu_top(self.pb_mt_agrandir).agrandir()
        ### /QPushButton ###


        ### QRadioButton ###
        ### /QRadioButton ###


        ### QScrollBoxArea ###
        ### /QScrollBoxArea ###


        ### QSlider ###
        ### /QSlider ###


        ### QSpinBox ###
        ### /QSpinBox ###


        ### QTableWidget ###
        ### /QTableWidget ###


        ### QText ###
        ### /QText ###


        ### QToolBox ###
        ### /QToolBox ###


        ### QTreeWidget ###
        ### /QTreeWidget ###

        # Lancement des fonctions de MEF global
        In_classe(ui=self)
    def IN_WG(self):
        # Base
        self.setCursor(Fct(cur=Cur().souris()).CUR())

        # Icone de l'app
        dim = Dim().h9()
        Fct(wg=self.lb_mt_ico, w=dim, h=dim).DIM()
        self.lb_mt_ico.setPixmap(QtGui.QPixmap(ICO_MAIN))
        self.lb_mt_ico.setScaledContents(True)
        self.lb_mt_nom.setText(config.nom)

        # Widget blanc pour centrer le nom de l'app
        dim = Dim().h10()*1.4
        Fct(wg=self.wg_mt_blank, w=dim * 4, h=dim).DIM()

        # Version de l'app
        self.lb_mb_version.setText(f" Version : {config.version}")

        # SizeGrip
        if config.resize:
            self.sizegrip.setCursor(Fct(cur=Cur().fleche_nwse()).CUR())
            self.sizegrip.setStyleSheet("QSizeGrip {"
                                        f"image: url({Img().resize()}th3.svg);"
                                        f"width: {Dim().h10()}px;"
                                        f"height: {Dim().h10()}px;"
                                        "}")
            self.hlay_menu_bottom.addWidget(self.sizegrip)
    def IN_CONNECTIONS(self):
        ## Menu_top
        self.pb_mt_option.clicked.connect(lambda: DLG_Option(fen=fen).MAIN())
        self.pb_mt_reduire.clicked.connect(lambda: self.reduire())
        self.pb_mt_agrandir.clicked.connect(lambda: self.agrandir())
        self.pb_mt_quitter.clicked.connect(lambda: self.cacher())
    def IN_ACT(self):
        pass
    def IN_WG_BASE(self):
        pass
    def IN_TRAY(self):
        self.tray.activated.connect(self.showTrayEvent)
        TrayIcon.Main(self.tray_menu)

        ### Actions
        qact_quitter = {
            "ico": Img().quitter(),
            "ico_rgb": "bn2",
            "txt": "Quitter",
            "shortcut": "Shift+Esc",
            "fct": self.quitterTray,
            "sht_1": QtCore.Qt.SHIFT,
            "sht_2": QtCore.Qt.Key_Escape,
            "sht_3": None,
            "height": None
        }

        ### Set actions
        act = lambda _act: (self, self.tray_menu, _act.get("ico"), _act.get("ico_rgb"), _act.get("txt"), _act.get("shortcut"), _act.get("fct"), _act.get("height"))
        Fct().QACTION(*act(qact_quitter))
        # self.tray_menu.addSeparator()

        ### Raccourcis clavier
        sht = lambda _sht: (self, _sht.get("sht_1"), _sht.get("sht_2"), _sht.get("sht_3"), _sht.get("fct"))
        Fct().QSHORTCUT(*sht(qact_quitter))


        self.tray.setContextMenu(self.tray_menu)
        self.tray.show()
    def INIT(self):
        self.IN_BASE()
        self.IN_CLASSE()
        self.IN_WG()
        self.IN_CONNECTIONS()
        self.IN_ACT()
        self.IN_WG_BASE()
        self.IN_TRAY()
    ############################
    ##    /INITIALISATION     ##
    ############################


    #####################
    ##     ACTIONS     ##
    #####################
    #####################
    ##    /ACTIONS     ##
    #####################


    #######################
    ##     FONCTIONS     ##
    #######################
    #######################
    ##    /FONCTIONS     ##
    #######################


    ###################
    ##     EVENT     ##
    ###################
    # fenetre
    def _resize(self):
        if config.resize:
            self.setMinimumWidth(config.widht)
            self.setMinimumHeight(config.height)
        else:
            self.setFixedWidth(config.widht)
            self.setFixedHeight(config.height)
    def _centreFen(self):
        center = QtGui.QScreen.availableGeometry(QtWidgets.QApplication.primaryScreen()).center()
        geo = self.frameGeometry()
        geo.moveCenter(center)
        self.move(geo.topLeft())
    # interaction des boutons
    def agrandir(self):
        if self.windowState() == QtCore.Qt.WindowMaximized:
            self.win_state = QtCore.Qt.WindowNoState
            self._centreFen()
            self._resize()
        else:
            self.win_state = QtCore.Qt.WindowMaximized

        self.setWindowState(self.win_state)
    def reduire(self):
        self.setWindowState(QtCore.Qt.WindowMinimized)
    def cacher(self):
        if config.auto_close: return self.quitter()
        self.hide()
        self._centreFen()
    def quitter(self):
        if DLG_Rep().QUITTER():
            if config.auto_close:
                app.quit()
                quit()
            else: self.hide()
    def quitterTray(self):
        self.show()
        fen.activateWindow()

        if fen.windowState() == QtCore.Qt.WindowMinimized:
            fen.setWindowState(QtCore.Qt.WindowActive)

        if DLG_Rep().QUITTER():
            app.quit()
            quit()
    # event
    def mousePressEvent(self, event):
        cur = QtGui.QCursor()
        verifHeight = cur.pos().y() - self.pos().y()
        if event.buttons() == QtCore.Qt.LeftButton and verifHeight < Dim().h9() and self.windowState() != QtCore.Qt.WindowMaximized:
            self.dragPos = event.globalPosition().toPoint()
            event.accept()
    def mouseDoubleClickEvent(self, event):
        cur = QtGui.QCursor()
        height_verif = cur.pos().y() - self.pos().y()
        if height_verif < Dim().h9():
            self.agrandir()
            event.accept()
    def mouseMoveEvent(self, event):
        def act_move(event):
            self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
            self.dragPos = event.globalPosition().toPoint()
            event.accept()

        cur = QtGui.QCursor()
        height_verif = cur.pos().y() - self.pos().y()

        if event.buttons() == QtCore.Qt.LeftButton and height_verif < Dim().h9() and self.windowState() != QtCore.Qt.WindowMaximized and cur.pos().y() <= 0:
            self.setCursor(Fct(cur=Cur().agrandir()).CUR())
        else:
            self.setCursor(Fct(cur=Cur().souris()).CUR())

        try:
            if event.buttons() == QtCore.Qt.LeftButton and height_verif < Dim().h9() and self.windowState() != QtCore.Qt.WindowMaximized:
                act_move(event)
            if event.buttons() == QtCore.Qt.LeftButton and height_verif < Dim().h9() and self.windowState() == QtCore.Qt.WindowMaximized:
                self.setWindowState(QtCore.Qt.WindowNoState)
                self.win_state = QtCore.Qt.WindowNoState
                act_move(event)
        except AttributeError: pass
    def mouseReleaseEvent(self, event):
        cur = QtGui.QCursor()
        height_verif = cur.pos().y() - self.pos().y()
        if height_verif < Dim().h9() and self.windowState() != QtCore.Qt.WindowMaximized and cur.pos().y() <= 0:
            self.setCursor(Fct(cur=Cur().souris()).CUR())
            self.agrandir()
            event.accept()
    def closeEvent(self, event):
        event.accept()
        app.quit()
    def showEvent(self, event):
        if self.win_state == QtCore.Qt.WindowMaximized:
            self.setWindowState(self.win_state)
        else:
            self.setWindowState(self.win_state)
            self._resize()
    def showTrayEvent(self, reason):
        if reason == QtWidgets.QSystemTrayIcon.Trigger:
            self.show()
            fen.activateWindow()

            if fen.windowState() == QtCore.Qt.WindowMinimized:
                fen.setWindowState(QtCore.Qt.WindowActive)
    ###################
    ##    /EVENT     ##
    ###################


ICO_MAIN = f"{Img().main()}th2.svg"
app = QtWidgets.QApplication(sys.argv)
splash = QtWidgets.QSplashScreen(QtGui.QPixmap(ICO_MAIN).scaledToHeight(400), QtCore.Qt.WindowStaysOnTopHint)
splash.show()
app.processEvents()

fen = main()
splash.finish(fen)
fen.show()

sys.exit(app.exec())
