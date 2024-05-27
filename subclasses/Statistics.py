import sys
sys.path.append('../DO AN')
from PyQt5 import QtWidgets,QtCore
import mysql.connector
import datetime
from PyQt5.QtCore import QTimer

class StatisticsWidget:
    def __init__(self, mysql_connector, main_ui, main_form):
        super().__init__()
        self._mysql_connector = mysql_connector
        self.main_ui = main_ui
        self.main_form = main_form
        self.tong_tien = 0
        self.ds_dv = []
        self.so_hd = None
        self.time = None
        
        self.cap_nhat_dt_slhd()
        self.top_kh()
        self.top_tho()
        self.main_ui.start_date_edit.dateChanged.connect(self.cap_nhat_dt_slhd)
        self.main_ui.end_date_edit.dateChanged.connect(self.cap_nhat_dt_slhd)
        
    def cap_nhat_dt_slhd_today(self):
        # Lấy ngày hôm nay
        ngay_hien_tai = datetime.date.today().strftime("%Y-%m-%d")
        return ngay_hien_tai
        
    def cap_nhat_dt_slhd(self):
        self.cap_nhat_dt_slhd_today()
        start_date = self.main_ui.start_date_edit.date()
        end_date = self.main_ui.end_date_edit.date()
        try:
            if start_date > end_date:
                QtWidgets.QMessageBox.information(self.main_form,"Lỗi","Ngày bắt đầu không được lớn hơn ngày kết thúc")
        except: QtWidgets.QMessageBox.information(self.main_form,"Lỗi","Ngày bắt đầu không được lớn hơn ngày kết thúc")
        
        start_date = start_date.toString("yyyy-MM-dd")
        end_date = end_date.toString("yyyy-MM-dd")
        query_dt = """SELECT SUM(tong_tien) FROM HoaDon
                WHERE DATE(thoi_gian_tt) BETWEEN %s AND %s"""
            
        query_luot = """SELECT COUNT(*) FROM HoaDon
                WHERE DATE(thoi_gian_tt) BETWEEN %s AND %s"""
        params=(start_date,end_date)
        result_dt = self._mysql_connector.execute_query(query=query_dt,params=params,select=True)
        result_luot = self._mysql_connector.execute_query(query=query_luot,params=params,select=True)
        
        if result_dt and result_dt[0][0] is not None:
            doanh_thu = result_dt[0][0]
        else:
            doanh_thu = 0
        formatted_dt = "{:,.0f} đ".format(doanh_thu).replace(',','.')
        self.main_ui.doanh_thu_label.setText(formatted_dt)
        
        if result_luot and result_luot[0][0] is not None:
            luot = result_luot[0][0]
        else:
            luot = 0
        formatted_luot = f"{luot} lượt"
        self.main_ui.so_luot_label.setText(formatted_luot)
        
    def top_kh(self):
        query = """SELECT ten_kh, so_lan_den FROM KhachHang
                    ORDER BY so_lan_den DESC LIMIT 3"""
        result = self._mysql_connector.execute_query(query=query,select=True)
        if result:
            self.main_ui.kh_top1.setText(result[0][0])
            self.main_ui.luot_kh1.setText(str(result[0][1]))
            
            self.main_ui.kh_top2.setText(result[1][0])
            self.main_ui.luot_kh2.setText(str(result[1][1]))
            
            self.main_ui.kh_top3.setText(result[2][0])
            self.main_ui.luot_kh3.setText(str(result[2][1]))
            
    def top_tho(self):
        query = """SELECT Tho.ten_tho, COUNT(*) AS so_lan_hot FROM HoaDon
                    INNER JOIN Tho ON Tho.ma_tho = HoaDon.ma_tho
                    GROUP BY Tho.ten_tho
                    ORDER BY so_lan_hot DESC LIMIT 3"""
        result = self._mysql_connector.execute_query(query=query,select=True)
        if result:
            self.main_ui.tho_top1.setText(result[0][0])
            self.main_ui.lan_tho1.setText(str(result[0][1]))
            
            self.main_ui.tho_top2.setText(result[1][0])
            self.main_ui.lan_tho2.setText(str(result[1][1]))
            
            self.main_ui.tho_top3.setText(result[2][0])
            self.main_ui.lan_tho3.setText(str(result[2][1]))