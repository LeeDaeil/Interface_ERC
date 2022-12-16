from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Interface_ABCWidget import *
from Interface_QSS import *

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.gridspec import GridSpec
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg

class ControlWindow(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setGeometry(438, 232, 1550, 1200)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 상단바 제거
        self.setAttribute(Qt.WA_TranslucentBackground)  # widget 투명화
        self.setStyleSheet(qss)  # qss load
        self.m_flag = False

        vl = QVBoxLayout(self)
        vl.setSpacing(0)
        vl.setContentsMargins(0, 0, 0, 0)
        self.title_label = ControlTitle_BG(self)
        vl.addWidget(self.title_label)
        vl.addWidget(ControlBoard_BG(self))

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
        
    def show(self) -> None:
        opmode = self.inmem.widget_ids['MainLeftTop2OperationSelectionBtn'].text()
        self.inmem.widget_ids['ControlOperationWidgetResult'].setText(opmode)
        if opmode == 'Startup':
            self.inmem.widget_ids['ControlTrendWidget'].setCurrentIndex(1)
            return super().show()
        if opmode == 'LOCA':
            self.inmem.widget_ids['ControlTrendWidget'].setCurrentIndex(2)
            return super().show()
        self.inmem.widget_ids['ControlTrendWidget'].setCurrentIndex(0)
        return super().show()
class ControlTitle_BG(ABCLabel):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setFixedHeight(25 + 10)  # Title size + margin * 2
        hl = QHBoxLayout(self)
        hl.setContentsMargins(10, 5, 5, 5)
        hl.addWidget(ControlTitle(self))
        hl.addStretch(1)
class ControlTitle(ABCLabel):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setText('Autonomous Control Signals')
        self.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)
        self.setFixedSize(320, 25)
class ControlBoard_BG(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        hl = QHBoxLayout(self)
        hl.setContentsMargins(10, 10, 10, 10)
        hl.setSpacing(10)
        vr = QVBoxLayout()
        vr.setContentsMargins(0, 0, 0, 0)
        vr.setSpacing(10)
        vl = QVBoxLayout()
        vl.setContentsMargins(0, 0, 0, 0)
        vl.setSpacing(10)
        
        hl.addLayout(vl)
        hl.addLayout(vr)
        # Left ------------------------------------------
        vl.addWidget(ControlOperationWidget(self))
        vl.addWidget(ControlTrendWidget(self))
        # Right -----------------------------------------
        vr.addWidget(ControlHistory(self))
        hl_in_vr = QHBoxLayout()
        hl_in_vr.addStretch(1)
        hl_in_vr.addWidget(ControlClose(self))
        vr.addLayout(hl_in_vr)
#--------------------------------------------------------------------------------------------------------
class ControlOperationWidget(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setFixedSize(1070, 50)
        hl = QHBoxLayout(self)
        hl.addWidget(ControlOperationWidgetTitle(self))
        hl.addWidget(ControlOperationWidgetResult(self))
        hl.setSpacing(10)
        hl.addStretch(1)
class ControlOperationWidgetTitle(ABCLabel):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setText('Operation Mode :')
class ControlOperationWidgetResult(ABCLabel):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setText('')
#--------------------------------------------------------------------------------------------------------
class ControlTrendWidget(ABCStackWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.addWidget(ControlTrendNoWidget(self))
        self.addWidget(ControlTrendStartUpWidget(self))
        self.addWidget(ControlTrendEmergencyWidget(self))
        self.setContentsMargins(10, 10, 10, 10)
class ControlTrendStartUpWidget(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        vl = QVBoxLayout(self)
        hl = QHBoxLayout()
        hl.addWidget(ControlTrendStartUpRODBOXWidget(self))
        hl.addWidget(ControlTrendStartUpPowerWidget(self))
        vl.addLayout(hl)
        vl.addWidget(ControlTrendStartUpTemperatureWidget(self))
class ControlTrendStartUpPowerWidget(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setFixedHeight(250)
        vl = QVBoxLayout(self)
        #
        self.fig = plt.Figure(tight_layout=True, facecolor=rgb_to_hex(LightGray))
        gs = GridSpec(1, 1, figure=self.fig)
        self.axs = [self.fig.add_subplot(gs[:, :])]
        self.fig.canvas.draw()
        self.canvas = FigureCanvasQTAgg(self.fig)
        vl.addWidget(self.canvas)
        #
        self.set_yaxis()
        paras = ['KCNTOMS', 'QPROREL']
        self.gp_db = {para: [self.inmem.ShMem.get_para_val(para)] for para in paras}
        #        
        self.startTimer(300)
        
    @ticker.FuncFormatter
    def major_formatter_time(time, pos):
        time = int(time/300)
        return f"{time}[Min]"

    @ticker.FuncFormatter
    def major_formatter_reactor_power(power, pos):
        return f"{power*100:.1f}[%]"
        
    def set_yaxis(self):
        self.axs[0].xaxis.set_major_formatter(self.major_formatter_time)
        self.axs[0].yaxis.set_major_formatter(self.major_formatter_reactor_power)
    
    def timerEvent(self, a0: 'QTimerEvent') -> None:
        if self.gp_db['KCNTOMS'][-1] != self.inmem.ShMem.get_para_val('KCNTOMS'):
            # 1. DB add
            [self.gp_db[para].append(self.inmem.ShMem.get_para_val(para)) for para in self.gp_db.keys()]
            # 2. Clear
            [ax.clear() for ax in self.axs]
            # 3. Draw
            self.axs[0].plot(self.gp_db['KCNTOMS'], self.gp_db['QPROREL'], label='Reactor power')
            # 4. Refresh
            self.set_yaxis()
            self.canvas.draw()
        return super().timerEvent(a0)
class ControlTrendStartUpTemperatureWidget(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        vl = QVBoxLayout(self)
        #
        self.fig = plt.Figure(tight_layout=True)
        gs = GridSpec(3, 2, figure=self.fig)
        self.axs = [
            self.fig.add_subplot(gs[0:2, 0]),
            self.fig.add_subplot(gs[0:2, 1]),
            self.fig.add_subplot(gs[2, 0]),
            self.fig.add_subplot(gs[2, 1]),
        ]
        self.fig.canvas.draw()
        self.canvas = FigureCanvasQTAgg(self.fig)
        vl.addWidget(self.canvas)
        #
        self.set_yaxis()
        paras = ['KCNTOMS', 'UAVLEGS', 'KBCDO20', 'KBCDO21', 'KBCDO22', 'KBCDO16', 'CXEMPCM']
        self.gp_db = {para: [self.inmem.ShMem.get_para_val(para)] for para in paras}
        #        
        self.startTimer(300)
        
    @ticker.FuncFormatter
    def major_formatter_time(time, pos):
        time = int(time/300)
        return f"{time}[Min]"

    @ticker.FuncFormatter
    def major_formatter_temp(temp, pos):
        return f"{int(temp)}[℃]"

    @ticker.FuncFormatter
    def major_formatter_mwe(Mwe, pos):
        return f"{int(Mwe)}[MWe]"

    @ticker.FuncFormatter
    def major_formatter_ppm(ppm, pos):
        return f"{int(ppm)}[PPM]"

    @ticker.FuncFormatter
    def major_formatter_liter(l, pos):
        return f"{int(l)}[L]"
        
    def set_yaxis(self):
        self.axs[0].xaxis.set_major_formatter(self.major_formatter_time)
        self.axs[1].xaxis.set_major_formatter(self.major_formatter_time)
        self.axs[2].xaxis.set_major_formatter(self.major_formatter_time)
        self.axs[3].xaxis.set_major_formatter(self.major_formatter_time)

        self.axs[0].yaxis.set_major_formatter(self.major_formatter_temp)
        self.axs[1].yaxis.set_major_formatter(self.major_formatter_mwe)
        self.axs[2].yaxis.set_major_formatter(self.major_formatter_ppm)
        self.axs[3].yaxis.set_major_formatter(self.major_formatter_liter)
    
    def timerEvent(self, a0: 'QTimerEvent') -> None:
        if self.gp_db['KCNTOMS'][-1] != self.inmem.ShMem.get_para_val('KCNTOMS'):
            # 1. DB add
            [self.gp_db[para].append(self.inmem.ShMem.get_para_val(para)) for para in self.gp_db.keys()]
            # 2. Clear
            [ax.clear() for ax in self.axs]
            # 3. Draw
            self.axs[0].plot(self.gp_db['KCNTOMS'], self.gp_db['UAVLEGS'], label='Reactor power')
            # 4. Refresh
            self.set_yaxis()
            self.canvas.draw()
        return super().timerEvent(a0)
class ControlTrendStartUpRODBOXWidget(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        hl = QHBoxLayout(self)
        hl.addWidget(ControlTrendStartUpRODWidget(self, bank='A'))
        hl.addWidget(ControlTrendStartUpRODWidget(self, bank='B'))
        hl.addWidget(ControlTrendStartUpRODWidget(self, bank='C'))
        hl.addWidget(ControlTrendStartUpRODWidget(self, bank='D'))
        hl.setSpacing(10)
        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
class ControlTrendStartUpRODWidget(ABCWidget):
    def __init__(self, parent, bank, widget_name=''):
        super().__init__(parent, widget_name)
        self.setFixedSize(54, 120 + 40)
        self.bank = bank
        self.bank_para = {'A':'KBCDO10', 'B':'KBCDO9', 'C':'KBCDO8', 'D':'KBCDO7'}[bank]
        self.startTimer(300)
        
    def paintEvent(self, a0: QPaintEvent) -> None:
        qp = QPainter()
        qp.begin(self)
        # Boundary
        qp.setPen(QPen(rgb_to_qCOLOR(DarkGray), 1.5))
        qp.drawRect(12, 5, 30, 119)
        # Rod
        qp.setPen(Qt.PenStyle.NoPen)
        qp.setBrush(QBrush(rgb_to_qCOLOR(DarkGray), Qt.BrushStyle.SolidPattern))
        qp.drawRect(12, 5, 30, int((228 - self.inmem.ShMem.get_para_val(self.bank_para))*0.5) + 5)
        # Label
        qp.setFont(QFont(Global_font, 12))
        qp.setPen(QPen(rgb_to_qCOLOR(Black), 1))
        qp.drawText(QRectF(0.0, 125, 54.0, 20), Qt.AlignCenter, f'Bank {self.bank}')
        qp.drawText(QRectF(0.0, 125 + 15, 54.0, 20), Qt.AlignCenter, f'[{self.inmem.ShMem.get_para_val(self.bank_para):03}]')
        qp.end()
    
    def timerEvent(self, a0: 'QTimerEvent') -> None:
        self.update()
        return super().timerEvent(a0)
class ControlTrendEmergencyWidget(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
class ControlTrendNoWidget(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        vl = QVBoxLayout(self)
        vl.addWidget(QLabel('No'))
#--------------------------------------------------------------------------------------------------------
class ControlHistory(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        hl = QHBoxLayout(self)
        hl.setContentsMargins(0, 0, 0, 0)
        scroll_ = ControlHistoryScroller(self)
        hl.addWidget(ControlHistoryTable(self, ScrollBarW=scroll_))
        hl.addWidget(scroll_)
class ControlHistoryTable(ABCTableWidget):
    def __init__(self, parent, widget_name='', ScrollBarW=''):
        super().__init__(parent, widget_name)
        self.setFixedSize(430, 1109)
        self.setContentsMargins(0, 0, 0, 0)
        self.setColumnCount(2)
        self.setColumnWidth(0, 100)
        # self.setColumnWidth(1, 100)
        self.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.horizontalHeader().setDefaultAlignment(Qt.AlignmentFlag.AlignLeft and Qt.AlignmentFlag.AlignVCenter)
        self.horizontalHeader().setFixedHeight(35)
        self.setHorizontalHeaderLabels([' Time', ' Description'])
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

    def add_new_item(self, des_):
        # E.x : self.add_new_item('Test')
        row_index = self.rowCount()
        self.insertRow(row_index)
        self.setItem(row_index, 0, QTableWidgetItem(des_))
        self.setItem(row_index, 1, QTableWidgetItem(f'[{self.inmem.get_time()}]'))
class ControlHistoryScroller(ABCScrollBar):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
class ControlClose(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setFixedSize(138, 25)
        self.setText('닫기')

    def mousePressEvent(self, e: QMouseEvent) -> None:
        self.inmem.widget_ids['ControlWindow'].close()
        return super().mousePressEvent(e)