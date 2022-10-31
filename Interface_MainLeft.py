from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Interface_ABCWidget import *
from Interface_MainLeftOperationSelection import *
from Interface_MainLeftPreTrip import *
from Interface_MainLeftSignal import *
from Interface_MainLeftCSFMonitoring import *

class MainLeft(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        vl = QVBoxLayout(self)
        vl.addWidget(MainLeftTop1(self))
        vl.addWidget(MainLeftTop2(self))
        vl.addWidget(MainLeftTop3(self))
        vl.addWidget(MainLeftTop4(self))

# ------------------------------------------------------------------------------------------------
class MainLeftTop1(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        hl = QHBoxLayout(self)
        hl.addWidget(MainLeftTop1ReactorPower(self))
        hl.addWidget(MainLeftTop1Electric(self))

class MainLeftTop1ReactorPower(ABCLabel):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.startTimer(200)
    
    def timerEvent(self, a0: 'QTimerEvent') -> None:
        self.setText(f'Reactor Power\n{self.inmem.ShMem.get_para_val("KBCDO23")}[%]')
        return super().timerEvent(a0)

class MainLeftTop1Electric(ABCLabel):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.startTimer(200)
    
    def timerEvent(self, a0: 'QTimerEvent') -> None:
        self.setText(f'Electric Power\n{self.inmem.ShMem.get_para_val("KBCDO22")}[%]')
        return super().timerEvent(a0)
# ------------------------------------------------------------------------------------------------
class MainLeftTop2(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        vl = QVBoxLayout(self)
        hl1 = QHBoxLayout()
        hl2 = QHBoxLayout()
        vl.addLayout(hl1)
        vl.addLayout(hl2)

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
        self.setFixedWidth(200)
        self.setText('Operation Selection')

class MainLeftTop2OperationSelectionBtn(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.w = OperationSelectionWindow(self)
        self.setText('Refueling')
    
    def mousePressEvent(self, e: QMouseEvent) -> None:
        self.w.show()
        return super().mousePressEvent(e)

class MainLeftTop2OperationController(ABCLabel):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setFixedWidth(200)
        self.setText('Operation Controller')

class MainLeftTop2OperationControllerBtnM(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setText('Manual')
        self.setCheckable(True)
        self.setChecked(True if self.inmem.ShMem.get_para_val('iFixMAMode') == 0 else False)
        self.blink = False
        self.startTimer(600)

    def nextCheckState(self) -> None:
        super().nextCheckState()
        print(f'{type(self).__name__} is changed as {self.isChecked()}')
        self.inmem.ShMem.change_para_val('iFixMAMode', 0)

    def timerEvent(self, e: QTimerEvent) -> None:
        if self.inmem.ShMem.get_para_val('iManBLK') == 0:
            self.setProperty('blinking', False)
        else:
            self.setProperty('blinking', self.blink)
            self.blink = not self.blink
        self.style().polish(self)
        return super().timerEvent(e)

class MainLeftTop2OperationControllerBtnA(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setText('Autonomous')
        self.setCheckable(True)
        self.setChecked(True if self.inmem.ShMem.get_para_val('iFixMAMode') == 1 else False)
        self.blink = False
        self.startTimer(600)

    def nextCheckState(self) -> None:
        super().nextCheckState()
        print(f'{type(self).__name__} is changed as {self.isChecked()}')
        self.inmem.ShMem.change_para_val('iFixMAMode', 1)
    
    def timerEvent(self, e: QTimerEvent) -> None:
        if self.inmem.ShMem.get_para_val('iAutoBLK') == 0:
            self.setProperty('blinking', False)
        else:
            self.setProperty('blinking', self.blink)
            self.blink = not self.blink
        self.style().polish(self)
        return super().timerEvent(e)
# ------------------------------------------------------------------------------------------------
class MainLeftTop3(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        vl = QVBoxLayout(self)
        hl = QHBoxLayout()
        hl.addWidget(MainLeftTop3PreTrip(self))
        hl.addWidget(MainLeftTop3Signal(self))
        vl.addLayout(hl)
        vl.addWidget(MainLeftTop3CSF(self))

class MainLeftTop3PreTrip(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.w = PretripWindow(self)
        self.setText('Pre-trip')
        self.blink = False
        self.startTimer(600)

    def mousePressEvent(self, e: QMouseEvent) -> None:
        self.w.show()
        return super().mousePressEvent(e)

    def timerEvent(self, e: QTimerEvent) -> None:
        if self.inmem.ShMem.get_para_val('iPreTripBLK') == 0:
            self.setProperty('blinking', False)
        else:
            self.setProperty('blinking', self.blink)
            self.blink = not self.blink
        self.style().polish(self)
        return super().timerEvent(e)
    
class MainLeftTop3Signal(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.w = SignalWindow(self)
        self.setText('Signal')
        self.blink = False
        self.startTimer(600)
    
    def mousePressEvent(self, e: QMouseEvent) -> None:
        self.w.show()
        return super().mousePressEvent(e)

    def timerEvent(self, e: QTimerEvent) -> None:
        if self.inmem.ShMem.get_para_val('iSignalBLK') == 0:
            self.setProperty('blinking', False)
        else:
            self.setProperty('blinking', self.blink)
            self.blink = not self.blink
        self.style().polish(self)
        return super().timerEvent(e)

class MainLeftTop3CSF(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.w = CSFMonitoringWindow(self)
        self.setText('CSF Monitoring')
        self.blink = False
        self.startTimer(600)
        
    def mousePressEvent(self, e: QMouseEvent) -> None:
        self.w.show()
        return super().mousePressEvent(e)
    
    def timerEvent(self, e: QTimerEvent) -> None:
        if self.inmem.ShMem.get_para_val('iCSFBLK') == 0:
            self.setProperty('blinking', False)
        else:
            self.setProperty('blinking', self.blink)
            self.blink = not self.blink
        self.style().polish(self)
        return super().timerEvent(e)
# ------------------------------------------------------------------------------------------------
class MainLeftTop4(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        
        vl = QVBoxLayout(self)
        vl.setContentsMargins(0, 0, 0, 10)
        gl1 = QGridLayout()
        gl2 = QGridLayout()
        vl.addLayout(gl1)
        vl.addLayout(gl2)
                
        for glayer, type_ in zip([gl1, gl2], ['nonem', 'em']):
            alarm_list = self.inmem.ShMem.get_alarm_para(type_)
            alarm_count = len(alarm_list)
            max_alarms_in_row = 5
            
            for i in range(0, (alarm_count//max_alarms_in_row) * max_alarms_in_row):
                col = i%max_alarms_in_row
                row = i//max_alarms_in_row
                if i < alarm_count:
                    glayer.addWidget(MainLeftTop4Alarm(self, alarm_id=alarm_list[i]), row, col)      
                else:
                    glayer.addWidget(MainLeftTop4Alarm(self, alarm_id='iEmptyAlem'), row, col) # empty alarm
class MainLeftTop4Alarm(ABCPushButton):
    def __init__(self, parent, widget_name='', alarm_id=''):
        super().__init__(parent, widget_name)
        self.setText(self.inmem.ShMem.get_alarm_des(alarm_id))
        self.alarm_id = alarm_id
        self.blink = False
        self.startTimer(600)
    
    def timerEvent(self, e: QTimerEvent) -> None:
        if self.inmem.ShMem.get_para_val(self.alarm_id) == 0:
            self.setProperty('blinking', False)
        else:
            self.setProperty('blinking', self.blink)
            self.blink = not self.blink
        self.style().polish(self)
        return super().timerEvent(e)