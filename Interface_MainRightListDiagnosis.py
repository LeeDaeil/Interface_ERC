from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Interface_ABCWidget import *
from Interface_QSS import qss

class DiagnosisWindow(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setGeometry(0, 0, 500, 400)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 상단바 제거
        self.setStyleSheet(qss) # qss load
        self.m_flag = False

        vl = QVBoxLayout(self)
        self.title_label = DiagnosisTitle(self)
        vl.addWidget(self.title_label)
        vl.addWidget(DiagnosisResultWidget(self))
        vl.addWidget(DiagnosisResultAlarmWidget(self))

        hl = QHBoxLayout()
        hl.addStretch(1)
        hl.addWidget(DiagnosisResultClose(self))
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
class DiagnosisTitle(ABCLabel):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setText('Diagnosis Validation')
        self.setFixedHeight(30)
class DiagnosisResultWidget(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        hl = QHBoxLayout(self)
        hl.addWidget(DiagnosisResultWidgetTitle(self))
        hl.addWidget(DiagnosisResultWidgetResult(self))
class DiagnosisResultWidgetTitle(ABCLabel):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setText('Diagnosis Validation Result :')
class DiagnosisResultWidgetResult(ABCLabel):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setText('')
class DiagnosisResultAlarmWidget(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.startTimer(600)
        self.gl = QGridLayout(self)

        self.fault_alarms = {
            0:  DiagnosisResultPackWidget(self, in_text='Normal',                           nub=0),
            1:  DiagnosisResultPackWidget(self, in_text='Feedwater pump outlet press',      nub=1),
            2:  DiagnosisResultPackWidget(self, in_text='Feedwater line #1 flow',           nub=2),
            3:  DiagnosisResultPackWidget(self, in_text='Feedwater line #2 flow',           nub=3),
            4:  DiagnosisResultPackWidget(self, in_text='Feedwater line #3 flow',           nub=4),
            5:  DiagnosisResultPackWidget(self, in_text='Feedwater temperature',            nub=5),
            6:  DiagnosisResultPackWidget(self, in_text='Main steam flow',                  nub=6),
            7:  DiagnosisResultPackWidget(self, in_text='Steam line #3 flow',               nub=7),
            8:  DiagnosisResultPackWidget(self, in_text='Steam line #2 flow',               nub=8),
            9:  DiagnosisResultPackWidget(self, in_text='Steam line #1 flow',               nub=9),
            10: DiagnosisResultPackWidget(self, in_text='Main steam header pressure',       nub=10),
            11: DiagnosisResultPackWidget(self, in_text='Charging line outlet temperature', nub=11),
            12: DiagnosisResultPackWidget(self, in_text='Loop #1 cold-leg temperature',     nub=12),
            13: DiagnosisResultPackWidget(self, in_text='Loop #2 cold-leg temperature',     nub=13),
            14: DiagnosisResultPackWidget(self, in_text='Loop #3 cold-leg temperature',     nub=14),
            15: DiagnosisResultPackWidget(self, in_text='PRZ temperature',                  nub=15),
            16: DiagnosisResultPackWidget(self, in_text='Core outlet temperature',          nub=16),
            17: DiagnosisResultPackWidget(self, in_text='Net letdown flow',                 nub=17),
            18: DiagnosisResultPackWidget(self, in_text='PRZ level',                        nub=18),
            19: DiagnosisResultPackWidget(self, in_text='PRZ pressure (wide range)',        nub=19),
            20: DiagnosisResultPackWidget(self, in_text='Loop #1 flow',                     nub=20),
            21: DiagnosisResultPackWidget(self, in_text='Loop #2 flow',                     nub=21),
            22: DiagnosisResultPackWidget(self, in_text='Loop #3 flow',                     nub=22),
            23: DiagnosisResultPackWidget(self, in_text='S/G #1 level',                     nub=23),
            24: DiagnosisResultPackWidget(self, in_text='S/G #2 level',                     nub=24),
            25: DiagnosisResultPackWidget(self, in_text='S/G #3 level',                     nub=25),
            26: DiagnosisResultPackWidget(self, in_text='S/G #1 pressure',                  nub=26),
            27: DiagnosisResultPackWidget(self, in_text='S/G #2 pressure',                  nub=27),
            28: DiagnosisResultPackWidget(self, in_text='S/G #3 pressure',                  nub=28),
        }

        for i, item in enumerate(self.fault_alarms.values()):
            col = i%3
            row = i//3
            self.gl.addWidget(item, row, col)
        
    def timerEvent(self, a0: 'QTimerEvent') -> None:
        [self.fault_alarms[key].blink_fun() for key in self.fault_alarms.keys()]
        return super().timerEvent(a0)
class DiagnosisResultPackWidget(ABCWidget):
    def __init__(self, parent, in_text='', nub='', widget_name=''):
        super().__init__(parent, widget_name)
        self.nub = nub
        self.in_text = in_text
        hl = QHBoxLayout(self)
        self.ab_name_w = DiagnosisResultAlarmItem(self, in_text=in_text)
        self.ab_val_w = DiagnosisResultAlarmItem(self, in_text='')
        hl.addWidget(self.ab_name_w)
        hl.addWidget(self.ab_val_w)

    def blink_fun(self):
        self.ab_val_w.setText(f'{self.inmem.ShMem.get_para_val(f"iDAB{self.nub:02}")} [%]')
        if self.nub == self.inmem.ShMem.get_para_val('iDABNub'):
            self.inmem.widget_ids['DiagnosisResultWidgetResult'].setText(self.in_text)
            self.ab_name_w.blink_fun(True if self.nub != 0 else False)
            self.ab_val_w.blink_fun(True if self.nub != 0 else False)
        else:
            self.ab_name_w.blink_fun(False)
            self.ab_val_w.blink_fun(False)
            
class DiagnosisResultAlarmItem(ABCLabel):
    def __init__(self, parent, widget_name='', in_text=''):
        super().__init__(parent, widget_name)
        self.setText(in_text)
        self.blink = False

    def blink_fun(self, run=False):
        if run:
            self.blink = not self.blink
            self.setProperty('blinking', self.blink)
        else:
            self.setProperty('blinking', False)
        self.style().polish(self)
class DiagnosisResultClose(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setText('닫기')

    def mousePressEvent(self, e: QMouseEvent) -> None:
        self.inmem.widget_ids['DiagnosisWindow'].close()
        return super().mousePressEvent(e)