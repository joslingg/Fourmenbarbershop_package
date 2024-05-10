# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'barber_edit.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Fourmenbarbershop_package.gui import bg_img_rc

class Ui_barber_edit_form(object):
    def setupUi(self, barber_edit_form):
        barber_edit_form.setObjectName("barber_edit_form")
        barber_edit_form.resize(451, 524)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/Barbershop/2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        barber_edit_form.setWindowIcon(icon)
        barber_edit_form.setStyleSheet("QPushButton{\n"
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
        self.groupBox_2 = QtWidgets.QGroupBox(barber_edit_form)
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
        self.groupBox.setGeometry(QtCore.QRect(10, -30, 411, 381))
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
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 11, 411, 351))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.ma_tho_edit = QtWidgets.QLineEdit(self.layoutWidget)
        self.ma_tho_edit.setMinimumSize(QtCore.QSize(200, 0))
        self.ma_tho_edit.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        self.ma_tho_edit.setFont(font)
        self.ma_tho_edit.setStyleSheet("background-color: rgb(216, 216, 216);")
        self.ma_tho_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.ma_tho_edit.setReadOnly(True)
        self.ma_tho_edit.setObjectName("ma_tho_edit")
        self.gridLayout.addWidget(self.ma_tho_edit, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.ten_tho_edit = QtWidgets.QLineEdit(self.layoutWidget)
        self.ten_tho_edit.setMinimumSize(QtCore.QSize(200, 0))
        self.ten_tho_edit.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        self.ten_tho_edit.setFont(font)
        self.ten_tho_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.ten_tho_edit.setObjectName("ten_tho_edit")
        self.gridLayout.addWidget(self.ten_tho_edit, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.sdt_tho_edit = QtWidgets.QLineEdit(self.layoutWidget)
        self.sdt_tho_edit.setMinimumSize(QtCore.QSize(200, 0))
        self.sdt_tho_edit.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        self.sdt_tho_edit.setFont(font)
        self.sdt_tho_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.sdt_tho_edit.setObjectName("sdt_tho_edit")
        self.gridLayout.addWidget(self.sdt_tho_edit, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.so_nam_kn_edit = QtWidgets.QLineEdit(self.layoutWidget)
        self.so_nam_kn_edit.setMinimumSize(QtCore.QSize(200, 0))
        self.so_nam_kn_edit.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        self.so_nam_kn_edit.setFont(font)
        self.so_nam_kn_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.so_nam_kn_edit.setObjectName("so_nam_kn_edit")
        self.gridLayout.addWidget(self.so_nam_kn_edit, 3, 1, 1, 1)
        self.luu_edit_tho_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.luu_edit_tho_btn.setGeometry(QtCore.QRect(200, 360, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.luu_edit_tho_btn.setFont(font)
        self.luu_edit_tho_btn.setObjectName("luu_edit_tho_btn")
        self.ket_thuc_edit_tho_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.ket_thuc_edit_tho_btn.setGeometry(QtCore.QRect(310, 360, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ket_thuc_edit_tho_btn.setFont(font)
        self.ket_thuc_edit_tho_btn.setObjectName("ket_thuc_edit_tho_btn")
        self.widget_5 = QtWidgets.QWidget(barber_edit_form)
        self.widget_5.setGeometry(QtCore.QRect(10, -20, 431, 531))
        self.widget_5.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(255, 222, 223);\n"
"color: rgb(136, 0, 0);\n"
"")
        self.widget_5.setObjectName("widget_5")
        self.label_15 = QtWidgets.QLabel(barber_edit_form)
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

        self.retranslateUi(barber_edit_form)
        QtCore.QMetaObject.connectSlotsByName(barber_edit_form)
        barber_edit_form.setTabOrder(self.ma_tho_edit, self.ten_tho_edit)
        barber_edit_form.setTabOrder(self.ten_tho_edit, self.sdt_tho_edit)
        barber_edit_form.setTabOrder(self.sdt_tho_edit, self.so_nam_kn_edit)
        barber_edit_form.setTabOrder(self.so_nam_kn_edit, self.luu_edit_tho_btn)
        barber_edit_form.setTabOrder(self.luu_edit_tho_btn, self.ket_thuc_edit_tho_btn)

    def retranslateUi(self, barber_edit_form):
        _translate = QtCore.QCoreApplication.translate
        barber_edit_form.setWindowTitle(_translate("barber_edit_form", "Sửa thợ"))
        self.label_2.setText(_translate("barber_edit_form", "Mã thợ:"))
        self.label_3.setText(_translate("barber_edit_form", "Tên thợ:"))
        self.label_4.setText(_translate("barber_edit_form", "SĐT thợ:"))
        self.label_5.setText(_translate("barber_edit_form", "Số năm KN:"))
        self.luu_edit_tho_btn.setText(_translate("barber_edit_form", "Lưu"))
        self.ket_thuc_edit_tho_btn.setText(_translate("barber_edit_form", "Kết thúc"))
        self.label_15.setText(_translate("barber_edit_form", "SỬA THỢ"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    barber_edit_form = QtWidgets.QDialog()
    ui = Ui_barber_edit_form()
    ui.setupUi(barber_edit_form)
    barber_edit_form.show()
    sys.exit(app.exec_())
