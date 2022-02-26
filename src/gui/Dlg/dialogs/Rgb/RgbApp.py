from PySide6 import QtCore, QtWidgets, QtGui

from ... import rgb_ui
from .....build import *
from .....In_classe import In_classe


class RgbApp(rgb_ui.Ui_Rgb, QtWidgets.QDialog):
    dragPos: QtCore.QPoint
    rep = False
    rgb_rtn = (0, 0, 0)

    def __init__(self,
                 titre,
                 rgb,
                 ico,
                 tm,
                 txt_pb_ok,
                 txt_pb_annuler,
                 width,
                 height,
                 opacity,
    ):
        super(RgbApp, self).__init__()

        self.titre = titre
        self.rgb = rgb
        self.ico = ico
        self.tm = tm
        self.txt_pb_ok = txt_pb_ok
        self.txt_pb_annuler = txt_pb_annuler
        self.width = width
        self.height = height
        self.opacity = opacity

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setupUi(self)
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
        ### QFrame ###
        Frame.Cadre(self.fr_main).th3()
        Frame.Base_th(self.fr_body, rgb=Rgb().th1())
        Frame.Menu_bottom_dlg(self.fr_rgb_bottom)
        Frame.Base_th(self.fr_rgb_colors)
        ### /QFrame ###


        ### QLabel ###
        Label.Base_tr(self.lb_rgb_red, self.lb_rgb_green, self.lb_rgb_blue, font_size=Font().h4())
        ### /QLabel ###


        ### QPushButton ###
        PushButton.dlg_ok(self.pb_rgb_ok)
        PushButton.dlg_nok_inv(self.pb_rgb_annuler)
        ### /QPushButton ###


        ### QSpinBox ###
        SpinBox.rgb_bd_th3(self.sb_rgb_red, self.sb_rgb_green, self.sb_rgb_blue)
        ### /QSpinBox ###


        ### QSlider ###
        Slider.rgb(self.sd_rgb_red, self.sd_rgb_green, self.sd_rgb_blue)
        ### /QSlider ###


        ### QText ###
        TextEdit.rgb_hex(self.le_rgb_hex)
        ### /QText ###

        # Lancement des fonctions de MEF global
        In_classe(ui=self)
    def IN_WG(self):
        # Base
        self.setCursor(Fct(cur=Cur().souris()).CUR())

        # Frame menu_top
        self.fr_menu_top.setFixedHeight(Dim().h9())

        # Menu_top
        dim = Dim().h9()
        Fct(wg=self.lb_mt_ico, w=dim, h=dim).DIM()
        self.lb_mt_ico.setPixmap(QtGui.QPixmap(f"{self.ico}{self.tm}.svg"))
        self.lb_mt_ico.setScaledContents(True)
        self.lb_mt_nom.setText(self.titre)

        # Message
        self.lb_rgb_red.setText("ROUGE")
        self.lb_rgb_green.setText("VERT")
        self.lb_rgb_blue.setText("BLEU")

        # pb dlg
        self.pb_rgb_ok.setText(self.txt_pb_ok)
        self.pb_rgb_annuler.setText(self.txt_pb_annuler)
        self.pb_rgb_annuler.setDefault(True)
    def IN_CONNECTIONS(self):
        # Menu_top
        self.pb_mt_quitter.clicked.connect(lambda: self.close())

        # Slider
        self.sd_rgb_red.valueChanged.connect(lambda: self._set_sb_val())
        self.sd_rgb_green.valueChanged.connect(lambda: self._set_sb_val())
        self.sd_rgb_blue.valueChanged.connect(lambda: self._set_sb_val())
        # Spin box
        self.sb_rgb_red.valueChanged.connect(lambda: self._set_sd_val())
        self.sb_rgb_green.valueChanged.connect(lambda: self._set_sd_val())
        self.sb_rgb_blue.valueChanged.connect(lambda: self._set_sd_val())
        # hex
        self.le_rgb_hex.textEdited.connect(lambda: self._set_rgb_val_hex())

        # pb dlg
        self.pb_rgb_ok.clicked.connect(lambda: self.OK())
        self.pb_rgb_annuler.clicked.connect(lambda: self.close())
    def IN_ACT(self):
        pass
    def IN_WG_BASE(self):
        # Frame colors
        self.fr_rgb_colors.setFixedWidth(250)

        # slider / spin box
        self.sd_rgb_red.setValue(1)
        self.sd_rgb_red.setValue(0)

        self.sd_rgb_red.setValue(self.rgb[0])
        self.sd_rgb_green.setValue(self.rgb[1])
        self.sd_rgb_blue.setValue(self.rgb[2])
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
    def __set_fr_color(self):
        rgb = self.sd_rgb_red.value(), self.sd_rgb_green.value(), self.sd_rgb_blue.value()
        _rgb = rgb + (255, )

        rgb_red_1 = 0, rgb[1], rgb[2], 255
        rgb_red_2 = 255, rgb[1], rgb[2], 255

        rgb_green_1 = rgb[0], 0, rgb[2], 255
        rgb_green_2 = rgb[0], 255, rgb[2], 255

        rgb_blue_1 = rgb[0], rgb[1], 0, 255
        rgb_blue_2 = rgb[0], rgb[1], 255, 255

        self.le_rgb_hex.setText(Fct().RGB_HEX(rgb=rgb))

        Frame.palette_rgb(self.fr_rgb_colors, rgb=_rgb)
        Slider.rgb(self.sd_rgb_red, rgb=_rgb, rgb_1=rgb_red_1, rgb_2=rgb_red_2)
        Slider.rgb(self.sd_rgb_green, rgb=_rgb, rgb_1=rgb_green_1, rgb_2=rgb_green_2)
        Slider.rgb(self.sd_rgb_blue, rgb=_rgb, rgb_1=rgb_blue_1, rgb_2=rgb_blue_2)
    def _set_sb_val(self):
        self.sb_rgb_red.setValue(self.sd_rgb_red.value())
        self.sb_rgb_green.setValue(self.sd_rgb_green.value())
        self.sb_rgb_blue.setValue(self.sd_rgb_blue.value())

        self.__set_fr_color()
    def _set_sd_val(self):
        self.sd_rgb_red.setValue(self.sb_rgb_red.value())
        self.sd_rgb_green.setValue(self.sb_rgb_green.value())
        self.sd_rgb_blue.setValue(self.sb_rgb_blue.value())
    def _set_rgb_val_hex(self):
        hex_colors = self.le_rgb_hex.text()

        try: rgb = Fct().HEX_RGB(hex_colors=hex_colors)
        except: return

        if len(rgb) == 3:
            r = rgb[0]
            g = rgb[1]
            b = rgb[2]

            self.sb_rgb_red.setValue(r)
            self.sb_rgb_green.setValue(g)
            self.sb_rgb_blue.setValue(b)

            self.sd_rgb_red.setValue(r)
            self.sd_rgb_green.setValue(g)
            self.sd_rgb_blue.setValue(b)
    #####################
    ##    /ACTIONS     ##
    #####################


    #######################
    ##     FONCTIONS     ##
    #######################
    def OK(self):
        self.rep = True
        self.rgb_rtn = (self.sd_rgb_red.value(), self.sd_rgb_green.value(), self.sd_rgb_blue.value())
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
