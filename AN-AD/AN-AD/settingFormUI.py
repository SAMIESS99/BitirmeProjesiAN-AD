# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\setting.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_settingForm(object):
    def setupUi(self, settingForm):
        settingForm.setObjectName("settingForm")
        settingForm.resize(1060, 787)
        self.centralwidget = QtWidgets.QWidget(settingForm)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(60, 20, 941, 271))
        self.groupBox_4.setObjectName("groupBox_4")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_4)
        self.layoutWidget.setGeometry(QtCore.QRect(110, 60, 241, 74))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_3.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_3.addWidget(self.lineEdit_2)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox)
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_4)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 60, 95, 71))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 160, 231, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_4)
        self.tableWidget.setGeometry(QtCore.QRect(380, 0, 561, 271))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(380, 580, 211, 41))
        self.pushButton.setObjectName("pushButton")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(50, 300, 951, 201))
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget2.setGeometry(QtCore.QRect(120, 50, 241, 81))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout.addWidget(self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_5.setClearButtonEnabled(False)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout.addWidget(self.lineEdit_5)
        self.spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox.setGeometry(QtCore.QRect(540, 50, 119, 20))
        self.spinBox.setToolTip("")
        self.spinBox.setObjectName("spinBox")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(430, 50, 93, 19))
        self.label_3.setObjectName("label_3")
        self.layoutWidget3 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget3.setGeometry(QtCore.QRect(30, 51, 81, 81))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.groupBox.raise_()
        self.groupBox_4.raise_()
        self.pushButton.raise_()
        settingForm.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(settingForm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1060, 21))
        self.menubar.setObjectName("menubar")
        settingForm.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(settingForm)
        self.statusbar.setObjectName("statusbar")
        settingForm.setStatusBar(self.statusbar)

        self.retranslateUi(settingForm)
        QtCore.QMetaObject.connectSlotsByName(settingForm)

    def retranslateUi(self, settingForm):
        _translate = QtCore.QCoreApplication.translate
        settingForm.setWindowTitle(_translate("settingForm", "Setting"))
        self.groupBox_4.setTitle(_translate("settingForm", "Ayarlar"))
        self.comboBox.setItemText(0, _translate("settingForm", "Console Log"))
        self.comboBox.setItemText(1, _translate("settingForm", "Popup"))
        self.comboBox.setItemText(2, _translate("settingForm", "Alarm"))
        self.comboBox.setItemText(3, _translate("settingForm", "Mail"))
        self.label.setText(_translate("settingForm", "Uyarı paket sayısı "))
        self.label_2.setText(_translate("settingForm", "Uyarı Mesajı"))
        self.label_7.setText(_translate("settingForm", "Uyarı Eylemi"))
        self.pushButton_2.setText(_translate("settingForm", "Ekle"))
        self.pushButton.setText(_translate("settingForm", "Kayıt Et"))
        self.groupBox.setTitle(_translate("settingForm", "GroupBox"))
        self.label_3.setText(_translate("settingForm", "Kontrol zaman dilimi"))
        self.label_5.setText(_translate("settingForm", "Kime"))
        self.label_6.setText(_translate("settingForm", "Mail"))
        self.label_8.setText(_translate("settingForm", "Şifre"))
