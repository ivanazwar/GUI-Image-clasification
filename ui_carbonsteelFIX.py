# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'carbonsteelclasification3.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QProgressBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1521, 820)
        font = QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color:rgb(255, 255, 255)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.main_widget = QWidget(self.centralwidget)
        self.main_widget.setObjectName(u"main_widget")
        self.main_widget.setGeometry(QRect(0, 50, 1841, 741))
        self.main_widget.setStyleSheet(u"background-color: rgb(244, 246, 255);")
        self.widget = QWidget(self.main_widget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 1841, 41))
        self.widget.setStyleSheet(u"background-color: rgb(243, 198, 35);")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(630, 8, 71, 31))
        self.label.setPixmap(QPixmap(u":/res/icon/Logo-its-biru-transparan.png"))
        self.label.setScaledContents(True)
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(710, 8, 41, 31))
        self.label_4.setPixmap(QPixmap(u":/res/icon/1542522165-1elektro.png"))
        self.label_4.setScaledContents(True)
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(770, 10, 91, 31))
        self.label_5.setPixmap(QPixmap(u":/res/icon/logo_image_1631632938.png"))
        self.label_5.setScaledContents(True)
        self.widget_4 = QWidget(self.main_widget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(450, 60, 561, 501))
        self.widget_4.setStyleSheet(u"QWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"}")
        self.widget_6 = QWidget(self.widget_4)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(0, 0, 561, 41))
        self.widget_6.setStyleSheet(u"QWidget{\n"
"background-color: #E85C0D;\n"
"    border-top-left-radius: 15px;\n"
"    border-top-right-radius: 15px;\n"
"    border-bottom-right-radius: 0;\n"
"    border-bottom-left-radius: 0;\n"
"}")
        self.widget_7 = QWidget(self.widget_6)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setGeometry(QRect(20, 700, 521, 711))
        self.widget_7.setStyleSheet(u"QWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 35px;\n"
"}")
        self.label_13 = QLabel(self.widget_7)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 30, 511, 431))
        self.label_13.setPixmap(QPixmap(u":/res/icon/Please insert Image.png"))
        self.label_13.setAlignment(Qt.AlignCenter)
        self.pb_insertimage_13 = QPushButton(self.widget_7)
        self.pb_insertimage_13.setObjectName(u"pb_insertimage_13")
        self.pb_insertimage_13.setGeometry(QRect(20, 470, 491, 51))
        font1 = QFont()
        font1.setFamilies([u"Comic Sans MS"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.pb_insertimage_13.setFont(font1)
        self.pb_insertimage_13.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"border:none;\n"
"background-color: rgb(235, 131, 23);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"color:white;\n"
"background-color: #F3C623\n"
"\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/res/icon/photo (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_insertimage_13.setIcon(icon)
        self.pb_insertimage_13.setIconSize(QSize(30, 30))
        self.pb_insertimage_13.setCheckable(True)
        self.pb_insertimage_13.setAutoExclusive(True)
        self.pb_insertimage_14 = QPushButton(self.widget_7)
        self.pb_insertimage_14.setObjectName(u"pb_insertimage_14")
        self.pb_insertimage_14.setGeometry(QRect(20, 530, 491, 51))
        self.pb_insertimage_14.setFont(font1)
        self.pb_insertimage_14.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"border:none;\n"
"background-color: #2C7865;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"color:white;\n"
"background-color: #4CCD99\n"
"\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/res/icon/image.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_insertimage_14.setIcon(icon1)
        self.pb_insertimage_14.setIconSize(QSize(30, 30))
        self.pb_insertimage_14.setCheckable(True)
        self.pb_insertimage_14.setAutoExclusive(True)
        self.pb_insertimage_15 = QPushButton(self.widget_7)
        self.pb_insertimage_15.setObjectName(u"pb_insertimage_15")
        self.pb_insertimage_15.setGeometry(QRect(20, 590, 491, 101))
        self.pb_insertimage_15.setFont(font1)
        self.pb_insertimage_15.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"border:none;\n"
"background-color: #821131;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"color:white;\n"
"background-color: #C7253E\n"
"\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/res/icon/image-processing.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_insertimage_15.setIcon(icon2)
        self.pb_insertimage_15.setIconSize(QSize(60, 60))
        self.pb_insertimage_15.setCheckable(True)
        self.pb_insertimage_15.setAutoExclusive(True)
        self.label_14 = QLabel(self.widget_7)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(520, 200, 511, 431))
        self.label_14.setPixmap(QPixmap(u":/res/icon/Please insert Image.png"))
        self.label_14.setAlignment(Qt.AlignCenter)
        self.label_8 = QLabel(self.widget_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(230, 0, 91, 41))
        font2 = QFont()
        font2.setPointSize(17)
        font2.setBold(True)
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_9 = QLabel(self.widget_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 60, 531, 351))
        self.label_9.setPixmap(QPixmap(u":/res/icon/efearg.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setAlignment(Qt.AlignCenter)
        self.lblimg_resultimage = QLabel(self.widget_4)
        self.lblimg_resultimage.setObjectName(u"lblimg_resultimage")
        self.lblimg_resultimage.setGeometry(QRect(30, 70, 511, 331))
        self.lblimg_resultimage.setPixmap(QPixmap(u":/res/icon/Teks paragraf Anda.png"))
        self.lblimg_resultimage.setScaledContents(True)
        self.lblimg_resultimage.setAlignment(Qt.AlignCenter)
        self.label_11 = QLabel(self.widget_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 420, 191, 51))
        font3 = QFont()
        font3.setFamilies([u"Yu Gothic UI Semibold"])
        font3.setPointSize(14)
        font3.setBold(True)
        self.label_11.setFont(font3)
        self.label_11.setLayoutDirection(Qt.RightToLeft)
        self.label_11.setAutoFillBackground(False)
        self.label_11.setStyleSheet(u"\n"
"color: rgb(166, 166, 166);")
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lbl_resultPrediction = QLabel(self.widget_4)
        self.lbl_resultPrediction.setObjectName(u"lbl_resultPrediction")
        self.lbl_resultPrediction.setGeometry(QRect(220, 420, 281, 51))
        font4 = QFont()
        font4.setFamilies([u"Yu Gothic UI Semibold"])
        font4.setPointSize(16)
        font4.setBold(True)
        self.lbl_resultPrediction.setFont(font4)
        self.lbl_resultPrediction.setLayoutDirection(Qt.RightToLeft)
        self.lbl_resultPrediction.setAutoFillBackground(False)
        self.lbl_resultPrediction.setStyleSheet(u"\n"
"color: rgb(166, 166, 166);")
        self.lbl_resultPrediction.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_7 = QLabel(self.widget_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 10, 51, 41))
        self.label_7.setFont(font)
        self.label_7.setPixmap(QPixmap(u":/res/icon/performance.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setAlignment(Qt.AlignCenter)
        self.widget_2 = QWidget(self.main_widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(10, 60, 431, 661))
        self.widget_2.setStyleSheet(u"QWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 35px;\n"
"}")
        self.lblimg_insertImage = QLabel(self.widget_2)
        self.lblimg_insertImage.setObjectName(u"lblimg_insertImage")
        self.lblimg_insertImage.setGeometry(QRect(20, 20, 391, 321))
        self.lblimg_insertImage.setStyleSheet(u"")
        self.lblimg_insertImage.setPixmap(QPixmap(u":/res/icon/Please insert Image.png"))
        self.lblimg_insertImage.setScaledContents(True)
        self.lblimg_insertImage.setAlignment(Qt.AlignCenter)
        self.pb_choseimage = QPushButton(self.widget_2)
        self.pb_choseimage.setObjectName(u"pb_choseimage")
        self.pb_choseimage.setGeometry(QRect(20, 360, 391, 41))
        font5 = QFont()
        font5.setFamilies([u"Comic Sans MS"])
        font5.setPointSize(11)
        font5.setBold(True)
        self.pb_choseimage.setFont(font5)
        self.pb_choseimage.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"border:none;\n"
"background-color: rgb(235, 131, 23);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(235, 131, 23);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #F3C623\n"
"}\n"
"\n"
"")
        self.pb_choseimage.setIcon(icon)
        self.pb_choseimage.setIconSize(QSize(25, 25))
        self.pb_choseimage.setCheckable(False)
        self.pb_choseimage.setAutoExclusive(False)
        self.pb_clearimage = QPushButton(self.widget_2)
        self.pb_clearimage.setObjectName(u"pb_clearimage")
        self.pb_clearimage.setGeometry(QRect(20, 420, 391, 41))
        self.pb_clearimage.setFont(font5)
        self.pb_clearimage.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"border:none;\n"
"background-color: #2C7865;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2C7865;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #4CCD99;\n"
"}\n"
"")
        self.pb_clearimage.setIcon(icon1)
        self.pb_clearimage.setIconSize(QSize(25, 25))
        self.pb_clearimage.setCheckable(False)
        self.pb_clearimage.setAutoExclusive(True)
        self.label_6 = QLabel(self.widget_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(520, 200, 511, 431))
        self.label_6.setPixmap(QPixmap(u":/res/icon/Please insert Image.png"))
        self.label_6.setAlignment(Qt.AlignCenter)
        self.tb_treshold = QLineEdit(self.widget_2)
        self.tb_treshold.setObjectName(u"tb_treshold")
        self.tb_treshold.setGeometry(QRect(20, 480, 321, 41))
        font6 = QFont()
        font6.setPointSize(12)
        self.tb_treshold.setFont(font6)
        self.tb_treshold.setStyleSheet(u"QLineEdit {\n"
"        border: 2px solid rgb(84, 84, 84);\n"
"        border-radius: 6px;\n"
"		color :rgb(84, 84, 84);\n"
"        background-color: rgb(255, 255, 255);\n"
"    }\n"
"    QLineEdit:hover {\n"
"        border: 2px solid rgb(48, 50, 62);\n"
"    }\n"
"    QLineEdit:focus {\n"
"        border: 2px solid #D10363; \n"
"		\n"
"	background-color: rgb(227, 227, 227);\n"
"	\n"
"    }\n"
"\n"
"\n"
"\n"
"")
        self.tb_treshold.setAlignment(Qt.AlignCenter)
        self.pb_setTreshold = QPushButton(self.widget_2)
        self.pb_setTreshold.setObjectName(u"pb_setTreshold")
        self.pb_setTreshold.setGeometry(QRect(350, 480, 61, 41))
        self.pb_setTreshold.setFont(font5)
        self.pb_setTreshold.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"border:none;\n"
"background-color: #D10363;\n"
"border-radius:8px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #D10363;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #EB3678;\n"
"}\n"
"")
        self.pb_setTreshold.setIconSize(QSize(30, 30))
        self.pb_setTreshold.setCheckable(False)
        self.pb_setTreshold.setAutoExclusive(False)
        self.pb_processimage = QPushButton(self.widget_2)
        self.pb_processimage.setObjectName(u"pb_processimage")
        self.pb_processimage.setGeometry(QRect(20, 550, 391, 91))
        font7 = QFont()
        font7.setFamilies([u"Comic Sans MS"])
        font7.setPointSize(15)
        font7.setBold(True)
        self.pb_processimage.setFont(font7)
        self.pb_processimage.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"border:none;\n"
"background-color: #821131;\n"
"border-radius:30px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #821131;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #A02334;\n"
"}\n"
"\n"
"")
        self.pb_processimage.setIcon(icon2)
        self.pb_processimage.setIconSize(QSize(60, 60))
        self.pb_processimage.setCheckable(False)
        self.pb_processimage.setAutoExclusive(False)
        self.widget_5 = QWidget(self.main_widget)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(450, 570, 561, 151))
        self.widget_5.setStyleSheet(u"QWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 35px;\n"
"}")
        self.widget_10 = QWidget(self.widget_5)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setGeometry(QRect(0, 0, 41, 151))
        self.widget_10.setStyleSheet(u"QWidget{\n"
"background-color: #10375C;\n"
"    border-top-left-radius: 25px;\n"
"    border-top-right-radius: 0;\n"
"    border-bottom-right-radius: 0;\n"
"    border-bottom-left-radius: 25px;\n"
"}")
        self.widget_11 = QWidget(self.widget_10)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setGeometry(QRect(740, 150, 741, 241))
        self.widget_11.setStyleSheet(u"QWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 35px;\n"
"}")
        self.widget_12 = QWidget(self.widget_10)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setGeometry(QRect(60, 140, 61, 241))
        self.widget_12.setStyleSheet(u"QWidget{\n"
"background-color: #10375C;\n"
"    border-top-left-radius: 35px;\n"
"    border-top-right-radius: 0;\n"
"    border-bottom-right-radius: 0;\n"
"    border-bottom-left-radius: 35px;\n"
"}")
        self.widget_13 = QWidget(self.widget_12)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setGeometry(QRect(740, 150, 741, 241))
        self.widget_13.setStyleSheet(u"QWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 35px;\n"
"}")
        self.widget_14 = QWidget(self.widget_5)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setGeometry(QRect(20, 50, 31, 51))
        self.widget_14.setStyleSheet(u"QWidget{\n"
"background-color: #10375C;\n"
"    border-top-left-radius: 0;\n"
"    border-top-right-radius: 25px;\n"
"    border-bottom-right-radius: 25px;\n"
"    border-bottom-left-radius: 0;\n"
"box-shadow: 0px -3px 5px #a6a6a6;\n"
"\n"
"}\n"
"\n"
"")
        self.widget_15 = QWidget(self.widget_14)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setGeometry(QRect(740, 150, 741, 241))
        self.widget_15.setStyleSheet(u"QWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 35px;\n"
"}")
        self.widget_16 = QWidget(self.widget_14)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setGeometry(QRect(60, 140, 61, 241))
        self.widget_16.setStyleSheet(u"QWidget{\n"
"background-color: #10375C;\n"
"    border-top-left-radius: 35px;\n"
"    border-top-right-radius: 0;\n"
"    border-bottom-right-radius: 0;\n"
"    border-bottom-left-radius: 35px;\n"
"}")
        self.widget_17 = QWidget(self.widget_16)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setGeometry(QRect(740, 150, 741, 241))
        self.widget_17.setStyleSheet(u"QWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 35px;\n"
"}")
        self.label_15 = QLabel(self.widget_5)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(60, 30, 131, 31))
        font8 = QFont()
        font8.setFamilies([u"Yu Gothic UI Semibold"])
        font8.setPointSize(9)
        font8.setBold(True)
        self.label_15.setFont(font8)
        self.label_15.setLayoutDirection(Qt.RightToLeft)
        self.label_15.setAutoFillBackground(False)
        self.label_15.setStyleSheet(u"color: rgb(136, 136, 136)\n"
"")
        self.label_15.setAlignment(Qt.AlignCenter)
        self.label_18 = QLabel(self.widget_5)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(50, 0, 221, 31))
        font9 = QFont()
        font9.setFamilies([u"Yu Gothic UI Semibold"])
        font9.setPointSize(13)
        font9.setBold(True)
        self.label_18.setFont(font9)
        self.label_18.setLayoutDirection(Qt.RightToLeft)
        self.label_18.setAutoFillBackground(False)
        self.label_18.setStyleSheet(u"color: #10375C\n"
"")
        self.label_18.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_16 = QLabel(self.widget_5)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(230, 30, 161, 31))
        self.label_16.setFont(font8)
        self.label_16.setLayoutDirection(Qt.RightToLeft)
        self.label_16.setAutoFillBackground(False)
        self.label_16.setStyleSheet(u"color: rgb(136, 136, 136)\n"
"")
        self.label_16.setAlignment(Qt.AlignCenter)
        self.label_17 = QLabel(self.widget_5)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(420, 30, 131, 31))
        self.label_17.setFont(font8)
        self.label_17.setLayoutDirection(Qt.RightToLeft)
        self.label_17.setAutoFillBackground(False)
        self.label_17.setStyleSheet(u"color: rgb(136, 136, 136)\n"
"")
        self.label_17.setAlignment(Qt.AlignCenter)
        self.lbl_HCS = QLabel(self.widget_5)
        self.lbl_HCS.setObjectName(u"lbl_HCS")
        self.lbl_HCS.setGeometry(QRect(60, 80, 81, 61))
        font10 = QFont()
        font10.setFamilies([u"Yu Gothic UI Semibold"])
        font10.setPointSize(15)
        font10.setBold(True)
        self.lbl_HCS.setFont(font10)
        self.lbl_HCS.setLayoutDirection(Qt.RightToLeft)
        self.lbl_HCS.setAutoFillBackground(False)
        self.lbl_HCS.setStyleSheet(u"color: rgb(136, 136, 136)\n"
"")
        self.lbl_HCS.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lbl_MCS = QLabel(self.widget_5)
        self.lbl_MCS.setObjectName(u"lbl_MCS")
        self.lbl_MCS.setGeometry(QRect(240, 80, 81, 61))
        self.lbl_MCS.setFont(font10)
        self.lbl_MCS.setLayoutDirection(Qt.RightToLeft)
        self.lbl_MCS.setAutoFillBackground(False)
        self.lbl_MCS.setStyleSheet(u"color: rgb(136, 136, 136)\n"
"")
        self.lbl_MCS.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lbl_LCS = QLabel(self.widget_5)
        self.lbl_LCS.setObjectName(u"lbl_LCS")
        self.lbl_LCS.setGeometry(QRect(410, 80, 81, 61))
        self.lbl_LCS.setFont(font10)
        self.lbl_LCS.setLayoutDirection(Qt.RightToLeft)
        self.lbl_LCS.setAutoFillBackground(False)
        self.lbl_LCS.setStyleSheet(u"color: rgb(136, 136, 136)\n"
"")
        self.lbl_LCS.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.widget_8 = QWidget(self.main_widget)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setGeometry(QRect(1020, 60, 441, 661))
        self.widget_8.setStyleSheet(u"QWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"}")
        self.PB_MCS = QProgressBar(self.widget_8)
        self.PB_MCS.setObjectName(u"PB_MCS")
        self.PB_MCS.setGeometry(QRect(20, 440, 381, 21))
        font11 = QFont()
        font11.setPointSize(10)
        font11.setBold(False)
        font11.setStrikeOut(False)
        font11.setKerning(True)
        self.PB_MCS.setFont(font11)
        self.PB_MCS.setStyleSheet(u"QProgressBar {\n"
"    background-color: rgb(200, 200, 200);\n"
"    color: rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"    border-radius: 10px;\n"
"    text-align: center; /* This property does not directly translate to Qt stylesheets */\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    border-radius: 10px;\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 1, y2: 1,\n"
"        stop: 0 rgba(185, 105, 254, 255), \n"
"        stop: 1 rgba(106, 211, 255, 255)\n"
"    );\n"
"}")
        self.PB_MCS.setValue(0)
        self.PB_MCS.setInvertedAppearance(False)
        self.pb_LCS = QProgressBar(self.widget_8)
        self.pb_LCS.setObjectName(u"pb_LCS")
        self.pb_LCS.setGeometry(QRect(20, 510, 381, 21))
        self.pb_LCS.setFont(font11)
        self.pb_LCS.setStyleSheet(u"QProgressBar {\n"
"    background-color: rgb(200, 200, 200);\n"
"       color: rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"\n"
"    border-radius: 10px;\n"
"    text-align: center; /* This property does not directly translate to Qt stylesheets */\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    border-radius: 10px;\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 1, y2: 1,\n"
"		stop: 0 #4a93ff,              /* Bright blue */\n"
"        stop: 0.14 #00b9fe,           /* Cyan */\n"
"        stop: 0.28 #00dbec,           /* Lighter Cyan */\n"
"        stop: 0.42 #00f4cd,           /* Pale turquoise */\n"
"        stop: 0.56 #00ffa4,           /* Mint green */\n"
"        stop: 0.70 #00ff75,           /* Lime green */\n"
"        stop: 0.85 #abff41,           /* Chartreuse green */\n"
"        stop: 1 #ffee00               /* Yellow */\n"
"\n"
"    );\n"
"}")
        self.pb_LCS.setValue(0)
        self.pb_LCS.setInvertedAppearance(False)
        self.pb_HCS = QProgressBar(self.widget_8)
        self.pb_HCS.setObjectName(u"pb_HCS")
        self.pb_HCS.setGeometry(QRect(20, 370, 381, 21))
        self.pb_HCS.setFont(font11)
        self.pb_HCS.setStyleSheet(u"QProgressBar {\n"
"    background-color: rgb(200, 200, 200);\n"
"       color: rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"\n"
"    border-radius: 10px;\n"
"    text-align: center; /* This property does not directly translate to Qt stylesheets */\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    border-radius: 10px;\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 1, y2: 1,\n"
"		stop: 0 rgba(255, 69, 0, 255),   /* Red Orange */\n"
"		stop: 1 rgba(255, 255, 0, 255)   /* Yellow */\n"
"\n"
"    );\n"
"}")
        self.pb_HCS.setValue(0)
        self.pb_HCS.setInvertedAppearance(False)
        self.label_25 = QLabel(self.widget_8)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(20, 340, 181, 21))
        font12 = QFont()
        font12.setFamilies([u"Yu Gothic UI Semibold"])
        font12.setPointSize(12)
        font12.setBold(True)
        self.label_25.setFont(font12)
        self.label_25.setLayoutDirection(Qt.RightToLeft)
        self.label_25.setAutoFillBackground(False)
        self.label_25.setStyleSheet(u"\n"
"color: rgb(16, 55, 92);\n"
"")
        self.label_25.setAlignment(Qt.AlignCenter)
        self.label_26 = QLabel(self.widget_8)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(20, 410, 211, 21))
        self.label_26.setFont(font12)
        self.label_26.setLayoutDirection(Qt.RightToLeft)
        self.label_26.setAutoFillBackground(False)
        self.label_26.setStyleSheet(u"\n"
"color: rgb(16, 55, 92);\n"
"")
        self.label_26.setAlignment(Qt.AlignCenter)
        self.label_27 = QLabel(self.widget_8)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(20, 480, 171, 21))
        self.label_27.setFont(font12)
        self.label_27.setLayoutDirection(Qt.RightToLeft)
        self.label_27.setAutoFillBackground(False)
        self.label_27.setStyleSheet(u"\n"
"color: rgb(16, 55, 92);\n"
"")
        self.label_27.setAlignment(Qt.AlignCenter)
        self.label_28 = QLabel(self.widget_8)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(40, 10, 341, 51))
        font13 = QFont()
        font13.setFamilies([u"LEMON MILK Medium"])
        font13.setPointSize(22)
        font13.setBold(True)
        self.label_28.setFont(font13)
        self.label_28.setLayoutDirection(Qt.RightToLeft)
        self.label_28.setAutoFillBackground(False)
        self.label_28.setStyleSheet(u"\n"
"color: rgb(16, 55, 92);\n"
"")
        self.label_28.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_29 = QLabel(self.widget_8)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(20, 70, 151, 41))
        self.label_29.setFont(font12)
        self.label_29.setLayoutDirection(Qt.RightToLeft)
        self.label_29.setAutoFillBackground(False)
        self.label_29.setStyleSheet(u"\n"
"color: rgb(16, 55, 92);\n"
"")
        self.label_29.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lbl_result = QLabel(self.widget_8)
        self.lbl_result.setObjectName(u"lbl_result")
        self.lbl_result.setGeometry(QRect(20, 560, 411, 71))
        font14 = QFont()
        font14.setFamilies([u"Freehand521 BT"])
        font14.setPointSize(24)
        font14.setBold(True)
        self.lbl_result.setFont(font14)
        self.lbl_result.setLayoutDirection(Qt.LeftToRight)
        self.lbl_result.setAutoFillBackground(False)
        self.lbl_result.setStyleSheet(u"\n"
"color: rgb(16, 55, 92);\n"
"")
        self.lbl_result.setAlignment(Qt.AlignCenter)
        self.lblimg_imagpredicted = QLabel(self.widget_8)
        self.lblimg_imagpredicted.setObjectName(u"lblimg_imagpredicted")
        self.lblimg_imagpredicted.setGeometry(QRect(18, 110, 411, 201))
        self.lblimg_imagpredicted.setAutoFillBackground(False)
        self.lblimg_imagpredicted.setPixmap(QPixmap(u":/res/icon/No source Image.png"))
        self.lblimg_imagpredicted.setAlignment(Qt.AlignCenter)
        self.Header_widget = QWidget(self.centralwidget)
        self.Header_widget.setObjectName(u"Header_widget")
        self.Header_widget.setGeometry(QRect(0, 0, 1841, 51))
        font15 = QFont()
        font15.setPointSize(10)
        self.Header_widget.setFont(font15)
        self.Header_widget.setStyleSheet(u"background-color: rgb(16, 55, 92);")
        self.label_3 = QLabel(self.Header_widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(520, 0, 471, 51))
        font16 = QFont()
        font16.setFamilies([u"Berlin Sans FB Demi"])
        font16.setPointSize(20)
        font16.setBold(True)
        self.label_3.setFont(font16)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1521, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_4.setText("")
        self.label_5.setText("")
        self.label_13.setText("")
        self.pb_insertimage_13.setText(QCoreApplication.translate("MainWindow", u"Chose Image", None))
        self.pb_insertimage_14.setText(QCoreApplication.translate("MainWindow", u"Clear Image", None))
        self.pb_insertimage_15.setText(QCoreApplication.translate("MainWindow", u"Process Image", None))
        self.label_14.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Result", None))
        self.label_9.setText("")
        self.lblimg_resultimage.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Result Prediction:", None))
        self.lbl_resultPrediction.setText(QCoreApplication.translate("MainWindow", u"-------------------------", None))
        self.label_7.setText("")
        self.lblimg_insertImage.setText("")
        self.pb_choseimage.setText(QCoreApplication.translate("MainWindow", u"Chose Image", None))
        self.pb_clearimage.setText(QCoreApplication.translate("MainWindow", u"Clear Image", None))
        self.label_6.setText("")
        self.tb_treshold.setPlaceholderText(QCoreApplication.translate("MainWindow", u" insert probability treshold!", None))
        self.pb_setTreshold.setText(QCoreApplication.translate("MainWindow", u"Set!", None))
        self.pb_processimage.setText(QCoreApplication.translate("MainWindow", u"Process Image", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"High Carbon Steel :", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Prediction Probability", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Medium Carbon Steel :", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Low Carbon Steel :", None))
        self.lbl_HCS.setText(QCoreApplication.translate("MainWindow", u"-----", None))
        self.lbl_MCS.setText(QCoreApplication.translate("MainWindow", u"-----", None))
        self.lbl_LCS.setText(QCoreApplication.translate("MainWindow", u"-----", None))
        self.PB_MCS.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
        self.pb_LCS.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
        self.pb_HCS.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"High Carbon Steel :", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Medium Carbon Steel :", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Low Carbon Steel :", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"RESULT ANALYSIS", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Image Predicted", None))
        self.lbl_result.setText(QCoreApplication.translate("MainWindow", u"-------------------------------", None))
        self.lblimg_imagpredicted.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"CARBON STEEL CLASIFICATION", None))
    # retranslateUi

