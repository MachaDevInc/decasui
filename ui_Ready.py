# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\DecasUI\DecasUI\Ready.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow2):
        MainWindow2.setObjectName("MainWindow2")
        MainWindow2.resize(1024, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow2)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("d:\\DecasUI\\DecasUI\\pics/Standby.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(370, 340, 261, 50))
        self.label_2.setObjectName("label_2")
        self.setting = QtWidgets.QPushButton(self.centralwidget)
        self.setting.setGeometry(QtCore.QRect(170, 440, 100, 100))
        self.setting.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("d:\\DecasUI\\DecasUI\\pics/1 (90 × 90 px) (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setting.setIcon(icon)
        self.setting.setIconSize(QtCore.QSize(100, 100))
        self.setting.setFlat(True)
        self.setting.setObjectName("setting")
        self.work = QtWidgets.QPushButton(self.centralwidget)
        self.work.setGeometry(QtCore.QRect(30, 440, 100, 100))
        self.work.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("d:\\DecasUI\\DecasUI\\pics/1 (90 × 90 px) (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.work.setIcon(icon1)
        self.work.setIconSize(QtCore.QSize(100, 100))
        self.work.setFlat(True)
        self.work.setObjectName("work")
        self.connection = QtWidgets.QPushButton(self.centralwidget)
        self.connection.setGeometry(QtCore.QRect(890, 440, 100, 100))
        self.connection.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("d:\\DecasUI\\DecasUI\\pics/cokk.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.connection.setIcon(icon2)
        self.connection.setIconSize(QtCore.QSize(100, 100))
        self.connection.setFlat(True)
        self.connection.setObjectName("connection")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(380, 70, 250, 250))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("d:\\DecasUI\\DecasUI\\pics/1 (400 × 400 px) (400 × 400 px).png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.time_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.time_2.setGeometry(QtCore.QRect(920, 70, 131, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.time_2.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.time_2.setFont(font)
        self.time_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.time_2.setReadOnly(True)
        self.time_2.setObjectName("time_2")
        self.date = QtWidgets.QTextEdit(self.centralwidget)
        self.date.setEnabled(True)
        self.date.setGeometry(QtCore.QRect(30, 30, 130, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.date.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.date.setFont(font)
        self.date.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.date.setReadOnly(True)
        self.date.setObjectName("date")
        self.time = QtWidgets.QTextEdit(self.centralwidget)
        self.time.setGeometry(QtCore.QRect(850, 30, 131, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.time.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.time.setFont(font)
        self.time.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.time.setReadOnly(True)
        self.time.setObjectName("time")
        MainWindow2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 17))
        self.menubar.setObjectName("menubar")
        MainWindow2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow2)
        self.statusbar.setObjectName("statusbar")
        MainWindow2.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow2)

    def retranslateUi(self, MainWindow2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow2.setWindowTitle(_translate("MainWindow2", "MainWindow"))
        self.label_2.setText(_translate("MainWindow2", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Device is Ready</span></p></body></html>"))
