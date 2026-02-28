import sys
import urllib.request

from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QLabel,QLineEdit,QPushButton,QMessageBox
from PyQt5.qtGui import QFont, QPalette, QColor

class CheckerApp(QWidget):
    def _init_(self):
    super()._init_()
    self.init_ui()

def init_ui(self):
    """Starts UI/Widget"""
    pass

def check_site(self):
    """ online check"""
    pass

def init_ui(self):
    """UI styling"""
    self.setWindowTitle("Connection Checker")
    self.setGeomtry(100,100,400,200)

#Customize font/palette
app_font= QFont("Arial",12)
self.setFont(app_font)

layout = QVBoxLayout()


self.label = QLabel("Enter Url")
self.label.setStyleSheet("color:#003366; font-size: 14px; font-weight: bold;")

layout.addWidget(self.label)

self.url_input = QLineEdit(self)
self.url_input.setPlaceholderText("URL...")

self.url_input.setStyleSheet("""

        QLineEdit{
                             border:2px solid #007BFF;
                             
                             
                             }

""")