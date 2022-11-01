from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Interface_ABCWidget import *
from Interface_ABCWidget import *
from Interface_QSS import qss

class CSFMonitoringWindow(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setGeometry(0, 0, 500, 400)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 상단바 제거
        self.setStyleSheet(qss) # qss load
        self.m_flag = False

        vl = QVBoxLayout(self)
        self.title_label = CSFMonitoringTitle(self)
        vl.addWidget(self.title_label)
        vl.addWidget(CSFMonitoringAlarmWidget(self))

        hl = QHBoxLayout()
        hl.addStretch(1)
        hl.addWidget(CSFMonitoringClose(self))
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
class CSFMonitoringTitle(ABCLabel):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setText('CSF Monitoring')
        self.setFixedHeight(30)
class CSFMonitoringAlarmWidget(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.startTimer(600)
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        vl = QVBoxLayout(self)
        
        self.csf_info = {
            'Reactivity Control': [QButtonGroup(), 'iCSFReactivity'],
            'Core Heat Removal': [QButtonGroup(), 'iCSFCoreHeat'],
            'RCS Heat Removal': [QButtonGroup(), 'iCSFRCSHeat'],
            'RCS Pressure Control': [QButtonGroup(), 'iCSFRCSPres'],
            'Containment Pressure and\nTemperature Control': [QButtonGroup(), 'iCSFCTMT'],
            'RCS Inventory Control': [QButtonGroup(), 'iCSFRCSInvt'],
        }

        for key, val in self.csf_info.items():
            h = QHBoxLayout()
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
            val[0].buttons()[state].setChecked(True)
        return super().timerEvent(a0)
class CSFMonitoringAlarmLabel(ABCLabel):
    def __init__(self, parent, widget_name='', in_text=''):
        super().__init__(parent, widget_name)
        self.setText(in_text)
class CSFMonitoringAlarmLevel1Item(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setText(f'Level 1')
        self.setCheckable(True)
        self.setChecked(True)
        self.setFixedWidth(80)

    def mousePressEvent(self, e: QMouseEvent) -> None:
        pass
class CSFMonitoringAlarmLevel2Item(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setText(f'Level 2')
        self.setCheckable(True)
        self.setChecked(False)
        self.setFixedWidth(80)

    def mousePressEvent(self, e: QMouseEvent) -> None:
        pass
class CSFMonitoringAlarmLevel3Item(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setText(f'Level 3')
        self.setCheckable(True)
        self.setChecked(False)
        self.setFixedWidth(80)

    def mousePressEvent(self, e: QMouseEvent) -> None:
        pass
class CSFMonitoringAlarmLevel4Item(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setText(f'Level 4')
        self.setCheckable(True)
        self.setChecked(False)
        self.setFixedWidth(80)

    def mousePressEvent(self, e: QMouseEvent) -> None:
        pass

class CSFMonitoringClose(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setText('닫기')

    def mousePressEvent(self, e: QMouseEvent) -> None:
        self.inmem.widget_ids['CSFMonitoringWindow'].close()
        return super().mousePressEvent(e)