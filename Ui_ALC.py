# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\cheat\ALC.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AzurLaneCheater(object):
    def setupUi(self, AzurLaneCheater):
        AzurLaneCheater.setObjectName("AzurLaneCheater")
        AzurLaneCheater.resize(707, 392)
        self.graphicsView = QtWidgets.QGraphicsView(AzurLaneCheater)
        self.graphicsView.setGeometry(QtCore.QRect(215, 10, 481, 311))
        self.graphicsView.setObjectName("graphicsView")

        self.Stage = QtWidgets.QComboBox(AzurLaneCheater)
        self.Stage.setGeometry(QtCore.QRect(20, 100, 161, 31))
        self.Stage.setObjectName("Stage")
        self.Stage.addItem("")
        self.Stage.addItem("")
        self.Stage.addItem("")
        self.Stage.addItem("")
        self.Stage.addItem("")

        self.label = QtWidgets.QLabel(AzurLaneCheater)
        self.label.setGeometry(QtCore.QRect(20, 60, 181, 41))
        self.label.setObjectName("label")
        
        self.confirm = QtWidgets.QPushButton(AzurLaneCheater)
        self.confirm.setGeometry(QtCore.QRect(110, 140, 75, 23))
        self.confirm.setObjectName("confirm")
        self.confirm.clicked.connect(self.F_confirm)

        self.label_2 = QtWidgets.QLabel(AzurLaneCheater)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 41, 31))
        self.label_2.setObjectName("label_2")

        self.nox_detect = QtWidgets.QLabel(AzurLaneCheater)
        self.nox_detect.setGeometry(QtCore.QRect(70, 30, 61, 31))
        self.nox_detect.setObjectName("nox_detect")

        self.label_3 = QtWidgets.QLabel(AzurLaneCheater)
        self.label_3.setGeometry(QtCore.QRect(20, 170, 181, 41))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(AzurLaneCheater)
        self.label_4.setGeometry(QtCore.QRect(30, 220, 71, 31))
        self.label_4.setObjectName("label_4")

        self.team1 = QtWidgets.QLabel(AzurLaneCheater)
        self.team1.setGeometry(QtCore.QRect(110, 220, 61, 31))
        self.team1.setObjectName("team1")

        self.label_5 = QtWidgets.QLabel(AzurLaneCheater)
        self.label_5.setGeometry(QtCore.QRect(30, 250, 71, 31))
        self.label_5.setObjectName("label_5")

        self.team2 = QtWidgets.QLabel(AzurLaneCheater)
        self.team2.setGeometry(QtCore.QRect(110, 250, 61, 31))
        self.team2.setObjectName("team2")

        self.close = QtWidgets.QPushButton(AzurLaneCheater)
        self.close.setGeometry(QtCore.QRect(620, 350, 75, 23))
        self.close.setObjectName("close")
        self.close.clicked.connect(QtWidgets.qApp.quit)
        
        self.label_6 = QtWidgets.QLabel(AzurLaneCheater)
        self.label_6.setGeometry(QtCore.QRect(30, 280, 71, 31))
        self.label_6.setObjectName("label_6")

        self.kill = QtWidgets.QLabel(AzurLaneCheater)
        self.kill.setGeometry(QtCore.QRect(110, 280, 61, 31))
        self.kill.setObjectName("kill")

        self.retranslateUi(AzurLaneCheater)
        QtCore.QMetaObject.connectSlotsByName(AzurLaneCheater)

    def retranslateUi(self, AzurLaneCheater):
        _translate = QtCore.QCoreApplication.translate
        AzurLaneCheater.setWindowTitle(_translate("AzurLaneCheater", "Dialog"))
        self.Stage.setItemText(0, _translate("AzurLaneCheater", "1-1"))
        self.Stage.setItemText(1, _translate("AzurLaneCheater", "3-4"))
        self.Stage.setItemText(2, _translate("AzurLaneCheater", "6-4"))
        self.Stage.setItemText(3, _translate("AzurLaneCheater", "7-2"))
        self.Stage.setItemText(4, _translate("AzurLaneCheater", "8-4"))
        self.label.setText(_translate("AzurLaneCheater", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">choose a stage :</span></p></body></html>"))
        self.confirm.setText(_translate("AzurLaneCheater", "confirm"))
        self.label_2.setText(_translate("AzurLaneCheater", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">nox :</span></p></body></html>"))
        self.nox_detect.setText(_translate("AzurLaneCheater", "<html><head/><body><p><br/></p></body></html>"))
        self.label_3.setText(_translate("AzurLaneCheater", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">State :</span></p></body></html>"))
        self.label_4.setText(_translate("AzurLaneCheater", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Team1 :</span></p></body></html>"))
        self.team1.setText(_translate("AzurLaneCheater", "<html><head/><body><p><br/></p></body></html>"))
        self.label_5.setText(_translate("AzurLaneCheater", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Team2 :</span></p></body></html>"))
        self.team2.setText(_translate("AzurLaneCheater", "<html><head/><body><p><br/></p></body></html>"))
        self.close.setText(_translate("AzurLaneCheater", "close"))
        self.label_6.setText(_translate("AzurLaneCheater", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Kill :</span></p></body></html>"))
        self.kill.setText(_translate("AzurLaneCheater", "<html><head/><body><p><br/></p></body></html>"))
    
    def F_confirm(self):
        print(self.Stage.currentText())
        