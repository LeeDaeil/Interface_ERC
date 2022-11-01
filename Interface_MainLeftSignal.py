from dis import dis
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Interface_ABCWidget import *
from Interface_QSS import qss

class SignalWindow(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setGeometry(0, 0, 500, 400)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 상단바 제거
        self.setStyleSheet(qss) # qss load
        self.m_flag = False

        vl = QVBoxLayout(self)
        self.title_label = SignalTitle(self)
        vl.addWidget(self.title_label)
        vl.addWidget(SignalResultWidget(self))

    # window drag
    def mousePressEvent(self, event):        
        if (event.button() == Qt.LeftButton) and self.title_label.underMouse():
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag and self.title_label.underMouse():
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 윈도우 position 변경
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

class SignalTitle(ABCLabel):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setText('Signal Validation')
        self.setFixedHeight(30)

class SignalResultWidget(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        hl = QHBoxLayout(self)
        hl.addWidget(SignalResultWidgetTitle(self))
        hl.addWidget(SignalResultWidgetResult(self))

class SignalResultWidgetTitle(ABCLabel):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setText('Signal Validation Result :')

class SignalResultWidgetResult(ABCLabel):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setText('')

class SignalResultAlarmWidget(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.startTimer(200)
        
        gl = QGridLayout(self)
        gl.addWidget(0, 0, SignalResultAlarmItem(self))
        
    def timerEvent(self, a0: 'QTimerEvent') -> None:
        dis_nub = self.inmem.ShMem.get_para_val('iSigValOnDis')
        return super().timerEvent(a0)

class SignalResultAlarmItem(ABCLabel):
    def __init__(self, parent, widget_name='', in_text=''):
        super().__init__(parent, widget_name)
        self.setText(in_text)