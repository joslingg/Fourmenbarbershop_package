import sys
sys.path.append('../DO AN')
from PyQt5 import QtWidgets,QtCore
from Fourmenbarbershop_package.gui import login_ui
from Fourmenbarbershop_package.subclasses.Signup import SignupForm

class LoginForm(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        #Khai báo login form
        self.login_ui = login_ui.Ui_login_form()
        self.login_ui.setupUi(self)
        
        self.login_ui.login_btn.clicked.connect(self.handle_login)
        self.login_ui.create_acc_link.clicked.connect(self.open_signup_form)
        
    def handle_login(self):
        pass
    def open_signup_form(self):
        self.signup_form = SignupForm()
        self.signup_form.exec_()
        

    
            