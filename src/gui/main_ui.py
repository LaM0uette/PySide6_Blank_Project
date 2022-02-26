# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QDoubleSpinBox, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QListView,
    QListWidget, QListWidgetItem, QPlainTextEdit, QProgressBar,
    QPushButton, QRadioButton, QScrollArea, QSizePolicy,
    QSlider, QSpacerItem, QSpinBox, QTableView,
    QTableWidget, QTableWidgetItem, QTextEdit, QToolBox,
    QTreeView, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_main(object):
    def setupUi(self, main):
        if not main.objectName():
            main.setObjectName(u"main")
        main.resize(841, 792)
        self.vlay_main = QVBoxLayout(main)
        self.vlay_main.setSpacing(0)
        self.vlay_main.setObjectName(u"vlay_main")
        self.vlay_main.setContentsMargins(0, 0, 0, 0)
        self.fr_main = QFrame(main)
        self.fr_main.setObjectName(u"fr_main")
        self.fr_main.setFrameShape(QFrame.StyledPanel)
        self.fr_main.setFrameShadow(QFrame.Raised)
        self.vlay_fr_main = QVBoxLayout(self.fr_main)
        self.vlay_fr_main.setSpacing(0)
        self.vlay_fr_main.setObjectName(u"vlay_fr_main")
        self.vlay_fr_main.setContentsMargins(0, 0, 0, 0)
        self.fr_menu_top = QFrame(self.fr_main)
        self.fr_menu_top.setObjectName(u"fr_menu_top")
        self.hlay_menu_top = QHBoxLayout(self.fr_menu_top)
        self.hlay_menu_top.setSpacing(0)
        self.hlay_menu_top.setObjectName(u"hlay_menu_top")
        self.hlay_menu_top.setContentsMargins(0, 0, 0, 0)
        self.lb_mt_ico = QLabel(self.fr_menu_top)
        self.lb_mt_ico.setObjectName(u"lb_mt_ico")

        self.hlay_menu_top.addWidget(self.lb_mt_ico)

        self.wg_mt_blank = QWidget(self.fr_menu_top)
        self.wg_mt_blank.setObjectName(u"wg_mt_blank")

        self.hlay_menu_top.addWidget(self.wg_mt_blank)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlay_menu_top.addItem(self.horizontalSpacer_2)

        self.lb_mt_nom = QLabel(self.fr_menu_top)
        self.lb_mt_nom.setObjectName(u"lb_mt_nom")

        self.hlay_menu_top.addWidget(self.lb_mt_nom)

        self.horizontalSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlay_menu_top.addItem(self.horizontalSpacer_1)

        self.pb_mt_option = QPushButton(self.fr_menu_top)
        self.pb_mt_option.setObjectName(u"pb_mt_option")

        self.hlay_menu_top.addWidget(self.pb_mt_option)

        self.pb_mt_reduire = QPushButton(self.fr_menu_top)
        self.pb_mt_reduire.setObjectName(u"pb_mt_reduire")

        self.hlay_menu_top.addWidget(self.pb_mt_reduire)

        self.pb_mt_agrandir = QPushButton(self.fr_menu_top)
        self.pb_mt_agrandir.setObjectName(u"pb_mt_agrandir")

        self.hlay_menu_top.addWidget(self.pb_mt_agrandir)

        self.pb_mt_quitter = QPushButton(self.fr_menu_top)
        self.pb_mt_quitter.setObjectName(u"pb_mt_quitter")

        self.hlay_menu_top.addWidget(self.pb_mt_quitter)


        self.vlay_fr_main.addWidget(self.fr_menu_top)

        self.fr_body = QFrame(self.fr_main)
        self.fr_body.setObjectName(u"fr_body")
        self.fr_body.setFrameShape(QFrame.StyledPanel)
        self.fr_body.setFrameShadow(QFrame.Raised)
        self.hlay_body = QVBoxLayout(self.fr_body)
        self.hlay_body.setSpacing(0)
        self.hlay_body.setObjectName(u"hlay_body")
        self.hlay_body.setContentsMargins(0, 0, 0, 0)
        self.sca_main = QScrollArea(self.fr_body)
        self.sca_main.setObjectName(u"sca_main")
        self.sca_main.setWidgetResizable(True)
        self.vlay_wg = QWidget()
        self.vlay_wg.setObjectName(u"vlay_wg")
        self.vlay_wg.setGeometry(QRect(0, 0, 818, 6320))
        self.verticalLayout = QVBoxLayout(self.vlay_wg)
        self.verticalLayout.setSpacing(100)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(100, 50, 100, 50)
        self.fr_ck = QFrame(self.vlay_wg)
        self.fr_ck.setObjectName(u"fr_ck")
        self.vlay_ck = QVBoxLayout(self.fr_ck)
        self.vlay_ck.setSpacing(10)
        self.vlay_ck.setObjectName(u"vlay_ck")
        self.vlay_ck.setContentsMargins(10, 10, 10, 10)
        self.lb_ck_demo = QLabel(self.fr_ck)
        self.lb_ck_demo.setObjectName(u"lb_ck_demo")

        self.vlay_ck.addWidget(self.lb_ck_demo)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.vlay_ck.addItem(self.verticalSpacer_15)

        self.ck_demo_th_1 = QCheckBox(self.fr_ck)
        self.ck_demo_th_1.setObjectName(u"ck_demo_th_1")

        self.vlay_ck.addWidget(self.ck_demo_th_1)

        self.ck_demo_th_2 = QCheckBox(self.fr_ck)
        self.ck_demo_th_2.setObjectName(u"ck_demo_th_2")

        self.vlay_ck.addWidget(self.ck_demo_th_2)

        self.ck_demo_th_3 = QCheckBox(self.fr_ck)
        self.ck_demo_th_3.setObjectName(u"ck_demo_th_3")

        self.vlay_ck.addWidget(self.ck_demo_th_3)

        self.ck_demo_tr_1 = QCheckBox(self.fr_ck)
        self.ck_demo_tr_1.setObjectName(u"ck_demo_tr_1")

        self.vlay_ck.addWidget(self.ck_demo_tr_1)

        self.ck_demo_tr_2 = QCheckBox(self.fr_ck)
        self.ck_demo_tr_2.setObjectName(u"ck_demo_tr_2")

        self.vlay_ck.addWidget(self.ck_demo_tr_2)

        self.ck_demo_tr_3 = QCheckBox(self.fr_ck)
        self.ck_demo_tr_3.setObjectName(u"ck_demo_tr_3")

        self.vlay_ck.addWidget(self.ck_demo_tr_3)


        self.verticalLayout.addWidget(self.fr_ck)

        self.fr_cb = QFrame(self.vlay_wg)
        self.fr_cb.setObjectName(u"fr_cb")
        self.vlay_cb = QVBoxLayout(self.fr_cb)
        self.vlay_cb.setSpacing(10)
        self.vlay_cb.setObjectName(u"vlay_cb")
        self.vlay_cb.setContentsMargins(10, 10, 10, 10)
        self.lb_cb_demo = QLabel(self.fr_cb)
        self.lb_cb_demo.setObjectName(u"lb_cb_demo")

        self.vlay_cb.addWidget(self.lb_cb_demo)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.vlay_cb.addItem(self.verticalSpacer_2)

        self.cb_demo_th = QComboBox(self.fr_cb)
        self.cb_demo_th.addItem("")
        self.cb_demo_th.addItem("")
        self.cb_demo_th.addItem("")
        self.cb_demo_th.addItem("")
        self.cb_demo_th.addItem("")
        self.cb_demo_th.addItem("")
        self.cb_demo_th.addItem("")
        self.cb_demo_th.addItem("")
        self.cb_demo_th.addItem("")
        self.cb_demo_th.addItem("")
        self.cb_demo_th.addItem("")
        self.cb_demo_th.addItem("")
        self.cb_demo_th.addItem("")
        self.cb_demo_th.addItem("")
        self.cb_demo_th.addItem("")
        self.cb_demo_th.addItem("")
        self.cb_demo_th.setObjectName(u"cb_demo_th")

        self.vlay_cb.addWidget(self.cb_demo_th)

        self.cb_demo_tr = QComboBox(self.fr_cb)
        self.cb_demo_tr.addItem("")
        self.cb_demo_tr.addItem("")
        self.cb_demo_tr.addItem("")
        self.cb_demo_tr.addItem("")
        self.cb_demo_tr.addItem("")
        self.cb_demo_tr.addItem("")
        self.cb_demo_tr.addItem("")
        self.cb_demo_tr.addItem("")
        self.cb_demo_tr.addItem("")
        self.cb_demo_tr.addItem("")
        self.cb_demo_tr.addItem("")
        self.cb_demo_tr.addItem("")
        self.cb_demo_tr.addItem("")
        self.cb_demo_tr.addItem("")
        self.cb_demo_tr.addItem("")
        self.cb_demo_tr.addItem("")
        self.cb_demo_tr.setObjectName(u"cb_demo_tr")

        self.vlay_cb.addWidget(self.cb_demo_tr)


        self.verticalLayout.addWidget(self.fr_cb)

        self.fr_de = QFrame(self.vlay_wg)
        self.fr_de.setObjectName(u"fr_de")
        self.vlay_de = QVBoxLayout(self.fr_de)
        self.vlay_de.setSpacing(10)
        self.vlay_de.setObjectName(u"vlay_de")
        self.vlay_de.setContentsMargins(10, 10, 10, 10)
        self.lb_de_demo = QLabel(self.fr_de)
        self.lb_de_demo.setObjectName(u"lb_de_demo")

        self.vlay_de.addWidget(self.lb_de_demo)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.vlay_de.addItem(self.verticalSpacer_12)

        self.de_demo_th = QDateEdit(self.fr_de)
        self.de_demo_th.setObjectName(u"de_demo_th")

        self.vlay_de.addWidget(self.de_demo_th)

        self.de_demo_tr = QDateEdit(self.fr_de)
        self.de_demo_tr.setObjectName(u"de_demo_tr")

        self.vlay_de.addWidget(self.de_demo_tr)


        self.verticalLayout.addWidget(self.fr_de)

        self.fr_fr = QFrame(self.vlay_wg)
        self.fr_fr.setObjectName(u"fr_fr")
        self.vlay_fr = QVBoxLayout(self.fr_fr)
        self.vlay_fr.setSpacing(10)
        self.vlay_fr.setObjectName(u"vlay_fr")
        self.vlay_fr.setContentsMargins(10, 10, 10, 10)
        self.lb_fr_demo = QLabel(self.fr_fr)
        self.lb_fr_demo.setObjectName(u"lb_fr_demo")

        self.vlay_fr.addWidget(self.lb_fr_demo)

        self.verticalSpacer_29 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.vlay_fr.addItem(self.verticalSpacer_29)

        self.fr_demo_th = QFrame(self.fr_fr)
        self.fr_demo_th.setObjectName(u"fr_demo_th")
        self.fr_demo_th.setMinimumSize(QSize(0, 120))
        self.fr_demo_th.setFrameShape(QFrame.StyledPanel)
        self.fr_demo_th.setFrameShadow(QFrame.Raised)

        self.vlay_fr.addWidget(self.fr_demo_th)

        self.fr_demo_cadre = QFrame(self.fr_fr)
        self.fr_demo_cadre.setObjectName(u"fr_demo_cadre")
        self.fr_demo_cadre.setMinimumSize(QSize(0, 120))
        self.fr_demo_cadre.setFrameShape(QFrame.StyledPanel)
        self.fr_demo_cadre.setFrameShadow(QFrame.Raised)

        self.vlay_fr.addWidget(self.fr_demo_cadre)

        self.fr_demo_cadre_hover = QFrame(self.fr_fr)
        self.fr_demo_cadre_hover.setObjectName(u"fr_demo_cadre_hover")
        self.fr_demo_cadre_hover.setMinimumSize(QSize(0, 120))
        self.fr_demo_cadre_hover.setFrameShape(QFrame.StyledPanel)
        self.fr_demo_cadre_hover.setFrameShadow(QFrame.Raised)

        self.vlay_fr.addWidget(self.fr_demo_cadre_hover)


        self.verticalLayout.addWidget(self.fr_fr)

        self.fr_lb = QFrame(self.vlay_wg)
        self.fr_lb.setObjectName(u"fr_lb")
        self.vlay_lb = QVBoxLayout(self.fr_lb)
        self.vlay_lb.setSpacing(10)
        self.vlay_lb.setObjectName(u"vlay_lb")
        self.vlay_lb.setContentsMargins(10, 10, 10, 10)
        self.lb_lb_demo = QLabel(self.fr_lb)
        self.lb_lb_demo.setObjectName(u"lb_lb_demo")

        self.vlay_lb.addWidget(self.lb_lb_demo)

        self.verticalSpacer_28 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.vlay_lb.addItem(self.verticalSpacer_28)

        self.lb_lb_demo_th = QLabel(self.fr_lb)
        self.lb_lb_demo_th.setObjectName(u"lb_lb_demo_th")

        self.vlay_lb.addWidget(self.lb_lb_demo_th)

        self.lb_lb_demo_tr = QLabel(self.fr_lb)
        self.lb_lb_demo_tr.setObjectName(u"lb_lb_demo_tr")

        self.vlay_lb.addWidget(self.lb_lb_demo_tr)


        self.verticalLayout.addWidget(self.fr_lb)

        self.fr_lw = QFrame(self.vlay_wg)
        self.fr_lw.setObjectName(u"fr_lw")
        self.vlay_lw = QVBoxLayout(self.fr_lw)
        self.vlay_lw.setSpacing(10)
        self.vlay_lw.setObjectName(u"vlay_lw")
        self.vlay_lw.setContentsMargins(10, 10, 10, 10)
        self.lb_lw_demo = QLabel(self.fr_lw)
        self.lb_lw_demo.setObjectName(u"lb_lw_demo")

        self.vlay_lw.addWidget(self.lb_lw_demo)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.vlay_lw.addItem(self.verticalSpacer_13)

        self.lv_demo_th = QListView(self.fr_lw)
        self.lv_demo_th.setObjectName(u"lv_demo_th")

        self.vlay_lw.addWidget(self.lv_demo_th)

        self.lw_demo_th = QListWidget(self.fr_lw)
        self.lw_demo_th.setObjectName(u"lw_demo_th")

        self.vlay_lw.addWidget(self.lw_demo_th)

        self.lv_demo_tr = QListView(self.fr_lw)
        self.lv_demo_tr.setObjectName(u"lv_demo_tr")

        self.vlay_lw.addWidget(self.lv_demo_tr)

        self.lw_demo_tr = QListWidget(self.fr_lw)
        self.lw_demo_tr.setObjectName(u"lw_demo_tr")

        self.vlay_lw.addWidget(self.lw_demo_tr)


        self.verticalLayout.addWidget(self.fr_lw)

        self.fr_pg = QFrame(self.vlay_wg)
        self.fr_pg.setObjectName(u"fr_pg")
        self.vlay_pg = QVBoxLayout(self.fr_pg)
        self.vlay_pg.setSpacing(10)
        self.vlay_pg.setObjectName(u"vlay_pg")
        self.vlay_pg.setContentsMargins(10, 10, 10, 10)
        self.lb_pg_demo = QLabel(self.fr_pg)
        self.lb_pg_demo.setObjectName(u"lb_pg_demo")

        self.vlay_pg.addWidget(self.lb_pg_demo)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.vlay_pg.addItem(self.verticalSpacer_17)

        self.pg_demo_th = QProgressBar(self.fr_pg)
        self.pg_demo_th.setObjectName(u"pg_demo_th")
        self.pg_demo_th.setValue(33)

        self.vlay_pg.addWidget(self.pg_demo_th)

        self.pg_demo_tr = QProgressBar(self.fr_pg)
        self.pg_demo_tr.setObjectName(u"pg_demo_tr")
        self.pg_demo_tr.setValue(66)

        self.vlay_pg.addWidget(self.pg_demo_tr)


        self.verticalLayout.addWidget(self.fr_pg)

        self.fr_pb = QFrame(self.vlay_wg)
        self.fr_pb.setObjectName(u"fr_pb")
        self.vlay_pb = QVBoxLayout(self.fr_pb)
        self.vlay_pb.setSpacing(0)
        self.vlay_pb.setObjectName(u"vlay_pb")
        self.vlay_pb.setContentsMargins(10, 10, 10, 10)
        self.lb_pb_demo = QLabel(self.fr_pb)
        self.lb_pb_demo.setObjectName(u"lb_pb_demo")

        self.vlay_pb.addWidget(self.lb_pb_demo)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.vlay_pb.addItem(self.verticalSpacer_14)

        self.pb_demo_txt = QPushButton(self.fr_pb)
        self.pb_demo_txt.setObjectName(u"pb_demo_txt")

        self.vlay_pb.addWidget(self.pb_demo_txt)

        self.verticalSpacer_3 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.vlay_pb.addItem(self.verticalSpacer_3)

        self.pb_demo_txt_inv = QPushButton(self.fr_pb)
        self.pb_demo_txt_inv.setObjectName(u"pb_demo_txt_inv")

        self.vlay_pb.addWidget(self.pb_demo_txt_inv)

        self.verticalSpacer_4 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.vlay_pb.addItem(self.verticalSpacer_4)

        self.pb_demo_th = QPushButton(self.fr_pb)
        self.pb_demo_th.setObjectName(u"pb_demo_th")

        self.vlay_pb.addWidget(self.pb_demo_th)

        self.verticalSpacer_5 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.vlay_pb.addItem(self.verticalSpacer_5)

        self.pb_demo_tr = QPushButton(self.fr_pb)
        self.pb_demo_tr.setObjectName(u"pb_demo_tr")

        self.vlay_pb.addWidget(self.pb_demo_tr)

        self.verticalSpacer_6 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.vlay_pb.addItem(self.verticalSpacer_6)

        self.pb_demo_ck = QPushButton(self.fr_pb)
        self.pb_demo_ck.setObjectName(u"pb_demo_ck")
        self.pb_demo_ck.setCheckable(True)

        self.vlay_pb.addWidget(self.pb_demo_ck)

        self.verticalSpacer_7 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.vlay_pb.addItem(self.verticalSpacer_7)

        self.pb_demo_ck_ico = QPushButton(self.fr_pb)
        self.pb_demo_ck_ico.setObjectName(u"pb_demo_ck_ico")
        self.pb_demo_ck_ico.setCheckable(True)

        self.vlay_pb.addWidget(self.pb_demo_ck_ico)

        self.verticalSpacer_8 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.vlay_pb.addItem(self.verticalSpacer_8)

        self.pb_demo_ico_ck = QPushButton(self.fr_pb)
        self.pb_demo_ico_ck.setObjectName(u"pb_demo_ico_ck")
        self.pb_demo_ico_ck.setCheckable(True)

        self.vlay_pb.addWidget(self.pb_demo_ico_ck)

        self.verticalSpacer_9 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.vlay_pb.addItem(self.verticalSpacer_9)

        self.pb_demo_zoom = QPushButton(self.fr_pb)
        self.pb_demo_zoom.setObjectName(u"pb_demo_zoom")
        self.pb_demo_zoom.setCheckable(True)

        self.vlay_pb.addWidget(self.pb_demo_zoom)

        self.verticalSpacer_10 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.vlay_pb.addItem(self.verticalSpacer_10)

        self.pb_demo_rd = QPushButton(self.fr_pb)
        self.pb_demo_rd.setObjectName(u"pb_demo_rd")

        self.vlay_pb.addWidget(self.pb_demo_rd)

        self.verticalSpacer_11 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.vlay_pb.addItem(self.verticalSpacer_11)

        self.pb_demo_bd = QPushButton(self.fr_pb)
        self.pb_demo_bd.setObjectName(u"pb_demo_bd")

        self.vlay_pb.addWidget(self.pb_demo_bd)


        self.verticalLayout.addWidget(self.fr_pb)

        self.fr_rb = QFrame(self.vlay_wg)
        self.fr_rb.setObjectName(u"fr_rb")
        self.vlay_rb = QVBoxLayout(self.fr_rb)
        self.vlay_rb.setSpacing(10)
        self.vlay_rb.setObjectName(u"vlay_rb")
        self.vlay_rb.setContentsMargins(10, 10, 10, 10)
        self.lb_rb_demo = QLabel(self.fr_rb)
        self.lb_rb_demo.setObjectName(u"lb_rb_demo")

        self.vlay_rb.addWidget(self.lb_rb_demo)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.vlay_rb.addItem(self.verticalSpacer_16)

        self.rb_demo_th_1 = QRadioButton(self.fr_rb)
        self.rb_demo_th_1.setObjectName(u"rb_demo_th_1")

        self.vlay_rb.addWidget(self.rb_demo_th_1)

        self.rb_demo_th_2 = QRadioButton(self.fr_rb)
        self.rb_demo_th_2.setObjectName(u"rb_demo_th_2")

        self.vlay_rb.addWidget(self.rb_demo_th_2)

        self.rb_demo_th_3 = QRadioButton(self.fr_rb)
        self.rb_demo_th_3.setObjectName(u"rb_demo_th_3")

        self.vlay_rb.addWidget(self.rb_demo_th_3)

        self.rb_demo_tr_1 = QRadioButton(self.fr_rb)
        self.rb_demo_tr_1.setObjectName(u"rb_demo_tr_1")

        self.vlay_rb.addWidget(self.rb_demo_tr_1)

        self.rb_demo_tr_2 = QRadioButton(self.fr_rb)
        self.rb_demo_tr_2.setObjectName(u"rb_demo_tr_2")

        self.vlay_rb.addWidget(self.rb_demo_tr_2)

        self.rb_demo_tr_3 = QRadioButton(self.fr_rb)
        self.rb_demo_tr_3.setObjectName(u"rb_demo_tr_3")

        self.vlay_rb.addWidget(self.rb_demo_tr_3)


        self.verticalLayout.addWidget(self.fr_rb)

        self.fr_sd = QFrame(self.vlay_wg)
        self.fr_sd.setObjectName(u"fr_sd")
        self.fr_sd.setFrameShape(QFrame.StyledPanel)
        self.fr_sd.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.fr_sd)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.hsd_demo = QSlider(self.fr_sd)
        self.hsd_demo.setObjectName(u"hsd_demo")
        self.hsd_demo.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.hsd_demo, 2, 1, 1, 1)

        self.vsd_demo = QSlider(self.fr_sd)
        self.vsd_demo.setObjectName(u"vsd_demo")
        self.vsd_demo.setOrientation(Qt.Vertical)

        self.gridLayout.addWidget(self.vsd_demo, 4, 1, 1, 1, Qt.AlignHCenter)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 4, 0, 1, 1)

        self.lb_sd_demo = QLabel(self.fr_sd)
        self.lb_sd_demo.setObjectName(u"lb_sd_demo")

        self.gridLayout.addWidget(self.lb_sd_demo, 0, 0, 1, 3)

        self.verticalSpacer_26 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_26, 1, 0, 1, 3)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 4, 2, 1, 1)

        self.verticalSpacer_27 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_27, 3, 0, 1, 3)


        self.verticalLayout.addWidget(self.fr_sd)

        self.fr_sb = QFrame(self.vlay_wg)
        self.fr_sb.setObjectName(u"fr_sb")
        self.glay_sb = QGridLayout(self.fr_sb)
        self.glay_sb.setSpacing(10)
        self.glay_sb.setObjectName(u"glay_sb")
        self.glay_sb.setContentsMargins(10, 10, 10, 10)
        self.lb_sb_demo = QLabel(self.fr_sb)
        self.lb_sb_demo.setObjectName(u"lb_sb_demo")

        self.glay_sb.addWidget(self.lb_sb_demo, 0, 0, 1, 3)

        self.sb_demo = QSpinBox(self.fr_sb)
        self.sb_demo.setObjectName(u"sb_demo")

        self.glay_sb.addWidget(self.sb_demo, 2, 1, 1, 1)

        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.glay_sb.addItem(self.verticalSpacer_18, 1, 0, 1, 3)

        self.sb_demo_2 = QSpinBox(self.fr_sb)
        self.sb_demo_2.setObjectName(u"sb_demo_2")

        self.glay_sb.addWidget(self.sb_demo_2, 3, 1, 1, 1)

        self.sb_demo_3 = QSpinBox(self.fr_sb)
        self.sb_demo_3.setObjectName(u"sb_demo_3")

        self.glay_sb.addWidget(self.sb_demo_3, 4, 1, 1, 1)

        self.dsb_demo = QDoubleSpinBox(self.fr_sb)
        self.dsb_demo.setObjectName(u"dsb_demo")

        self.glay_sb.addWidget(self.dsb_demo, 5, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.glay_sb.addItem(self.horizontalSpacer_3, 2, 2, 4, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.glay_sb.addItem(self.horizontalSpacer, 2, 0, 4, 1)


        self.verticalLayout.addWidget(self.fr_sb)

        self.fr_tw = QFrame(self.vlay_wg)
        self.fr_tw.setObjectName(u"fr_tw")
        self.vlay_tw = QVBoxLayout(self.fr_tw)
        self.vlay_tw.setSpacing(10)
        self.vlay_tw.setObjectName(u"vlay_tw")
        self.vlay_tw.setContentsMargins(10, 10, 10, 10)
        self.lb_tw_demo = QLabel(self.fr_tw)
        self.lb_tw_demo.setObjectName(u"lb_tw_demo")

        self.vlay_tw.addWidget(self.lb_tw_demo)

        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.vlay_tw.addItem(self.verticalSpacer_19)

        self.tv_demo_th = QTableView(self.fr_tw)
        self.tv_demo_th.setObjectName(u"tv_demo_th")

        self.vlay_tw.addWidget(self.tv_demo_th)

        self.tw_demo_th = QTableWidget(self.fr_tw)
        if (self.tw_demo_th.columnCount() < 12):
            self.tw_demo_th.setColumnCount(12)
        __qtablewidgetitem = QTableWidgetItem()
        self.tw_demo_th.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tw_demo_th.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tw_demo_th.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tw_demo_th.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tw_demo_th.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tw_demo_th.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tw_demo_th.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tw_demo_th.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tw_demo_th.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tw_demo_th.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tw_demo_th.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tw_demo_th.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        if (self.tw_demo_th.rowCount() < 23):
            self.tw_demo_th.setRowCount(23)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tw_demo_th.setVerticalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tw_demo_th.setVerticalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tw_demo_th.setVerticalHeaderItem(2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tw_demo_th.setVerticalHeaderItem(3, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tw_demo_th.setVerticalHeaderItem(4, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tw_demo_th.setVerticalHeaderItem(5, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tw_demo_th.setVerticalHeaderItem(6, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tw_demo_th.setVerticalHeaderItem(7, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tw_demo_th.setVerticalHeaderItem(8, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tw_demo_th.setVerticalHeaderItem(9, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tw_demo_th.setVerticalHeaderItem(10, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tw_demo_th.setVerticalHeaderItem(11, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tw_demo_th.setVerticalHeaderItem(12, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tw_demo_th.setVerticalHeaderItem(13, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tw_demo_th.setVerticalHeaderItem(14, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tw_demo_th.setVerticalHeaderItem(15, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tw_demo_th.setVerticalHeaderItem(16, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tw_demo_th.setVerticalHeaderItem(17, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tw_demo_th.setVerticalHeaderItem(18, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tw_demo_th.setVerticalHeaderItem(19, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tw_demo_th.setVerticalHeaderItem(20, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tw_demo_th.setVerticalHeaderItem(21, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tw_demo_th.setVerticalHeaderItem(22, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tw_demo_th.setItem(0, 0, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tw_demo_th.setItem(0, 1, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tw_demo_th.setItem(0, 2, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tw_demo_th.setItem(1, 0, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tw_demo_th.setItem(1, 1, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tw_demo_th.setItem(1, 2, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tw_demo_th.setItem(1, 3, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tw_demo_th.setItem(2, 0, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tw_demo_th.setItem(2, 1, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tw_demo_th.setItem(2, 2, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tw_demo_th.setItem(2, 3, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tw_demo_th.setItem(2, 5, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tw_demo_th.setItem(2, 6, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tw_demo_th.setItem(3, 0, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tw_demo_th.setItem(3, 1, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tw_demo_th.setItem(3, 2, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tw_demo_th.setItem(3, 3, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tw_demo_th.setItem(3, 6, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.tw_demo_th.setItem(4, 0, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.tw_demo_th.setItem(4, 1, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.tw_demo_th.setItem(4, 2, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.tw_demo_th.setItem(4, 5, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.tw_demo_th.setItem(4, 6, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.tw_demo_th.setItem(7, 6, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.tw_demo_th.setItem(8, 3, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.tw_demo_th.setItem(8, 5, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.tw_demo_th.setItem(8, 6, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.tw_demo_th.setItem(9, 2, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.tw_demo_th.setItem(9, 5, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.tw_demo_th.setItem(9, 6, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.tw_demo_th.setItem(10, 1, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.tw_demo_th.setItem(10, 2, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.tw_demo_th.setItem(10, 3, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.tw_demo_th.setItem(11, 0, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.tw_demo_th.setItem(12, 0, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.tw_demo_th.setItem(13, 0, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.tw_demo_th.setItem(13, 1, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.tw_demo_th.setItem(14, 0, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.tw_demo_th.setItem(14, 2, __qtablewidgetitem73)
        self.tw_demo_th.setObjectName(u"tw_demo_th")

        self.vlay_tw.addWidget(self.tw_demo_th)

        self.tv_demo_tr = QTableView(self.fr_tw)
        self.tv_demo_tr.setObjectName(u"tv_demo_tr")

        self.vlay_tw.addWidget(self.tv_demo_tr)

        self.tw_demo_tr = QTableWidget(self.fr_tw)
        if (self.tw_demo_tr.columnCount() < 12):
            self.tw_demo_tr.setColumnCount(12)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.tw_demo_tr.setHorizontalHeaderItem(0, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.tw_demo_tr.setHorizontalHeaderItem(1, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.tw_demo_tr.setHorizontalHeaderItem(2, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.tw_demo_tr.setHorizontalHeaderItem(3, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.tw_demo_tr.setHorizontalHeaderItem(4, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        self.tw_demo_tr.setHorizontalHeaderItem(5, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.tw_demo_tr.setHorizontalHeaderItem(6, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.tw_demo_tr.setHorizontalHeaderItem(7, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        self.tw_demo_tr.setHorizontalHeaderItem(8, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        self.tw_demo_tr.setHorizontalHeaderItem(9, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        self.tw_demo_tr.setHorizontalHeaderItem(10, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        self.tw_demo_tr.setHorizontalHeaderItem(11, __qtablewidgetitem85)
        if (self.tw_demo_tr.rowCount() < 23):
            self.tw_demo_tr.setRowCount(23)
        __qtablewidgetitem86 = QTableWidgetItem()
        self.tw_demo_tr.setVerticalHeaderItem(0, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        self.tw_demo_tr.setVerticalHeaderItem(1, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        self.tw_demo_tr.setVerticalHeaderItem(2, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        self.tw_demo_tr.setVerticalHeaderItem(3, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        self.tw_demo_tr.setVerticalHeaderItem(4, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        self.tw_demo_tr.setVerticalHeaderItem(5, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        self.tw_demo_tr.setVerticalHeaderItem(6, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        self.tw_demo_tr.setVerticalHeaderItem(7, __qtablewidgetitem93)
        __qtablewidgetitem94 = QTableWidgetItem()
        self.tw_demo_tr.setVerticalHeaderItem(8, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        self.tw_demo_tr.setVerticalHeaderItem(9, __qtablewidgetitem95)
        __qtablewidgetitem96 = QTableWidgetItem()
        self.tw_demo_tr.setVerticalHeaderItem(10, __qtablewidgetitem96)
        __qtablewidgetitem97 = QTableWidgetItem()
        self.tw_demo_tr.setVerticalHeaderItem(11, __qtablewidgetitem97)
        __qtablewidgetitem98 = QTableWidgetItem()
        self.tw_demo_tr.setVerticalHeaderItem(12, __qtablewidgetitem98)
        __qtablewidgetitem99 = QTableWidgetItem()
        self.tw_demo_tr.setVerticalHeaderItem(13, __qtablewidgetitem99)
        __qtablewidgetitem100 = QTableWidgetItem()
        self.tw_demo_tr.setVerticalHeaderItem(14, __qtablewidgetitem100)
        __qtablewidgetitem101 = QTableWidgetItem()
        self.tw_demo_tr.setVerticalHeaderItem(15, __qtablewidgetitem101)
        __qtablewidgetitem102 = QTableWidgetItem()
        self.tw_demo_tr.setVerticalHeaderItem(16, __qtablewidgetitem102)
        __qtablewidgetitem103 = QTableWidgetItem()
        self.tw_demo_tr.setVerticalHeaderItem(17, __qtablewidgetitem103)
        __qtablewidgetitem104 = QTableWidgetItem()
        self.tw_demo_tr.setVerticalHeaderItem(18, __qtablewidgetitem104)
        __qtablewidgetitem105 = QTableWidgetItem()
        self.tw_demo_tr.setVerticalHeaderItem(19, __qtablewidgetitem105)
        __qtablewidgetitem106 = QTableWidgetItem()
        self.tw_demo_tr.setVerticalHeaderItem(20, __qtablewidgetitem106)
        __qtablewidgetitem107 = QTableWidgetItem()
        self.tw_demo_tr.setVerticalHeaderItem(21, __qtablewidgetitem107)
        __qtablewidgetitem108 = QTableWidgetItem()
        self.tw_demo_tr.setVerticalHeaderItem(22, __qtablewidgetitem108)
        __qtablewidgetitem109 = QTableWidgetItem()
        self.tw_demo_tr.setItem(0, 0, __qtablewidgetitem109)
        __qtablewidgetitem110 = QTableWidgetItem()
        self.tw_demo_tr.setItem(0, 1, __qtablewidgetitem110)
        __qtablewidgetitem111 = QTableWidgetItem()
        self.tw_demo_tr.setItem(0, 2, __qtablewidgetitem111)
        __qtablewidgetitem112 = QTableWidgetItem()
        self.tw_demo_tr.setItem(1, 0, __qtablewidgetitem112)
        __qtablewidgetitem113 = QTableWidgetItem()
        self.tw_demo_tr.setItem(1, 1, __qtablewidgetitem113)
        __qtablewidgetitem114 = QTableWidgetItem()
        self.tw_demo_tr.setItem(1, 2, __qtablewidgetitem114)
        __qtablewidgetitem115 = QTableWidgetItem()
        self.tw_demo_tr.setItem(1, 3, __qtablewidgetitem115)
        __qtablewidgetitem116 = QTableWidgetItem()
        self.tw_demo_tr.setItem(2, 0, __qtablewidgetitem116)
        __qtablewidgetitem117 = QTableWidgetItem()
        self.tw_demo_tr.setItem(2, 1, __qtablewidgetitem117)
        __qtablewidgetitem118 = QTableWidgetItem()
        self.tw_demo_tr.setItem(2, 2, __qtablewidgetitem118)
        __qtablewidgetitem119 = QTableWidgetItem()
        self.tw_demo_tr.setItem(2, 3, __qtablewidgetitem119)
        __qtablewidgetitem120 = QTableWidgetItem()
        self.tw_demo_tr.setItem(2, 5, __qtablewidgetitem120)
        __qtablewidgetitem121 = QTableWidgetItem()
        self.tw_demo_tr.setItem(2, 6, __qtablewidgetitem121)
        __qtablewidgetitem122 = QTableWidgetItem()
        self.tw_demo_tr.setItem(3, 0, __qtablewidgetitem122)
        __qtablewidgetitem123 = QTableWidgetItem()
        self.tw_demo_tr.setItem(3, 1, __qtablewidgetitem123)
        __qtablewidgetitem124 = QTableWidgetItem()
        self.tw_demo_tr.setItem(3, 2, __qtablewidgetitem124)
        __qtablewidgetitem125 = QTableWidgetItem()
        self.tw_demo_tr.setItem(3, 3, __qtablewidgetitem125)
        __qtablewidgetitem126 = QTableWidgetItem()
        self.tw_demo_tr.setItem(3, 6, __qtablewidgetitem126)
        __qtablewidgetitem127 = QTableWidgetItem()
        self.tw_demo_tr.setItem(4, 0, __qtablewidgetitem127)
        __qtablewidgetitem128 = QTableWidgetItem()
        self.tw_demo_tr.setItem(4, 1, __qtablewidgetitem128)
        __qtablewidgetitem129 = QTableWidgetItem()
        self.tw_demo_tr.setItem(4, 2, __qtablewidgetitem129)
        __qtablewidgetitem130 = QTableWidgetItem()
        self.tw_demo_tr.setItem(4, 5, __qtablewidgetitem130)
        __qtablewidgetitem131 = QTableWidgetItem()
        self.tw_demo_tr.setItem(4, 6, __qtablewidgetitem131)
        __qtablewidgetitem132 = QTableWidgetItem()
        self.tw_demo_tr.setItem(7, 6, __qtablewidgetitem132)
        __qtablewidgetitem133 = QTableWidgetItem()
        self.tw_demo_tr.setItem(8, 3, __qtablewidgetitem133)
        __qtablewidgetitem134 = QTableWidgetItem()
        self.tw_demo_tr.setItem(8, 5, __qtablewidgetitem134)
        __qtablewidgetitem135 = QTableWidgetItem()
        self.tw_demo_tr.setItem(8, 6, __qtablewidgetitem135)
        __qtablewidgetitem136 = QTableWidgetItem()
        self.tw_demo_tr.setItem(9, 2, __qtablewidgetitem136)
        __qtablewidgetitem137 = QTableWidgetItem()
        self.tw_demo_tr.setItem(9, 5, __qtablewidgetitem137)
        __qtablewidgetitem138 = QTableWidgetItem()
        self.tw_demo_tr.setItem(9, 6, __qtablewidgetitem138)
        __qtablewidgetitem139 = QTableWidgetItem()
        self.tw_demo_tr.setItem(10, 1, __qtablewidgetitem139)
        __qtablewidgetitem140 = QTableWidgetItem()
        self.tw_demo_tr.setItem(10, 2, __qtablewidgetitem140)
        __qtablewidgetitem141 = QTableWidgetItem()
        self.tw_demo_tr.setItem(10, 3, __qtablewidgetitem141)
        __qtablewidgetitem142 = QTableWidgetItem()
        self.tw_demo_tr.setItem(11, 0, __qtablewidgetitem142)
        __qtablewidgetitem143 = QTableWidgetItem()
        self.tw_demo_tr.setItem(12, 0, __qtablewidgetitem143)
        __qtablewidgetitem144 = QTableWidgetItem()
        self.tw_demo_tr.setItem(13, 0, __qtablewidgetitem144)
        __qtablewidgetitem145 = QTableWidgetItem()
        self.tw_demo_tr.setItem(13, 1, __qtablewidgetitem145)
        __qtablewidgetitem146 = QTableWidgetItem()
        self.tw_demo_tr.setItem(14, 0, __qtablewidgetitem146)
        __qtablewidgetitem147 = QTableWidgetItem()
        self.tw_demo_tr.setItem(14, 2, __qtablewidgetitem147)
        self.tw_demo_tr.setObjectName(u"tw_demo_tr")

        self.vlay_tw.addWidget(self.tw_demo_tr)


        self.verticalLayout.addWidget(self.fr_tw)

        self.fr_le = QFrame(self.vlay_wg)
        self.fr_le.setObjectName(u"fr_le")
        self.vlay_le = QVBoxLayout(self.fr_le)
        self.vlay_le.setSpacing(10)
        self.vlay_le.setObjectName(u"vlay_le")
        self.vlay_le.setContentsMargins(10, 10, 10, 10)
        self.lb_le_demo = QLabel(self.fr_le)
        self.lb_le_demo.setObjectName(u"lb_le_demo")

        self.vlay_le.addWidget(self.lb_le_demo)

        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.vlay_le.addItem(self.verticalSpacer_20)

        self.le_demo_th = QLineEdit(self.fr_le)
        self.le_demo_th.setObjectName(u"le_demo_th")

        self.vlay_le.addWidget(self.le_demo_th)

        self.le_demo_tr = QLineEdit(self.fr_le)
        self.le_demo_tr.setObjectName(u"le_demo_tr")

        self.vlay_le.addWidget(self.le_demo_tr)


        self.verticalLayout.addWidget(self.fr_le)

        self.fr_te = QFrame(self.vlay_wg)
        self.fr_te.setObjectName(u"fr_te")
        self.vlay_te = QVBoxLayout(self.fr_te)
        self.vlay_te.setSpacing(10)
        self.vlay_te.setObjectName(u"vlay_te")
        self.vlay_te.setContentsMargins(10, 10, 10, 10)
        self.lb_te_demo = QLabel(self.fr_te)
        self.lb_te_demo.setObjectName(u"lb_te_demo")

        self.vlay_te.addWidget(self.lb_te_demo)

        self.verticalSpacer_21 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.vlay_te.addItem(self.verticalSpacer_21)

        self.te_demo_th = QTextEdit(self.fr_te)
        self.te_demo_th.setObjectName(u"te_demo_th")

        self.vlay_te.addWidget(self.te_demo_th)

        self.te_demo_tr = QTextEdit(self.fr_te)
        self.te_demo_tr.setObjectName(u"te_demo_tr")

        self.vlay_te.addWidget(self.te_demo_tr)


        self.verticalLayout.addWidget(self.fr_te)

        self.fr_pte = QFrame(self.vlay_wg)
        self.fr_pte.setObjectName(u"fr_pte")
        self.vlay_pte = QVBoxLayout(self.fr_pte)
        self.vlay_pte.setSpacing(10)
        self.vlay_pte.setObjectName(u"vlay_pte")
        self.vlay_pte.setContentsMargins(10, 10, 10, 10)
        self.lb_pte_demo = QLabel(self.fr_pte)
        self.lb_pte_demo.setObjectName(u"lb_pte_demo")

        self.vlay_pte.addWidget(self.lb_pte_demo)

        self.verticalSpacer_22 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.vlay_pte.addItem(self.verticalSpacer_22)

        self.pte_demo_th = QPlainTextEdit(self.fr_pte)
        self.pte_demo_th.setObjectName(u"pte_demo_th")

        self.vlay_pte.addWidget(self.pte_demo_th)

        self.pte_demo_tr = QPlainTextEdit(self.fr_pte)
        self.pte_demo_tr.setObjectName(u"pte_demo_tr")

        self.vlay_pte.addWidget(self.pte_demo_tr)


        self.verticalLayout.addWidget(self.fr_pte)

        self.fr_tb = QFrame(self.vlay_wg)
        self.fr_tb.setObjectName(u"fr_tb")
        self.fr_tb.setFrameShape(QFrame.StyledPanel)
        self.fr_tb.setFrameShadow(QFrame.Raised)
        self.vlay_fr_tb = QVBoxLayout(self.fr_tb)
        self.vlay_fr_tb.setSpacing(10)
        self.vlay_fr_tb.setObjectName(u"vlay_fr_tb")
        self.vlay_fr_tb.setContentsMargins(10, 10, 10, 10)
        self.lb_tb_demo = QLabel(self.fr_tb)
        self.lb_tb_demo.setObjectName(u"lb_tb_demo")

        self.vlay_fr_tb.addWidget(self.lb_tb_demo)

        self.verticalSpacer_25 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.vlay_fr_tb.addItem(self.verticalSpacer_25)

        self.tb_demo_th = QToolBox(self.fr_tb)
        self.tb_demo_th.setObjectName(u"tb_demo_th")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 596, 69))
        self.verticalLayout_2 = QVBoxLayout(self.page)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.fr_tb_demo_th_1 = QFrame(self.page)
        self.fr_tb_demo_th_1.setObjectName(u"fr_tb_demo_th_1")
        self.fr_tb_demo_th_1.setFrameShape(QFrame.StyledPanel)
        self.fr_tb_demo_th_1.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.fr_tb_demo_th_1)

        self.tb_demo_th.addItem(self.page, u"Page 1")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 596, 69))
        self.verticalLayout_3 = QVBoxLayout(self.page_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.fr_tb_demo_th_2 = QFrame(self.page_2)
        self.fr_tb_demo_th_2.setObjectName(u"fr_tb_demo_th_2")
        self.fr_tb_demo_th_2.setFrameShape(QFrame.StyledPanel)
        self.fr_tb_demo_th_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.fr_tb_demo_th_2)

        self.tb_demo_th.addItem(self.page_2, u"Page 2")

        self.vlay_fr_tb.addWidget(self.tb_demo_th)

        self.tb_demo_tr = QToolBox(self.fr_tb)
        self.tb_demo_tr.setObjectName(u"tb_demo_tr")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 596, 69))
        self.verticalLayout_4 = QVBoxLayout(self.page_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.fr_tb_demo_tr_1 = QFrame(self.page_3)
        self.fr_tb_demo_tr_1.setObjectName(u"fr_tb_demo_tr_1")
        self.fr_tb_demo_tr_1.setFrameShape(QFrame.StyledPanel)
        self.fr_tb_demo_tr_1.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.fr_tb_demo_tr_1)

        self.tb_demo_tr.addItem(self.page_3, u"Page 1")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setGeometry(QRect(0, 0, 596, 69))
        self.verticalLayout_5 = QVBoxLayout(self.page_4)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.fr_tb_demo_tr_2 = QFrame(self.page_4)
        self.fr_tb_demo_tr_2.setObjectName(u"fr_tb_demo_tr_2")
        self.fr_tb_demo_tr_2.setFrameShape(QFrame.StyledPanel)
        self.fr_tb_demo_tr_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.fr_tb_demo_tr_2)

        self.tb_demo_tr.addItem(self.page_4, u"Page 2")

        self.vlay_fr_tb.addWidget(self.tb_demo_tr)


        self.verticalLayout.addWidget(self.fr_tb)

        self.fr_trw = QFrame(self.vlay_wg)
        self.fr_trw.setObjectName(u"fr_trw")
        self.fr_trw.setFrameShape(QFrame.StyledPanel)
        self.fr_trw.setFrameShadow(QFrame.Raised)
        self.glay_fr_trw = QGridLayout(self.fr_trw)
        self.glay_fr_trw.setObjectName(u"glay_fr_trw")
        self.glay_fr_trw.setHorizontalSpacing(0)
        self.glay_fr_trw.setVerticalSpacing(10)
        self.glay_fr_trw.setContentsMargins(10, 10, 10, 10)
        self.trv_demo_th = QTreeView(self.fr_trw)
        self.trv_demo_th.setObjectName(u"trv_demo_th")

        self.glay_fr_trw.addWidget(self.trv_demo_th, 2, 1, 1, 1)

        self.verticalSpacer_24 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.glay_fr_trw.addItem(self.verticalSpacer_24, 4, 1, 1, 1)

        self.trw_demo_th = QTreeWidget(self.fr_trw)
        self.trw_demo_th.headerItem().setText(0, "")
        __qtreewidgetitem = QTreeWidgetItem(self.trw_demo_th)
        __qtreewidgetitem1 = QTreeWidgetItem(__qtreewidgetitem)
        __qtreewidgetitem2 = QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(self.trw_demo_th)
        QTreeWidgetItem(self.trw_demo_th)
        QTreeWidgetItem(self.trw_demo_th)
        __qtreewidgetitem3 = QTreeWidgetItem(self.trw_demo_th)
        __qtreewidgetitem4 = QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem4)
        QTreeWidgetItem(self.trw_demo_th)
        QTreeWidgetItem(self.trw_demo_th)
        __qtreewidgetitem5 = QTreeWidgetItem(self.trw_demo_th)
        __qtreewidgetitem6 = QTreeWidgetItem(__qtreewidgetitem5)
        __qtreewidgetitem7 = QTreeWidgetItem(__qtreewidgetitem6)
        QTreeWidgetItem(__qtreewidgetitem7)
        QTreeWidgetItem(self.trw_demo_th)
        __qtreewidgetitem8 = QTreeWidgetItem(self.trw_demo_th)
        __qtreewidgetitem9 = QTreeWidgetItem(__qtreewidgetitem8)
        QTreeWidgetItem(__qtreewidgetitem9)
        QTreeWidgetItem(self.trw_demo_th)
        QTreeWidgetItem(self.trw_demo_th)
        QTreeWidgetItem(self.trw_demo_th)
        __qtreewidgetitem10 = QTreeWidgetItem(self.trw_demo_th)
        __qtreewidgetitem11 = QTreeWidgetItem(__qtreewidgetitem10)
        __qtreewidgetitem12 = QTreeWidgetItem(__qtreewidgetitem11)
        __qtreewidgetitem13 = QTreeWidgetItem(__qtreewidgetitem12)
        __qtreewidgetitem14 = QTreeWidgetItem(__qtreewidgetitem13)
        QTreeWidgetItem(__qtreewidgetitem14)
        QTreeWidgetItem(__qtreewidgetitem14)
        QTreeWidgetItem(__qtreewidgetitem14)
        __qtreewidgetitem15 = QTreeWidgetItem(self.trw_demo_th)
        __qtreewidgetitem16 = QTreeWidgetItem(__qtreewidgetitem15)
        QTreeWidgetItem(__qtreewidgetitem16)
        QTreeWidgetItem(self.trw_demo_th)
        QTreeWidgetItem(self.trw_demo_th)
        QTreeWidgetItem(self.trw_demo_th)
        QTreeWidgetItem(self.trw_demo_th)
        QTreeWidgetItem(self.trw_demo_th)
        __qtreewidgetitem17 = QTreeWidgetItem(self.trw_demo_th)
        __qtreewidgetitem18 = QTreeWidgetItem(__qtreewidgetitem17)
        QTreeWidgetItem(__qtreewidgetitem18)
        QTreeWidgetItem(__qtreewidgetitem18)
        __qtreewidgetitem19 = QTreeWidgetItem(__qtreewidgetitem18)
        QTreeWidgetItem(__qtreewidgetitem19)
        QTreeWidgetItem(__qtreewidgetitem19)
        self.trw_demo_th.setObjectName(u"trw_demo_th")

        self.glay_fr_trw.addWidget(self.trw_demo_th, 3, 1, 1, 1)

        self.verticalSpacer_23 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.glay_fr_trw.addItem(self.verticalSpacer_23, 1, 0, 1, 3)

        self.lb_trw_demo = QLabel(self.fr_trw)
        self.lb_trw_demo.setObjectName(u"lb_trw_demo")

        self.glay_fr_trw.addWidget(self.lb_trw_demo, 0, 0, 1, 3)

        self.trw_demo_tr = QTreeWidget(self.fr_trw)
        self.trw_demo_tr.headerItem().setText(0, "")
        __qtreewidgetitem20 = QTreeWidgetItem(self.trw_demo_tr)
        __qtreewidgetitem21 = QTreeWidgetItem(__qtreewidgetitem20)
        __qtreewidgetitem22 = QTreeWidgetItem(__qtreewidgetitem21)
        QTreeWidgetItem(__qtreewidgetitem22)
        QTreeWidgetItem(self.trw_demo_tr)
        QTreeWidgetItem(self.trw_demo_tr)
        QTreeWidgetItem(self.trw_demo_tr)
        __qtreewidgetitem23 = QTreeWidgetItem(self.trw_demo_tr)
        __qtreewidgetitem24 = QTreeWidgetItem(__qtreewidgetitem23)
        QTreeWidgetItem(__qtreewidgetitem24)
        QTreeWidgetItem(self.trw_demo_tr)
        QTreeWidgetItem(self.trw_demo_tr)
        __qtreewidgetitem25 = QTreeWidgetItem(self.trw_demo_tr)
        __qtreewidgetitem26 = QTreeWidgetItem(__qtreewidgetitem25)
        __qtreewidgetitem27 = QTreeWidgetItem(__qtreewidgetitem26)
        QTreeWidgetItem(__qtreewidgetitem27)
        QTreeWidgetItem(self.trw_demo_tr)
        __qtreewidgetitem28 = QTreeWidgetItem(self.trw_demo_tr)
        __qtreewidgetitem29 = QTreeWidgetItem(__qtreewidgetitem28)
        QTreeWidgetItem(__qtreewidgetitem29)
        QTreeWidgetItem(self.trw_demo_tr)
        QTreeWidgetItem(self.trw_demo_tr)
        QTreeWidgetItem(self.trw_demo_tr)
        __qtreewidgetitem30 = QTreeWidgetItem(self.trw_demo_tr)
        __qtreewidgetitem31 = QTreeWidgetItem(__qtreewidgetitem30)
        __qtreewidgetitem32 = QTreeWidgetItem(__qtreewidgetitem31)
        __qtreewidgetitem33 = QTreeWidgetItem(__qtreewidgetitem32)
        __qtreewidgetitem34 = QTreeWidgetItem(__qtreewidgetitem33)
        QTreeWidgetItem(__qtreewidgetitem34)
        QTreeWidgetItem(__qtreewidgetitem34)
        QTreeWidgetItem(__qtreewidgetitem34)
        __qtreewidgetitem35 = QTreeWidgetItem(self.trw_demo_tr)
        __qtreewidgetitem36 = QTreeWidgetItem(__qtreewidgetitem35)
        QTreeWidgetItem(__qtreewidgetitem36)
        QTreeWidgetItem(self.trw_demo_tr)
        QTreeWidgetItem(self.trw_demo_tr)
        QTreeWidgetItem(self.trw_demo_tr)
        QTreeWidgetItem(self.trw_demo_tr)
        QTreeWidgetItem(self.trw_demo_tr)
        __qtreewidgetitem37 = QTreeWidgetItem(self.trw_demo_tr)
        __qtreewidgetitem38 = QTreeWidgetItem(__qtreewidgetitem37)
        QTreeWidgetItem(__qtreewidgetitem38)
        QTreeWidgetItem(__qtreewidgetitem38)
        __qtreewidgetitem39 = QTreeWidgetItem(__qtreewidgetitem38)
        QTreeWidgetItem(__qtreewidgetitem39)
        QTreeWidgetItem(__qtreewidgetitem39)
        self.trw_demo_tr.setObjectName(u"trw_demo_tr")

        self.glay_fr_trw.addWidget(self.trw_demo_tr, 6, 1, 1, 1)

        self.trv_demo_tr = QTreeView(self.fr_trw)
        self.trv_demo_tr.setObjectName(u"trv_demo_tr")

        self.glay_fr_trw.addWidget(self.trv_demo_tr, 5, 1, 1, 1)


        self.verticalLayout.addWidget(self.fr_trw)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.sca_main.setWidget(self.vlay_wg)

        self.hlay_body.addWidget(self.sca_main)


        self.vlay_fr_main.addWidget(self.fr_body)

        self.fr_menu_bottom = QFrame(self.fr_main)
        self.fr_menu_bottom.setObjectName(u"fr_menu_bottom")
        self.hlay_menu_bottom = QHBoxLayout(self.fr_menu_bottom)
        self.hlay_menu_bottom.setSpacing(0)
        self.hlay_menu_bottom.setObjectName(u"hlay_menu_bottom")
        self.hlay_menu_bottom.setContentsMargins(0, 0, 0, 0)
        self.lb_mb_version = QLabel(self.fr_menu_bottom)
        self.lb_mb_version.setObjectName(u"lb_mb_version")

        self.hlay_menu_bottom.addWidget(self.lb_mb_version)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlay_menu_bottom.addItem(self.horizontalSpacer_4)


        self.vlay_fr_main.addWidget(self.fr_menu_bottom)


        self.vlay_main.addWidget(self.fr_main)


        self.retranslateUi(main)

        self.tb_demo_th.setCurrentIndex(1)
        self.tb_demo_tr.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(main)
    # setupUi

    def retranslateUi(self, main):
        self.lb_ck_demo.setText(QCoreApplication.translate("main", u"QCheckBox :", None))
        self.ck_demo_th_1.setText(QCoreApplication.translate("main", u"CheckBox", None))
        self.ck_demo_th_2.setText(QCoreApplication.translate("main", u"CheckBox", None))
        self.ck_demo_th_3.setText(QCoreApplication.translate("main", u"CheckBox", None))
        self.ck_demo_tr_1.setText(QCoreApplication.translate("main", u"CheckBox", None))
        self.ck_demo_tr_2.setText(QCoreApplication.translate("main", u"CheckBox", None))
        self.ck_demo_tr_3.setText(QCoreApplication.translate("main", u"CheckBox", None))
        self.lb_cb_demo.setText(QCoreApplication.translate("main", u"QComboBox :", None))
        self.cb_demo_th.setItemText(0, QCoreApplication.translate("main", u"cb_demo_th", None))
        self.cb_demo_th.setItemText(1, QCoreApplication.translate("main", u"cb_demo_th", None))
        self.cb_demo_th.setItemText(2, QCoreApplication.translate("main", u"cb_demo_th", None))
        self.cb_demo_th.setItemText(3, QCoreApplication.translate("main", u"cb_demo_th", None))
        self.cb_demo_th.setItemText(4, QCoreApplication.translate("main", u"cb_demo_th", None))
        self.cb_demo_th.setItemText(5, QCoreApplication.translate("main", u"cb_demo_th", None))
        self.cb_demo_th.setItemText(6, QCoreApplication.translate("main", u"cb_demo_th", None))
        self.cb_demo_th.setItemText(7, QCoreApplication.translate("main", u"cb_demo_th", None))
        self.cb_demo_th.setItemText(8, QCoreApplication.translate("main", u"cb_demo_th", None))
        self.cb_demo_th.setItemText(9, QCoreApplication.translate("main", u"cb_demo_th", None))
        self.cb_demo_th.setItemText(10, QCoreApplication.translate("main", u"cb_demo_th", None))
        self.cb_demo_th.setItemText(11, QCoreApplication.translate("main", u"cb_demo_th", None))
        self.cb_demo_th.setItemText(12, QCoreApplication.translate("main", u"cb_demo_th", None))
        self.cb_demo_th.setItemText(13, QCoreApplication.translate("main", u"cb_demo_th", None))
        self.cb_demo_th.setItemText(14, QCoreApplication.translate("main", u"cb_demo_th", None))
        self.cb_demo_th.setItemText(15, QCoreApplication.translate("main", u"cb_demo_th", None))

        self.cb_demo_tr.setItemText(0, QCoreApplication.translate("main", u"cb_demo_tr", None))
        self.cb_demo_tr.setItemText(1, QCoreApplication.translate("main", u"cb_demo_tr", None))
        self.cb_demo_tr.setItemText(2, QCoreApplication.translate("main", u"cb_demo_tr", None))
        self.cb_demo_tr.setItemText(3, QCoreApplication.translate("main", u"cb_demo_tr", None))
        self.cb_demo_tr.setItemText(4, QCoreApplication.translate("main", u"cb_demo_tr", None))
        self.cb_demo_tr.setItemText(5, QCoreApplication.translate("main", u"cb_demo_tr", None))
        self.cb_demo_tr.setItemText(6, QCoreApplication.translate("main", u"cb_demo_tr", None))
        self.cb_demo_tr.setItemText(7, QCoreApplication.translate("main", u"cb_demo_tr", None))
        self.cb_demo_tr.setItemText(8, QCoreApplication.translate("main", u"cb_demo_tr", None))
        self.cb_demo_tr.setItemText(9, QCoreApplication.translate("main", u"cb_demo_tr", None))
        self.cb_demo_tr.setItemText(10, QCoreApplication.translate("main", u"cb_demo_tr", None))
        self.cb_demo_tr.setItemText(11, QCoreApplication.translate("main", u"cb_demo_tr", None))
        self.cb_demo_tr.setItemText(12, QCoreApplication.translate("main", u"cb_demo_tr", None))
        self.cb_demo_tr.setItemText(13, QCoreApplication.translate("main", u"cb_demo_tr", None))
        self.cb_demo_tr.setItemText(14, QCoreApplication.translate("main", u"cb_demo_tr", None))
        self.cb_demo_tr.setItemText(15, QCoreApplication.translate("main", u"cb_demo_tr", None))

        self.lb_de_demo.setText(QCoreApplication.translate("main", u"QDateEdit :", None))
        self.lb_fr_demo.setText(QCoreApplication.translate("main", u"QFrame :", None))
        self.lb_lb_demo.setText(QCoreApplication.translate("main", u"QLabel :", None))
        self.lb_lb_demo_th.setText(QCoreApplication.translate("main", u"QLabel th", None))
        self.lb_lb_demo_tr.setText(QCoreApplication.translate("main", u"QLabel tr", None))
        self.lb_lw_demo.setText(QCoreApplication.translate("main", u"QListWidget :", None))
        self.lb_pg_demo.setText(QCoreApplication.translate("main", u"QProgressBar :", None))
        self.lb_pb_demo.setText(QCoreApplication.translate("main", u"QPushButton :", None))
        self.pb_demo_txt.setText(QCoreApplication.translate("main", u"PushButton text", None))
        self.pb_demo_txt_inv.setText(QCoreApplication.translate("main", u"PushButton text invers\u00e9", None))
        self.pb_demo_th.setText(QCoreApplication.translate("main", u"PushButton th", None))
        self.pb_demo_tr.setText(QCoreApplication.translate("main", u"PushButton transparent", None))
        self.pb_demo_ck.setText(QCoreApplication.translate("main", u"PushButton checkable", None))
        self.pb_demo_ck_ico.setText(QCoreApplication.translate("main", u"PushButton checkable avec icone", None))
        self.pb_demo_rd.setText(QCoreApplication.translate("main", u"PushButton rd", None))
        self.pb_demo_bd.setText(QCoreApplication.translate("main", u"PushButton bd", None))
        self.lb_rb_demo.setText(QCoreApplication.translate("main", u"QRadioButton :", None))
        self.rb_demo_th_1.setText(QCoreApplication.translate("main", u"RadioButton", None))
        self.rb_demo_th_2.setText(QCoreApplication.translate("main", u"RadioButton", None))
        self.rb_demo_th_3.setText(QCoreApplication.translate("main", u"RadioButton", None))
        self.rb_demo_tr_1.setText(QCoreApplication.translate("main", u"RadioButton", None))
        self.rb_demo_tr_2.setText(QCoreApplication.translate("main", u"RadioButton", None))
        self.rb_demo_tr_3.setText(QCoreApplication.translate("main", u"RadioButton", None))
        self.lb_sd_demo.setText(QCoreApplication.translate("main", u"QSlider :", None))
        self.lb_sb_demo.setText(QCoreApplication.translate("main", u"QSpinBox / QDoubleSpinBox :", None))
        self.lb_tw_demo.setText(QCoreApplication.translate("main", u"QTableWidget :", None))
        ___qtablewidgetitem = self.tw_demo_th.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("main", u"New Column", None));
        ___qtablewidgetitem1 = self.tw_demo_th.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("main", u"New Column", None));
        ___qtablewidgetitem2 = self.tw_demo_th.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("main", u"New Column", None));
        ___qtablewidgetitem3 = self.tw_demo_th.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("main", u"New Column", None));
        ___qtablewidgetitem4 = self.tw_demo_th.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("main", u"New Column", None));
        ___qtablewidgetitem5 = self.tw_demo_th.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("main", u"New Column", None));
        ___qtablewidgetitem6 = self.tw_demo_th.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("main", u"New Column", None));
        ___qtablewidgetitem7 = self.tw_demo_th.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("main", u"New Column", None));
        ___qtablewidgetitem8 = self.tw_demo_th.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("main", u"New Column", None));
        ___qtablewidgetitem9 = self.tw_demo_th.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("main", u"New Column", None));
        ___qtablewidgetitem10 = self.tw_demo_th.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("main", u"New Column", None));
        ___qtablewidgetitem11 = self.tw_demo_th.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("main", u"New Column", None));
        ___qtablewidgetitem12 = self.tw_demo_th.verticalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("main", u"New Row", None));
        ___qtablewidgetitem13 = self.tw_demo_th.verticalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("main", u"New Row", None));
        ___qtablewidgetitem14 = self.tw_demo_th.verticalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("main", u"New Row", None));
        ___qtablewidgetitem15 = self.tw_demo_th.verticalHeaderItem(3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("main", u"New Row", None));
        ___qtablewidgetitem16 = self.tw_demo_th.verticalHeaderItem(4)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("main", u"New Row", None));
        ___qtablewidgetitem17 = self.tw_demo_th.verticalHeaderItem(5)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("main", u"New Row", None));
        ___qtablewidgetitem18 = self.tw_demo_th.verticalHeaderItem(6)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("main", u"New Row", None));
        ___qtablewidgetitem19 = self.tw_demo_th.verticalHeaderItem(7)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("main", u"New Row", None));
        ___qtablewidgetitem20 = self.tw_demo_th.verticalHeaderItem(8)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("main", u"New Row", None));
        ___qtablewidgetitem21 = self.tw_demo_th.verticalHeaderItem(9)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("main", u"New Row", None));
        ___qtablewidgetitem22 = self.tw_demo_th.verticalHeaderItem(10)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("main", u"New Row", None));
        ___qtablewidgetitem23 = self.tw_demo_th.verticalHeaderItem(11)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("main", u"New Row", None));
        ___qtablewidgetitem24 = self.tw_demo_th.verticalHeaderItem(12)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("main", u"New Row", None));
        ___qtablewidgetitem25 = self.tw_demo_th.verticalHeaderItem(13)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("main", u"New Row", None));
        ___qtablewidgetitem26 = self.tw_demo_th.verticalHeaderItem(14)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("main", u"New Row", None));
        ___qtablewidgetitem27 = self.tw_demo_th.verticalHeaderItem(15)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("main", u"New Row", None));
        ___qtablewidgetitem28 = self.tw_demo_th.verticalHeaderItem(16)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("main", u"New Row", None));
        ___qtablewidgetitem29 = self.tw_demo_th.verticalHeaderItem(17)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("main", u"New Row", None));
        ___qtablewidgetitem30 = self.tw_demo_th.verticalHeaderItem(18)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("main", u"New Row", None));
        ___qtablewidgetitem31 = self.tw_demo_th.verticalHeaderItem(19)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("main", u"New Row", None));
        ___qtablewidgetitem32 = self.tw_demo_th.verticalHeaderItem(20)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("main", u"New Row", None));
        ___qtablewidgetitem33 = self.tw_demo_th.verticalHeaderItem(21)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("main", u"New Row", None));
        ___qtablewidgetitem34 = self.tw_demo_th.verticalHeaderItem(22)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("main", u"New Row", None));

        __sortingEnabled = self.tw_demo_th.isSortingEnabled()
        self.tw_demo_th.setSortingEnabled(False)
        ___qtablewidgetitem35 = self.tw_demo_th.item(0, 0)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("main", u"fdsfsdf", None));
        ___qtablewidgetitem36 = self.tw_demo_th.item(0, 1)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("main", u"sdfsdfsdfsd", None));
        ___qtablewidgetitem37 = self.tw_demo_th.item(0, 2)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("main", u"fdsfdsf", None));
        ___qtablewidgetitem38 = self.tw_demo_th.item(1, 0)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("main", u"vcbfgnbg", None));
        ___qtablewidgetitem39 = self.tw_demo_th.item(1, 1)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("main", u"gfhfhgf", None));
        ___qtablewidgetitem40 = self.tw_demo_th.item(1, 2)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("main", u"dsf", None));
        ___qtablewidgetitem41 = self.tw_demo_th.item(1, 3)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("main", u"fvbccvbvc", None));
        ___qtablewidgetitem42 = self.tw_demo_th.item(2, 0)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("main", u"vcbfgnbg", None));
        ___qtablewidgetitem43 = self.tw_demo_th.item(2, 1)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("main", u"vcbfgnbg", None));
        ___qtablewidgetitem44 = self.tw_demo_th.item(2, 2)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("main", u"hfghgfh", None));
        ___qtablewidgetitem45 = self.tw_demo_th.item(2, 3)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("main", u"bcvbcvb", None));
        ___qtablewidgetitem46 = self.tw_demo_th.item(2, 5)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("main", u"fvbccvbvc", None));
        ___qtablewidgetitem47 = self.tw_demo_th.item(2, 6)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("main", u"fvbccvbvc", None));
        ___qtablewidgetitem48 = self.tw_demo_th.item(3, 0)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("main", u"nhnbv", None));
        ___qtablewidgetitem49 = self.tw_demo_th.item(3, 1)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("main", u"bcvbcvb", None));
        ___qtablewidgetitem50 = self.tw_demo_th.item(3, 2)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("main", u"dsf", None));
        ___qtablewidgetitem51 = self.tw_demo_th.item(3, 3)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("main", u"bcvbcvb", None));
        ___qtablewidgetitem52 = self.tw_demo_th.item(3, 6)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("main", u"fvbccvbvc", None));
        ___qtablewidgetitem53 = self.tw_demo_th.item(4, 0)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("main", u"bcvbcvb", None));
        ___qtablewidgetitem54 = self.tw_demo_th.item(4, 1)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("main", u"bcvbcvb", None));
        ___qtablewidgetitem55 = self.tw_demo_th.item(4, 2)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("main", u"bcvbcvb", None));
        ___qtablewidgetitem56 = self.tw_demo_th.item(4, 5)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("main", u"fvbccvbvc", None));
        ___qtablewidgetitem57 = self.tw_demo_th.item(4, 6)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("main", u"fvbccvbvc", None));
        ___qtablewidgetitem58 = self.tw_demo_th.item(7, 6)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("main", u"bcvbcvb", None));
        ___qtablewidgetitem59 = self.tw_demo_th.item(8, 3)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("main", u"bcvbcvb", None));
        ___qtablewidgetitem60 = self.tw_demo_th.item(8, 5)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("main", u"bcvbcvb", None));
        ___qtablewidgetitem61 = self.tw_demo_th.item(8, 6)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("main", u"bcvbcvb", None));
        ___qtablewidgetitem62 = self.tw_demo_th.item(9, 2)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("main", u"bcvbcvb", None));
        ___qtablewidgetitem63 = self.tw_demo_th.item(9, 5)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("main", u"bcvbcvb", None));
        ___qtablewidgetitem64 = self.tw_demo_th.item(9, 6)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("main", u"bcvbcvb", None));
        ___qtablewidgetitem65 = self.tw_demo_th.item(10, 1)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("main", u"bcvbcvb", None));
        ___qtablewidgetitem66 = self.tw_demo_th.item(10, 2)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("main", u"bcvbcvb", None));
        ___qtablewidgetitem67 = self.tw_demo_th.item(10, 3)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("main", u"bcvbcvb", None));
        ___qtablewidgetitem68 = self.tw_demo_th.item(11, 0)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("main", u"fvbccvbvc", None));
        ___qtablewidgetitem69 = self.tw_demo_th.item(12, 0)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("main", u"fvbccvbvc", None));
        ___qtablewidgetitem70 = self.tw_demo_th.item(13, 0)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("main", u"fvbccvbvc", None));
        ___qtablewidgetitem71 = self.tw_demo_th.item(13, 1)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("main", u"fvbccvbvc", None));
        ___qtablewidgetitem72 = self.tw_demo_th.item(14, 0)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("main", u"fvbccvbvc", None));
        ___qtablewidgetitem73 = self.tw_demo_th.item(14, 2)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("main", u"fvbccvbvc", None));
        self.tw_demo_th.setSortingEnabled(__sortingEnabled)

        ___qtablewidgetitem74 = self.tw_demo_tr.horizontalHeaderItem(0)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("main", u"New Column", None));
        ___qtablewidgetitem75 = self.tw_demo_tr.horizontalHeaderItem(1)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("main", u"New Column", None));
        ___qtablewidgetitem76 = self.tw_demo_tr.horizontalHeaderItem(2)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("main", u"New Column", None));
        ___qtablewidgetitem77 = self.tw_demo_tr.horizontalHeaderItem(3)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("main", u"New Column", None));
        ___qtablewidgetitem78 = self.tw_demo_tr.horizontalHeaderItem(4)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("main", u"New Column", None));
        ___qtablewidgetitem79 = self.tw_demo_tr.horizontalHeaderItem(5)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("main", u"New Column", None));
        ___qtablewidgetitem80 = self.tw_demo_tr.horizontalHeaderItem(6)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("main", u"New Column", None));
        ___qtablewidgetitem81 = self.tw_demo_tr.horizontalHeaderItem(7)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("main", u"New Column", None));
        ___qtablewidgetitem82 = self.tw_demo_tr.horizontalHeaderItem(8)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("main", u"New Column", None));
        ___qtablewidgetitem83 = self.tw_demo_tr.horizontalHeaderItem(9)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("main", u"New Column", None));
        ___qtablewidgetitem84 = self.tw_demo_tr.horizontalHeaderItem(10)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("main", u"New Column", None));
        ___qtablewidgetitem85 = self.tw_demo_tr.horizontalHeaderItem(11)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("main", u"New Column", None));
        ___qtablewidgetitem86 = self.tw_demo_tr.verticalHeaderItem(0)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("main", u"New Row", None));
        ___qtablewidgetitem87 = self.tw_demo_tr.verticalHeaderItem(1)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("main", u"New Row", None));
        ___qtablewidgetitem88 = self.tw_demo_tr.verticalHeaderItem(2)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("main", u"New Row", None));
        ___qtablewidgetitem89 = self.tw_demo_tr.verticalHeaderItem(3)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("main", u"New Row", None));
        ___qtablewidgetitem90 = self.tw_demo_tr.verticalHeaderItem(4)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("main", u"New Row", None));
        ___qtablewidgetitem91 = self.tw_demo_tr.verticalHeaderItem(5)
        ___qtablewidgetitem91.setText(QCoreApplication.translate("main", u"New Row", None));
        ___qtablewidgetitem92 = self.tw_demo_tr.verticalHeaderItem(6)
        ___qtablewidgetitem92.setText(QCoreApplication.translate("main", u"New Row", None));
        ___qtablewidgetitem93 = self.tw_demo_tr.verticalHeaderItem(7)
        ___qtablewidgetitem93.setText(QCoreApplication.translate("main", u"New Row", None));
        ___qtablewidgetitem94 = self.tw_demo_tr.verticalHeaderItem(8)
        ___qtablewidgetitem94.setText(QCoreApplication.translate("main", u"New Row", None));
        ___qtablewidgetitem95 = self.tw_demo_tr.verticalHeaderItem(9)
        ___qtablewidgetitem95.setText(QCoreApplication.translate("main", u"New Row", None));
        ___qtablewidgetitem96 = self.tw_demo_tr.verticalHeaderItem(10)
        ___qtablewidgetitem96.setText(QCoreApplication.translate("main", u"New Row", None));
        ___qtablewidgetitem97 = self.tw_demo_tr.verticalHeaderItem(11)
        ___qtablewidgetitem97.setText(QCoreApplication.translate("main", u"New Row", None));
        ___qtablewidgetitem98 = self.tw_demo_tr.verticalHeaderItem(12)
        ___qtablewidgetitem98.setText(QCoreApplication.translate("main", u"New Row", None));
        ___qtablewidgetitem99 = self.tw_demo_tr.verticalHeaderItem(13)
        ___qtablewidgetitem99.setText(QCoreApplication.translate("main", u"New Row", None));
        ___qtablewidgetitem100 = self.tw_demo_tr.verticalHeaderItem(14)
        ___qtablewidgetitem100.setText(QCoreApplication.translate("main", u"New Row", None));
        ___qtablewidgetitem101 = self.tw_demo_tr.verticalHeaderItem(15)
        ___qtablewidgetitem101.setText(QCoreApplication.translate("main", u"New Row", None));
        ___qtablewidgetitem102 = self.tw_demo_tr.verticalHeaderItem(16)
        ___qtablewidgetitem102.setText(QCoreApplication.translate("main", u"New Row", None));
        ___qtablewidgetitem103 = self.tw_demo_tr.verticalHeaderItem(17)
        ___qtablewidgetitem103.setText(QCoreApplication.translate("main", u"New Row", None));
        ___qtablewidgetitem104 = self.tw_demo_tr.verticalHeaderItem(18)
        ___qtablewidgetitem104.setText(QCoreApplication.translate("main", u"New Row", None));
        ___qtablewidgetitem105 = self.tw_demo_tr.verticalHeaderItem(19)
        ___qtablewidgetitem105.setText(QCoreApplication.translate("main", u"New Row", None));
        ___qtablewidgetitem106 = self.tw_demo_tr.verticalHeaderItem(20)
        ___qtablewidgetitem106.setText(QCoreApplication.translate("main", u"New Row", None));
        ___qtablewidgetitem107 = self.tw_demo_tr.verticalHeaderItem(21)
        ___qtablewidgetitem107.setText(QCoreApplication.translate("main", u"New Row", None));
        ___qtablewidgetitem108 = self.tw_demo_tr.verticalHeaderItem(22)
        ___qtablewidgetitem108.setText(QCoreApplication.translate("main", u"New Row", None));

        __sortingEnabled1 = self.tw_demo_tr.isSortingEnabled()
        self.tw_demo_tr.setSortingEnabled(False)
        ___qtablewidgetitem109 = self.tw_demo_tr.item(0, 0)
        ___qtablewidgetitem109.setText(QCoreApplication.translate("main", u"fdsfsdf", None));
        ___qtablewidgetitem110 = self.tw_demo_tr.item(0, 1)
        ___qtablewidgetitem110.setText(QCoreApplication.translate("main", u"sdfsdfsdfsd", None));
        ___qtablewidgetitem111 = self.tw_demo_tr.item(0, 2)
        ___qtablewidgetitem111.setText(QCoreApplication.translate("main", u"fdsfdsf", None));
        ___qtablewidgetitem112 = self.tw_demo_tr.item(1, 0)
        ___qtablewidgetitem112.setText(QCoreApplication.translate("main", u"vcbfgnbg", None));
        ___qtablewidgetitem113 = self.tw_demo_tr.item(1, 1)
        ___qtablewidgetitem113.setText(QCoreApplication.translate("main", u"gfhfhgf", None));
        ___qtablewidgetitem114 = self.tw_demo_tr.item(1, 2)
        ___qtablewidgetitem114.setText(QCoreApplication.translate("main", u"dsf", None));
        ___qtablewidgetitem115 = self.tw_demo_tr.item(1, 3)
        ___qtablewidgetitem115.setText(QCoreApplication.translate("main", u"fvbccvbvc", None));
        ___qtablewidgetitem116 = self.tw_demo_tr.item(2, 0)
        ___qtablewidgetitem116.setText(QCoreApplication.translate("main", u"vcbfgnbg", None));
        ___qtablewidgetitem117 = self.tw_demo_tr.item(2, 1)
        ___qtablewidgetitem117.setText(QCoreApplication.translate("main", u"vcbfgnbg", None));
        ___qtablewidgetitem118 = self.tw_demo_tr.item(2, 2)
        ___qtablewidgetitem118.setText(QCoreApplication.translate("main", u"hfghgfh", None));
        ___qtablewidgetitem119 = self.tw_demo_tr.item(2, 3)
        ___qtablewidgetitem119.setText(QCoreApplication.translate("main", u"bcvbcvb", None));
        ___qtablewidgetitem120 = self.tw_demo_tr.item(2, 5)
        ___qtablewidgetitem120.setText(QCoreApplication.translate("main", u"fvbccvbvc", None));
        ___qtablewidgetitem121 = self.tw_demo_tr.item(2, 6)
        ___qtablewidgetitem121.setText(QCoreApplication.translate("main", u"fvbccvbvc", None));
        ___qtablewidgetitem122 = self.tw_demo_tr.item(3, 0)
        ___qtablewidgetitem122.setText(QCoreApplication.translate("main", u"nhnbv", None));
        ___qtablewidgetitem123 = self.tw_demo_tr.item(3, 1)
        ___qtablewidgetitem123.setText(QCoreApplication.translate("main", u"bcvbcvb", None));
        ___qtablewidgetitem124 = self.tw_demo_tr.item(3, 2)
        ___qtablewidgetitem124.setText(QCoreApplication.translate("main", u"dsf", None));
        ___qtablewidgetitem125 = self.tw_demo_tr.item(3, 3)
        ___qtablewidgetitem125.setText(QCoreApplication.translate("main", u"bcvbcvb", None));
        ___qtablewidgetitem126 = self.tw_demo_tr.item(3, 6)
        ___qtablewidgetitem126.setText(QCoreApplication.translate("main", u"fvbccvbvc", None));
        ___qtablewidgetitem127 = self.tw_demo_tr.item(4, 0)
        ___qtablewidgetitem127.setText(QCoreApplication.translate("main", u"bcvbcvb", None));
        ___qtablewidgetitem128 = self.tw_demo_tr.item(4, 1)
        ___qtablewidgetitem128.setText(QCoreApplication.translate("main", u"bcvbcvb", None));
        ___qtablewidgetitem129 = self.tw_demo_tr.item(4, 2)
        ___qtablewidgetitem129.setText(QCoreApplication.translate("main", u"bcvbcvb", None));
        ___qtablewidgetitem130 = self.tw_demo_tr.item(4, 5)
        ___qtablewidgetitem130.setText(QCoreApplication.translate("main", u"fvbccvbvc", None));
        ___qtablewidgetitem131 = self.tw_demo_tr.item(4, 6)
        ___qtablewidgetitem131.setText(QCoreApplication.translate("main", u"fvbccvbvc", None));
        ___qtablewidgetitem132 = self.tw_demo_tr.item(7, 6)
        ___qtablewidgetitem132.setText(QCoreApplication.translate("main", u"bcvbcvb", None));
        ___qtablewidgetitem133 = self.tw_demo_tr.item(8, 3)
        ___qtablewidgetitem133.setText(QCoreApplication.translate("main", u"bcvbcvb", None));
        ___qtablewidgetitem134 = self.tw_demo_tr.item(8, 5)
        ___qtablewidgetitem134.setText(QCoreApplication.translate("main", u"bcvbcvb", None));
        ___qtablewidgetitem135 = self.tw_demo_tr.item(8, 6)
        ___qtablewidgetitem135.setText(QCoreApplication.translate("main", u"bcvbcvb", None));
        ___qtablewidgetitem136 = self.tw_demo_tr.item(9, 2)
        ___qtablewidgetitem136.setText(QCoreApplication.translate("main", u"bcvbcvb", None));
        ___qtablewidgetitem137 = self.tw_demo_tr.item(9, 5)
        ___qtablewidgetitem137.setText(QCoreApplication.translate("main", u"bcvbcvb", None));
        ___qtablewidgetitem138 = self.tw_demo_tr.item(9, 6)
        ___qtablewidgetitem138.setText(QCoreApplication.translate("main", u"bcvbcvb", None));
        ___qtablewidgetitem139 = self.tw_demo_tr.item(10, 1)
        ___qtablewidgetitem139.setText(QCoreApplication.translate("main", u"bcvbcvb", None));
        ___qtablewidgetitem140 = self.tw_demo_tr.item(10, 2)
        ___qtablewidgetitem140.setText(QCoreApplication.translate("main", u"bcvbcvb", None));
        ___qtablewidgetitem141 = self.tw_demo_tr.item(10, 3)
        ___qtablewidgetitem141.setText(QCoreApplication.translate("main", u"bcvbcvb", None));
        ___qtablewidgetitem142 = self.tw_demo_tr.item(11, 0)
        ___qtablewidgetitem142.setText(QCoreApplication.translate("main", u"fvbccvbvc", None));
        ___qtablewidgetitem143 = self.tw_demo_tr.item(12, 0)
        ___qtablewidgetitem143.setText(QCoreApplication.translate("main", u"fvbccvbvc", None));
        ___qtablewidgetitem144 = self.tw_demo_tr.item(13, 0)
        ___qtablewidgetitem144.setText(QCoreApplication.translate("main", u"fvbccvbvc", None));
        ___qtablewidgetitem145 = self.tw_demo_tr.item(13, 1)
        ___qtablewidgetitem145.setText(QCoreApplication.translate("main", u"fvbccvbvc", None));
        ___qtablewidgetitem146 = self.tw_demo_tr.item(14, 0)
        ___qtablewidgetitem146.setText(QCoreApplication.translate("main", u"fvbccvbvc", None));
        ___qtablewidgetitem147 = self.tw_demo_tr.item(14, 2)
        ___qtablewidgetitem147.setText(QCoreApplication.translate("main", u"fvbccvbvc", None));
        self.tw_demo_tr.setSortingEnabled(__sortingEnabled1)

        self.lb_le_demo.setText(QCoreApplication.translate("main", u"QLineEdit :", None))
        self.le_demo_th.setPlaceholderText(QCoreApplication.translate("main", u"Je suis le text de test...", None))
        self.le_demo_tr.setPlaceholderText(QCoreApplication.translate("main", u"Je suis le text de test...", None))
        self.lb_te_demo.setText(QCoreApplication.translate("main", u"QTextEdit :", None))
        self.te_demo_th.setHtml(QCoreApplication.translate("main", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.te_demo_th.setPlaceholderText(QCoreApplication.translate("main", u"Je suis le text de test...", None))
        self.te_demo_tr.setPlaceholderText(QCoreApplication.translate("main", u"Je suis le text de test...", None))
        self.lb_pte_demo.setText(QCoreApplication.translate("main", u"QPlainText :", None))
        self.pte_demo_th.setPlaceholderText(QCoreApplication.translate("main", u"Je suis le text de test...", None))
        self.pte_demo_tr.setPlaceholderText(QCoreApplication.translate("main", u"Je suis le text de test...", None))
        self.lb_tb_demo.setText(QCoreApplication.translate("main", u"QToolBox :", None))
        self.tb_demo_th.setItemText(self.tb_demo_th.indexOf(self.page), QCoreApplication.translate("main", u"Page 1", None))
        self.tb_demo_th.setItemText(self.tb_demo_th.indexOf(self.page_2), QCoreApplication.translate("main", u"Page 2", None))
        self.tb_demo_tr.setItemText(self.tb_demo_tr.indexOf(self.page_3), QCoreApplication.translate("main", u"Page 1", None))
        self.tb_demo_tr.setItemText(self.tb_demo_tr.indexOf(self.page_4), QCoreApplication.translate("main", u"Page 2", None))

        __sortingEnabled2 = self.trw_demo_th.isSortingEnabled()
        self.trw_demo_th.setSortingEnabled(False)
        ___qtreewidgetitem = self.trw_demo_th.topLevelItem(0)
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("main", u"New Item", None));
        ___qtreewidgetitem1 = ___qtreewidgetitem.child(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("main", u"New Subitem", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("main", u"New Subitem", None));
        ___qtreewidgetitem3 = ___qtreewidgetitem2.child(0)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("main", u"New Subitem", None));
        ___qtreewidgetitem4 = self.trw_demo_th.topLevelItem(1)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("main", u"New Item", None));
        ___qtreewidgetitem5 = self.trw_demo_th.topLevelItem(2)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("main", u"New Item", None));
        ___qtreewidgetitem6 = self.trw_demo_th.topLevelItem(3)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("main", u"New Item", None));
        ___qtreewidgetitem7 = self.trw_demo_th.topLevelItem(4)
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("main", u"New Item", None));
        ___qtreewidgetitem8 = ___qtreewidgetitem7.child(0)
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("main", u"New Subitem", None));
        ___qtreewidgetitem9 = ___qtreewidgetitem8.child(0)
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("main", u"New Subitem", None));
        ___qtreewidgetitem10 = self.trw_demo_th.topLevelItem(5)
        ___qtreewidgetitem10.setText(0, QCoreApplication.translate("main", u"New Item", None));
        ___qtreewidgetitem11 = self.trw_demo_th.topLevelItem(6)
        ___qtreewidgetitem11.setText(0, QCoreApplication.translate("main", u"New Item", None));
        ___qtreewidgetitem12 = self.trw_demo_th.topLevelItem(7)
        ___qtreewidgetitem12.setText(0, QCoreApplication.translate("main", u"New Item", None));
        ___qtreewidgetitem13 = ___qtreewidgetitem12.child(0)
        ___qtreewidgetitem13.setText(0, QCoreApplication.translate("main", u"New Subitem", None));
        ___qtreewidgetitem14 = ___qtreewidgetitem13.child(0)
        ___qtreewidgetitem14.setText(0, QCoreApplication.translate("main", u"New Subitem", None));
        ___qtreewidgetitem15 = ___qtreewidgetitem14.child(0)
        ___qtreewidgetitem15.setText(0, QCoreApplication.translate("main", u"New Subitem", None));
        ___qtreewidgetitem16 = self.trw_demo_th.topLevelItem(8)
        ___qtreewidgetitem16.setText(0, QCoreApplication.translate("main", u"New Item", None));
        ___qtreewidgetitem17 = self.trw_demo_th.topLevelItem(9)
        ___qtreewidgetitem17.setText(0, QCoreApplication.translate("main", u"New Item", None));
        ___qtreewidgetitem18 = ___qtreewidgetitem17.child(0)
        ___qtreewidgetitem18.setText(0, QCoreApplication.translate("main", u"New Subitem", None));
        ___qtreewidgetitem19 = ___qtreewidgetitem18.child(0)
        ___qtreewidgetitem19.setText(0, QCoreApplication.translate("main", u"New Subitem", None));
        ___qtreewidgetitem20 = self.trw_demo_th.topLevelItem(10)
        ___qtreewidgetitem20.setText(0, QCoreApplication.translate("main", u"New Item", None));
        ___qtreewidgetitem21 = self.trw_demo_th.topLevelItem(11)
        ___qtreewidgetitem21.setText(0, QCoreApplication.translate("main", u"New Item", None));
        ___qtreewidgetitem22 = self.trw_demo_th.topLevelItem(12)
        ___qtreewidgetitem22.setText(0, QCoreApplication.translate("main", u"New Item", None));
        ___qtreewidgetitem23 = self.trw_demo_th.topLevelItem(13)
        ___qtreewidgetitem23.setText(0, QCoreApplication.translate("main", u"New Item", None));
        ___qtreewidgetitem24 = ___qtreewidgetitem23.child(0)
        ___qtreewidgetitem24.setText(0, QCoreApplication.translate("main", u"New Subitem", None));
        ___qtreewidgetitem25 = ___qtreewidgetitem24.child(0)
        ___qtreewidgetitem25.setText(0, QCoreApplication.translate("main", u"New Subitem", None));
        ___qtreewidgetitem26 = ___qtreewidgetitem25.child(0)
        ___qtreewidgetitem26.setText(0, QCoreApplication.translate("main", u"New Subitem", None));
        ___qtreewidgetitem27 = ___qtreewidgetitem26.child(0)
        ___qtreewidgetitem27.setText(0, QCoreApplication.translate("main", u"New Subitem", None));
        ___qtreewidgetitem28 = ___qtreewidgetitem27.child(0)
        ___qtreewidgetitem28.setText(0, QCoreApplication.translate("main", u"New Subitem", None));
        ___qtreewidgetitem29 = ___qtreewidgetitem27.child(1)
        ___qtreewidgetitem29.setText(0, QCoreApplication.translate("main", u"New Item", None));
        ___qtreewidgetitem30 = ___qtreewidgetitem27.child(2)
        ___qtreewidgetitem30.setText(0, QCoreApplication.translate("main", u"New Item", None));
        ___qtreewidgetitem31 = self.trw_demo_th.topLevelItem(14)
        ___qtreewidgetitem31.setText(0, QCoreApplication.translate("main", u"New Item", None));
        ___qtreewidgetitem32 = ___qtreewidgetitem31.child(0)
        ___qtreewidgetitem32.setText(0, QCoreApplication.translate("main", u"New Subitem", None));
        ___qtreewidgetitem33 = ___qtreewidgetitem32.child(0)
        ___qtreewidgetitem33.setText(0, QCoreApplication.translate("main", u"New Subitem", None));
        ___qtreewidgetitem34 = self.trw_demo_th.topLevelItem(15)
        ___qtreewidgetitem34.setText(0, QCoreApplication.translate("main", u"New Item", None));
        ___qtreewidgetitem35 = self.trw_demo_th.topLevelItem(16)
        ___qtreewidgetitem35.setText(0, QCoreApplication.translate("main", u"New Item", None));
        ___qtreewidgetitem36 = self.trw_demo_th.topLevelItem(17)
        ___qtreewidgetitem36.setText(0, QCoreApplication.translate("main", u"New Item", None));
        ___qtreewidgetitem37 = self.trw_demo_th.topLevelItem(18)
        ___qtreewidgetitem37.setText(0, QCoreApplication.translate("main", u"New Item", None));
        ___qtreewidgetitem38 = self.trw_demo_th.topLevelItem(19)
        ___qtreewidgetitem38.setText(0, QCoreApplication.translate("main", u"New Item", None));
        ___qtreewidgetitem39 = self.trw_demo_th.topLevelItem(20)
        ___qtreewidgetitem39.setText(0, QCoreApplication.translate("main", u"New Item", None));
        ___qtreewidgetitem40 = ___qtreewidgetitem39.child(0)
        ___qtreewidgetitem40.setText(0, QCoreApplication.translate("main", u"New Subitem", None));
        ___qtreewidgetitem41 = ___qtreewidgetitem40.child(0)
        ___qtreewidgetitem41.setText(0, QCoreApplication.translate("main", u"New Subitem", None));
        ___qtreewidgetitem42 = ___qtreewidgetitem40.child(1)
        ___qtreewidgetitem42.setText(0, QCoreApplication.translate("main", u"New Item", None));
        ___qtreewidgetitem43 = ___qtreewidgetitem40.child(2)
        ___qtreewidgetitem43.setText(0, QCoreApplication.translate("main", u"New Item", None));
        ___qtreewidgetitem44 = ___qtreewidgetitem43.child(0)
        ___qtreewidgetitem44.setText(0, QCoreApplication.translate("main", u"New Subitem", None));
        ___qtreewidgetitem45 = ___qtreewidgetitem43.child(1)
        ___qtreewidgetitem45.setText(0, QCoreApplication.translate("main", u"New Item", None));
        self.trw_demo_th.setSortingEnabled(__sortingEnabled2)

        self.lb_trw_demo.setText(QCoreApplication.translate("main", u"QTreeWidget :", None))

        __sortingEnabled3 = self.trw_demo_tr.isSortingEnabled()
        self.trw_demo_tr.setSortingEnabled(False)
        ___qtreewidgetitem46 = self.trw_demo_tr.topLevelItem(0)
        ___qtreewidgetitem46.setText(0, QCoreApplication.translate("main", u"New Item", None));
        ___qtreewidgetitem47 = ___qtreewidgetitem46.child(0)
        ___qtreewidgetitem47.setText(0, QCoreApplication.translate("main", u"New Subitem", None));
        ___qtreewidgetitem48 = ___qtreewidgetitem47.child(0)
        ___qtreewidgetitem48.setText(0, QCoreApplication.translate("main", u"New Subitem", None));
        ___qtreewidgetitem49 = ___qtreewidgetitem48.child(0)
        ___qtreewidgetitem49.setText(0, QCoreApplication.translate("main", u"New Subitem", None));
        ___qtreewidgetitem50 = self.trw_demo_tr.topLevelItem(1)
        ___qtreewidgetitem50.setText(0, QCoreApplication.translate("main", u"New Item", None));
        ___qtreewidgetitem51 = self.trw_demo_tr.topLevelItem(2)
        ___qtreewidgetitem51.setText(0, QCoreApplication.translate("main", u"New Item", None));
        ___qtreewidgetitem52 = self.trw_demo_tr.topLevelItem(3)
        ___qtreewidgetitem52.setText(0, QCoreApplication.translate("main", u"New Item", None));
        ___qtreewidgetitem53 = self.trw_demo_tr.topLevelItem(4)
        ___qtreewidgetitem53.setText(0, QCoreApplication.translate("main", u"New Item", None));
        ___qtreewidgetitem54 = ___qtreewidgetitem53.child(0)
        ___qtreewidgetitem54.setText(0, QCoreApplication.translate("main", u"New Subitem", None));
        ___qtreewidgetitem55 = ___qtreewidgetitem54.child(0)
        ___qtreewidgetitem55.setText(0, QCoreApplication.translate("main", u"New Subitem", None));
        ___qtreewidgetitem56 = self.trw_demo_tr.topLevelItem(5)
        ___qtreewidgetitem56.setText(0, QCoreApplication.translate("main", u"New Item", None));
        ___qtreewidgetitem57 = self.trw_demo_tr.topLevelItem(6)
        ___qtreewidgetitem57.setText(0, QCoreApplication.translate("main", u"New Item", None));
        ___qtreewidgetitem58 = self.trw_demo_tr.topLevelItem(7)
        ___qtreewidgetitem58.setText(0, QCoreApplication.translate("main", u"New Item", None));
        ___qtreewidgetitem59 = ___qtreewidgetitem58.child(0)
        ___qtreewidgetitem59.setText(0, QCoreApplication.translate("main", u"New Subitem", None));
        ___qtreewidgetitem60 = ___qtreewidgetitem59.child(0)
        ___qtreewidgetitem60.setText(0, QCoreApplication.translate("main", u"New Subitem", None));
        ___qtreewidgetitem61 = ___qtreewidgetitem60.child(0)
        ___qtreewidgetitem61.setText(0, QCoreApplication.translate("main", u"New Subitem", None));
        ___qtreewidgetitem62 = self.trw_demo_tr.topLevelItem(8)
        ___qtreewidgetitem62.setText(0, QCoreApplication.translate("main", u"New Item", None));
        ___qtreewidgetitem63 = self.trw_demo_tr.topLevelItem(9)
        ___qtreewidgetitem63.setText(0, QCoreApplication.translate("main", u"New Item", None));
        ___qtreewidgetitem64 = ___qtreewidgetitem63.child(0)
        ___qtreewidgetitem64.setText(0, QCoreApplication.translate("main", u"New Subitem", None));
        ___qtreewidgetitem65 = ___qtreewidgetitem64.child(0)
        ___qtreewidgetitem65.setText(0, QCoreApplication.translate("main", u"New Subitem", None));
        ___qtreewidgetitem66 = self.trw_demo_tr.topLevelItem(10)
        ___qtreewidgetitem66.setText(0, QCoreApplication.translate("main", u"New Item", None));
        ___qtreewidgetitem67 = self.trw_demo_tr.topLevelItem(11)
        ___qtreewidgetitem67.setText(0, QCoreApplication.translate("main", u"New Item", None));
        ___qtreewidgetitem68 = self.trw_demo_tr.topLevelItem(12)
        ___qtreewidgetitem68.setText(0, QCoreApplication.translate("main", u"New Item", None));
        ___qtreewidgetitem69 = self.trw_demo_tr.topLevelItem(13)
        ___qtreewidgetitem69.setText(0, QCoreApplication.translate("main", u"New Item", None));
        ___qtreewidgetitem70 = ___qtreewidgetitem69.child(0)
        ___qtreewidgetitem70.setText(0, QCoreApplication.translate("main", u"New Subitem", None));
        ___qtreewidgetitem71 = ___qtreewidgetitem70.child(0)
        ___qtreewidgetitem71.setText(0, QCoreApplication.translate("main", u"New Subitem", None));
        ___qtreewidgetitem72 = ___qtreewidgetitem71.child(0)
        ___qtreewidgetitem72.setText(0, QCoreApplication.translate("main", u"New Subitem", None));
        ___qtreewidgetitem73 = ___qtreewidgetitem72.child(0)
        ___qtreewidgetitem73.setText(0, QCoreApplication.translate("main", u"New Subitem", None));
        ___qtreewidgetitem74 = ___qtreewidgetitem73.child(0)
        ___qtreewidgetitem74.setText(0, QCoreApplication.translate("main", u"New Subitem", None));
        ___qtreewidgetitem75 = ___qtreewidgetitem73.child(1)
        ___qtreewidgetitem75.setText(0, QCoreApplication.translate("main", u"New Item", None));
        ___qtreewidgetitem76 = ___qtreewidgetitem73.child(2)
        ___qtreewidgetitem76.setText(0, QCoreApplication.translate("main", u"New Item", None));
        ___qtreewidgetitem77 = self.trw_demo_tr.topLevelItem(14)
        ___qtreewidgetitem77.setText(0, QCoreApplication.translate("main", u"New Item", None));
        ___qtreewidgetitem78 = ___qtreewidgetitem77.child(0)
        ___qtreewidgetitem78.setText(0, QCoreApplication.translate("main", u"New Subitem", None));
        ___qtreewidgetitem79 = ___qtreewidgetitem78.child(0)
        ___qtreewidgetitem79.setText(0, QCoreApplication.translate("main", u"New Subitem", None));
        ___qtreewidgetitem80 = self.trw_demo_tr.topLevelItem(15)
        ___qtreewidgetitem80.setText(0, QCoreApplication.translate("main", u"New Item", None));
        ___qtreewidgetitem81 = self.trw_demo_tr.topLevelItem(16)
        ___qtreewidgetitem81.setText(0, QCoreApplication.translate("main", u"New Item", None));
        ___qtreewidgetitem82 = self.trw_demo_tr.topLevelItem(17)
        ___qtreewidgetitem82.setText(0, QCoreApplication.translate("main", u"New Item", None));
        ___qtreewidgetitem83 = self.trw_demo_tr.topLevelItem(18)
        ___qtreewidgetitem83.setText(0, QCoreApplication.translate("main", u"New Item", None));
        ___qtreewidgetitem84 = self.trw_demo_tr.topLevelItem(19)
        ___qtreewidgetitem84.setText(0, QCoreApplication.translate("main", u"New Item", None));
        ___qtreewidgetitem85 = self.trw_demo_tr.topLevelItem(20)
        ___qtreewidgetitem85.setText(0, QCoreApplication.translate("main", u"New Item", None));
        ___qtreewidgetitem86 = ___qtreewidgetitem85.child(0)
        ___qtreewidgetitem86.setText(0, QCoreApplication.translate("main", u"New Subitem", None));
        ___qtreewidgetitem87 = ___qtreewidgetitem86.child(0)
        ___qtreewidgetitem87.setText(0, QCoreApplication.translate("main", u"New Subitem", None));
        ___qtreewidgetitem88 = ___qtreewidgetitem86.child(1)
        ___qtreewidgetitem88.setText(0, QCoreApplication.translate("main", u"New Item", None));
        ___qtreewidgetitem89 = ___qtreewidgetitem86.child(2)
        ___qtreewidgetitem89.setText(0, QCoreApplication.translate("main", u"New Item", None));
        ___qtreewidgetitem90 = ___qtreewidgetitem89.child(0)
        ___qtreewidgetitem90.setText(0, QCoreApplication.translate("main", u"New Subitem", None));
        ___qtreewidgetitem91 = ___qtreewidgetitem89.child(1)
        ___qtreewidgetitem91.setText(0, QCoreApplication.translate("main", u"New Item", None));
        self.trw_demo_tr.setSortingEnabled(__sortingEnabled3)

        pass
    # retranslateUi

