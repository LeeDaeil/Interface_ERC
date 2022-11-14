from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Interface_ABCWidget import *
from Interface_QSS import *
class MainMiddle(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        
        vl = QVBoxLayout(self)
        self.GraphicsScene = MainMiddleMimicScene(self)
        self.GraphicsView = MainMiddleMimicView(self, scene=self.GraphicsScene)
        vl.addWidget(self.GraphicsView)
        
    def resizeEvent(self, a0: QResizeEvent) -> None:
        w, h = self.GraphicsView.size().width(), self.GraphicsView.size().height()
        self.GraphicsScene.setSceneRect(QRectF(0, 0, w, h))
class MainMiddleMimicView(ABCGraphicsView):
    def __init__(self, parent, widget_name='', scene=None):
        super().__init__(parent, widget_name)
        self.setScene(scene)
        self.setStyleSheet("border: 0px")
class MainMiddleMimicScene(ABCGraphicsScene):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setBackgroundBrush(rgb_to_qCOLOR(Gray))
        
        self.added_items = {
            0: PumpG(self, 30, 30, 'TEMP 1', 'iTestS', 'iTestA')
        }
        
        self.addItem(self.added_items[0])
        self.startTimer(200)
        
    def timerEvent(self, a0: 'QTimerEvent') -> None:
        [self.added_items[key].update_state() for key in self.added_items.keys()]
        return super().timerEvent(a0)
        
class PumpG(ABCGraphicsItemGroup):
    def __init__(self, parent, x, y, comp_name, para_name, alarm_name, widget_name=''):
        super().__init__(parent, widget_name)
        self.DistCompToName = 1.5
        self.compLabel = CompLabel(self, comp_name, alarm_name)
        self.comp = SvgPump(self)
        #
        self.compLabel.setPos(0, self.comp.Hight + self.DistCompToName)
        x = 0 if self.comp.Width > self.compLabel.Width else (self.compLabel.Width - self.comp.Width) * 0.5
        self.comp.setPos(x, 0)
        #        
        self.para_name = para_name
        self.addToGroup(self.compLabel)
        self.addToGroup(self.comp)
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.setPos(x, y)
    
    def update_state(self):
        self.comp.update_state(self.inmem.ShMem.get_para_val(self.para_name))
        self.compLabel.update()

class CompLabel(ABCGraphicsRectItem):
    def __init__(self, parent, compname, alarm_name, widget_name=''):
        super().__init__(parent, widget_name)
        self.CompName = compname
        self.CompNameFont = QFont(Global_font, Mimic_font_size_nub, weight=QFont.Bold)
        self.CompNameFontMatrix = QFontMetrics(self.CompNameFont)
        self.CompNameWidth = self.CompNameFontMatrix.width(self.CompName)
        self.CompNameHight = self.CompNameFontMatrix.height()
        
        self.AlarmLineTick = 3
        self.AlarmLineDist = 4
        self.DistAlarmToName = 2
        
        self.Width = self.AlarmLineTick * 2 + self.DistAlarmToName * 2 + self.CompNameWidth
        self.Hight = self.AlarmLineTick * 2 + self.DistAlarmToName * 2 + self.CompNameHight
        
        self.alarm_name = alarm_name
        self.setRect(0, 0, self.Width, self.Hight)
        
    def paint(self, painter: QPainter, option: 'QStyleOptionGraphicsItem', widget) -> None:
        painter.setFont(self.CompNameFont)
        painter.drawText(self.boundingRect(), Qt.AlignmentFlag.AlignCenter|Qt.AlignmentFlag.AlignHCenter, self.CompName)
        
        painter.setBrush(QBrush(rgb_to_qCOLOR(DarkYellow)))
        painter.setPen(QPen(Qt.PenStyle.NoPen))
        if self.inmem.ShMem.get_para_val(f'{self.alarm_name}') == 1:
            painter.drawRect(0, self.AlarmLineTick, 13, 3)
            painter.drawRect(13 + 8, self.AlarmLineTick, self.Width - 13 * 2 - 8 * 2, 3)
            painter.drawRect(self.Width - 13, self.AlarmLineTick, 13, 3)
        else:
            pass

        
# ==========================================================================================
#
# SVG images
#
# ==========================================================================================
class SvgPump(ABCGraphicsSvgItem):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setSharedRenderer(QSvgRenderer('./Img/images.svg'))
        self.setScale(3.7795275591)
        # ---------------------------
        self.setElementId('Pump_Off')
        self.Hight = self.sceneBoundingRect().height()
        self.Width = self.sceneBoundingRect().width()
    
    def update_state(self, state):
        state = "On" if state == 1 else "Off"
        self.setElementId(f'Pump_{state}')