from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Interface_ABCWidget import *
from Interface_MainLeftOperationSelection import *
from Interface_MainLeftPreTrip import *
from Interface_MainLeftSignal import *

class MainLeft(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        vl = QVBoxLayout(self)
        vl.addWidget(MainLeftTop1(self))
        vl.addWidget(MainLeftTop2(self))
        vl.addWidget(MainLeftTop3(self))

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
        self.btngroup.addButton(MainLeftTop2OperationControllerBtnA(self))
        self.btngroup.addButton(MainLeftTop2OperationControllerBtnM(self))
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
        vl.addWidget(MainLeftTop3PreTrip(self))
        vl.addWidget(MainLeftTop3Signal(self))

class MainLeftTop3PreTrip(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setText('Pre-trip')

    def mousePressEvent(self, e: QMouseEvent) -> None:
        w = PretripWindow(self)
        w.show()
        return super().mousePressEvent(e)

class MainLeftTop3Signal(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setText('Signal')
    
    def mousePressEvent(self, e: QMouseEvent) -> None:
        w = SignalWindow(self)
        w.show()
        return super().mousePressEvent(e)