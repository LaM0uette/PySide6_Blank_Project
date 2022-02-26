from PySide6 import QtCore, QtWidgets, QtGui

from ... import msg_ui
from .....build import *
from .....In_classe import In_classe


class MsgApp(msg_ui.Ui_Msg, QtWidgets.QDialog):
    dragPos: QtCore.QPoint

    def __init__(self,
                 titre,
                 msg,
                 ico,
                 tm,
                 txt_pb_ok,
                 width,
                 height,
                 opacity,
    ):
        super(MsgApp, self).__init__()

        self.titre = titre
        self.msg = msg
        self.ico = ico
        self.tm = tm
        self.txt_pb_ok = txt_pb_ok
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
        Frame.Menu_bottom_dlg(self.fr_msg_bottom)
        ### /QFrame ###


        ### QLabel ###
        Label.Base_tr(self.lb_msg_text)
        ### /QLabel ###


        ### QPushButton ###
        PushButton.dlg_ok(self.pb_msg_ok)
        ### /QPushButton ###

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
        self.lb_msg_text.setText(self.msg)

        # pb dlg
        self.pb_msg_ok.setText(self.txt_pb_ok)
        self.pb_msg_ok.setDefault(True)
    def IN_CONNECTIONS(self):
        ## Menu_top
        self.pb_mt_quitter.clicked.connect(lambda: self.close())

        # pb dlg
        self.pb_msg_ok.clicked.connect(lambda: self.close())
    def IN_ACT(self):
        pass
    def IN_WG_BASE(self):
        pass
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
