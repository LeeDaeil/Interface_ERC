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
        vl.addWidget(SignalResultAlarmWidget(self))

        hl = QHBoxLayout()
        hl.addStretch(1)
        hl.addWidget(SignalResultClose(self))
        vl.addLayout(hl)
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
        self.startTimer(600)
        self.gl = QGridLayout(self)

        self.fault_alarms = {
            1: SignalResultAlarmItem(self, in_text='Feedwater pump outlet press'),
            2: SignalResultAlarmItem(self, in_text='Feedwater line #1 flow'),
            3: SignalResultAlarmItem(self, in_text='Feedwater line #2 flow'),
            4: SignalResultAlarmItem(self, in_text='Feedwater line #3 flow'),
            5: SignalResultAlarmItem(self, in_text='Feedwater temperature'),
            6: SignalResultAlarmItem(self, in_text='Main steam flow'),
            7: SignalResultAlarmItem(self, in_text='Steam line #3 flow'),
            8: SignalResultAlarmItem(self, in_text='Steam line #2 flow'),
            9: SignalResultAlarmItem(self, in_text='Steam line #1 flow'),
            10: SignalResultAlarmItem(self, in_text='Main steam header pressure'),
            11: SignalResultAlarmItem(self, in_text='Charging line outlet temperature'),
            12: SignalResultAlarmItem(self, in_text='Loop #1 cold-leg temperature'),
            13: SignalResultAlarmItem(self, in_text='Loop #2 cold-leg temperature'),
            14: SignalResultAlarmItem(self, in_text='Loop #3 cold-leg temperature'),
            15: SignalResultAlarmItem(self, in_text='PRZ temperature'),
            16: SignalResultAlarmItem(self, in_text='Core outlet temperature'),
            17: SignalResultAlarmItem(self, in_text='Net letdown flow'),
            18: SignalResultAlarmItem(self, in_text='PRZ level'),
            19: SignalResultAlarmItem(self, in_text='PRZ pressure (wide range)'),
            20: SignalResultAlarmItem(self, in_text='Loop #1 flow'),
            21: SignalResultAlarmItem(self, in_text='Loop #2 flow'),
            22: SignalResultAlarmItem(self, in_text='Loop #3 flow'),
            23: SignalResultAlarmItem(self, in_text='S/G #1 level'),
            24: SignalResultAlarmItem(self, in_text='S/G #2 level'),
            25: SignalResultAlarmItem(self, in_text='S/G #3 level'),
            26: SignalResultAlarmItem(self, in_text='S/G #1 pressure'),
            27: SignalResultAlarmItem(self, in_text='S/G #2 pressure'),
            28: SignalResultAlarmItem(self, in_text='S/G #3 pressure'),
        }

        for i, item in enumerate(self.fault_alarms.values()):
            col = i%4
            row = i//4
            self.gl.addWidget(item, row, col)
        
    def timerEvent(self, a0: 'QTimerEvent') -> None:
        dis_nub = self.inmem.ShMem.get_para_val('iSigValOnDis')
        for key in self.fault_alarms.keys():
            self.fault_alarms[key].blink_fun(True if key == dis_nub else False)
        return super().timerEvent(a0)
class SignalResultAlarmItem(ABCLabel):
    def __init__(self, parent, widget_name='', in_text=''):
        super().__init__(parent, widget_name)
        self.setText(in_text)
        self.blink = False

    def blink_fun(self, run=False):
        if run:
            self.blink = not self.blink
            self.setProperty('blinking', self.blink)
            self.inmem.widget_ids['SignalResultWidgetResult'].setText(self.text())
        else:
            self.setProperty('blinking', False)
        self.style().polish(self)
class SignalResultClose(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setText('닫기')

    def mousePressEvent(self, e: QMouseEvent) -> None:
        self.inmem.widget_ids['SignalWindow'].close()
        return super().mousePressEvent(e)