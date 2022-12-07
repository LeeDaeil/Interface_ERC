from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Interface_ABCWidget import *
from Interface_QSS import qss

class DiagnosisWindow(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setGeometry(594, 323, 500, 400)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 상단바 제거
        self.setAttribute(Qt.WA_TranslucentBackground)  # widget 투명화
        self.setStyleSheet(qss) # qss load
        self.m_flag = False

        vl = QVBoxLayout(self)
        vl.setSpacing(0)
        vl.setContentsMargins(0, 0, 0, 0)
        self.title_label = DiagnosisTitle_BG(self)
        vl.addWidget(self.title_label)
        vl.addWidget(DiagnosisResultWidget_BG(self))
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
        print(self.widget_name, self.geometry())
class DiagnosisTitle_BG(ABCLabel):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setFixedHeight(25 + 10) # Title size + margin * 2
        hl = QHBoxLayout(self)
        hl.setContentsMargins(5, 5, 5, 5)
        hl.addWidget(DiagnosisTitle(self))
        hl.addStretch(1)
class DiagnosisTitle(ABCLabel):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setText('Diagnosis Validation')
        self.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)
        self.setFixedHeight(30)
class DiagnosisResultWidget_BG(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        vl = QVBoxLayout(self)
        vl.setContentsMargins(10, 10, 10, 10)
        vl.addWidget(DiagnosisResultWidget(self))
        vl.addWidget(DiagnosisResultAlarmWidget(self))
        hl = QHBoxLayout()
        hl.addStretch(1)
        hl.addWidget(DiagnosisResultClose(self))
        vl.addLayout(hl)
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
        self.gl.setContentsMargins(2, 2, 2, 2)
        self.gl.setSpacing(0)

        self.fault_alarms = {
            0:  DiagnosisResultPackWidget(self, in_text='Normal',                                         nub=0, corners=['1', '2']),
            1:  DiagnosisResultPackWidget(self, in_text='AB21-01\n가압기 압력 채널 고장(고)',               nub=1),
            2:  DiagnosisResultPackWidget(self, in_text='AB21-02\n가압기 압력 채널 고장(저)',               nub=2, corners=['2', '3']),
            3:  DiagnosisResultPackWidget(self, in_text='AB20-01\n가압기 수위 채널 고장(고)',               nub=3),
            4:  DiagnosisResultPackWidget(self, in_text='AB20-04\n가압기 수위 채널 고장(저)',               nub=4),
            5:  DiagnosisResultPackWidget(self, in_text='AB15-07\n증기발생기 수위 채널 고장(고)',          nub=5, corners=['2', '4']),
            6:  DiagnosisResultPackWidget(self, in_text='AB15-08\n증기발생기 수위 채널 고장(저)',          nub=6),
            7:  DiagnosisResultPackWidget(self, in_text='AB63-04\n제어봉 낙하',                            nub=7),
            8:  DiagnosisResultPackWidget(self, in_text='AB63-02\n제어봉의 계속적인 삽입',                  nub=8, corners=['2', '4']),
            9:  DiagnosisResultPackWidget(self, in_text='AB63-03\n제어봉의 계속적인 인출',                  nub=9),
            10: DiagnosisResultPackWidget(self, in_text='AB21-12\n가압기 PORV 고장(열림)',                 nub=10),
            11: DiagnosisResultPackWidget(self, in_text='AB19-02\n가압기 안전 밸브 고장(열림)',             nub=11, corners=['2', '4']),
            12: DiagnosisResultPackWidget(self, in_text='AB21-11\n가압기 살수 밸브 고장(열림)',             nub=12),
            13: DiagnosisResultPackWidget(self, in_text='AB23-03\n1차측 RCS 누설 (Leak)',                  nub=13),
            14: DiagnosisResultPackWidget(self, in_text='AB80-02\n주급수 펌프 2/3대 정지',                  nub=14, corners=['2', '4']),
            15: DiagnosisResultPackWidget(self, in_text='AB06-02\n재생열 교환기 전단 파열',                 nub=15),
            16: DiagnosisResultPackWidget(self, in_text='AB59-02\n충전수 유량조절밸브 전단 누설 (Leak)',    nub=16),
            17: DiagnosisResultPackWidget(self, in_text='AB23-01\n1차측 CVCS 계통 누설 (Leak)',            nub=17, corners=['2', '4']),
            18: DiagnosisResultPackWidget(self, in_text='AB23-06\n증기발생기 전열관 누설 (Leak)',           nub=18, corners=['7', '6']),
            19: DiagnosisResultPackWidget(self, in_text='AB59-01\n충전수 유량조절밸브 후단 누설 (Leak)',    nub=19, corners=['6', '6']),
            20: DiagnosisResultPackWidget(self, in_text='AB64-03\n주증기관 밸브 고장 (닫힘)',               nub=20, corners=['6', '5']),
        }

        for i, item in enumerate(self.fault_alarms.values()):
            col = i%3
            row = i//3
            self.gl.addWidget(item, row, col)
        
    def timerEvent(self, a0: 'QTimerEvent') -> None:
        [self.fault_alarms[key].blink_fun() for key in self.fault_alarms.keys()]
        return super().timerEvent(a0)
class DiagnosisResultPackWidget(ABCWidget):
    def __init__(self, parent, in_text='', nub='', corners=['2', '2'], widget_name=''):
        super().__init__(parent, widget_name)
        self.nub = nub
        self.in_text = in_text
        hl = QHBoxLayout(self)
        hl.setContentsMargins(0, 0, 0, 0)
        hl.setSpacing(0)
        self.ab_name_w = DiagnosisResultAlarmItem(self, in_text=in_text, corner=corners[0])
        self.ab_name_w.setFixedWidth(370)
        self.ab_val_w = DiagnosisResultAlarmItem(self, in_text='', corner=corners[1])
        self.ab_val_w.setFixedWidth(80)
        hl.addWidget(self.ab_name_w)
        hl.addWidget(self.ab_val_w)

    def blink_fun(self):
        self.ab_val_w.setText(f'{self.inmem.ShMem.get_para_val(f"iDAB{self.nub:02}")}%')
        if self.nub == self.inmem.ShMem.get_para_val('iDABNub'):
            self.inmem.widget_ids['DiagnosisResultWidgetResult'].setText(self.in_text)
            self.ab_name_w.blink_fun(True if self.nub != 0 else False)
            self.ab_val_w.blink_fun(True if self.nub != 0 else False)
        else:
            self.ab_name_w.blink_fun(False)
            self.ab_val_w.blink_fun(False)
class DiagnosisResultAlarmItem(ABCLabel):
    def __init__(self, parent, widget_name='', in_text='', corner='2'):
        super().__init__(parent, widget_name)
        self.setText(in_text)
        self.setProperty('Corner', corner)
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