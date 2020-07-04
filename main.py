# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_search_engine(object):
    def setupUi(self, search_engine):
        search_engine.setObjectName("search_engine")
        search_engine.resize(922, 561)
        self.centralwidget = QtWidgets.QWidget(search_engine)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(4, 0, 911, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.search_for = QtWidgets.QLineEdit(self.centralwidget)
        self.search_for.setGeometry(QtCore.QRect(210, 140, 501, 31))
        self.search_for.setObjectName("search_for")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 90, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 140, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.directory = QtWidgets.QLineEdit(self.centralwidget)
        self.directory.setGeometry(QtCore.QRect(210, 90, 501, 31))
        self.directory.setObjectName("directory")
        self.search_btn = QtWidgets.QPushButton(self.centralwidget)
        self.search_btn.setGeometry(QtCore.QRect(760, 140, 111, 31))
        self.search_btn.setObjectName("search_btn")
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(10, 220, 901, 241))
        self.table.setRowCount(100)
        self.table.setColumnCount(2)
        self.table.setObjectName("table")
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        self.table.horizontalHeader().setVisible(True)
        self.table.horizontalHeader().setDefaultSectionSize(200)
        self.table.horizontalHeader().setHighlightSections(True)
        self.table.horizontalHeader().setMinimumSectionSize(50)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.no_match = QtWidgets.QLabel(self.centralwidget)
        self.no_match.setGeometry(QtCore.QRect(4, 175, 911, 41))
        self.no_match.setTextFormat(QtCore.Qt.RichText)
        self.no_match.setAlignment(QtCore.Qt.AlignCenter)
        self.no_match.setObjectName("no_match")
        self.clear_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clear_btn.setGeometry(QtCore.QRect(760, 480, 111, 31))
        self.clear_btn.setObjectName("clear_btn")
        search_engine.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(search_engine)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 922, 26))
        self.menubar.setObjectName("menubar")
        search_engine.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(search_engine)
        self.statusbar.setObjectName("statusbar")
        search_engine.setStatusBar(self.statusbar)

        self.retranslateUi(search_engine)
        QtCore.QMetaObject.connectSlotsByName(search_engine)

    def retranslateUi(self, search_engine):
        _translate = QtCore.QCoreApplication.translate
        search_engine.setWindowTitle(_translate("search_engine", "MainWindow"))
        self.label.setText(_translate("search_engine", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">File Search Engine</span></p></body></html>"))
        self.label_3.setText(_translate("search_engine", "<html><head/><body><p align=\"center\">Directory  :</p></body></html>"))
        self.label_4.setText(_translate("search_engine", "<html><head/><body><p align=\"center\">Search for :</p></body></html>"))
        self.search_btn.setText(_translate("search_engine", "Search"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("search_engine", "File name"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("search_engine", "Line"))
        self.no_match.setText(_translate("search_engine", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\"><br/></span></p></body></html>"))
        self.clear_btn.setText(_translate("search_engine", "Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    search_engine = QtWidgets.QMainWindow()
    ui = Ui_search_engine()
    ui.setupUi(search_engine)
    search_engine.show()
    sys.exit(app.exec_())

