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
            1:  DiagnosisResultAlarmItem(self, in_text='Feedwater pump outlet press'),
            2:  DiagnosisResultAlarmItem(self, in_text='Feedwater line #1 flow'),
            3:  DiagnosisResultAlarmItem(self, in_text='Feedwater line #2 flow'),
            4:  DiagnosisResultAlarmItem(self, in_text='Feedwater line #3 flow'),
            5:  DiagnosisResultAlarmItem(self, in_text='Feedwater temperature'),
            6:  DiagnosisResultAlarmItem(self, in_text='Main steam flow'),
            7:  DiagnosisResultAlarmItem(self, in_text='Steam line #3 flow'),
            8:  DiagnosisResultAlarmItem(self, in_text='Steam line #2 flow'),
            9:  DiagnosisResultAlarmItem(self, in_text='Steam line #1 flow'),
            10: DiagnosisResultAlarmItem(self, in_text='Main steam header pressure'),
            11: DiagnosisResultAlarmItem(self, in_text='Charging line outlet temperature'),
            12: DiagnosisResultAlarmItem(self, in_text='Loop #1 cold-leg temperature'),
            13: DiagnosisResultAlarmItem(self, in_text='Loop #2 cold-leg temperature'),
            14: DiagnosisResultAlarmItem(self, in_text='Loop #3 cold-leg temperature'),
            15: DiagnosisResultAlarmItem(self, in_text='PRZ temperature'),
            16: DiagnosisResultAlarmItem(self, in_text='Core outlet temperature'),
            17: DiagnosisResultAlarmItem(self, in_text='Net letdown flow'),
            18: DiagnosisResultAlarmItem(self, in_text='PRZ level'),
            19: DiagnosisResultAlarmItem(self, in_text='PRZ pressure (wide range)'),
            20: DiagnosisResultAlarmItem(self, in_text='Loop #1 flow'),
            21: DiagnosisResultAlarmItem(self, in_text='Loop #2 flow'),
            22: DiagnosisResultAlarmItem(self, in_text='Loop #3 flow'),
            23: DiagnosisResultAlarmItem(self, in_text='S/G #1 level'),
            24: DiagnosisResultAlarmItem(self, in_text='S/G #2 level'),
            25: DiagnosisResultAlarmItem(self, in_text='S/G #3 level'),
            26: DiagnosisResultAlarmItem(self, in_text='S/G #1 pressure'),
            27: DiagnosisResultAlarmItem(self, in_text='S/G #2 pressure'),
            28: DiagnosisResultAlarmItem(self, in_text='S/G #3 pressure'),
        }

        for i, item in enumerate(self.fault_alarms.values()):
            col = i%3
            row = i//3
            self.gl.addWidget(item, row, col)
        
    # def timerEvent(self, a0: 'QTimerEvent') -> None:
    #     dis_nub = self.inmem.ShMem.get_para_val('iSigValOnDis')
    #     for key in self.fault_alarms.keys():
    #         self.fault_alarms[key].blink_fun(True if key == dis_nub else False)
    #     return super().timerEvent(a0)
class DiagnosisResultPackWidget(ABCWidget):
    def __init__(self, parent, in_text='', nub='', widget_name=''):
        super().__init__(parent, widget_name)
        self.nub = nub
        self.in_text = in_text
        hl = QHBoxLayout(self)
        self.ab_name_w = DiagnosisResultAlarmItem(self, in_text=in_text)
        self.ab_val_w = DiagnosisResultAlarmItem(self, in_text='')
        hl.addWidget(DiagnosisResultAlarmItem)

    def blink_fun(self, run=False):
        if run:
            self.inmem.widget_ids['DiagnosisResultWidgetResult'].setText(self.in_text)
        self.ab_val_w.setText(f'{self.inmem.ShMem.get_para_val(f"AB{self.nub:02}")}')
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