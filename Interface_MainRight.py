from abc import ABC
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Interface_ABCWidget import *
from Interface_MainRightUnknownEvent import *
from Interface_MainRightOperationStrategy import *
from Interface_MainRightListAlarm import *
from Interface_MainRightListControl import *
from Interface_MainRightListDiagnosis import *
from Interface_MainRightListLCO import *

class MainRight(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setFixedWidth(450)
        
        vl = QVBoxLayout(self)
        vl.addWidget(MainRightTop1(self))
        vl.addWidget(MainRightTop2(self))
        vl.addWidget(MainRightTop3(self))
        
class MainRightTop1(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        vl = QVBoxLayout(self)
        vl.addWidget(MainRightTop1Title(self))
        
        hl = QHBoxLayout()
        self.btn_group = QButtonGroup()
        self.btn_list = [MainRightTop1Normal(self), MainRightTop1Abnormal(self), MainRightTop1Emergency(self)]        
        [self.btn_group.addButton(w) for w in self.btn_list]
        [hl.addWidget(w) for w in self.btn_list]
        vl.addLayout(hl)

        self.startTimer(200)
    
    def timerEvent(self, a0: 'QTimerEvent') -> None:
        history_val = self.inmem.ShMem.get_para_val('iOpHistory')
        for i, btn in enumerate(self.btn_group.buttons()):
            if self.inmem.ShMem.get_para_val('iOpHistory') == i:
                btn.setChecked(True)
        return super().timerEvent(a0)

class MainRightTop1Title(ABCLabel):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setText('Operation History')

class MainRightTop1Normal(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setText('Normal')
        self.setCheckable(True)
        self.setChecked(False)

class MainRightTop1Abnormal(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setText('Abnormal')
        self.setCheckable(True)
        self.setChecked(False)

class MainRightTop1Emergency(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setText('Emergency')
        self.setCheckable(True)
        self.setChecked(False)

class MainRightTop2(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        
        hl = QHBoxLayout(self)
        scroll_ = MainRightTop2Scroller(self)

        hl.addWidget(MainRightTop2TimeTable(self, ScrollBarW=scroll_))
        hl.addWidget(scroll_)

class MainRightTop2TimeTable(ABCTableWidget):
    def __init__(self, parent, widget_name='', ScrollBarW=''):
        super().__init__(parent, widget_name)
        self.setColumnCount(3)
        self.setColumnWidth(0, 20)
        self.setColumnWidth(1, 80)
        self.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.horizontalHeader().setDefaultAlignment(Qt.AlignmentFlag.AlignLeft)
        self.setHorizontalHeaderLabels(['T', 'Time', 'Description'])
        self.verticalHeader().setVisible(False)
        self.setShowGrid(False)
        # Scroll
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBar(ScrollBarW)

    def resizeEvent(self, e: QResizeEvent) -> None:
        radius = 10.0
        path = QPainterPath()
        path.moveTo(self.rect().width() - radius, 0)
        path.arcTo(QRectF(0, 0, radius*2, radius*2), 90, 90)
        path.lineTo(0, self.rect().height())
        path.lineTo(self.rect().width(), self.rect().height())
        path.lineTo(self.rect().width(), radius)
        path.arcTo(QRectF(self.rect().width() - radius*2, 0, radius*2, radius*2), 0, 90)
        self.setMask(QRegion(path.toFillPolygon().toPolygon()))
        return super().resizeEvent(e)

    def add_new_item(self, t_, des_):
        row_index = self.rowCount()
        self.insertRow(row_index)
        self.setItem(row_index, 0, QTableWidgetItem(f'[{t_}]'))
        self.setItem(row_index, 1, QTableWidgetItem(f'[{self.inmem.get_time()}]'))
        self.setItem(row_index, 2, QTableWidgetItem(des_))
        
class MainRightTop2Scroller(ABCScrollBar):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)

class MainRightTop3(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        
        gl = QGridLayout(self)
        gl.addWidget(MainRightTop3UnknownEvent(self), 0, 0)
        gl.addWidget(MainRightTop3OperationStrategy(self), 0, 1)
        gl.addWidget(MainRightTop3ListAlarm(self), 1, 0)
        gl.addWidget(MainRightTop3Control(self), 1, 1)
        gl.addWidget(MainRightTop3Diagnosis(self), 2, 0)
        gl.addWidget(MainRightTop3LCO(self), 2, 1)

class MainRightTop3UnknownEvent(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.w = UnknownEventWindow(self)
        self.setText('Unknown Event')
    
    def mousePressEvent(self, e: QMouseEvent) -> None:
        self.w.show()
        return super().mousePressEvent(e)

class MainRightTop3OperationStrategy(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.w = OperationStrategyWindow(self)
        self.setText('Operation Strategy')

    def mousePressEvent(self, e: QMouseEvent) -> None:
        self.w.show()
        return super().mousePressEvent(e)

class MainRightTop3ListAlarm(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.w = ListAlarmWindow(self)
        self.setText('List Alarm')

    def mousePressEvent(self, e: QMouseEvent) -> None:
        self.w.show()
        return super().mousePressEvent(e)

class MainRightTop3Control(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.w = ControlWindow(self)
        self.setText('Control')

    def mousePressEvent(self, e: QMouseEvent) -> None:
        self.w.show()
        return super().mousePressEvent(e)

class MainRightTop3Diagnosis(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.w = DiagnosisWindow(self)
        self.setText('Diagnosis')

    def mousePressEvent(self, e: QMouseEvent) -> None:
        self.w.show()
        return super().mousePressEvent(e)

class MainRightTop3LCO(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.w = LCOWindow(self)
        self.setText('LCO')
        
    def mousePressEvent(self, e: QMouseEvent) -> None:
        self.w.show()
        return super().mousePressEvent(e)