from abc import ABC
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Interface_ABCWidget import *
from Interface_MainRightUnknownEvent import *
from Interface_MainRightOperationStrategy import *
from Interface_MainRightListAlarm import *
from Interface_MainRightListControl import *
from Interface_MainLeftDiagnosis import *
from Interface_MainRightListLCO import *

Total_W = 554
class MainRight(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setContentsMargins(0, 0, 0, 0)
        self.setFixedWidth(Total_W)
        vl = QVBoxLayout(self)
        vl.setContentsMargins(0, 0, 0, 0)
        vl.addWidget(MainRightTop1(self))
        vl.addWidget(MainRightTop2(self))
        vl.addWidget(MainRightTop3(self))
        vl.setSpacing(10)
        
class MainRightTop1(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        vl = QVBoxLayout(self)
        vl.setContentsMargins(0, 0, 0, 0)
        vl.addWidget(MainRightTop1Title(self))
        
        hl = QHBoxLayout()
        hl.setContentsMargins(0, 0, 0, 0)
        self.btn_group = QButtonGroup()
        self.btn_list = [MainRightTop1Normal(self), MainRightTop1Abnormal(self), MainRightTop1Emergency(self)]        
        [self.btn_group.addButton(w) for w in self.btn_list]
        [hl.addWidget(w) for w in self.btn_list]
        hl.setSpacing(10)
        vl.addLayout(hl)
        vl.setSpacing(10)

        self.startTimer(200)
    
    def timerEvent(self, a0: 'QTimerEvent') -> None:
        for i, btn in enumerate(self.btn_group.buttons()):
            if self.inmem.ShMem.get_para_val('iOpHistory') == i:
                btn.setChecked(True)
        return super().timerEvent(a0)

class MainRightTop1Title(ABCLabel):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setFixedSize(Total_W, 40)
        self.setText('Operation History')

class MainRightTop1Normal(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setText('Normal')
        self.setFixedSize((Total_W-10*2)/3, 40)
        self.setCheckable(True)
        self.setChecked(False)

class MainRightTop1Abnormal(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setText('Abnormal')
        self.setFixedSize((Total_W-10*2)/3, 40)
        self.setCheckable(True)
        self.setChecked(False)

class MainRightTop1Emergency(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setText('Emergency')
        self.setFixedSize((Total_W-10*2)/3, 40)
        self.setCheckable(True)
        self.setChecked(False)

class MainRightTop2(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)

        hl = QHBoxLayout(self)
        hl.setContentsMargins(0, 0, 0, 0)
        scroll_ = MainRightTop2Scroller(self)

        hl.addWidget(MainRightTop2TimeTable(self, ScrollBarW=scroll_))
        hl.addWidget(scroll_)

class MainRightTop2TimeTable(ABCTableWidget):
    def __init__(self, parent, widget_name='', ScrollBarW=''):
        super().__init__(parent, widget_name)
        self.setFixedHeight(1085)
        self.setColumnCount(3)
        self.setColumnWidth(0, 20)
        self.setColumnWidth(1, 80)
        self.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.horizontalHeader().setDefaultAlignment(Qt.AlignmentFlag.AlignLeft and Qt.AlignmentFlag.AlignVCenter)
        self.horizontalHeader().setFixedHeight(35)
        self.setHorizontalHeaderLabels([' T', 'Time', 'Description'])
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
        gl.setContentsMargins(0, 0, 0, 0)
        gl.addWidget(MainRightTop3LCO(self), 0, 0)
        gl.addWidget(MainRightTop3OperationStrategy(self), 0, 1)
        gl.addWidget(MainRightTop3ListAlarm(self), 1, 0)
        gl.addWidget(MainRightTop3Control(self), 1, 1)
        gl.setSpacing(10)
class MainRightTop3LCO(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.w = LCOWindow(self)
        self.setText('LCO')
        self.setFixedHeight(50)

    def mousePressEvent(self, e: QMouseEvent) -> None:
        self.w.show()
        return super().mousePressEvent(e)
class MainRightTop3OperationStrategy(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.w = OperationStrategyWindow(self)
        self.setText('Operation Strategy')
        self.setFixedHeight(50)

    def mousePressEvent(self, e: QMouseEvent) -> None:
        self.w.show()
        return super().mousePressEvent(e)

class MainRightTop3ListAlarm(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.w = ListAlarmWindow(self)
        self.setText('List Alarm')
        self.setFixedHeight(50)

    def mousePressEvent(self, e: QMouseEvent) -> None:
        self.w.show()
        return super().mousePressEvent(e)

class MainRightTop3Control(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.w = ControlWindow(self)
        self.setText('Control')
        self.setFixedHeight(50)

    def mousePressEvent(self, e: QMouseEvent) -> None:
        self.w.show()
        return super().mousePressEvent(e)

class MainRightTop3Diagnosis(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.w = DiagnosisWindow(self)
        self.setText('Diagnosis')
        self.setFixedHeight(50)

    def mousePressEvent(self, e: QMouseEvent) -> None:
        self.w.show()
        return super().mousePressEvent(e)

