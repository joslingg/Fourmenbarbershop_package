# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'booking_edit.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from Fourmenbarbershop_package.gui import bg_img_rc
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_booking_edit_form(object):
    def setupUi(self, booking_edit_form):
        booking_edit_form.setObjectName("booking_edit_form")
        booking_edit_form.resize(451, 524)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/Barbershop/2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        booking_edit_form.setWindowIcon(icon)
        booking_edit_form.setStyleSheet("QPushButton{\n"
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
        self.groupBox_2 = QtWidgets.QGroupBox(booking_edit_form)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 90, 431, 411))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("QGroupBox{\n"
"    border: 0;\n"
"}")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox.setGeometry(QtCore.QRect(10, -20, 411, 371))
        self.groupBox.setStyleSheet("QGroupBox{\n"
"    border: 0px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QLabel {\n"
"    color: rgb(136, 0, 0);\n"
"}")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setContentsMargins(1, -1, 1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.ma_lich_edit = QtWidgets.QLineEdit(self.groupBox)
        self.ma_lich_edit.setMinimumSize(QtCore.QSize(200, 0))
        self.ma_lich_edit.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        self.ma_lich_edit.setFont(font)
        self.ma_lich_edit.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.ma_lich_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.ma_lich_edit.setReadOnly(True)
        self.ma_lich_edit.setObjectName("ma_lich_edit")
        self.gridLayout.addWidget(self.ma_lich_edit, 0, 1, 1, 1)
        self.sdt_kh_lich_edit = QtWidgets.QLineEdit(self.groupBox)
        self.sdt_kh_lich_edit.setMinimumSize(QtCore.QSize(200, 0))
        self.sdt_kh_lich_edit.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        self.sdt_kh_lich_edit.setFont(font)
        self.sdt_kh_lich_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.sdt_kh_lich_edit.setObjectName("sdt_kh_lich_edit")
        self.gridLayout.addWidget(self.sdt_kh_lich_edit, 1, 1, 1, 1)
        self.time_lich_chkbx = QtWidgets.QDateTimeEdit(self.groupBox)
        self.time_lich_chkbx.setMinimumSize(QtCore.QSize(200, 20))
        self.time_lich_chkbx.setMaximumSize(QtCore.QSize(250, 40))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.time_lich_chkbx.setFont(font)
        self.time_lich_chkbx.setLocale(QtCore.QLocale(QtCore.QLocale.Vietnamese, QtCore.QLocale.Vietnam))
        self.time_lich_chkbx.setAlignment(QtCore.Qt.AlignCenter)
        self.time_lich_chkbx.setDate(QtCore.QDate(2024, 4, 25))
        self.time_lich_chkbx.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.time_lich_chkbx.setCalendarPopup(True)
        self.time_lich_chkbx.setTimeSpec(QtCore.Qt.LocalTime)
        self.time_lich_chkbx.setObjectName("time_lich_chkbx")
        self.gridLayout.addWidget(self.time_lich_chkbx, 5, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.ten_kh_lich_edit = QtWidgets.QLineEdit(self.groupBox)
        self.ten_kh_lich_edit.setMinimumSize(QtCore.QSize(200, 0))
        self.ten_kh_lich_edit.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        self.ten_kh_lich_edit.setFont(font)
        self.ten_kh_lich_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.ten_kh_lich_edit.setObjectName("ten_kh_lich_edit")
        self.gridLayout.addWidget(self.ten_kh_lich_edit, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)
        self.ma_tho_chkbx = QtWidgets.QComboBox(self.groupBox)
        self.ma_tho_chkbx.setMinimumSize(QtCore.QSize(0, 32))
        self.ma_tho_chkbx.setObjectName("ma_tho_chkbx")
        self.gridLayout.addWidget(self.ma_tho_chkbx, 3, 1, 1, 1)
        self.dich_vu_lich_chkbx = QtWidgets.QComboBox(self.groupBox)
        self.dich_vu_lich_chkbx.setMinimumSize(QtCore.QSize(0, 32))
        self.dich_vu_lich_chkbx.setObjectName("dich_vu_lich_chkbx")
        self.gridLayout.addWidget(self.dich_vu_lich_chkbx, 4, 1, 1, 1)
        self.luu_lich_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.luu_lich_btn.setGeometry(QtCore.QRect(200, 360, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.luu_lich_btn.setFont(font)
        self.luu_lich_btn.setObjectName("luu_lich_btn")
        self.ket_thuc_lich_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.ket_thuc_lich_btn.setGeometry(QtCore.QRect(310, 360, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ket_thuc_lich_btn.setFont(font)
        self.ket_thuc_lich_btn.setObjectName("ket_thuc_lich_btn")
        self.widget_5 = QtWidgets.QWidget(booking_edit_form)
        self.widget_5.setGeometry(QtCore.QRect(10, -20, 431, 531))
        self.widget_5.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(255, 222, 223);\n"
"color: rgb(136, 0, 0);\n"
"")
        self.widget_5.setObjectName("widget_5")
        self.label_15 = QtWidgets.QLabel(booking_edit_form)
        self.label_15.setGeometry(QtCore.QRect(100, 0, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(136, 0, 0, 70%);\n"
"border-radius: 0px;\n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.widget_5.raise_()
        self.groupBox_2.raise_()
        self.label_15.raise_()

        self.retranslateUi(booking_edit_form)
        QtCore.QMetaObject.connectSlotsByName(booking_edit_form)
        booking_edit_form.setTabOrder(self.ma_lich_edit, self.sdt_kh_lich_edit)
        booking_edit_form.setTabOrder(self.sdt_kh_lich_edit, self.ten_kh_lich_edit)
        booking_edit_form.setTabOrder(self.ten_kh_lich_edit, self.ma_tho_chkbx)
        booking_edit_form.setTabOrder(self.ma_tho_chkbx, self.dich_vu_lich_chkbx)
        booking_edit_form.setTabOrder(self.dich_vu_lich_chkbx, self.time_lich_chkbx)
        booking_edit_form.setTabOrder(self.time_lich_chkbx, self.luu_lich_btn)
        booking_edit_form.setTabOrder(self.luu_lich_btn, self.ket_thuc_lich_btn)

    def retranslateUi(self, booking_edit_form):
        _translate = QtCore.QCoreApplication.translate
        booking_edit_form.setWindowTitle(_translate("booking_edit_form", "Sửa đặt lịch"))
        self.label_3.setText(_translate("booking_edit_form", "SĐT KH:"))
        self.label_5.setText(_translate("booking_edit_form", "Mã thợ:"))
        self.time_lich_chkbx.setDisplayFormat(_translate("booking_edit_form", "dd/MM/yyyy h:mm AP"))
        self.label_4.setText(_translate("booking_edit_form", "Tên KH:"))
        self.label_2.setText(_translate("booking_edit_form", "Mã lịch hẹn:"))
        self.label_6.setText(_translate("booking_edit_form", "Dịch vụ chính:"))
        self.label_7.setText(_translate("booking_edit_form", "Thời gian đặt:"))
        self.luu_lich_btn.setText(_translate("booking_edit_form", "Lưu"))
        self.ket_thuc_lich_btn.setText(_translate("booking_edit_form", "Kết thúc"))
        self.label_15.setText(_translate("booking_edit_form", "SỬA LỊCH HẸN"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    booking_edit_form = QtWidgets.QDialog()
    ui = Ui_booking_edit_form()
    ui.setupUi(booking_edit_form)
    booking_edit_form.show()
    sys.exit(app.exec_())
