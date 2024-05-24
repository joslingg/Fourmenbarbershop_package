import sys
sys.path.append('../DO AN')
from PyQt5 import QtWidgets,QtCore
import mysql.connector
import datetime

class PaymentWidget:
    def __init__(self, mysql_connector, main_ui, main_form):
        super().__init__()
        self._mysql_connector = mysql_connector
        self.main_ui = main_ui
        self.main_form = main_form
        self.tong_tien = 0
        self.ds_dv = []
        self.so_hd = None
        self.time = None
        
        
        
        self.main_ui.ten_tho_cbx.addItems(self.get_ten_tho())
        self.main_ui.tiep_btn.clicked.connect(self.tao_moi_hd)
        self.main_ui.sdt_kh_tbx.textChanged.connect(self.get_ten_kh)
        self.main_ui.dich_vu_cbx.addItems(self.get_dich_vu())
        self.main_ui.them_btn.clicked.connect(self.them_dich_vu)
        self.main_ui.ds_dich_vu_tb.itemChanged.connect(self.tinh_tien)
        self.main_ui.giam_gia_tbx.textChanged.connect(self.tinh_tien)
        self.main_ui.luu_btn.clicked.connect(self.luu_hd)
        self.main_ui.bo_qua_btn.clicked.connect(self.bo_qua_hd)
        self.main_ui.ds_dich_vu_tb.itemSelectionChanged.connect(self.get_info_dv)
        self.main_ui.xoa_btn.clicked.connect(self.xoa_dich_vu)
        
        
    
    #Lấy tên thợ hiển thị lên combobox  
    def get_ten_tho(self):
        query = "SELECT ten_tho FROM Tho"
        result = self._mysql_connector.execute_query(query=query,select=True)
        l_ten_tho = [result[0] for result in result]
        return l_ten_tho
    
    def tao_moi_hd(self):
        #Sinh số HĐ
        print("dang tao moi hd")
        def generate_sohd():
            query = "SELECT so_hd FROM HoaDon ORDER BY so_hd DESC LIMIT 1"
            obj_type = "HD"
            byte = 3
            first_id = "001"
            so_hd = self.main_form.generate_ma(query=query,obj_type=obj_type,byte=byte,first_id=first_id)
            self.main_ui.so_hd_tbx.setText(so_hd)
            self.so_hd = so_hd
            return so_hd
        
        #Lấy thời gian hiện tại
        def get_time():
            current_time = datetime.datetime.now()
            formated_current_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
            self.main_ui.time_tbx.setText(formated_current_time)
            self.time = formated_current_time
            return formated_current_time
        
        self.main_ui.sdt_kh_tbx.clear()
        self.main_ui.ten_kh_tbx.clear()
        self.main_ui.giam_gia_tbx.clear()
        self.main_ui.tong_tien_tbx.clear()
        #Clear row table
        self.main_ui.ds_dich_vu_tb.setRowCount(0)
        #Set số lượng về 1
        self.main_ui.sl_dich_vu_cbx.setValue(1)
        #Set combobox về giá trị đầu
        self.main_ui.ten_tho_cbx.setCurrentIndex(0)
        self.main_ui.dich_vu_cbx.setCurrentIndex(0)
        generate_sohd()
        get_time()


    
    #Sinh số CTHĐ
    def generate_socthd(self):
        query = "SELECT so_cthd FROM ChiTietHoaDon ORDER BY so_cthd DESC LIMIT 1"
        obj_type = "CTHD"
        byte = 3
        first_id = "001"
        result = self._mysql_connector.execute_query(query,select=True)
        if result:
            last_ma = result[0][0]
            last_number = int(last_ma[4:])
            so_cthd = obj_type+str(last_number).zfill(byte)
            return so_cthd
        else:
            return str(obj_type+first_id)
    
    
    
    #Lấy thông tin dịch vụ được chọn
    def get_info_dv(self):
        selected_items = self.main_ui.ds_dich_vu_tb.selectedItems()
        if not selected_items:
                return
        row = self.main_ui.ds_dich_vu_tb.currentRow()
        return row
    
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
    
    #Lấy danh sách dịch vụ hiển thị lên combobox     
    def get_dich_vu(self):
        query = "SELECT ten_dv FROM DichVu"
        result = self._mysql_connector.execute_query(query=query,select=True)
        l_ten_dv = [result[0] for result in result]
        return l_ten_dv
    
    #Thêm dịch vụ
    def them_dich_vu(self):
        dich_vu = self.main_ui.dich_vu_cbx.currentText()
        so_luong = self.main_ui.sl_dich_vu_cbx.value()
        
        query = "SELECT don_gia FROM DichVu WHERE ten_dv=%s"
        result = self._mysql_connector.execute_query(query=query,params=(dich_vu,),select=True)
        don_gia = result[0][0]
        formatted_dg = "{:,.0f}".format(don_gia).replace(',','.')
        thanh_tien = int(so_luong)*float(don_gia)
        formatted_tt = "{:,.0f}".format(thanh_tien).replace(',','.')
        self.tong_tien+=thanh_tien
        
        if dich_vu and so_luong is not None:
            rowCount = self.main_ui.ds_dich_vu_tb.rowCount()
            self.main_ui.ds_dich_vu_tb.insertRow(rowCount)
            
            self.main_ui.ds_dich_vu_tb.setItem(rowCount,0,self.main_form.create_centered_item(dich_vu))
            self.main_ui.ds_dich_vu_tb.setItem(rowCount,1,self.main_form.create_centered_item(str(so_luong)))
            self.main_ui.ds_dich_vu_tb.setItem(rowCount,2,self.main_form.create_centered_item(str(formatted_dg)))
            self.main_ui.ds_dich_vu_tb.setItem(rowCount,3,self.main_form.create_centered_item(str(formatted_tt)))
        
        self.tinh_tien()

    #Xoá dịch vụ
    def xoa_dich_vu(self):
        selected_dv = self.get_info_dv()
        if selected_dv is not None:
            item = self.main_ui.ds_dich_vu_tb.item(selected_dv, 3)
            if item is not None:
                thanh_tien = float(item.text().replace('.', '').replace(',',''))
                self.tong_tien -= thanh_tien
            self.main_ui.ds_dich_vu_tb.removeRow(selected_dv)
        self.tinh_tien() 
        
    #Tính tiền 
    def tinh_tien(self):
        try:
            giam_gia = self.main_ui.giam_gia_tbx.text()
            tong_tien_dv = self.tong_tien
            
            if giam_gia:
                giam_gia_int = int(giam_gia)
                tong_hoa_don = tong_tien_dv - ((int(giam_gia_int)/100) * tong_tien_dv)
            else:
                tong_hoa_don = tong_tien_dv
            
            formatted_tong_hd = "{:,.0f}".format(tong_hoa_don).replace(',','.')
            self.main_ui.tong_tien_tbx.setText(str(formatted_tong_hd))
        except mysql.connector.Error as err:
            print(err)
            QtWidgets.QMessageBox.information(self.main_form,"Thông báo","Nhập không đúng định dạng")
    
    def bo_qua_hd(self):
        #Clear textbox
        self.main_ui.so_hd_tbx.clear()
        self.main_ui.time_tbx.clear()
        self.main_ui.sdt_kh_tbx.clear()
        self.main_ui.ten_kh_tbx.clear()
        self.main_ui.giam_gia_tbx.clear()
        self.main_ui.tong_tien_tbx.clear()
        #Clear row table
        self.main_ui.ds_dich_vu_tb.setRowCount(0)
        #Set số lượng về 1
        self.main_ui.sl_dich_vu_cbx.setValue(1)
        #Set combobox về giá trị đầu
        self.main_ui.ten_tho_cbx.setCurrentIndex(0)
        self.main_ui.dich_vu_cbx.setCurrentIndex(0)
    
    #Lưu hoá đơn
    def luu_hd(self):
        print("dang luu hd")
        so_hd = self.so_hd
        sdt_kh = self.main_ui.sdt_kh_tbx.text()
        giam_gia_text = self.main_ui.giam_gia_tbx.text()
        giam_gia = int(giam_gia_text) if giam_gia_text else 0
        thoi_gian_tt = self.time
        so_cthd = self.generate_socthd()
        
        #Lấy mã khách hàng từ sdt
        query_kh = "SELECT ma_kh FROM KhachHang WHERE sdt_kh=%s"
        result_kh = self._mysql_connector.execute_query(query=query_kh,params=(sdt_kh,),select=True)
        if result_kh:
            ma_kh = result_kh[0][0]
        else:
            ma_kh = None
        
        #Lấy mã thợ từ combobox
        ten_tho = self.main_ui.ten_tho_cbx.currentText()
        query_tho = "SELECT ma_tho FROM Tho WHERE ten_tho = %s"
        result_tho = self._mysql_connector.execute_query(query=query_tho,params=(ten_tho,),select=True)
        if result_tho:
            ma_tho = result_tho[0][0]
        else:
            ma_tho = None
        
        query_hd = "INSERT INTO HoaDon (so_hd,ma_kh,sdt_kh,ma_tho,giam_gia,tong_tien,thoi_gian_tt) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        params_hd = (so_hd,ma_kh,sdt_kh,ma_tho,giam_gia,self.tong_tien,thoi_gian_tt)
        self._mysql_connector.execute_query(query=query_hd,params=params_hd)
        
        for row in range(self.main_ui.ds_dich_vu_tb.rowCount()):
            dich_vu = self.main_ui.ds_dich_vu_tb.item(row, 0).text()
            so_luong = self.main_ui.ds_dich_vu_tb.item(row, 1).text()
            don_gia = float(self.main_ui.ds_dich_vu_tb.item(row, 2).text().replace('.', '').replace(',', ''))
            thanh_tien = float(self.main_ui.ds_dich_vu_tb.item(row, 3).text().replace('.', '').replace(',', ''))
              
            last_number = int(so_cthd[4:])
            new_number = last_number + 1
            so_cthd = "CTHD"+str(new_number).zfill(3)

            print(so_cthd)
            #Lấy mã dịch vụ từ combobox
            ten_dv = dich_vu
            query_dv = "SELECT ma_dv FROM DichVu WHERE ten_dv = %s"
            result_dv = self._mysql_connector.execute_query(query=query_dv,params=(ten_dv,),select=True)
            if result_dv:
                ma_dv = result_dv[0][0]
            else:
                ma_dv = None
            
            print(dich_vu)
            self.ds_dv.append((so_cthd, so_hd, ma_dv, so_luong, don_gia, thanh_tien))
        query_cthd = "INSERT INTO ChiTietHoaDon (so_cthd,so_hd,ma_dv,so_luong_dv,don_gia,thanh_tien) VALUES (%s,%s,%s,%s,%s,%s)"
        params_cthd = self.ds_dv
        self._mysql_connector.execute_many_query(query=query_cthd,params=params_cthd)
        print("Lưu hoá đơn thành công")
        QtWidgets.QMessageBox.information(self.main_form,"Thông báo","Lưu hoá đơn thành công")
        self.tong_tien = 0
            