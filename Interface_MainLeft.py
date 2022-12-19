from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Interface_ABCWidget import *
from Interface_MainLeftOperationSelection import *
from Interface_MainLeftPreTrip import *
from Interface_MainLeftSignal import *
from Interface_MainLeftCSFMonitoring import *
from Interface_MainLeftDiagnosis import *
from Interface_QSS import rgb_to_qCOLOR, DarkRed

#
Total_W = 580 #642
Selection_W = 280
SelectionMA = (Total_W - Selection_W - 10 * 4)/2
class MainLeft(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setFixedWidth(Total_W)
        self.setAttribute(Qt.WA_TranslucentBackground)
        vl = QVBoxLayout(self)
        vl.setContentsMargins(0, 0, 0, 0)
        vl.addWidget(MainLeftTop1(self))
        vl.addWidget(MainLeftTop2(self))
        vl.addWidget(MainLeftTop3(self))
        vl.addWidget(MainLeftTop4_1(self))
        vl.addWidget(MainLeftTop4_2(self))
        vl.setSpacing(10)
        vl.addStretch(1)
# ------------------------------------------------------------------------------------------------
class MainLeftTop1(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setFixedHeight(74)
        hl = QHBoxLayout(self)
        hl.setContentsMargins(0, 0, 0, 0)
        hl.addWidget(MainLeftTop1ReactorPower(self))
        hl.addWidget(MainLeftTop1Electric(self))
class MainLeftTop1ReactorPower(ABCLabel):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
    
    def call_update(self):
        self.setText(f'Reactor Power\n{self.inmem.ShMem.get_para_val("QPROREL")*100:.1f} [%]')
class MainLeftTop1Electric(ABCLabel):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
    
    def call_update(self):
        self.setText(f'Electric Power\n{int(self.inmem.ShMem.get_para_val("KBCDO22"))} [MWe]')
# ------------------------------------------------------------------------------------------------
class MainLeftTop2(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setFixedHeight(110)
        vl = QVBoxLayout(self)
        vl.setContentsMargins(10, 10, 10, 10)
        hl1 = QHBoxLayout()
        hl2 = QHBoxLayout()
        vl.addLayout(hl1)
        vl.addLayout(hl2)
        vl.setSpacing(10)
        hl1.addWidget(MainLeftTop2OperationSelection(self))
        hl1.addWidget(MainLeftTop2OperationSelectionBtn(self))
        hl2.addWidget(MainLeftTop2OperationController(self))
        self.btngroup = QButtonGroup()
        self.btngroup.addButton(MainLeftTop2OperationControllerBtnM(self))
        self.btngroup.addButton(MainLeftTop2OperationControllerBtnA(self))
        [hl2.addWidget(w_btn) for w_btn in self.btngroup.buttons()]
class MainLeftTop2OperationSelection(ABCLabel):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setFixedSize(Selection_W, 40)
        self.setText('Operation Selection')
class MainLeftTop2OperationSelectionBtn(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setFixedHeight(40)
        self.w = OperationSelectionWindow(self)
        self.update_text()
    
    def update_text(self):
        OpMode = self.inmem.ShMem.get_para_val('iFixOpMode')
        self.setText(self.inmem.widget_ids['OperationSelectionTree'].transform_nub_to_procedure_name(OpMode))

    def mousePressEvent(self, e: QMouseEvent) -> None:
        self.w.show()
        self.w.initiation()
        return super().mousePressEvent(e)
class MainLeftTop2OperationController(ABCLabel):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setFixedSize(Selection_W, 40)
        self.setText('Operation Controller')
class MainLeftTop2OperationControllerBtnM(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setFixedSize(SelectionMA, 40)
        self.setText('Manual')
        self.setCheckable(True)
        self.setChecked(True if self.inmem.ShMem.get_para_val('iFixMAMode') == 0 else False)
        self.blink = False

    def nextCheckState(self) -> None:
        super().nextCheckState()
        print(f'{type(self).__name__} is changed as {self.isChecked()}')
        self.inmem.ShMem.change_para_val('iFixMAMode', 0)

    def call_update(self):
        if self.inmem.ShMem.get_para_val('iManBLK') == 0:
            self.setProperty('blinking', False)
        else:
            self.setProperty('blinking', self.blink)
            self.blink = not self.blink
        self.style().polish(self)
class MainLeftTop2OperationControllerBtnA(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setFixedSize(SelectionMA, 40)
        self.setText('Autonomous')
        self.setCheckable(True)
        self.setChecked(True if self.inmem.ShMem.get_para_val('iFixMAMode') == 1 else False)
        self.blink = False

    def nextCheckState(self) -> None:
        super().nextCheckState()
        print(f'{type(self).__name__} is changed as {self.isChecked()}')
        self.inmem.ShMem.change_para_val('iFixMAMode', 1)
    
    def call_update(self):
        if self.inmem.ShMem.get_para_val('iAutoBLK') == 0:
            self.setProperty('blinking', False)
        else:
            self.setProperty('blinking', self.blink)
            self.blink = not self.blink
        self.style().polish(self)
# ------------------------------------------------------------------------------------------------
class MainLeftTop3(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        vl = QVBoxLayout(self)
        hl1 = QHBoxLayout()
        vl.setContentsMargins(0, 0, 0, 0)
        hl1.setContentsMargins(0, 0, 0, 0)
        hl1.addWidget(MainLeftTop3PreTrip(self))
        hl1.addWidget(MainLeftTop3Signal(self))
        hl1.setSpacing(10)
        hl1.addStretch(1)
        vl.addLayout(hl1)
        #
        hl2 = QHBoxLayout()
        hl2.setContentsMargins(0, 0, 0, 0)
        hl2.addWidget(MainLeftTop3CSF(self))
        hl2.addWidget(MainLeftTop3Diagnosis(self))
        hl2.setSpacing(10)
        hl2.addStretch(1)
        vl.addLayout(hl2)
        #
        vl.setSpacing(10)
class MainLeftTop3PreTrip(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setFixedSize((Total_W-10)/2, 50)
        # self.w = PretripWindow(self)
        self.setText('Pre-trip')
        self.blink = False

    def mousePressEvent(self, e: QMouseEvent) -> None:
        # self.w.show()
        return super().mousePressEvent(e)

    def call_update(self):
        if self.inmem.ShMem.get_para_val('iPreTripBLK') == 0:
            self.setProperty('blinking', False)
        else:
            self.setProperty('blinking', self.blink)
            self.blink = not self.blink
        self.style().polish(self)
class MainLeftTop3Signal(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setFixedSize((Total_W-10)/2, 50)
        self.w = SignalWindow(self)
        self.setText('Signal')
        self.blink = False
    
    def mousePressEvent(self, e: QMouseEvent) -> None:
        # L
        self.inmem.widget_ids['SignalWindow'].close()
        self.inmem.widget_ids['CSFMonitoringWindow'].close()
        self.inmem.widget_ids['DiagnosisWindow'].close()
        # R
        self.inmem.widget_ids['LCOWindow'].close()
        self.inmem.widget_ids['OperationStrategyWindow'].close()
        self.inmem.widget_ids['ControlWindow'].close()
        self.inmem.widget_ids['ListAlarmWindow'].close()
        self.w.show()
        return super().mousePressEvent(e)

    def call_update(self):
        if self.inmem.ShMem.get_para_val('iSignalBLK') == 0:
            self.setProperty('blinking', False)
        else:
            self.setProperty('blinking', self.blink)
            self.blink = not self.blink
        self.style().polish(self)
class MainLeftTop3CSF(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setFixedSize((Total_W-10)/2, 50)
        self.w = CSFMonitoringWindow(self)
        self.setText('CSF Monitoring')
        self.blink = False
        
    def mousePressEvent(self, e: QMouseEvent) -> None:
        # L
        self.inmem.widget_ids['SignalWindow'].close()
        self.inmem.widget_ids['CSFMonitoringWindow'].close()
        self.inmem.widget_ids['DiagnosisWindow'].close()
        # R
        self.inmem.widget_ids['LCOWindow'].close()
        self.inmem.widget_ids['OperationStrategyWindow'].close()
        self.inmem.widget_ids['ControlWindow'].close()
        self.inmem.widget_ids['ListAlarmWindow'].close()
        self.w.show()
        return super().mousePressEvent(e)
    
    def call_update(self):
        if self.inmem.ShMem.get_para_val('iCSFBLK') == 0:
            self.setProperty('blinking', False)
        else:
            self.setProperty('blinking', self.blink)
            self.blink = not self.blink
        self.style().polish(self)
class MainLeftTop3Diagnosis(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setFixedSize((Total_W-10)/2, 50)
        self.w = DiagnosisWindow(self)
        self.setText('Diagnosis')
        self.blink = False
        
    def mousePressEvent(self, e: QMouseEvent) -> None:
        # L
        self.inmem.widget_ids['SignalWindow'].close()
        self.inmem.widget_ids['CSFMonitoringWindow'].close()
        self.inmem.widget_ids['DiagnosisWindow'].close()
        # R
        self.inmem.widget_ids['LCOWindow'].close()
        self.inmem.widget_ids['OperationStrategyWindow'].close()
        self.inmem.widget_ids['ControlWindow'].close()
        self.inmem.widget_ids['ListAlarmWindow'].close()
        self.w.show()
        return super().mousePressEvent(e)
    
    def call_update(self):
        if self.inmem.ShMem.get_para_val('iDigBLK') == 0:
            self.setProperty('blinking', False)
        else:
            self.setProperty('blinking', self.blink)
            self.blink = not self.blink
        self.style().polish(self)
# ------------------------------------------------------------------------------------------------
class MainLeftTop4_1(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        gl = QGridLayout(self)
        gl.setContentsMargins(0, 0, 0, 0)
        alarm_list = self.inmem.ShMem.get_alarm_para('nonem')
        alarm_count = len(alarm_list)
        max_alarms_in_row = 5

        for i in range(0, ((alarm_count//max_alarms_in_row) + 1) * max_alarms_in_row):
            col = i%max_alarms_in_row
            row = i//max_alarms_in_row
            if i < alarm_count:
                gl.addWidget(MainLeftTop4Alarm(self, alarm_id=alarm_list[i]), row, col)
            else:
                gl.addWidget(MainLeftTop4Alarm(self, alarm_id='iEmptyAlnon'), row, col) # empty alarm
class MainLeftTop4_2(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setAttribute(Qt.WA_TranslucentBackground)  # Border 투명화
        gl = QGridLayout(self)
        gl.setContentsMargins(0, 0, 0, 0)
        alarm_list = self.inmem.ShMem.get_alarm_para('em')
        alarm_count = len(alarm_list)
        max_alarms_in_row = 5
        
        for i in range(0, ((alarm_count//max_alarms_in_row) + 1) * max_alarms_in_row):
            col = i%max_alarms_in_row
            row = i//max_alarms_in_row
            if i < alarm_count:
                gl.addWidget(MainLeftTop4Alarm(self, alarm_id=alarm_list[i]), row, col)
            else:
                gl.addWidget(MainLeftTop4Alarm(self, alarm_id='iEmptyAlem'), row, col) # empty alarm
class MainLeftTop4Alarm(ABCLabel):
    def __init__(self, parent, widget_name='', alarm_id=''):
        super().__init__(parent, widget_name)
        self.setFixedSize((Total_W-5*4)/5, 52)
        self.setContentsMargins(0, 0, 0, 0)
        self.alarm_id = alarm_id
        self.blink = False
        self.setText(self.inmem.ShMem.get_alarm_des(alarm_id))
        self.setAlignment(Qt.AlignCenter)
        self.setWordWrap(True)
        self.startTimer(300)

    def timerEvent(self, e: QTimerEvent) -> None:
        if self.inmem.ShMem.get_para_val(self.alarm_id) == 0:
            self.setProperty('blinking', False)
        else:
            self.setProperty('blinking', self.blink)
            self.blink = not self.blink
        self.style().polish(self)
        return super().timerEvent(e)