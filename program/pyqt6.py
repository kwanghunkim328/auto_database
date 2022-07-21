import sys
from PyQt6.QtWidgets import *
from PyQt6 import uic
import os

UI_class = uic.loadUiType('uniform.ui')[0]

class main_window(QMainWindow, UI_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('자사몰 네이버 포맷')
    
        self.ImWeb_file.setText('자사몰')
        self.Naver_file.setText('스마트스토어')
        self.original_label.setText('오리지널 저장 경로')
        self.honest_label.setText('어니스트 저장 경로')
    
        self.ImWeb_file_btn.clicked.connect(self.imweb_FileLoad)
        self.Naver_file_btn.clicked.connect(self.naver_FileLoad)  
        self.Format_func_btn.clicked.connect(self.Format_functions)
        
    def imweb_FileLoad(self):
        global iwfname
        iwfname = QFileDialog.getOpenFileName(self)
        self.ImWeb_file.setText(os.path.basename(iwfname[0]))
        
    
    
    def naver_FileLoad(self):
        global nvfname
        nvfname = QFileDialog.getOpenFileName(self)
        self.Naver_file.setText(os.path.basename(nvfname[0]))
        
        
    
    def Format_functions(self):
        print(iwfname[0])
        print(nvfname[0])
        
        
    
            
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    Window = main_window()
    Window.show()
    app.exec()
        