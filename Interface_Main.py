import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Function_Mem_ShMem import InterfaceMem
from Interface_ABCWidget import *
from Interface_QSS import qss

from Interface_MainTopBar import MainTopBar
from Interface_MainLeft import MainLeft
from Interface_MainMiddle import MainMiddle
from Interface_MainRight import MainRight

class Main(QWidget):
    def __init__(self, ShMem):
        super(Main, self).__init__()
        self.inmem:InterfaceMem = InterfaceMem(ShMem, self)
        self.setGeometry(0, 0, 2560, 1440)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 상단바 제거
        self.setObjectName('Main')
        self.setStyleSheet(qss) # qss load
        self.m_flag = False
        # Frame ------------------------------------------------------
        hl = QVBoxLayout(self)
        hl.setContentsMargins(0, 0, 0, 0)
        self.maintopbar = MainTopBar(self)
        hl.addWidget(self.maintopbar)
        hl.setSpacing(0)
        vl = QHBoxLayout()
        vl.setContentsMargins(10, 10, 10, 10)        
        vl.addWidget(MainLeft(self))
        vl.addWidget(MainMiddle(self))
        vl.addWidget(MainRight(self))
        vl.setSpacing(10)
        hl.addLayout(vl)

        # End frame --------------------------------------------------
    def check_mouse_in_area(self):
        return any([self.underMouse()])
    # window drag
    def mousePressEvent(self, event):        
        if (event.button() == Qt.LeftButton) and self.check_mouse_in_area():
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag and self.check_mouse_in_area():
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 윈도우 position 변경
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def close(self) -> bool:
        QApplication.closeAllWindows()
        return super().close()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        qp.setPen(QPen(QColor(192, 0, 0), 2))
        qp.drawRect(5, 1195, 590, 236)
        qp.end()
