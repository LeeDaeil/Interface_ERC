from datetime import datetime

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Interface_ABCWidget import *

class MainTopBar(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setFixedHeight(50)
        # Frame ------------------------------------------------------
        hl = QHBoxLayout(self)
        self.timerlabel = MainTopBarTimer(self)
        hl.addWidget(self.timerlabel)
        hl.addStretch(1)
        hl.setContentsMargins(10, 8, 10, 7)
        hl.addWidget(MainTopBarClose(self))
    
    def check_mouse_in_area(self):
        return any([self.underMouse(), self.timerlabel.underMouse()])
    
class MainTopBarTimer(ABCLabel):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setFixedSize(376, 35)
        self.startTimer(200)

    def timerEvent(self, a0: 'QTimerEvent') -> None:
        current_time = datetime.now() + self.inmem.get_time()
        real_time = current_time.strftime('%Y.%m.%d')
        real_time2 = current_time.strftime("%H:%M:%S")
        self.setText(real_time + " / " + real_time2)
        return super().timerEvent(a0)

class MainTopBarClose(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setFixedSize(35, 35)

    def mousePressEvent(self, e: QMouseEvent) -> None:
        self.inmem.widget_ids['Main'].close()
        return super().mousePressEvent(e)