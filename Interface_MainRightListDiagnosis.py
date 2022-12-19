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
        self.startTimer(300)
        self.gl = QGridLayout(self)

        self.fault_alarms = {
            0:  DiagnosisResultPackWidget(self, in_text='Normal',                                 nub=0),
            1:  DiagnosisResultPackWidget(self, in_text='AB21-01\n가압기 압력 채널 고장(고)',       nub=1),
            2:  DiagnosisResultPackWidget(self, in_text='AB21-02\n가압기 압력 채널 고장(저)',       nub=2),
            3:  DiagnosisResultPackWidget(self, in_text='AB20-01\n가압기 수위 채널 고장(고)',       nub=3),
            4:  DiagnosisResultPackWidget(self, in_text='AB20-04\n가압기 수위 채널 고장(저)',       nub=4),
            5:  DiagnosisResultPackWidget(self, in_text='AB15-07\n증기발생기 수위\n채널 고장(고)',  nub=5),
            6:  DiagnosisResultPackWidget(self, in_text='AB15-08\n증기발생기 수위\n채널 고장(저)',  nub=6),
            7:  DiagnosisResultPackWidget(self, in_text='AB63-04\n제어봉 낙하',                    nub=7),
            8:  DiagnosisResultPackWidget(self, in_text='AB63-02\n제어봉의 계속적인 삽입',          nub=8),
            9:  DiagnosisResultPackWidget(self, in_text='AB63-03\n제어봉의 계속적인 인출',          nub=9),
            10: DiagnosisResultPackWidget(self, in_text='AB21-12\n가압기 PORV 고장(열림)',         nub=10),
            11: DiagnosisResultPackWidget(self, in_text='AB19-02\n가압기 안전 밸브 고장(열림)',     nub=11),
            12: DiagnosisResultPackWidget(self, in_text='AB21-11\n가압기 살수 밸브 고장(열림)',     nub=12),
            13: DiagnosisResultPackWidget(self, in_text='AB23-03\n1차측 RCS 누설 (Leak)',          nub=13),
            14: DiagnosisResultPackWidget(self, in_text='AB80-02\n주급수 펌프 2/3대 정지',          nub=14),
            15: DiagnosisResultPackWidget(self, in_text='AB06-02\n재생열 교환기 전단 파열',         nub=15),
            16: DiagnosisResultPackWidget(self, in_text='AB59-02\n충전수 유량조절밸브\n전단 누설 (Leak)',          nub=16),
            17: DiagnosisResultPackWidget(self, in_text='AB23-01\n1차측 CVCS 계통\n누설 (Leak)',   nub=17),
            18: DiagnosisResultPackWidget(self, in_text='AB23-06\n증기발생기 전열관\n누설 (Leak)',  nub=18),
            19: DiagnosisResultPackWidget(self, in_text='AB59-01\n충전수 유량조절밸브\n후단 누설 (Leak)',  nub=19),
            20: DiagnosisResultPackWidget(self, in_text='AB64-03\n주증기관 밸브 고장 (닫힘)',       nub=20),
        }

        for i, item in enumerate(self.fault_alarms.values()):
            col = i%3
            row = i//3
            self.gl.addWidget(item, row, col)
        
    def timerEvent(self, a0: 'QTimerEvent') -> None:
        [self.fault_alarms[key].blink_fun() for key in self.fault_alarms.keys()]
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