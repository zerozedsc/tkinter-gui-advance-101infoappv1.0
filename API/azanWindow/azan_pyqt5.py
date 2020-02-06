# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets




class Ui_azanWindow(object):


    def exitWindow(self):
        print("EXIT")
        import main_win
        win = main_win.mainWIN()
        win
        return True
        # win.screenMain.mainloop()

    def setupUi(self, azanWindow):
        azanWindow.setObjectName("azanWindow")
        azanWindow.resize(495, 500)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        azanWindow.setFont(font)
        azanWindow.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(azanWindow)
        self.centralwidget.setObjectName("centralwidget")


        # background function
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 10, 500, 500))
        self.background.setText("")
        self.background.setObjectName("background")


        # exit
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(420, 450, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        self.exitButton.setFont(font)
        self.exitButton.setAutoFillBackground(False)
        self.exitButton.setStyleSheet("")
        self.exitButton.setObjectName("exitButton")
        self.exitButton.clicked.connect(self.exitWindow)

        # subuh func
        self.lcd_Subuh = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_Subuh.setGeometry(QtCore.QRect(230, 370, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Prototype")
        font.setBold(True)
        font.setWeight(75)
        self.lcd_Subuh.setFont(font)
        self.lcd_Subuh.setObjectName("lcd_Subuh")
        self.label_Subuh = QtWidgets.QLabel(self.centralwidget)
        self.label_Subuh.setGeometry(QtCore.QRect(160, 370, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_Subuh.setFont(font)
        self.label_Subuh.setObjectName("label_Subuh")


        # Imsak func
        self.lcd_Imsak = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_Imsak.setGeometry(QtCore.QRect(110, 310, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Prototype")
        font.setBold(True)
        font.setWeight(75)
        self.lcd_Imsak.setFont(font)
        self.lcd_Imsak.setObjectName("lcd_Imsak")
        self.label_Imsak = QtWidgets.QLabel(self.centralwidget)
        self.label_Imsak.setGeometry(QtCore.QRect(47, 310, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_Imsak.setFont(font)
        self.label_Imsak.setObjectName("label_Imsak")


        # syuruk func
        self.lcd_Syuruk = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_Syuruk.setGeometry(QtCore.QRect(360, 310, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Prototype")
        font.setBold(True)
        font.setWeight(75)
        self.lcd_Syuruk.setFont(font)
        self.lcd_Syuruk.setObjectName("lcd_Syuruk")
        self.label_Syuruk = QtWidgets.QLabel(self.centralwidget)
        self.label_Syuruk.setGeometry(QtCore.QRect(285, 310, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_Syuruk.setFont(font)
        self.label_Syuruk.setObjectName("label_Syuruk")


        # zuhur func
        self.lcd_Zuhur = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_Zuhur.setGeometry(QtCore.QRect(360, 240, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Prototype")
        font.setBold(True)
        font.setWeight(75)
        self.lcd_Zuhur.setFont(font)
        self.lcd_Zuhur.setObjectName("lcd_Zuhur")
        self.label_Zuhur = QtWidgets.QLabel(self.centralwidget)
        self.label_Zuhur.setGeometry(QtCore.QRect(295, 240, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_Zuhur.setFont(font)
        self.label_Zuhur.setObjectName("label_Zuhur")


        # asar func
        self.lcd_Asar = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_Asar.setGeometry(QtCore.QRect(360, 170, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Prototype")
        font.setBold(True)
        font.setWeight(75)
        self.lcd_Asar.setFont(font)
        self.lcd_Asar.setObjectName("lcd_Asar")
        self.label_Asar = QtWidgets.QLabel(self.centralwidget)
        self.label_Asar.setGeometry(QtCore.QRect(310, 170, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_Asar.setFont(font)
        self.label_Asar.setObjectName("label_Asar")


       # maghrib func
        self.label_Maghrib = QtWidgets.QLabel(self.centralwidget)
        self.label_Maghrib.setGeometry(QtCore.QRect(20, 170, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_Maghrib.setFont(font)
        self.label_Maghrib.setObjectName("label_Maghrib")
        self.lcd_Maghrib = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_Maghrib.setGeometry(QtCore.QRect(110, 170, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Prototype")
        font.setBold(True)
        font.setWeight(75)
        self.lcd_Maghrib.setFont(font)
        self.lcd_Maghrib.setObjectName("lcd_Maghrib")


        # isyak func
        self.lcd_Isyak = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_Isyak.setGeometry(QtCore.QRect(110, 240, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Prototype")
        font.setBold(True)
        font.setWeight(75)
        self.lcd_Isyak.setFont(font)
        self.lcd_Isyak.setObjectName("lcd_Isyak")
        self.label_Isyak = QtWidgets.QLabel(self.centralwidget)
        self.label_Isyak.setGeometry(QtCore.QRect(50, 240, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_Isyak.setFont(font)
        self.label_Isyak.setObjectName("label_Isyak")


        # state comboBox func
        self.combo_State = QtWidgets.QComboBox(self.centralwidget)
        self.combo_State.setGeometry(QtCore.QRect(210, 60, 151, 22))
        self.combo_State.setObjectName("combo_State")
        self.combo_State.addItem("")
        self.combo_State.addItem("")
        self.combo_State.addItem("")
        self.combo_State.addItem("")
        self.combo_State.addItem("")
        self.combo_State.addItem("")
        self.combo_State.addItem("")
        self.combo_State.addItem("")
        self.combo_State.addItem("")
        self.combo_State.addItem("")
        self.combo_State.addItem("")
        self.combo_State.addItem("")
        self.combo_State.addItem("")
        self.label_state = QtWidgets.QLabel(self.centralwidget)
        self.label_state.setGeometry(QtCore.QRect(130, 60, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto Bk")
        font.setPointSize(14)
        font.setItalic(True)
        self.label_state.setFont(font)
        self.label_state.setObjectName("label_state")


        # Tarikh Func
        self.label_Tarikh = QtWidgets.QLabel(self.centralwidget)
        self.label_Tarikh.setGeometry(QtCore.QRect(130, 30, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto Bk")
        font.setPointSize(14)
        font.setItalic(True)
        self.label_Tarikh.setFont(font)
        self.label_Tarikh.setObjectName("label_Tarikh")
        self.set_Tarikh = QtWidgets.QLabel(self.centralwidget)
        self.set_Tarikh.setGeometry(QtCore.QRect(210, 30, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto Bk")
        font.setPointSize(14)
        font.setItalic(True)
        self.set_Tarikh.setFont(font)
        self.set_Tarikh.setObjectName("set_Tarikh")


        # District comboBox func
        self.combo_District = QtWidgets.QComboBox(self.centralwidget)
        self.combo_District.setGeometry(QtCore.QRect(210, 90, 151, 22))
        self.combo_District.setObjectName("combo_State_2")
        self.label_District = QtWidgets.QLabel(self.centralwidget)
        self.label_District.setGeometry(QtCore.QRect(122, 90, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto Bk")
        font.setPointSize(14)
        font.setItalic(True)
        self.label_District.setFont(font)
        self.label_District.setObjectName("label_state_2")


        # countdown waktu solat Funct
        self.set_Countdown = QtWidgets.QLabel(self.centralwidget)
        self.set_Countdown.setGeometry(QtCore.QRect(50, 140, 411, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(11)
        self.set_Countdown.setFont(font)
        self.set_Countdown.setObjectName("set_Countdown")


        azanWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(azanWindow)
        QtCore.QMetaObject.connectSlotsByName(azanWindow)

    def retranslateUi(self, azanWindow):
        _translate = QtCore.QCoreApplication.translate
        azanWindow.setWindowTitle(_translate("azanWindow", "Azan Window"))
        self.exitButton.setText(_translate("azanWindow", "EXIT"))
        self.label_Maghrib.setText(_translate("azanWindow", "MAGHRIB"))
        self.label_Isyak.setText(_translate("azanWindow", "ISYAK"))
        self.label_Imsak.setText(_translate("azanWindow", "IMSAK"))
        self.label_Subuh.setText(_translate("azanWindow", "SUBUH"))
        self.label_Syuruk.setText(_translate("azanWindow", "SYURUK"))
        self.label_Zuhur.setText(_translate("azanWindow", "ZUHUR"))
        self.label_Asar.setText(_translate("azanWindow", "ASAR"))
        self.combo_State.setItemText(0, _translate("azanWindow", "Kelantan"))
        self.combo_State.setItemText(1, _translate("azanWindow", "Selangor"))
        self.combo_State.setItemText(2, _translate("azanWindow", "Terengganu"))
        self.combo_State.setItemText(3, _translate("azanWindow", "Pahang"))
        self.combo_State.setItemText(4, _translate("azanWindow", "Kedah"))
        self.combo_State.setItemText(5, _translate("azanWindow", "Perak"))
        self.combo_State.setItemText(6, _translate("azanWindow", "Perlis"))
        self.combo_State.setItemText(7, _translate("azanWindow", "Johor"))
        self.combo_State.setItemText(8, _translate("azanWindow", "Pulau Pinang"))
        self.combo_State.setItemText(9, _translate("azanWindow", "Negeri Sembilan"))
        self.combo_State.setItemText(10, _translate("azanWindow", "Melaka"))
        self.combo_State.setItemText(11, _translate("azanWindow", "Sabah"))
        self.combo_State.setItemText(12, _translate("azanWindow", "Sarawak"))
        self.label_state.setText(_translate("azanWindow", "NEGERI:"))
        self.label_Tarikh.setText(_translate("azanWindow", "TARIKH:"))
        self.set_Tarikh.setText(_translate("azanWindow", "1/1/2020"))
        self.label_District.setText(_translate("azanWindow", "DAERAH:"))
        self.set_Countdown.setText(_translate("azanWindow", "TINGGAL MINIT UNTUK SOLAT"))


# CANT USE IT, BECAUSE I DONT KNOW HOW TO BIND IT TOGETHER WITH TKINTER
