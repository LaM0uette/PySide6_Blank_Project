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

        MyPushButton.Base(self.pb_demo_th).Base()
        MyPushButton.Base(self.pb_demo_tr).Transparent()

        MyPushButton.Txt(self.pb_demo_txt).txt()
        MyPushButton.Txt(self.pb_demo_txt_inv).inverse()
        ### /QPushButton  ###


        ###  QToolButton  ###
        MyToolButton.Base(self.tb_demo_th).Base()
        MyToolButton.Base(self.tb_demo_tr).Transparent()
        ### /QToolButton  ###


        ###  QRadioButton  ###
        for wg in [self.rb_demo_th_1, self.rb_demo_th_2, self.rb_demo_th_3]: MyRadioButton.Demo(wg).Base()
        for wg in [self.rb_demo_tr_1, self.rb_demo_tr_2, self.rb_demo_tr_3]: MyRadioButton.Demo(wg).Transparent()
        ### /QRadioButton  ###


        ###  QCheckBox  ###
        for wg in [self.ck_demo_th_1, self.ck_demo_th_2, self.ck_demo_th_3]: MyCheckBox.Demo(wg).Base()
        for wg in [self.ck_demo_tr_1, self.ck_demo_tr_2, self.ck_demo_tr_3]: MyCheckBox.Demo(wg).Transparent()
        ### /QCheckBox  ###


        ###  QCommandLinkButton  ###
        MyCommandLinkButton.Base(self.clb_demo_th).Base()
        MyCommandLinkButton.Base(self.clb_demo_tr).Transparent()
        ### /QCommandLinkButton  ###


        # ### QListView ###
        MyListView.Demo(self.lv_demo_th).Base()
        MyListView.Demo(self.lv_demo_tr).Transparent()
        # ### /QListView ###


        ### QTreeView ###
        MyTreeView.Demo(self.trv_demo_th).Base()
        MyTreeView.Demo(self.trv_demo_tr).Transparent()
        ### /QTreeView ###


        ### QTableView ###
        MyTableView.Demo(self.tv_demo_th).Base()
        MyTableView.Demo(self.tv_demo_tr).Transparent()
        ### /QTableView ###


        # ### QListWidget ###
        MyListWidget.Demo(self.lw_demo_th).Base()
        MyListWidget.Demo(self.lw_demo_tr).Transparent()
        # ### /QListWidget ###


        ### QTreeWidget ###
        MyTreeWidget.Demo(self.trw_demo_th).Base()
        MyTreeWidget.Demo(self.trw_demo_tr).Transparent()
        ### /QTreeWidget ###


        ### QTableWidget ###
        MyTableWidget.Demo(self.tw_demo_th).Base()
        MyTableWidget.Demo(self.tw_demo_tr).Transparent()
        ### /QTableWidget ###


        # ### QScrollBoxArea ###
        MyScrollArea.Base(self.sca_main).Main()
        # ### /QScrollBoxArea ###


        ### QToolBox ###
        MyToolBox.Demo(self.tbx_demo_th).Base()
        MyToolBox.Demo(self.tbx_demo_tr).Transparent()
        ### /QToolBox ###


        ###  QFrame  ###
        MyFrame.Base(self.fr_body).Base(rgb=PaRgb.TH1)
        MyFrame.Menu(self.fr_menu_top).top()
        MyFrame.Menu(self.fr_menu_bottom).bottom()
        MyFrame.Cadre(self.fr_main).th2_fin()

        for wg in [
            self.fr_cb, self.fr_de, self.fr_lw, self.fr_pb, self.fr_ck,
            self.fr_rb, self.fr_pg, self.fr_sb, self.fr_tw, self.fr_le,
            self.fr_te, self.fr_pte, self.fr_tb, self.fr_trw, self.fr_sd,
            self.fr_demo_cadre, self.fr_fr, self.fr_lb
        ]: MyFrame.Cadre(wg).bn1()

        MyFrame.Demo_hover(self.fr_demo_cadre_hover)
        for wg in [self.fr_demo_th, self.fr_tbx_demo_th_1, self.fr_tbx_demo_th_2]: MyFrame.Base(wg).Base()
        for wg in [self.fr_tbx_demo_tr_1, self.fr_tbx_demo_tr_2]: MyFrame.Base(wg).Transparent()
        ### /QFrame  ###


        ### QComboBox ###
        MyComboBox.Base(self.cb_demo_th).Base()
        MyComboBox.Base(self.cb_demo_tr).Transparent()
        ### /QComboBox ###


        ### QComboBox ###
        MyFontComboBox.Base(self.fcb_demo_th).Base()
        MyFontComboBox.Base(self.fcb_demo_tr).Transparent()
        ### /QComboBox ###


        ### QLineEdit ###
        MyLineEdit.Base(self.le_demo_th).Base()
        MyLineEdit.Base(self.le_demo_tr).Transparent()
        ### /QLineEdit ###


        ### QTextEdit ###
        MyTextEdit.Demo(self.te_demo_th).Base()
        MyTextEdit.Demo(self.te_demo_tr).Transparent()
        ### /QTextEdit ###


        ### QPlainTextEdit ###
        MyPlainTextEdit.Demo(self.pte_demo_th).Base()
        MyPlainTextEdit.Demo(self.pte_demo_tr).Transparent()
        ### /QPlainTextEdit ###


        ### QSpinBox ###
        MySpinBox.PlusMinus(self.sb_demo).Base()
        MySpinBox.PlusMinus(self.sb_demo_3).Transparent()
        MySpinBox.UpDown(self.sb_demo_2).Base()
        ### /QSpinBox ###


        ### QDoubleSpinBox ###
        MyDoubleSpinBox.UpDown(self.dsb_demo).Transparent()
        ### /QDoubleSpinBox ###


        ### QTimeEdit ###
        MyTimeEdit.Base(self.tie_demo_th).Base()
        MyTimeEdit.Base(self.tie_demo_tr).Transparent()
        ### /QTimeEdit ###


        ### QDateEdit ###
        MyDateEdit.Base(self.de_demo_th).Base()
        MyDateEdit.Base(self.de_demo_tr).Transparent()
        ### /QDateEdit ###


        ### QDateTimeEdit ###
        MyDateTimeEdit.Base(self.dte_demo_th).Base()
        MyDateTimeEdit.Base(self.dte_demo_tr).Transparent()
        ### /QDateTimeEdit ###


        # ### QSlider ###
        # MySlider.Base(self.hsd_demo).th()
        # MySlider.Base(self.vsd_demo).rond()
        # ### /QSlider ###


        ### QLabel ###
        MyLabel.Base(self.lb_mt_ico).ico_main()
        MyLabel.Demo(self.lb_lb_demo_th).Base()
        MyLabel.Base(self.lb_mt_nom).Transparent(font=PaFont.HH3)
        MyLabel.Base(self.lb_mb_version).Transparent()
        MyLabel.Demo(self.lb_lb_demo_tr).Transparent()
        for wg in [
            self.lb_cb_demo, self.lb_de_demo, self.lb_lw_demo, self.lb_pb_demo, self.lb_ck_demo,
            self.lb_rb_demo, self.lb_pg_demo, self.lb_sb_demo, self.lb_tw_demo, self.lb_le_demo,
            self.lb_te_demo, self.lb_pte_demo, self.lb_tb_demo, self.lb_trw_demo, self.lb_sd_demo,
            self.lb_fr_demo, self.lb_lb_demo
        ]: MyLabel.Demo(wg).wg_categorie()
        ### /QLabel ###


        ### QProgressBar ###
        MyProgressBar.Demo(self.pg_demo_th).Base()
        MyProgressBar.Demo(self.pg_demo_tr).Transparent()
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




        # Demo lw
        model = QtGui.QStandardItemModel(60, 1)
        for i in range(60):
            self.lw_demo_th.addItem(f"je suis l'item : {i}")
            self.lw_demo_tr.addItem(f"je suis l'item : {i}")
            model.setItem(i, 0, QtGui.QStandardItem(f"je suis l'item : {i}"))
        self.lv_demo_th.setModel(model)
        self.lv_demo_tr.setModel(model)

        # Demo tv
        model = QtGui.QStandardItemModel(20, 100)
        for ic in range(100):
            for ir in range(20):
                model.setItem(ir, ic, QtGui.QStandardItem(f"item:{ic + ir}"))
        self.tv_demo_th.setModel(model)
        self.tv_demo_tr.setModel(model)

        model = QtWidgets.QFileSystemModel()
        model.setRootPath('')
        self.trv_demo_th.setModel(model)
        self.trv_demo_tr.setModel(model)
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
