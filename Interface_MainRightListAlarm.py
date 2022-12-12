from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Interface_ABCWidget import *
from Interface_QSS import qss


class ListAlarmWindow(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setGeometry(1107, 866, 880, 565)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 상단바 제거
        self.setAttribute(Qt.WA_TranslucentBackground)  # widget 투명화
        self.setStyleSheet(qss)  # qss load
        self.m_flag = False

        vl = QVBoxLayout(self)
        vl.setSpacing(0)
        vl.setContentsMargins(0, 0, 0, 0)
        self.title_label = ListAlarmTitle_BG(self)
        vl.addWidget(self.title_label)
        vl.addWidget(ListAlarmBoard_BG(self))

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


class ListAlarmTitle_BG(ABCLabel):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setFixedHeight(25 + 10)  # Title size + margin * 2
        hl = QHBoxLayout(self)
        hl.setContentsMargins(10, 5, 5, 5)
        hl.addWidget(ListAlarmTitle(self))
        hl.addStretch(1)


class ListAlarmTitle(ABCLabel):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setText('List Alarm')
        self.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)
        self.setFixedSize(240, 25)


class ListAlarmBoard_BG(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        vl = QVBoxLayout(self)
        vl.setContentsMargins(10, 10, 10, 10)
        vl.addWidget(ListAlarmBoard(self))
        hl = QHBoxLayout()
        hl.addWidget(ListROAlarmSorting(self))
        hl.addWidget(ListTOAlarmSorting(self))
        hl.addWidget(ListEOAlarmSorting(self))
        hl.addStretch(1)
        hl.addWidget(ListAlarmClose(self))
        hl.setSpacing(18)
        vl.addLayout(hl)


class ListAlarmBoard(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        hl = QHBoxLayout(self)
        hl.setContentsMargins(0, 0, 0, 0)
        scroll_ = ListAlarmScroller(self)
        hl.addWidget(ListAlarmTable(self, ScrollBarW=scroll_))
        hl.addWidget(scroll_)

class ListAlarmTable(ABCTableWidget):
    def __init__(self, parent, widget_name='', ScrollBarW=''):
        super().__init__(parent, widget_name)
        self.setFixedHeight(457)
        self.setContentsMargins(0, 0, 0, 0)
        self.setColumnCount(5)
        self.setColumnWidth(0, 435)
        self.setColumnWidth(1, 100)
        self.setColumnWidth(2, 100)
        self.setColumnWidth(3, 100)
        self.setColumnWidth(4, 100)
        self.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.horizontalHeader().setDefaultAlignment(Qt.AlignmentFlag.AlignLeft and Qt.AlignmentFlag.AlignVCenter)
        self.horizontalHeader().setFixedHeight(35)
        self.setHorizontalHeaderLabels([' Description', ' Value', ' Setpoint', ' Unit', ' Time'])
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
        path.arcTo(QRectF(0, 0, radius * 2, radius * 2), 90, 90)
        path.lineTo(0, self.rect().height())
        path.lineTo(self.rect().width(), self.rect().height())
        path.lineTo(self.rect().width(), radius)
        path.arcTo(QRectF(self.rect().width() - radius * 2, 0, radius * 2, radius * 2), 0, 90)
        self.setMask(QRegion(path.toFillPolygon().toPolygon()))
        return super().resizeEvent(e)

    def add_new_item(self, oper_, des_, val_, setp_, unit_):
        # E.x : self.add_new_item('RO', 'Test', '10', '15', '%')
        row_index = self.rowCount()
        self.insertRow(row_index)
        items = [QTableWidgetItem(des_), QTableWidgetItem(val_), QTableWidgetItem(setp_), QTableWidgetItem(unit_), QTableWidgetItem(f'[{self.inmem.get_time()}]')]
        for i, w in enumerate(items):
            w.operator_type = oper_         # Operator 별 Alarm sorting 용
            self.setItem(row_index, i, w)
            
class ListAlarmScroller(ABCScrollBar):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)

class ListROAlarmSorting(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setFixedSize(178, 38)
        self.setText('RO Alarm Sorting')

class ListTOAlarmSorting(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setFixedSize(178, 38)
        self.setText('TO Alarm Sorting')

class ListEOAlarmSorting(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setFixedSize(178, 38)
        self.setText('EO Alarm Sorting')

class ListAlarmClose(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setFixedSize(178, 38)
        self.setText('닫기')

    def mousePressEvent(self, e: QMouseEvent) -> None:
        self.inmem.widget_ids['ListAlarmWindow'].close()
        return super().mousePressEvent(e)