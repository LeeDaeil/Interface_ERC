import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Function_Mem_ShMem import InterfaceMem
from Interface_ABCWidget import *
from Interface_QSS import qss

from Interface_MainTopBar import MainTopBar
from Interface_MainLeft import MainLeft

class Main(QWidget):
    def __init__(self, ShMem):
        super(Main, self).__init__()
        self.inmem:InterfaceMem = InterfaceMem(ShMem, self)
        self.setGeometry(0, 0, 1920, 1080)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 상단바 제거
        self.setObjectName('Main')
        self.setStyleSheet(qss) # qss load
        self.m_flag = False
        # Frame ------------------------------------------------------
        hl = QVBoxLayout(self)
        self.maintopbar = MainTopBar(self)
        hl.addWidget(self.maintopbar)
        #
        vl = QHBoxLayout()
        hl.addLayout(vl)
        vl.addWidget(MainLeft(self))
        # End frame --------------------------------------------------
        
    # window drag
    def mousePressEvent(self, event):        
        if (event.button() == Qt.LeftButton) and self.maintopbar.check_mouse_in_area():
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag and self.maintopbar.check_mouse_in_area():
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 윈도우 position 변경
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def close(self) -> bool:
        QApplication.closeAllWindows()
        return super().close()