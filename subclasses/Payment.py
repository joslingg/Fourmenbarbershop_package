import sys
sys.path.append('../DO AN')
from PyQt5 import QtWidgets,QtCore
from Fourmenbarbershop_package.gui import booking_ui
from Fourmenbarbershop_package.gui import booking_edit
from Fourmenbarbershop_package.gui import FourMenBarberShop_ui
import mysql.connector
import datetime

class PaymentWidget:
    def __init__(self, mysql_connector, main_ui, main_form):
        super().__init__()
        self._mysql_connector = mysql_connector
        self.main_ui = main_ui
        self.main_form = main_form
        
        self.main_ui.ten_tho_cbx.addItems(self.get_ten_tho())
        self.main_ui.tiep_btn.clicked.connect(self.generate_sohd)
        self.main_ui.tiep_btn.clicked.connect(self.get_time)
        self.main_ui.sdt_kh_tbx.textChanged.connect(self.get_ten_kh)
        self.main_ui.dich_vu_cbx.addItems(self.get_dich_vu())
        self.main_ui.them_btn.clicked.connect(self.them_dich_vu)
        
    def get_ten_tho(self):
        query = "SELECT ten_tho FROM Tho"
        result = self._mysql_connector.execute_query(query=query,select=True)
        l_ten_tho = [result[0] for result in result]
        return l_ten_tho
    
    def generate_sohd(self):
        query = "SELECT so_hd FROM HoaDon ORDER BY so_hd DESC LIMIT 1"
        obj_type = "HD"
        byte = 5
        first_id = "001"
        so_hd = self.main_form.generate_ma(query=query,obj_type=obj_type,byte=byte,first_id=first_id)
        self.main_ui.so_hd_tbx.setText(so_hd)
        return so_hd
    
    def get_time(self):
        current_time = datetime.datetime.now()
        formated_current_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
        self.main_ui.time_tbx.setText(formated_current_time)
        print(formated_current_time)
        return formated_current_time
    
    #Hàm tìm tên khách hàng khi nhập sdt
    def get_ten_kh(self):
        sdt_kh = self.main_ui.sdt_kh_tbx.text()
        query = "SELECT ten_kh FROM KhachHang WHERE sdt_kh=%s"
        result = self._mysql_connector.execute_query(query=query,params=(sdt_kh,),select=True)
        if result:
            ten_kh = result[0][0]
            self.main_ui.ten_kh_tbx.setText(ten_kh)
        else:
            ten_kh = 'Khách vãng lai'
            self.main_ui.ten_kh_tbx.setText(ten_kh)
            
    def get_dich_vu(self):
        query = "SELECT ten_dv FROM DichVu"
        result = self._mysql_connector.execute_query(query=query,select=True)
        l_ten_dv = [result[0] for result in result]
        return l_ten_dv
    def them_dich_vu(self):
        dich_vu = self.main_ui.dich_vu_cbx.currentText()
        so_luong = self.main_ui.sl_dich_vu_cbx.value()
        
        query = "SELECT don_gia FROM DichVu WHERE ten_dv=%s"
        result = self._mysql_connector.execute_query(query=query,params=(dich_vu,),select=True)
        don_gia = result[0][0]
        formatted_dg = "{:,.0f}".format(don_gia).replace(',','.')
        thanh_tien = int(so_luong)*float(don_gia)
        formatted_tt = "{:,.0f}".format(thanh_tien).replace(',','.')
        
        if dich_vu and so_luong is not None:
            rowCount = self.main_ui.ds_dich_vu_tb.rowCount()
            self.main_ui.ds_dich_vu_tb.insertRow(rowCount)
            self.main_ui.ds_dich_vu_tb.setItem(rowCount,0,QtWidgets.QTableWidgetItem(dich_vu))
            self.main_ui.ds_dich_vu_tb.setItem(rowCount,1,QtWidgets.QTableWidgetItem(str(so_luong)))
            self.main_ui.ds_dich_vu_tb.setItem(rowCount,2,QtWidgets.QTableWidgetItem(str(don_gia)))
            self.main_ui.ds_dich_vu_tb.setItem(rowCount,3,QtWidgets.QTableWidgetItem(str(formatted_tt)))