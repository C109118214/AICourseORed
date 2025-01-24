# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 22:41:51 2025

@author: USER
"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.symbolInput = QtWidgets.QLineEdit(self.centralwidget)
        self.symbolInput.setObjectName("symbolInput")
        self.symbolInput.setPlaceholderText("輸入加密貨幣對（如 BTCUSDT）")
        self.verticalLayout.addWidget(self.symbolInput)
        
        self.intervalComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.intervalComboBox.setObjectName("intervalComboBox")
        self.intervalComboBox.addItems(["1m", "5m", "15m", "30m", "1h", "4h", "1d"])
        self.verticalLayout.addWidget(self.intervalComboBox)
        
        self.loadButton = QtWidgets.QPushButton(self.centralwidget)
        self.loadButton.setObjectName("loadButton")
        self.loadButton.setText("加載數據")
        self.verticalLayout.addWidget(self.loadButton)
        
        self.ma5Button = QtWidgets.QPushButton(self.centralwidget)
        self.ma5Button.setObjectName("ma5Button")
        self.ma5Button.setText("顯示 MA5")
        self.verticalLayout.addWidget(self.ma5Button)
        
        self.ma10Button = QtWidgets.QPushButton(self.centralwidget)
        self.ma10Button.setObjectName("ma10Button")
        self.ma10Button.setText("顯示 MA10")
        self.verticalLayout.addWidget(self.ma10Button)
        
        self.indicatorButton = QtWidgets.QPushButton(self.centralwidget)
        self.indicatorButton.setObjectName("indicatorButton")
        self.indicatorButton.setText("顯示 RSI")
        self.verticalLayout.addWidget(self.indicatorButton)
        
        self.plotWidget = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.plotWidget.setObjectName("plotWidget")
        self.verticalLayout.addWidget(self.plotWidget)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "加密貨幣 K 線圖查詢工具"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
