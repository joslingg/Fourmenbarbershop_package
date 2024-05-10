import sys
sys.path.append('../DO AN')
from PyQt5 import QtWidgets,QtCore
from Fourmenbarbershop_package.gui import booking_ui
from Fourmenbarbershop_package.gui import booking_edit
from Fourmenbarbershop_package.gui import FourMenBarberShop_ui

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
        self.
    def open_booking_form(self):
        self.booking_form.show()
        #self.booking_ui.ma_lich_edit.setText(str(self.get_ma()))
        self.booking_ui.ma_tho_chkbx.addItems(self.get_ten_tho())
        self.booking_ui.dich_vu_lich_chkbx.addItems(self.get_dich_vu())
        #self.booking_ui.luu_lich_btn.clicked.connect(self.insert_lich)
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
                    INNER JOIN DichVu ON DatLich.ma_dv=DichVu.ma_dv"""
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
         
    def get_ngay(self):
        date = self.main_ui.calendarWidget.selectionDate()     
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