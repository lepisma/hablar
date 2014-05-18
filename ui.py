# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created: Mon May 19 00:24:31 2014
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(712, 581)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.start_button = QtGui.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(10, 520, 111, 51))
        self.start_button.setObjectName(_fromUtf8("start_button"))
        self.close_button = QtGui.QPushButton(self.centralwidget)
        self.close_button.setGeometry(QtCore.QRect(600, 520, 101, 51))
        self.close_button.setObjectName(_fromUtf8("close_button"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(140, 520, 451, 51))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.connect_button = QtGui.QPushButton(self.frame)
        self.connect_button.setGeometry(QtCore.QRect(350, 10, 91, 31))
        self.connect_button.setObjectName(_fromUtf8("connect_button"))
        self.ip = QtGui.QLineEdit(self.frame)
        self.ip.setGeometry(QtCore.QRect(10, 10, 331, 31))
        self.ip.setObjectName(_fromUtf8("ip"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 671, 480))
        self.label.setMinimumSize(QtCore.QSize(640, 480))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Hablar | Chat", None))
        self.start_button.setText(_translate("MainWindow", "Start Session", None))
        self.close_button.setText(_translate("MainWindow", "Close", None))
        self.connect_button.setText(_translate("MainWindow", "Connect", None))

