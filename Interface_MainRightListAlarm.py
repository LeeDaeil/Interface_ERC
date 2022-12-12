from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Interface_ABCWidget import *
from Interface_QSS import qss, rgb_to_qCOLOR, DarkGray

class ListAlarmWindow(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setGeometry(1107, 230, 880, 1200)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 상단바 제거
        self.setAttribute(Qt.WA_TranslucentBackground)  # widget 투명화
        self.setStyleSheet(qss) # qss load
        self.m_flag = False
        
        vl = QVBoxLayout(self)
        vl.setSpacing(0)
        vl.setContentsMargins(0, 0, 0, 0)
        self.title_label = ListAlarmTitle_BG(self)
        vl.addWidget(self.title_label)
        vl.addWidget(ListAlarmWidget_BG(self))
        
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

class ListAlarmTitle_BG(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setFixedHeight(25 + 10) # Title size + margin * 2
        layout = QHBoxLayout(self)
        layout.addWidget(ListAlarmTitle(self))
        layout.setContentsMargins(5, 5, 5, 5)
        layout.addStretch(1)
class ListAlarmTitle(ABCLabel):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setText('List Alarm')
        self.setFixedSize(240, 25)
class ListAlarmWidget_BG(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        vl = QVBoxLayout(self)
        vl.setContentsMargins(10, 10, 10, 10)
        vl.addWidget(ListAlarmWidget(self))
        hl = QHBoxLayout()
        hl.addWidget(ListAlarmOperatorSorting(self, 'RO'))
        hl.addWidget(ListAlarmOperatorSorting(self, 'TO'))
        hl.addWidget(ListAlarmOperatorSorting(self, 'EO'))
        hl.addStretch(1)
        hl.addWidget(ListAlarmClose(self))
        vl.addLayout(hl)
class ListAlarmWidget(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setFixedSize(835 + 10 + 15, 1081) # InsideTable(835) Margin(10) Scroll(15)
        ListAlarmTable_w = ListAlarmTable(self)
        
        hl1 = QHBoxLayout(self) # 테이블과 스크롤
        hl1.setContentsMargins(0 ,0, 0, 0)
        hl2 = QHBoxLayout() # 테이블 헤더
        hl2.setContentsMargins(0, 0, 0, 0)
        hl2.setSpacing(0)
        vl1 = QVBoxLayout() # 테이블과 테이블 헤더
        vl1.setContentsMargins(0, 0, 0, 0)
        vl1.setSpacing(0)
        #
        hl1.addLayout(vl1)
        hl1.addStretch(1)
        hl1.addWidget(ListAlarmTable_w.verticalScrollBar())
        #
        hl2.addWidget(ListAlarmHeaderLabel(self, Qt.AlignmentFlag.AlignVCenter|Qt.AlignmentFlag.AlignLeft, ' Description', 442, 'L'))
        hl2.addWidget(ListAlarmHeaderLabel(self, Qt.AlignmentFlag.AlignVCenter|Qt.AlignmentFlag.AlignLeft, ' Value', 99))
        hl2.addWidget(ListAlarmHeaderLabel(self, Qt.AlignmentFlag.AlignVCenter|Qt.AlignmentFlag.AlignLeft, ' Setpoint', 120))
        hl2.addWidget(ListAlarmHeaderLabel(self, Qt.AlignmentFlag.AlignVCenter|Qt.AlignmentFlag.AlignLeft, ' Unit', 89))
        hl2.addWidget(ListAlarmHeaderLabel(self, Qt.AlignmentFlag.AlignVCenter|Qt.AlignmentFlag.AlignLeft, ' Time', 85, 'R'))
        #
        vl1.addLayout(hl2)
        vl1.addWidget(ListAlarmTable_w)
class ListAlarmHeaderLabel(ABCLabel):
    def __init__(self, parent, alignment, in_text, width, pos='In', widget_name=''):
        super().__init__(parent, widget_name)
        self.setAlignment(alignment)
        self.setText(in_text)
        self.setFixedSize(width, 35)
        self.setProperty('Pos', pos)
class ListAlarmTable(ABCTableWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        # self.setRowCount(100)
        self.setFixedWidth(835)
        self.setShowGrid(True)  # Grid 지우기
        self.verticalHeader().setVisible(False)  # Row 넘버 숨기기
        self.horizontalHeader().setVisible(False)  # Table Header 숨기기
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # Scroll Bar 설정
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # Scroll Bar 설정
        self.verticalScrollBar().setFixedWidth(15)

    def paintEvent(self, event):
        painter = QPainter(self.viewport())
        painter.setPen(QPen(rgb_to_qCOLOR(DarkGray), 1))
        painter.drawLine(0, 35 * 5, 835, 35 * 5)
        painter.drawLine(0, 35 * 10, 835, 35 * 10)
        painter.drawLine(0, 35 * 15, 835, 35 * 15)
        painter.end()
        
# class ListAlarmItemLabel(ABCWidget):
#     def __init__(self, parent, widget_name=''):
#         super().__init__(parent, widget_name)
        
class ListAlarmOperatorSorting(ABCPushButton):
    def __init__(self, parent, operator='', widget_name=''):
        super().__init__(parent, widget_name)
        self.setFixedSize(160, 38)
        self.operator = operator
        self.setText(f'{operator} Alarm Sorting')

    def mousePressEvent(self, e: QMouseEvent) -> None:
        print(f'Call Sorting Function -> {self.operator}')
        return super().mousePressEvent(e)   
class ListAlarmClose(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setFixedSize(160, 38)
        self.setText('닫기')

    def mousePressEvent(self, e: QMouseEvent) -> None:
        self.inmem.widget_ids['ListAlarmWindow'].close()
        return super().mousePressEvent(e)