import glob
import os
import time

from PySide6 import QtCore, QtWidgets, QtGui

from ... import option_ui
from ..Msg import DLG_Msg
from ..Rgb import DLG_Rgb
from .....build import *
from .....config import *
from .....In_classe import In_classe


class OptionApp(option_ui.Ui_Option, QtWidgets.QDialog):
    dragPos: QtCore.QPoint

    def __init__(self,
                 fen,
                 titre,
                 msg,
                 ico,
                 tm,
                 txt_pb_appliquer,
                 txt_pb_ok,
                 width,
                 height,
                 opacity,
    ):
        super(OptionApp, self).__init__()

        self.fen = fen
        self.titre = titre
        self.msg = msg
        self.ico = ico
        self.tm = tm
        self.txt_pb_ok = txt_pb_ok
        self.txt_pb_appliquer = txt_pb_appliquer
        self.width = width
        self.height = height
        self.opacity = opacity

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setupUi(self)

        # Global
        self.reload = False
        self.dct_pg = {
            "Polices": [self.pg_opt_font],
            "Configs": [self.pg_opt_configs],
            "Thèmes": [self.pg_opt_themes],
            "Infos": [self.pg_opt_infos],
        }

        self.INIT()


    ############################
    ##     INITIALISATION     ##
    ############################
    def IN_BASE(self):
        # Fenetre
        self.setWindowTitle(self.titre)
        self.setFixedWidth(self.width)
        self.setFixedHeight(self.height)
        self.setWindowOpacity(self.opacity)
    def IN_CLASSE(self):
        ### QCheckBox ###
        CheckBox.Base_tr(self.ck_opt_cfg_autoreload, self.ck_opt_cfg_autoclose, self.ck_opt_cfg_resize)
        ### /QCheckBox ###


        ### QComboBox ###
        ComboBox.Base_th(self.fcb_opt_ft_font, self.cb_opt_tm_theme)
        ### /QComboBox ###


        ### QFrame ###
        Frame.Cadre(
            self.fr_main,
            self.fr_opt_ft_h1, self.fr_opt_ft_h2, self.fr_opt_ft_h3, self.fr_opt_ft_h4, self.fr_opt_ft_h5,
            self.fr_opt_cfg_opacity, self.fr_opt_cfg_autoclose, self.fr_opt_cfg_resize
        ).th3()
        Frame.Base_th(self.fr_body, rgb=Rgb().th1())
        Frame.Menu_bottom_dlg(self.fr_opt_bottom)
        ### /QFrame ###


        ### QLabel ###
        Label.Titre(self.lb_opt_info_nom)
        Label.Base_tr(self.lb_opt_info_desc, self.lb_opt_info_auteur, self.lb_opt_info_version, self.lb_opt_ft_h1,
                      self.lb_opt_ft_h2, self.lb_opt_ft_h3, self.lb_opt_ft_h4, self.lb_opt_ft_h5, self.lb_opt_cfg_opacity,
                      self.lb_opt_cfg_autoreload, self.lb_opt_cfg_autoclose, self.lb_opt_cfg_resize, self.lb_opt_cfg_resize_width,
                      self.lb_opt_cfg_resize_height)
        ### /QLabel ###


        ### QPushButton ###
        PushButton.dlg_ok(self.pb_opt_appliquer)
        PushButton.dlg_ok_inv(self.pb_opt_ok)

        PushButton.plein(self.pb_opt_tm_th1).th1()
        PushButton.plein(self.pb_opt_tm_th2).th2()
        PushButton.plein(self.pb_opt_tm_th3).th3()
        PushButton.plein(self.pb_opt_tm_bn1).bn1()
        PushButton.plein(self.pb_opt_tm_bn2).bn2()
        ### /QPushButton ###


        ### QSpinBox ###
        SpinBox.Plus_moins_bd_th3(self.sb_opt_ft_h1, self.sb_opt_ft_h2, self.sb_opt_ft_h3, self.sb_opt_ft_h4, self.sb_opt_ft_h5, self.sb_opt_cfg_opacity)
        SpinBox.Plus_moins_inf_bd_th3(self.sb_opt_cfg_resize_width, self.sb_opt_cfg_resize_height)
        ### /QSpinBox ###


        ### QText ###
        TextEdit.tr_taille(self.le_opt_ft_texte_h1, h=Font().h1())
        TextEdit.tr_taille(self.le_opt_ft_texte_h2, h=Font().h2())
        TextEdit.tr_taille(self.le_opt_ft_texte_h3, h=Font().h3())
        TextEdit.tr_taille(self.le_opt_ft_texte_h4, h=Font().h4())
        TextEdit.tr_taille(self.le_opt_ft_texte_h5, h=Font().h5())
        ### /QText ###


        ### QTreeWidget ###
        TreeWidget.option(self.trw_option)
        ### /QTreeWidget ###

        # Lancement des fonctions de MEF global
        In_classe(ui=self)
    def IN_WG(self):
        # Base
        self.setCursor(Fct(cur=Cur().souris()).CUR())
        self.setStyleSheet(f"background-color: rgba{Rgb().th1()};")

        # Frame menu_top
        self.fr_menu_top.setFixedHeight(Dim().h9())

        # Menu_top
        dim = Dim().h9()
        Fct(wg=self.lb_mt_ico, w=dim, h=dim).DIM()
        self.lb_mt_ico.setPixmap(QtGui.QPixmap(f"{self.ico}{self.tm}.svg"))
        self.lb_mt_ico.setScaledContents(True)
        self.lb_mt_nom.setText(self.titre)

        # Configs
        try:
            self.fcb_opt_ft_font.setCurrentText(config.font)
            self.sb_opt_ft_h1.setValue(Font().h1())
            self.sb_opt_ft_h2.setValue(Font().h2())
            self.sb_opt_ft_h3.setValue(Font().h3())
            self.sb_opt_ft_h4.setValue(Font().h4())
            self.sb_opt_ft_h5.setValue(Font().h5())

            self.sb_opt_cfg_opacity.setValue(config.opacity*100)
            self.ck_opt_cfg_autoreload.setChecked(True) if config.auto_reload == True else self.ck_opt_cfg_autoreload.setChecked(False)
            self.ck_opt_cfg_autoclose.setChecked(True) if config.auto_close == True else self.ck_opt_cfg_autoclose.setChecked(False)
            self.ck_opt_cfg_resize.setChecked(True) if config.resize == True else self.ck_opt_cfg_resize.setChecked(False)

            self.sb_opt_cfg_resize_width.setValue(config.widht)
            self.sb_opt_cfg_resize_height.setValue(config.height)
        except: pass

        # infos
        self.lb_opt_info_nom.setText(config.nom)
        self.lb_opt_info_desc.setText(config.description)
        self.lb_opt_info_auteur.setText(f"Auteur : {config.auteur}")
        self.lb_opt_info_version.setText(f"Version : {config.version}")

        # pb dlg
        self.pb_opt_ok.setText(self.txt_pb_ok)
        self.pb_opt_ok.setDefault(True)
        self.pb_opt_appliquer.setText(self.txt_pb_appliquer)
        self.pb_opt_appliquer.setDefault(True)
    def IN_CONNECTIONS(self):
        # Menu_top
        self.pb_mt_quitter.clicked.connect(lambda: self.close())
        self.trw_option.itemClicked.connect(self._set_opt)

        # Connection value change #
        ## font combo box
        self.fcb_opt_ft_font.currentTextChanged.connect(self._val_change_appliquer)
        ## spin box
        self.sb_opt_ft_h1.valueChanged.connect(self._val_change_appliquer)
        self.sb_opt_ft_h2.valueChanged.connect(self._val_change_appliquer)
        self.sb_opt_ft_h3.valueChanged.connect(self._val_change_appliquer)
        self.sb_opt_ft_h4.valueChanged.connect(self._val_change_appliquer)
        self.sb_opt_ft_h5.valueChanged.connect(self._val_change_appliquer)
        ## slider
        self.sb_opt_cfg_opacity.valueChanged.connect(self._val_change_appliquer)
        self.sb_opt_cfg_resize_width.valueChanged.connect(lambda: self._val_change_appliquer(val="true"))
        self.sb_opt_cfg_resize_height.valueChanged.connect(lambda: self._val_change_appliquer(val="true"))
        self.ck_opt_cfg_autoreload.stateChanged.connect(self._val_change_appliquer)
        self.ck_opt_cfg_autoclose.stateChanged.connect(self._val_change_appliquer)
        self.ck_opt_cfg_resize.stateChanged.connect(lambda: self._val_change_appliquer(val="true"))
        ## combo box theme
        self.cb_opt_tm_theme.currentTextChanged.connect(self._val_change_appliquer)

        # pb tm
        self.pb_opt_tm_th1.clicked.connect(lambda: self._pb_tm_maj(tm="th1"))
        self.pb_opt_tm_th2.clicked.connect(lambda: self._pb_tm_maj(tm="th2"))
        self.pb_opt_tm_th3.clicked.connect(lambda: self._pb_tm_maj(tm="th3"))
        self.pb_opt_tm_bn1.clicked.connect(lambda: self._pb_tm_maj(tm="bn1"))
        self.pb_opt_tm_bn2.clicked.connect(lambda: self._pb_tm_maj(tm="bn2"))

        # pb dlg
        self.pb_opt_ok.clicked.connect(lambda: self.OK())
        self.pb_opt_appliquer.clicked.connect(self._appliquer)
    def IN_ACT(self):
        # MAJ de la liste des thèmes
        self._maj_cb_theme()
    def IN_WG_BASE(self):
        # stk
        self.stk_option.setCurrentWidget(self.pg_opt_menu)

        # pb appliquer
        self.pb_opt_appliquer.setVisible(False)
    def INIT(self):
        self.IN_BASE()
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
    def __reload(self):
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)

        importlib.reload(config)

        Fct().GEN_SVG()
        time.sleep(0.5)

        importlib.reload(rld)

        self.IN_WG()
        self.IN_CLASSE()

        self.fen.IN_BASE()
        self.fen.IN_CLASSE()

        QtWidgets.QApplication.restoreOverrideCursor()

        if self.reload:
            DLG_Msg().INFO(msg="Modifications appliquées !\nCertains paramètres peuvent nécessiter un redémarrage de l'application.")
            self.reload = False
    ## configuration
    def _maj_cb_theme(self):
        self.cb_opt_tm_theme.clear()
        for i, js in enumerate(glob.glob(f"{vrb.DO_THEME}*.json")):
            tm = os.path.basename(js).split(".")[0]
            self.cb_opt_tm_theme.addItem(tm)
            if tm == config.theme:
                self.cb_opt_tm_theme.setCurrentIndex(i)
    def _set_opt(self, item):
        self.stk_option.setCurrentWidget(self.dct_pg.get(item.text(0))[0])
    def _pb_tm_maj(self, tm):
        dct_colors = {
            "th1": Rgb().th1(),
            "th2": Rgb().th2(),
            "th3": Rgb().th3(),
            "bn1": Rgb().bn1(),
            "bn2": Rgb().bn2(),
        }
        rep, colors = DLG_Rgb().GET(rgb=dct_colors.get(tm))
        if rep:
            self._val_change_appliquer()

            dct = {
                f"{tm}": list(colors),
            }
            Json(lien_json=f"{vrb.DO_THEME}{config.theme}.json").UPDATE(dct)

            self.__reload()
    # application des modifs
    def _val_change_appliquer(self, val=""):
        if not self.pb_opt_appliquer.isVisible():
            self.pb_opt_appliquer.setVisible(True)
        if val == "true":
            self.reload = True
    def _appliquer(self):
        self.pb_opt_appliquer.setVisible(False)

        config_ini = Ini(lien_ini=vrb.INI_CONFIG)
        config = config_ini.OPEN_INI()
        config["config"]["theme"] = self.cb_opt_tm_theme.currentText()
        config["config"]["font"] = self.fcb_opt_ft_font.currentText()
        config["config"]["widht"] = f"{self.sb_opt_cfg_resize_width.value()}"
        config["config"]["height"] = f"{self.sb_opt_cfg_resize_height.value()}"
        config["config"]["opacity"] = f"{self.sb_opt_cfg_opacity.value() / 100}"
        config["var"]["autoreload"] = "true" if self.ck_opt_cfg_autoreload.isChecked() == True else "false"
        config["var"]["autoclose"] = "true" if self.ck_opt_cfg_autoclose.isChecked() == True else "false"
        config["var"]["resize"] = "true" if self.ck_opt_cfg_resize.isChecked() == True else "false"
        config_ini.WRITE_INI(ini=config)

        dct = {
            "h1": self.sb_opt_ft_h1.value(),
            "h2": self.sb_opt_ft_h2.value(),
            "h3": self.sb_opt_ft_h3.value(),
            "h4": self.sb_opt_ft_h4.value(),
            "h5": self.sb_opt_ft_h5.value(),
        }
        Json(lien_json=vrb.JS_FONT).UPDATE(dct)

        self.__reload()
    #####################
    ##    /ACTIONS     ##
    #####################


    #######################
    ##     FONCTIONS     ##
    #######################
    def OK(self):
        if self.pb_opt_appliquer.isVisible():
            self._appliquer()
        self.close()
    #######################
    ##    /FONCTIONS     ##
    #######################


    ###################
    ##     EVENT     ##
    ###################
    def mousePressEvent(self, event):
        cur = QtGui.QCursor()
        verifHeight = cur.pos().y() - self.pos().y()
        if event.buttons() == QtCore.Qt.LeftButton and verifHeight < Dim().h9():
            self.dragPos = event.globalPosition().toPoint()
            event.accept()
    def mouseMoveEvent(self, event):
        def act_move(event):
            self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
            self.dragPos = event.globalPosition().toPoint()
            event.accept()

        cur = QtGui.QCursor()
        height_verif = cur.pos().y() - self.pos().y()

        try:
            if event.buttons() == QtCore.Qt.LeftButton and height_verif < Dim().h9():
                act_move(event)
            if event.buttons() == QtCore.Qt.LeftButton and height_verif < Dim().h9():
                act_move(event)
        except AttributeError: pass
    ###################
    ##    /EVENT     ##
    ###################
