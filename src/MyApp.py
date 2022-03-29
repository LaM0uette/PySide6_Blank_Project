import sys
import time

from PySide6 import QtCore, QtWidgets, QtGui

from src import *
from src.gui import *


# Renommez des de bases
class main(Ui_main, QtWidgets.QWidget):
    dragPos: QtCore.QPoint

    def __init__(self):
        super(main, self).__init__()

        ### AJOUTS DE BASE ###
            # size_grip
        self.size_grip = QtWidgets.QSizeGrip(self)
            # tray
        self.tray = QtWidgets.QSystemTrayIcon(QtGui.QPixmap(f"{PaImg.MAIN}th3.svg"), self)
        self.tray.activated.connect(self.trayActivate)
        self.timer_double_click = QtCore.QTimer(self)
        self.timer_double_click.setSingleShot(True)
        self.timer_double_click.timeout.connect(self.traySingleClick)
            # tray_menu
        self.tray_menu = QtWidgets.QMenu()
        self.tray_menu.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ### VARIABLES DE BASES ###
        self.win_state = QtCore.Qt.WindowNoState

        ### FONCTIONS AU LANCEMENT ###
        self.INIT(
            [self.IN_BASE, "Config()uration des éléments principaux"],
            [self.IN_SETUP_UI, "Setup de l'interface graphique"],
            [self.IN_CLASSE, "Initialisation des Widgets"],
            [self.IN_WG, "Config()uration de base des Widgets"],
            [self.IN_CONNECTIONS, "Ajout des connexions"],
            [self.IN_ACT, "Fonctions de base"],
            [self.IN_WG_BASE, "Etat de base des Widgets"],
            [self.IN_TRAY, "Finalisation de la Config()uration"]
        )

        splash_screen.close()

        ### CREATION DES EVENT ###
        self.evt = Event(self)
        self.mousePressEvent = self.evt.mousePressEvent
        self.mouseDoubleClickEvent = self.evt.mouseDoubleClickEvent
        self.mouseMoveEvent = self.evt.mouseMoveEvent
        self.mouseReleaseEvent = self.evt.mouseReleaseEvent

    ############################
    ##     INITIALISATION     ##
    ############################
    def IN_BASE(self):
        ### Fenetre principal ###
        self.setWindowTitle(Config.nom)
        self.setWindowIcon(QtGui.QPixmap(f"{PaImg.MAIN}th3.svg"))
        self.setWindowOpacity(Config.opacity)

        self.setGraphicsEffect(PaShadow.OMBRE_PORTEE(self))

        self.e_resize_screen()
    def IN_SETUP_UI(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        ### Ui principal ###
        self.setupUi(self)
        self.vlay_main.setContentsMargins(v_gb.MARGIN_APP, v_gb.MARGIN_APP, v_gb.MARGIN_APP, v_gb.MARGIN_APP)
    def IN_CLASSE(self):
        ###  QPushButton  ###
        MyPushButton.MenuTop(self.pb_mt_option).option()
        MyPushButton.MenuTop(self.pb_mt_reduire).reduire()
        MyPushButton.MenuTop(self.pb_mt_agrandir).agrandir()
        MyPushButton.MenuTop(self.pb_mt_quitter).quitter()
        ### /QPushButton  ###


        ###  QToolButton  ###
        ### /QToolButton  ###


        ###  QRadioButton  ###
        ### /QRadioButton  ###


        ###  QCheckBox  ###
        ### /QCheckBox  ###


        ###  QCommandLinkButton  ###
        ### /QCommandLinkButton  ###


        # ### QListView ###
        # ### /QListView ###


        ### QTreeView ###
        ### /QTreeView ###


        ### QTableView ###
        ### /QTableView ###


        # ### QListWidget ###
        # ### /QListWidget ###


        ### QTreeWidget ###
        ### /QTreeWidget ###


        ### QTableWidget ###
        ### /QTableWidget ###


        # ### QScrollBoxArea ###
        # ### /QScrollBoxArea ###


        ### QToolBox ###
        ### /QToolBox ###


        ###  QFrame  ###
        MyFrame.Base(self.fr_body).Base_no_radius(rgb=PaRgb.TH1)
        MyFrame.Menu(self.fr_menu_top).top()
        MyFrame.Menu(self.fr_menu_bottom).bottom()
        MyFrame.Cadre(self.fr_main).th2_fin()
        ### /QFrame  ###


        ### QComboBox ###
        ### /QComboBox ###


        ### QComboBox ###
        ### /QComboBox ###


        ### QLineEdit ###
        ### /QLineEdit ###


        ### QTextEdit ###
        ### /QTextEdit ###


        ### QPlainTextEdit ###
        ### /QPlainTextEdit ###


        ### QSpinBox ###
        ### /QSpinBox ###


        ### QDoubleSpinBox ###
        ### /QDoubleSpinBox ###


        ### QTimeEdit ###
        ### /QTimeEdit ###


        ### QDateEdit ###
        ### /QDateEdit ###


        ### QDateTimeEdit ###
        ### /QDateTimeEdit ###


        # ### QSlider ###
        # MySlider.Base(self.hsd_demo).th()
        # MySlider.Base(self.vsd_demo).rond()
        # ### /QSlider ###


        ### QLabel ###
        MyLabel.Base(self.lb_mt_ico).ico_main()
        MyLabel.Base(self.lb_mt_nom).Transparent(font=PaFont.HH3)
        MyLabel.Base(self.lb_mb_version).Transparent()
        ### /QLabel ###


        ### QProgressBar ###
        ### /QProgressBar ###
    def IN_WG(self):
        ### Base ###
        self.setCursor(Functions().SET_CURSOR(PaCur.SOURIS))

        ### Nom de l'app ###
        self.lb_mt_nom.setText(Config.nom)


        ### Widget blanc pour centrer le nom de l'app ###
        dim = PaDim.H9 * 1.4
        Functions().SET_DIM(self.wg_mt_blank, width=dim*3, height=dim)


        ### Version de l'app ###
        self.lb_mb_version.setText(f" Version : {Config.version}")


        ### size_grip ###
        if Config.resize:
            self.size_grip.setCursor(Functions().SET_CURSOR(PaCur.FLECHE_NWSE))
            self.size_grip.setStyleSheet(
                f"""
                QSizeGrip {{
                image: url({PaImg.RESIZE}th3.svg);
                width: {PaDim.H10}px;
                height: {PaDim.H10}px;
                }}
                """
            )
            self.hlay_menu_bottom.addWidget(self.size_grip)
    def IN_CONNECTIONS(self):
        ### Menu_top ###
        self.pb_mt_option.clicked.connect(lambda: OptionBox.MAIN(fen_main=fen))
        self.pb_mt_reduire.clicked.connect(lambda: self.evt.e_reduire())
        self.pb_mt_agrandir.clicked.connect(lambda: self.evt.e_agrandir())
        self.pb_mt_quitter.clicked.connect(lambda: self.evt.e_cacher())
    def IN_ACT(self):
        pass
    def IN_WG_BASE(self):
        pass
    def IN_TRAY(self):
        ### Actions ###
        Functions.ADD_QACTION(
            self,
            tray=self.tray_menu,
            ico=PaImg.QUITTER,
            ico_rgb="bn2",
            txt="Quitter",
            shortcut_txt="Shift+Esc",
            status_tip="Quitter",
            fct=self.e_quitter_tray,
            sht_1=PaKeys.SHIFT,
            sht_2=PaKeys.ESCAPE
        )

        # self.tray_menu.addSeparator()

        self.tray.setContextMenu(self.tray_menu)
        self.tray.show()
    def INIT(self, *args):
        for fct in args:
            splash_screen.lb_chargement.setText(fct[1])
            splash_screen.pg_chargement.setValue(splash_screen.pg_chargement.value() + 100 / len(args))
            fct[0]()

        splash_screen.lb_chargement.setText("Lancement de l'application")
        splash_screen.pg_chargement.setValue(100)
        time.sleep(0)
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
    def e_resize_screen(self):
        if Config.resize:
            self.setMinimumWidth(Config.widht)
            self.setMinimumHeight(Config.height)
        else:
            self.setFixedWidth(Config.widht)
            self.setFixedHeight(Config.height)
    #####
    def traySingleClick(self):
        screen = QtWidgets.QApplication.primaryScreen().availableGeometry()
        widget = toolBox.geometry()

        toolBox.open()
        toolBox.show()
        toolBox.activateWindow()

        toolBox.move(screen.width()-widget.width(), screen.height()-widget.height())
    def trayDoubleClick(self):
        self.timer_double_click.stop()
        self.show()
        fen.activateWindow()

        if fen.windowState() == QtCore.Qt.WindowMinimized:
            fen.setWindowState(QtCore.Qt.WindowActive)
    def trayActivate(self, reason):
        if reason == QtWidgets.QSystemTrayIcon.Trigger:
            self.timer_double_click.start(app.doubleClickInterval())

        elif reason == QtWidgets.QSystemTrayIcon.DoubleClick:
            self.trayDoubleClick()
    def e_quitter(self):
        """Permet de quitter l'application"""
        if not Config.auto_close:
            self.hide()
        elif ResponseBox.QUITTER():
            app.quit()
    def e_quitter_tray(self):
        self.show()
        fen.activateWindow()

        if fen.windowState() == QtCore.Qt.WindowMinimized:
            fen.setWindowState(QtCore.Qt.WindowActive)

        if ResponseBox.QUITTER():
            app.quit()
    #####
    def closeEvent(self, event):
        event.accept()
        app.quit()
    ###################
    ##    /EVENT     ##
    ###################


if __name__ == "__main__":
    if Config.debug:
        Functions().GEN_SVG()

    app = QtWidgets.QApplication(sys.argv)
    splash_screen = SplashScreen()
    splash_screen.open()
    toolBox = ToolBoxUi()
    app.processEvents()

    fen = main()
    fen.show()

    sys.exit(app.exec())
