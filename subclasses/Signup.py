import sys
sys.path.append('../DO AN')
from PyQt5 import QtWidgets,QtCore
from Fourmenbarbershop_package.gui import signup_ui


class SignupForm(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        #Khai báo signup form
        self.signup_ui = signup_ui.Ui_signup_form()
        self.signup_ui.setupUi(self)
        
        self.signup_ui.signup_btn.clicked.connect(self.handle_signup)
    
    def handle_signup(self):
        pass
