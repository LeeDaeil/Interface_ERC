from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Interface_ABCWidget import *
from Interface_QSS import qss

class CSFMonitoringWindow(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setGeometry(594, 324, 850, 600)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 상단바 제거
        self.setAttribute(Qt.WA_TranslucentBackground)  # widget 투명화
        self.setStyleSheet(qss) # qss load
        self.m_flag = False

        vl = QVBoxLayout(self)
        vl.setSpacing(0)
        vl.setContentsMargins(0, 0, 0, 0)
        self.title_label = CSFMonitoringTitle_BG(self)
        vl.addWidget(self.title_label)
        vl.addWidget(CSFMonitoringAlarmWidget_BG(self))
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
class CSFMonitoringTitle_BG(ABCLabel):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setFixedHeight(25 + 10) # Title size + margin * 2
        hl = QHBoxLayout(self)
        hl.setContentsMargins(10, 5, 5, 5)
        hl.addWidget(CSFMonitoringTitle(self))
        hl.addStretch(1)
class CSFMonitoringTitle(ABCLabel):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setText('CSF Monitoring')
        self.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)
        self.setFixedSize(240, 25)
class CSFMonitoringAlarmWidget_BG(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        vl = QVBoxLayout(self)
        vl.setContentsMargins(15, 15, 15, 15)
        vl.setSpacing(15)
        vl.addWidget(CSFMonitoringAlarmWidget(self))
        hl = QHBoxLayout()
        hl.addStretch(1)
        hl.setContentsMargins(0, 0, 0, 0)
        hl.addWidget(CSFMonitoringClose(self))
        vl.addLayout(hl)
class CSFMonitoringAlarmWidget(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.startTimer(600)
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        vl = QVBoxLayout(self)
        vl.setContentsMargins(0, 0, 0, 0)
        vl.setSpacing(15)
        self.csf_info = {
            'Reactivity Control': [QButtonGroup(), 'iCSFReactivity'],
            'Core Heat Removal': [QButtonGroup(), 'iCSFCoreHeat'],
            'RCS Heat Removal': [QButtonGroup(), 'iCSFRCSHeat'],
            'RCS Pressure Control': [QButtonGroup(), 'iCSFRCSPres'],
            'Containment Pressure and Temperature Control': [QButtonGroup(), 'iCSFCTMT'],
            'RCS Inventory Control': [QButtonGroup(), 'iCSFRCSInvt'],
        }

        for key, val in self.csf_info.items():
            h = QHBoxLayout()
            h.setContentsMargins(0, 0, 0, 0)
            h.setSpacing(10)
            h.addWidget(CSFMonitoringAlarmLabel(self, in_text=key))
            val[0].addButton(CSFMonitoringAlarmLevel1Item(self))
            val[0].addButton(CSFMonitoringAlarmLevel2Item(self))
            val[0].addButton(CSFMonitoringAlarmLevel3Item(self))
            val[0].addButton(CSFMonitoringAlarmLevel4Item(self))
            [h.addWidget(w) for w in val[0].buttons()]
            vl.addLayout(h)

        QButtonGroup().buttons()

    def timerEvent(self, a0: 'QTimerEvent') -> None:
        for key, val in self.csf_info.items():
            state = self.inmem.ShMem.get_para_val(val[1])
            val[0].buttons()[int(state)].setChecked(True)
        return super().timerEvent(a0)
class CSFMonitoringAlarmLabel(ABCLabel):
    def __init__(self, parent, widget_name='', in_text=''):
        super().__init__(parent, widget_name)
        self.setText(in_text)
        self.setWordWrap(True)
        self.setFixedSize(260, 70)
class CSFMonitoringAlarmLevel1Item(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setText(f'Level 1')
        self.setCheckable(True)
        self.setChecked(True)
        self.setFixedSize(130, 70)
class CSFMonitoringAlarmLevel2Item(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setText(f'Level 2')
        self.setCheckable(True)
        self.setChecked(False)
        self.setFixedSize(130, 70)
class CSFMonitoringAlarmLevel3Item(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setText(f'Level 3')
        self.setCheckable(True)
        self.setChecked(False)
        self.setFixedSize(130, 70)
class CSFMonitoringAlarmLevel4Item(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setText(f'Level 4')
        self.setCheckable(True)
        self.setChecked(False)
        self.setFixedSize(130, 70)
class CSFMonitoringClose(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setFixedSize(160, 25)
        self.setText('닫기')

    def mousePressEvent(self, e: QMouseEvent) -> None:
        self.inmem.widget_ids['CSFMonitoringWindow'].close()
        return super().mousePressEvent(e)