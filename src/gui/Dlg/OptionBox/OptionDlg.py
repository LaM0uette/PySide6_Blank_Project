import glob
import os

from PySide6 import QtCore, QtWidgets

from src import *
from src.gui.dlg.MsgBox.MsgBox import MsgBox
from src.gui.dlg.RgbBox.RgbBox import RgbBox
from src.gui.ui import option_ui
from src.gui.events.Event import Event


class OptionDlg(option_ui.Ui_Option, QtWidgets.QDialog):
    dragPos: QtCore.QPoint

    def __init__(
            self,
            fen_main,
            title,
            msg,
            ico,
            ico_rgb,
            txt_apply,
            txt_ok,
            width,
            height,
            opacity,
    ):
        super(OptionDlg, self).__init__()

        self.fen_main = fen_main
        self.title = title
        self.msg = msg
        self.ico = ico
        self.ico_rgb = ico_rgb
        self.txt_ok = txt_ok
        self.txt_pb_appliquer = txt_apply
        self.width = width
        self.height = height
        self.opacity = opacity

        # Global
        self.reload = False

        self.INIT()

        self.dct_pg = {
            "Configs": [self.pg_opt_configs],
            "Thèmes": [self.pg_opt_themes],
            "Infos": [self.pg_opt_infos],
        }

        ### CREATION DES EVENT ###
        self.evt = Event(self)
        self.mousePressEvent = self.evt.mousePressEvent
        self.mouseMoveEvent = self.evt.mouseMoveEvent

    ############################
    ##     INITIALISATION     ##
    ############################
    def IN_BASE(self):
        ### Fenetre ###
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
        ### QCheckBox ###
        for wg in [
            self.ck_opt_cfg_debug, self.ck_opt_cfg_autoclose, self.ck_opt_cfg_resize, self.ck_opt_cfg_ui_pin
        ]: MyCheckBox.Base(wg).Transparent()
        ### /QCheckBox ###


        ### QComboBox ###
        for wg in [self.fcb_opt_ft_font, self.cb_opt_tm_theme]: MyComboBox.Base(wg).Font()
        ### /QComboBox ###


        ### QFrame ###
        MyFrame.Menu(self.fr_menu_top).top()
        MyFrame.Cadre(self.fr_main).th2_fin()
        for wg in [self.fr_opt_cfg_opacity, self.fr_opt_cfg_autoclose, self.fr_opt_cfg_resize]: MyFrame.Cadre(wg).th3()
        MyFrame.Dlg(self.fr_body).th(rgb=PaRgb.TH1)
        MyFrame.Menu(self.fr_opt_bottom).bottom_dlg()
        ### /QFrame ###


        ### QLabel ###
        MyLabel.Base(self.lb_mt_ico).ico_main()
        MyLabel.Base(self.lb_mt_nom).Transparent(font=PaFont.HH3)
        MyLabel.Base(self.lb_opt_info_nom).Title()
        for wg in [
            self.lb_opt_info_desc, self.lb_opt_info_auteur, self.lb_opt_info_version, self.lb_opt_cfg_opacity,
            self.lb_opt_cfg_debug, self.lb_opt_cfg_autoclose, self.lb_opt_cfg_resize, self.lb_opt_cfg_ui_pin, self.lb_opt_cfg_resize_width,
            self.lb_opt_cfg_resize_height
        ]: MyLabel.Base(wg).Transparent()
        ### /QLabel ###


        ### QPushButton ###
        MyPushButton.Dlg(self.pb_opt_appliquer).ok()
        MyPushButton.Dlg(self.pb_opt_ok).nok_inv()
        MyPushButton.MenuTop(self.pb_mt_quitter).quitter()

        MyPushButton.Plein(self.pb_opt_tm_th1).th1()
        MyPushButton.Plein(self.pb_opt_tm_th2).th2()
        MyPushButton.Plein(self.pb_opt_tm_th3).th3()
        MyPushButton.Plein(self.pb_opt_tm_bn1).bn1()
        MyPushButton.Plein(self.pb_opt_tm_bn2).bn2()
        ### /QPushButton ###


        ### QSpinBox ###
        MySpinBox.Dlg(self.sb_opt_cfg_opacity).th()
        for wg in [self.sb_opt_cfg_resize_width, self.sb_opt_cfg_resize_height]: MySpinBox.Dlg(wg).inf()
        ### /QSpinBox ###


        ### QTreeWidget ###
        MyTreeWidget.Base(self.trw_option).Option()
        ### /QTreeWidget ###
    def IN_WG(self):
        # Base
        self.setCursor(Functions().SET_CURSOR(cur=PaCur.SOURIS))

        # Frame menu_top
        self.fr_menu_top.setFixedHeight(PaDim.H9)

        # Menu_top
        self.lb_mt_nom.setText(self.title)

        # Configs
        try:
            self.fcb_opt_ft_font.setCurrentText(Config.font)

            self.sb_opt_cfg_opacity.setValue(Config.opacity*100)
            self.ck_opt_cfg_debug.setChecked(True) if Config.debug == True else self.ck_opt_cfg_debug.setChecked(False)
            self.ck_opt_cfg_autoclose.setChecked(True) if Config.auto_close == True else self.ck_opt_cfg_autoclose.setChecked(False)
            self.ck_opt_cfg_resize.setChecked(True) if Config.resize == True else self.ck_opt_cfg_resize.setChecked(False)
            self.ck_opt_cfg_ui_pin.setChecked(True) if Config.toolbox_pin == True else self.ck_opt_cfg_ui_pin.setChecked(False)

            self.sb_opt_cfg_resize_width.setValue(Config.widht)
            self.sb_opt_cfg_resize_height.setValue(Config.height)
        except: pass

        # infos
        self.lb_opt_info_nom.setText(Config.nom)
        self.lb_opt_info_desc.setText(Config.description)
        self.lb_opt_info_auteur.setText(f"Auteur : {Config.auteur}")
        self.lb_opt_info_version.setText(f"Version : {Config.version}")

        # pb dlg
        self.pb_opt_ok.setText(self.txt_ok)
        self.pb_opt_ok.setDefault(True)
        self.pb_opt_appliquer.setText(self.txt_pb_appliquer)
        self.pb_opt_appliquer.setDefault(True)
    def IN_CONNECTIONS(self):
        # Menu_top
        self.pb_mt_quitter.clicked.connect(lambda: self.close())
        self.trw_option.itemClicked.connect(self.f_set_menu_option)

        # Connection value change #
        # font combo box
        self.fcb_opt_ft_font.currentTextChanged.connect(self.a_maj_button_appliquer)
        self.fcb_opt_ft_font.currentTextChanged.connect(self.a_maj_cb_font)

        # slider
        self.sb_opt_cfg_opacity.valueChanged.connect(self.a_maj_button_appliquer)
        self.sb_opt_cfg_resize_width.valueChanged.connect(lambda: self.a_maj_button_appliquer(_reload="True"))
        self.sb_opt_cfg_resize_height.valueChanged.connect(lambda: self.a_maj_button_appliquer(_reload="True"))
        self.ck_opt_cfg_debug.stateChanged.connect(self.a_maj_button_appliquer)
        self.ck_opt_cfg_autoclose.stateChanged.connect(self.a_maj_button_appliquer)
        self.ck_opt_cfg_resize.stateChanged.connect(lambda: self.a_maj_button_appliquer(_reload="True"))
        self.ck_opt_cfg_ui_pin.stateChanged.connect(lambda: self.a_maj_button_appliquer(_reload="True"))

        # combo box theme
        self.cb_opt_tm_theme.currentTextChanged.connect(self.a_maj_button_appliquer)

        # pb tm
        self.pb_opt_tm_th1.clicked.connect(lambda: self.f_maj_rgb_theme(rgb="th1"))
        self.pb_opt_tm_th2.clicked.connect(lambda: self.f_maj_rgb_theme(rgb="th2"))
        self.pb_opt_tm_th3.clicked.connect(lambda: self.f_maj_rgb_theme(rgb="th3"))
        self.pb_opt_tm_bn1.clicked.connect(lambda: self.f_maj_rgb_theme(rgb="bn1"))
        self.pb_opt_tm_bn2.clicked.connect(lambda: self.f_maj_rgb_theme(rgb="bn2"))

        # pb dlg
        self.pb_opt_ok.clicked.connect(lambda: self.f_ok())
        self.pb_opt_appliquer.clicked.connect(self.f_appliquer)
    def IN_ACT(self):
        # MAJ de la liste des thèmes
        self.a_maj_liste_themes()
    def IN_WG_BASE(self):
        # pb appliquer
        self.pb_opt_appliquer.setVisible(False)
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


    #####################
    ##     ACTIONS     ##
    #####################
    def _a_reload_ui(self):
        MyPushButton.Plein(self.pb_opt_tm_th1).th1()
        MyPushButton.Plein(self.pb_opt_tm_th2).th2()
        MyPushButton.Plein(self.pb_opt_tm_th3).th3()
        MyPushButton.Plein(self.pb_opt_tm_bn1).bn1()
        MyPushButton.Plein(self.pb_opt_tm_bn2).bn2()

        # QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        #
        # Functions().GEN_SVG()
        # time.sleep(0.5)
        #
        # self.IN_WG()
        # self.IN_CLASSE()
        #
        # self.fen_main.IN_BASE()
        # self.fen_main.IN_WG()
        # self.fen_main.IN_CLASSE()
        #
        # QtWidgets.QApplication.restoreOverrideCursor()
        #
        # if self.reload:
        MsgBox().INFO(msg="Modifications appliquées !\nVeuillez redémarrer l'application pour appliquer les modifications.")
        self.reload = False
    #####
    def a_maj_liste_themes(self):
        self.cb_opt_tm_theme.clear()

        for i, js in enumerate(glob.glob(f"theme/*.json")):
            theme = os.path.basename(js).split(".")[0]
            self.cb_opt_tm_theme.addItem(theme)

            cfg = Json(lien_json=f"config/config.json").OPEN()
            if theme == cfg["config"]["theme"]:
                self.cb_opt_tm_theme.setCurrentIndex(i)
    def a_maj_cb_font(self):
        for wg in [self.fcb_opt_ft_font, self.cb_opt_tm_theme]: MyComboBox.Base(wg).Font(font=self.fcb_opt_ft_font.currentText())
    def a_maj_button_appliquer(self, _reload="False"):
        if not self.pb_opt_appliquer.isVisible():
            self.pb_opt_appliquer.setVisible(True)

        if _reload == "True":
            self.reload = True
    #####################
    ##    /ACTIONS     ##
    #####################


    #######################
    ##     FONCTIONS     ##
    #######################
    def f_set_menu_option(self, item):
        self.stk_option.setCurrentWidget(self.dct_pg.get(item.text(0))[0])
    def f_maj_rgb_theme(self, rgb):
        dct_colors = {
            "th1": PaRgb.TH1,
            "th2": PaRgb.TH2,
            "th3": PaRgb.TH3,
            "bn1": PaRgb.BN1,
            "bn2": PaRgb.BN2,
        }
        colors = RgbBox.GET(rgb=dct_colors.get(rgb))
        if colors:
            self.a_maj_button_appliquer()

            dct = {f"{rgb}": list(colors)}
            Json(lien_json=f"theme/{Config.theme}.json").UPDATE(dct)

            self._a_reload_ui()
    #####
    def f_appliquer(self):
        self.pb_opt_appliquer.setVisible(False)

        dct = {
            "config": {
                "theme": self.cb_opt_tm_theme.currentText(),
                "font": self.fcb_opt_ft_font.currentText(),
                "widht": self.sb_opt_cfg_resize_width.value(),
                "height": self.sb_opt_cfg_resize_height.value(),
                "opacity": self.sb_opt_cfg_opacity.value() / 100,
                "cur": "MyApp"
            },
            "var": {
                "debug": True if self.ck_opt_cfg_debug.isChecked() else False,
                "resize": True if self.ck_opt_cfg_resize.isChecked() else False,
                "auto_close": True if self.ck_opt_cfg_autoclose.isChecked() else False,
                "toolbox_pin": True if self.ck_opt_cfg_ui_pin.isChecked() else False
            }
        }
        Json(lien_json=f"config/config.json").UPDATE(dct)

        self._a_reload_ui()
    def f_ok(self):
        if self.pb_opt_appliquer.isVisible():
            self.f_appliquer()
        self.close()
    #######################
    ##    /FONCTIONS     ##
    #######################
