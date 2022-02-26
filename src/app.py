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
        CheckBox.Base_th(self.ck_demo_th_1, self.ck_demo_th_2, self.ck_demo_th_3)
        CheckBox.Base_tr(self.ck_demo_tr_1, self.ck_demo_tr_2, self.ck_demo_tr_3)
        ### /QCheckBox ###


        ### QComboBox ###
        ComboBox.Base_th(self.cb_demo_th)
        ComboBox.Base_tr(self.cb_demo_tr)
        ### /QComboBox ###


        ### QDateEdit ###
        DateEdit.Base_th(self.de_demo_th)
        DateEdit.Base_tr(self.de_demo_tr)
        ### /QDateEdit ###


        ### QFrame ###
        Frame.Base_th(self.fr_demo_th, self.fr_tb_demo_th_1, self.fr_tb_demo_th_2)
        Frame.Base_tr(self.fr_tb_demo_tr_1, self.fr_tb_demo_tr_2)
        Frame.Base_th(self.fr_body)
        Frame.Cadre(
            self.fr_cb, self.fr_de, self.fr_lw, self.fr_pb, self.fr_ck,
            self.fr_rb, self.fr_pg, self.fr_sb, self.fr_tw, self.fr_le,
            self.fr_te, self.fr_pte, self.fr_tb, self.fr_trw, self.fr_sd,
            self.fr_demo_cadre, self.fr_fr, self.fr_lb
        ).bn1()
        Frame.Menu_bottom(self.fr_menu_bottom)
        Frame.Demo_hover(self.fr_demo_cadre_hover)
        ### /QFrame ###


        ### QLabel ###
        Label.Base_tr(self.lb_mb_version)
        Label.Demo_th(self.lb_lb_demo_th)
        Label.Demo_tr(self.lb_lb_demo_tr)
        Label.DemoCat(
            self.lb_cb_demo, self.lb_de_demo, self.lb_lw_demo, self.lb_pb_demo, self.lb_ck_demo,
            self.lb_rb_demo, self.lb_pg_demo, self.lb_sb_demo, self.lb_tw_demo, self.lb_le_demo,
            self.lb_te_demo, self.lb_pte_demo, self.lb_tb_demo, self.lb_trw_demo, self.lb_sd_demo,
            self.lb_fr_demo, self.lb_lb_demo
        )
        ### /QLabel ###


        ### QListWidget ###
        ListWidget.Demo_th(self.lv_demo_th, self.lw_demo_th)
        ListWidget.Demo_tr(self.lv_demo_tr, self.lw_demo_tr)
        ### /QListWidget ###


        ### QProgressBar ###
        ProgressBar.Demo_th(self.pg_demo_th)
        ProgressBar.Demo_tr(self.pg_demo_tr)
        ### /QProgressBar ###


        ### QPushButton ###
        PushButton.Base_th(self.pb_demo_th, self.pb_demo_ck)
        PushButton.Base_tr(self.pb_demo_tr)

        PushButton.menu_top(self.pb_mt_option).option()
        PushButton.menu_top(self.pb_mt_reduire).reduire()
        PushButton.menu_top(self.pb_mt_agrandir).agrandir()

        PushButton.txt(self.pb_demo_txt)
        PushButton.txt_inv(self.pb_demo_txt_inv)

        PushButton.Demo_bd(self.pb_demo_rd)
        PushButton.Demo_rd(self.pb_demo_bd)

        PushButton.ck_ico(self.pb_demo_ck_ico, self.pb_demo_ico_ck)
        PushButton.zoom(self.pb_demo_zoom)
        ### /QPushButton ###


        ### QRadioButton ###
        RadioButton.Base_th(self.rb_demo_th_1, self.rb_demo_th_2, self.rb_demo_th_3)
        RadioButton.Base_tr(self.rb_demo_tr_1, self.rb_demo_tr_2, self.rb_demo_tr_3)
        ### /QRadioButton ###


        ### QScrollBoxArea ###
        ScrollArea.Demo(self.sca_main)
        ### /QScrollBoxArea ###


        ### QSlider ###
        Slider.Base_rond(self.hsd_demo)
        Slider.Base_rond(self.vsd_demo)
        ### /QSlider ###


        ### QSpinBox ###
        SpinBox.Plus_moins_th(self.sb_demo)
        SpinBox.Plus_moins_tr(self.sb_demo_3)
        SpinBox.Up_down_th(self.sb_demo_2)
        SpinBox.Up_down_tr(self.dsb_demo)
        ### /QSpinBox ###


        ### QTableWidget ###
        TableWidget.Demo_th(self.tv_demo_th, self.tw_demo_th)
        TableWidget.Demo_tr(self.tv_demo_tr, self.tw_demo_tr)
        ### /QTableWidget ###


        ### QText ###
        TextEdit.Base_th(self.le_demo_th)
        TextEdit.Base_tr(self.le_demo_tr)
        TextEdit.Demo_th(self.te_demo_th, self.pte_demo_th)
        TextEdit.Demo_tr(self.te_demo_tr, self.pte_demo_tr)
        ### /QText ###


        ### QToolBox ###
        ToolBox.Demo_th(self.tb_demo_th)
        ToolBox.Demo_tr(self.tb_demo_tr)
        ### /QToolBox ###


        ### QTreeWidget ###
        TreeWidget.Base_th(self.trv_demo_th, self.trw_demo_th)
        TreeWidget.Base_tr(self.trv_demo_tr, self.trw_demo_tr)
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
                model.setItem(ir, ic, QtGui.QStandardItem(f"item:{ic+ir}"))
        self.tv_demo_th.setModel(model)
        self.tv_demo_tr.setModel(model)

        model = QtWidgets.QFileSystemModel()
        model.setRootPath('')
        self.trv_demo_th.setModel(model)
        self.trv_demo_tr.setModel(model)
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
