import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *  # 아이콘 객체

app = QApplication(sys.argv) # 필수객체

class MyWindow(QMainWindow): # 윈도우 객체
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('ex')  # 윈도우 창 타이틀
        
        self.setGeometry(300,300,400,400) # 창 위치 x,y / 창 크기 x,y
        
        # self.setWindowIcon(QIcon('path')) # 아이콘 적용

# window = QWidget() # 화면 창
window = MyWindow()

window.show() # 출력 

app.exec_() # 닫기 전 까지 loop 