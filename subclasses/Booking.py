import sys
sys.path.append('../DO AN')
from PyQt5 import QtWidgets,QtCore
from Fourmenbarbershop_package.gui import booking_ui
from Fourmenbarbershop_package.gui import booking_edit
from Fourmenbarbershop_package.gui import FourMenBarberShop_ui
import mysql.connector

class BookingWidget:
    def __init__(self, mysql_connector, main_ui, main_form):
        super().__init__()
        self._mysql_connector = mysql_connector
        self.main_ui = main_ui
        self.main_form = main_form
        
        #Khai báo customer form - Mở form thêm khách hàng
        self.booking_form = QtWidgets.QDialog()
        self.booking_ui = booking_ui.Ui_booking_form()
        self.booking_ui.setupUi(self.booking_form)
        
        #Khai báo customer_edit form
        self.booking_edit_form = QtWidgets.QDialog()
        self.booking_edit_ui = booking_edit.Ui_booking_edit_form()
        self.booking_edit_ui.setupUi(self.booking_edit_form)
        #self.main_ui.ds_lich_hen_tb.itemSelectionChanged.connect(self.get_info_lich)
        self.main_ui.calendarWidget.selectionChanged.connect(self.get_ngay)
    def open_booking_form(self):
        self.booking_form.show()
        self.booking_ui.ma_lich_edit.setText(str(self.get_ma()))
        self.booking_ui.ma_tho_chkbx.addItems(self.get_ten_tho())
        self.booking_ui.dich_vu_lich_chkbx.addItems(self.get_dich_vu())
        self.booking_ui.luu_lich_btn.clicked.connect(self.insert_dl)
        self.booking_ui.sdt_kh_lich_edit.textChanged.connect(self.get_ten_kh)
        self.booking_ui.ket_thuc_lich_btn.clicked.connect(self.close_booking_form)
    def close_booking_form(self):
        self.booking_form.close()
        
    def open_booking_edit_form(self):
        self.booking_edit_form.show()
        #self.booking_edit_ui.luu_lich_btn.clicked.connect(self.update_kh)
        self.booking_edit_ui.ket_thuc_lich_btn.clicked.connect(self.close_booking_edit_form)
    def close_booking_edit_form(self):
        self.customer_edit_form.close()
    

    #Show data lịch hẹn
    def show_data_lichhen(self):
        query = """SELECT DatLich.ma_dl,KhachHang.ten_kh,KhachHang.sdt_kh,Tho.ten_tho,DichVu.ten_dv,DatLich.thoi_gian_dat FROM DatLich 
                    INNER JOIN KhachHang ON DatLich.ma_kh=KhachHang.ma_kh
                    INNER JOIN Tho ON DatLich.ma_tho=Tho.ma_tho
                    INNER JOIN DichVu ON DatLich.ma_dv=DichVu.ma_dv ORDER BY thoi_gian_dat DESC"""
        result = self._mysql_connector.execute_query(query,select=True)
        if result:
            self.main_ui.ds_lich_hen_tb.setRowCount(len(result))
            self.main_ui.ds_lich_hen_tb.setColumnCount(6)
            for row_index,row in enumerate(result):
                for col_index,value in enumerate(row):
                    item = QtWidgets.QTableWidgetItem(str(value))
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.main_ui.ds_lich_hen_tb.setItem(row_index,col_index,item)
        else:
            print("Không có data đặt lịch")

    def get_ten_kh(self):
        sdt_kh = self.booking_ui.sdt_kh_lich_edit.text()
        query = "SELECT ten_kh FROM KhachHang WHERE sdt_kh=%s"
        result = self._mysql_connector.execute_query(query=query,params=(sdt_kh,),select=True)
        if result:
            ten_kh = result[0][0]
            self.booking_ui.ten_kh_lich_edit.setText(ten_kh)
        else:
            ten_kh = 'Vãng lai'
            self.booking_ui.ten_kh_lich_edit.setText(ten_kh)
         
    def get_ngay(self):
        date = self.main_ui.calendarWidget.selectedDate()     
        print(date)
            
    def get_ten_tho(self):
        query = "SELECT ten_tho FROM Tho"
        result = self._mysql_connector.execute_query(query=query,select=True)
        l_ten_tho = [result[0] for result in result]
        return l_ten_tho
    
    def get_dich_vu(self):
        query = "SELECT ten_dv FROM DichVu"
        result = self._mysql_connector.execute_query(query=query,select=True)
        l_ten_dv = [result[0] for result in result]
        return l_ten_dv

    def get_ma(self):
        query = "SELECT ma_dl FROM DatLich ORDER BY ma_dl DESC LIMIT 1"
        obj_type = "DL"
        byte = 3
        first_id = "001"
        ma_dl = self.main_form.generate_ma(query=query,obj_type=obj_type,byte=byte,first_id=first_id)
        return ma_dl
    #Insert - Lịch
    def insert_dl(self):
        try:
            ma_dl = self.get_ma()
            self.booking_ui.ma_lich_edit.setText(ma_dl)
            
            #Lấy mã khách hàng từ combobox
            sdt_kh = self.booking_ui.sdt_kh_lich_edit.text()
            query_kh = "SELECT ma_kh FROM KhachHang where sdt_kh = %s"
            result_kh = self._mysql_connector.execute_query(query=query_kh,params=(sdt_kh,),select=True)
            if result_kh:
                ma_kh = result_kh[0][0]
            else:
                ma_kh = None
            
            
            #Lấy mã thợ từ combobox
            ten_tho = self.booking_ui.ma_tho_chkbx.currentText()
            query_tho = "SELECT ma_tho FROM Tho WHERE ten_tho = %s"
            result_tho = self._mysql_connector.execute_query(query=query_tho,params=(ten_tho,),select=True)
            if result_tho:
                ma_tho = result_tho[0][0]
            
            #Lấy mã dịch vụ từ combobox
            ten_dv = self.booking_ui.dich_vu_lich_chkbx.currentText()
            query_dv = "SELECT ma_dv FROM DichVu WHERE ten_dv = %s"
            result_dv = self._mysql_connector.execute_query(query=query_dv,params=(ten_dv,),select=True)
            if result_dv:
                ma_dv = result_dv[0][0]
                        
            query = "INSERT INTO DatLich (ma_dl,ma_kh,sdt_kh,ma_tho,ma_dv) VALUES (%s,%s,%s,%s,%s)"
            params = (ma_dl,ma_kh,sdt_kh,ma_tho,ma_dv)
            self._mysql_connector.execute_query(query=query,params=params)
            self.show_data_lichhen()
            self.booking_form.close()
            print("Insert successfully")
        except mysql.connector.Error as err:
            print(f'Lỗi: {err}')
    '''
    def get_info_dl(self):
        try:
            selected_items = self.main_ui.ds_dl_tablewidget.selectedItems()
            if not selected_items:
                return
            row = self.main_ui.ds_dl_tablewidget.currentRow()
            ma_dl = self.main_ui.ds_dl_tablewidget.item(row,0).text()
            ten_dl = self.main_ui.ds_dl_tablewidget.item(row,1).text()
            sdt_dl = self.main_ui.ds_dl_tablewidget.item(row,2).text()
            so_nam = self.main_ui.ds_dl_tablewidget.item(row,3).text()
            self.barber_edit_ui.ma_dl_edit.setText(ma_dl)
            self.barber_edit_ui.ten_dl_edit.setText(ten_dl)
            self.barber_edit_ui.sdt_dl_edit.setText(sdt_dl)
            self.barber_edit_ui.so_nam_kn_edit.setText(so_nam)
            return ma_dl
        except mysql.connector.Error as err:
            print(f'Lỗi: {err}')
            
    #Update - Thợ
    def update_dl(self):
        try:
            ma_kh = self.barber_edit_ui.ma_dl_edit.text()
            ten_dl = self.barber_edit_ui.ten_dl_edit.text()
            sdt_dl = self.barber_edit_ui.sdt_dl_edit.text()
            so_nam = self.barber_edit_ui.so_nam_kn_edit.text()
            
            query = "UPDATE Tho SET ten_dl=%s, sdt_dl=%s, so_nam_kinh_nghiem=%s WHERE ma_dl=%s"
            params = (ten_dl,sdt_dl,so_nam,ma_kh)
            self._mysql_connector.execute_query(query=query,params=params)
            self.show_data_dl()
            print('Update successfully')
            self.barber_edit_form.close()
        except mysql.connector.Error as err:
            print(f"Lỗi: {err}")
    
    #Xoá - Thợ
    def delete_dl(self):
        try:
            ma_dl = self.get_info_dl()
            
            query = "DELETE FROM Tho WHERE ma_dl = %s"
            params = (ma_dl,)
            self._mysql_connector.execute_query(query=query,params=params)
            self.msgBox = QtWidgets.QMessageBox()
            self.msgBox.setWindowTitle("Xác nhận xoá")
            self.msgBox.setIcon(QtWidgets.QMessageBox.Question)
            self.msgBox.setText(f"Có chắc bạn muốn xoá thợ {ma_dl} không?")
            self.msgBox.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            self.msgBox.setDefaultButton(QtWidgets.QMessageBox.No)
            ret = self.msgBox.exec()
            if ret == self.msgBox.Yes:
                self._mysql_connector.execute_query(query,params=params)
                self.show_data_dl()
                print("Delete successfully")
            else:
                return
        except mysql.connector.Error as err:
            print(f"Lỗi: {err}")
            '''