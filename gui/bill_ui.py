# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bill.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_bill_form(object):
    def setupUi(self, bill_form):
        bill_form.setObjectName("bill_form")
        bill_form.resize(960, 720)
        bill_form.setMinimumSize(QtCore.QSize(960, 720))
        bill_form.setMaximumSize(QtCore.QSize(960, 720))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/Barbershop/2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        bill_form.setWindowIcon(icon)
        bill_form.setStyleSheet("QPushButton{\n"
"    padding: 10 0 10 0;\n"
"    border-radius: 20;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(31, 76, 124);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(46, 123, 175);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(10, 158, 69);\n"
"}")
        self.ds_hd_tb = QtWidgets.QTableWidget(bill_form)
        self.ds_hd_tb.setGeometry(QtCore.QRect(20, 120, 921, 491))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.ds_hd_tb.setFont(font)
        self.ds_hd_tb.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.SelectedClicked)
        self.ds_hd_tb.setObjectName("ds_hd_tb")
        self.ds_hd_tb.setColumnCount(7)
        self.ds_hd_tb.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ds_hd_tb.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ds_hd_tb.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ds_hd_tb.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ds_hd_tb.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ds_hd_tb.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        item.setFont(font)
        self.ds_hd_tb.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        item.setFont(font)
        self.ds_hd_tb.setHorizontalHeaderItem(6, item)
        self.ds_hd_tb.horizontalHeader().setCascadingSectionResizes(True)
        self.ds_hd_tb.horizontalHeader().setDefaultSectionSize(114)
        self.ds_hd_tb.horizontalHeader().setMinimumSectionSize(50)
        self.ds_hd_tb.verticalHeader().setSortIndicatorShown(False)
        self.ds_hd_tb.verticalHeader().setStretchLastSection(False)
        self.label_17 = QtWidgets.QLabel(bill_form)
        self.label_17.setGeometry(QtCore.QRect(270, 0, 421, 71))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(136, 0, 0, 70%);\n"
"border-radius: 0px;\n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.widget_10 = QtWidgets.QWidget(bill_form)
        self.widget_10.setGeometry(QtCore.QRect(10, 0, 941, 711))
        self.widget_10.setStyleSheet("background-color: rgba(255, 233, 234, 83%);\n"
"border-radius: 20px;")
        self.widget_10.setObjectName("widget_10")
        self.tim_hd_tbx = QtWidgets.QLineEdit(bill_form)
        self.tim_hd_tbx.setGeometry(QtCore.QRect(730, 65, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(10)
        self.tim_hd_tbx.setFont(font)
        self.tim_hd_tbx.setStyleSheet("QLineEdit{\n"
"    padding-left: 10px;\n"
"}\n"
"\n"
"QLineEdit::hover{\n"
"    border: 0.5px solid brown;\n"
"}")
        self.tim_hd_tbx.setObjectName("tim_hd_tbx")
        self.tim_hd_btn = QtWidgets.QPushButton(bill_form)
        self.tim_hd_btn.setGeometry(QtCore.QRect(900, 65, 41, 41))
        self.tim_hd_btn.setStyleSheet("QPushButton{\n"
"    border-radius: 0;\n"
"    background-color: rgb(136, 0, 0);\n"
"}\n"
"QPushButton::hover{\n"
"    border: 0.5px solid brown;\n"
"    background-color: rgb(171, 0, 0);\n"
"}")
        self.tim_hd_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tim_hd_btn.setIcon(icon1)
        self.tim_hd_btn.setObjectName("tim_hd_btn")
        self.layoutWidget_6 = QtWidgets.QWidget(bill_form)
        self.layoutWidget_6.setGeometry(QtCore.QRect(280, 626, 401, 71))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_5.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_5.setSpacing(28)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.sua_hd_btn = QtWidgets.QPushButton(self.layoutWidget_6)
        self.sua_hd_btn.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.sua_hd_btn.setFont(font)
        self.sua_hd_btn.setStyleSheet("")
        self.sua_hd_btn.setObjectName("sua_hd_btn")
        self.horizontalLayout_5.addWidget(self.sua_hd_btn)
        self.xoa_hd_btn = QtWidgets.QPushButton(self.layoutWidget_6)
        self.xoa_hd_btn.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.xoa_hd_btn.setFont(font)
        self.xoa_hd_btn.setStyleSheet("")
        self.xoa_hd_btn.setObjectName("xoa_hd_btn")
        self.horizontalLayout_5.addWidget(self.xoa_hd_btn)
        self.dateEdit = QtWidgets.QDateEdit(bill_form)
        self.dateEdit.setGeometry(QtCore.QRect(20, 65, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.dateEdit.setFont(font)
        self.dateEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dateEdit.setAutoFillBackground(False)
        self.dateEdit.setStyleSheet("color: rgb(78, 74, 212);")
        self.dateEdit.setLocale(QtCore.QLocale(QtCore.QLocale.Vietnamese, QtCore.QLocale.Vietnam))
        self.dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setTimeSpec(QtCore.Qt.TimeZone)
        self.dateEdit.setDate(QtCore.QDate(2024, 5, 24))
        self.dateEdit.setObjectName("dateEdit")
        self.label = QtWidgets.QLabel(bill_form)
        self.label.setGeometry(QtCore.QRect(20, 30, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(136, 0, 0);")
        self.label.setObjectName("label")
        self.widget_10.raise_()
        self.ds_hd_tb.raise_()
        self.label_17.raise_()
        self.tim_hd_tbx.raise_()
        self.tim_hd_btn.raise_()
        self.layoutWidget_6.raise_()
        self.dateEdit.raise_()
        self.label.raise_()

        self.retranslateUi(bill_form)
        QtCore.QMetaObject.connectSlotsByName(bill_form)

    def retranslateUi(self, bill_form):
        _translate = QtCore.QCoreApplication.translate
        bill_form.setWindowTitle(_translate("bill_form", "Danh sách hoá đơn"))
        item = self.ds_hd_tb.horizontalHeaderItem(0)
        item.setText(_translate("bill_form", "Số HĐ"))
        item = self.ds_hd_tb.horizontalHeaderItem(1)
        item.setText(_translate("bill_form", "Mã KH"))
        item = self.ds_hd_tb.horizontalHeaderItem(2)
        item.setText(_translate("bill_form", "SĐT KH"))
        item = self.ds_hd_tb.horizontalHeaderItem(3)
        item.setText(_translate("bill_form", "Mã thợ"))
        item = self.ds_hd_tb.horizontalHeaderItem(4)
        item.setText(_translate("bill_form", "Giảm giá"))
        item = self.ds_hd_tb.horizontalHeaderItem(5)
        item.setText(_translate("bill_form", "Tổng tiền"))
        item = self.ds_hd_tb.horizontalHeaderItem(6)
        item.setText(_translate("bill_form", "Thời gian TT"))
        self.label_17.setText(_translate("bill_form", "DANH SÁCH HOÁ ĐƠN"))
        self.tim_hd_tbx.setPlaceholderText(_translate("bill_form", "Tìm hoá đơn"))
        self.sua_hd_btn.setText(_translate("bill_form", "Sửa"))
        self.xoa_hd_btn.setText(_translate("bill_form", "Xoá"))
        self.dateEdit.setDisplayFormat(_translate("bill_form", "dd/MM/yyyy"))
        self.label.setText(_translate("bill_form", "Chọn ngày:"))
from Fourmenbarbershop_package.gui import bg_img_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    bill_form = QtWidgets.QWidget()
    ui = Ui_bill_form()
    ui.setupUi(bill_form)
    bill_form.show()
    sys.exit(app.exec_())
