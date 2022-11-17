from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Interface_ABCWidget import *
from Interface_QSS import *
import typing
import json

TEST = True
def CPrint(txt):
    if TEST: print(txt)
class MainMiddle(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        
        vl = QVBoxLayout(self)
        self.GraphicsScene = MainMiddleMimicScene(self)
        self.GraphicsView = MainMiddleMimicView(self, scene=self.GraphicsScene)
        vl.addWidget(self.GraphicsView)
        
        # ---------------------------------
        # 단축키 섹션
        # ---------------------------------
        self.shortcut_save_scene = QShortcut(QKeySequence('Ctrl+S'), self, self.inmem.widget_ids['MainMiddleMimicScene'].save_scene)
        self.shortcut_load_scene = QShortcut(QKeySequence('Ctrl+L'), self, self.inmem.widget_ids['MainMiddleMimicScene'].load_scene)
        self.shortcut_move_item_up = QShortcut(Qt.Key.Key_Up, self, lambda: self.inmem.widget_ids['MainMiddleMimicScene'].move_item('up'))
        self.shortcut_move_item_up = QShortcut(Qt.Key.Key_Down, self, lambda: self.inmem.widget_ids['MainMiddleMimicScene'].move_item('down'))
        self.shortcut_move_item_up = QShortcut(Qt.Key.Key_Right, self, lambda: self.inmem.widget_ids['MainMiddleMimicScene'].move_item('right'))
        self.shortcut_move_item_up = QShortcut(Qt.Key.Key_Left, self, lambda: self.inmem.widget_ids['MainMiddleMimicScene'].move_item('left'))
        
    def resizeEvent(self, a0: QResizeEvent) -> None:
        w, h = self.GraphicsView.size().width(), self.GraphicsView.size().height()
        self.GraphicsScene.setSceneRect(QRectF(0, 0, w, h))
class MainMiddleMimicView(ABCGraphicsView):
    def __init__(self, parent, widget_name='', scene=None):
        super().__init__(parent, widget_name)
        self.setScene(scene)
        self.setStyleSheet("border: 0px")
        self.setDragMode(QGraphicsView.DragMode.RubberBandDrag)
class MainMiddleMimicScene(ABCGraphicsScene):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setBackgroundBrush(rgb_to_qCOLOR(Gray))
        
        self.ItemBox = {}
        self.ItemAgs = {}
        
        self.load_scene()
                
        self.startTimer(600)
    
    def load_scene(self):
        """
        저장 화면 불러오기 (Ctrl+L)
        """
        print('MainMiddle Mimic 화면 Load')
        # If any items is added in scene, the items will be removed.
        for item in self.items():
            self.removeItem(item)
        # load json file
        with open('./Interface_MainMiddle_Mimic.json') as f:
            self.ItemAgs = json.load(f)

        for id in self.ItemAgs:
            if self.ItemAgs[id]['CType'] == 'Pump':
                self.ItemBox[id] = PumpG(self, self.ItemAgs[id])
            elif self.ItemAgs[id]['CType'] == 'Img':
                self.ItemBox[id] = ImgG(self, self.ItemAgs[id])
            elif self.ItemAgs[id]['CType'] == 'Pipe':
                self.ItemBox[id] = LineG(self, self.ItemAgs[id])                
            self.addItem(self.ItemBox[id])
    
    def save_scene(self):
        """
        현재 화면 저장 (Ctrl+S)
        """
        with open('Interface_MainMiddle_Mimic.json', 'w') as f:
            for id in self.ItemBox.keys():
                self.ItemAgs[id] = self.ItemBox[id].args
            json.dump(self.ItemAgs, f, indent=2)
        print('MainMiddle Mimic 화면 Save')
    
    def move_item(self, direction):
        # If one or more than one item is selected and Up key is pressed, the item selected will be moved up, down, right or left.
        for item in self.selectedItems():
            if direction == 'up':
                item.move_pos(0, -1)
            if direction == 'down':
                item.move_pos(0, 1)
            if direction == 'right':
                item.move_pos(1, 0)
            if direction == 'left':
                item.move_pos(-1, 0)
    
    def timerEvent(self, a0: 'QTimerEvent') -> None:
        [item.update_state() for item in self.ItemBox.values()]
        return super().timerEvent(a0)
# ==========================================================================================
#
# Comp element
#
# ==========================================================================================
class CompLabel(ABCGraphicsRectItem):
    def __init__(self, parent, args, widget_name=''):
        super().__init__(parent, widget_name)
        self.CompName = args['comp_name']
        self.CompNameFont = QFont(Global_font, Mimic_font_size_nub, weight=QFont.Bold)
        self.CompNameFontMatrix = QFontMetrics(self.CompNameFont)
        self.CompNameWidth = self.CompNameFontMatrix.width(self.CompName)
        self.CompNameHight = self.CompNameFontMatrix.height()
        
        self.AlarmLineTick = 3
        self.AlarmLineDist = 8
        self.DistAlarmToName = 2
        
        self.Width = self.AlarmLineTick * 2 + self.DistAlarmToName * 2 + self.CompNameWidth
        self.Hight = self.AlarmLineTick * 2 + self.DistAlarmToName * 2 + self.CompNameHight
        
        self.alarm_name = args['alarm_name']
        self.setRect(0, 0, self.Width, self.Hight)
        
        self.blink = False
        
    def paint(self, painter: QPainter, option: 'QStyleOptionGraphicsItem', widget) -> None:
        painter.setFont(self.CompNameFont)
        painter.drawText(self.boundingRect(), Qt.AlignmentFlag.AlignCenter|Qt.AlignmentFlag.AlignHCenter, self.CompName)
        
        painter.setPen(QPen(rgb_to_qCOLOR(DarkYellow), self.AlarmLineTick, Qt.PenStyle.SolidLine))
        
        if self.inmem.ShMem.get_para_val(f'{self.alarm_name}') == 1:
            self.blink = not self.blink
            if self.blink:
                # TopLine
                painter.drawLine(0, self.AlarmLineTick, 13, self.AlarmLineTick)
                painter.drawLine(self.Width - 13, self.AlarmLineTick, self.Width, self.AlarmLineTick)
                # BottomLine
                painter.drawLine(0, self.Hight - self.AlarmLineTick, 13, self.Hight - self.AlarmLineTick)
                painter.drawLine(self.Width - 13, self.Hight - self.AlarmLineTick, self.Width, self.Hight - self.AlarmLineTick)
                # RightLine
                painter.drawLine(0, self.AlarmLineTick, 0, self.AlarmLineTick + 8)
                painter.drawLine(0, self.Hight - self.AlarmLineTick, 0, self.Hight - self.AlarmLineTick - 8)
                # LeftLine
                painter.drawLine(self.Width, self.AlarmLineTick, self.Width, self.AlarmLineTick + 8)
                painter.drawLine(self.Width, self.Hight - self.AlarmLineTick, self.Width, self.Hight - self.AlarmLineTick - 8)
                
                # middleLine
                middle_width = self.Width - (13 + self.AlarmLineDist) * 2
                middle_bar_w = (middle_width - self.AlarmLineDist) * 0.5
                
                painter.drawLine(13 + self.AlarmLineDist, self.AlarmLineTick, 13 + self.AlarmLineDist + middle_bar_w, self.AlarmLineTick) # top right
                painter.drawLine(self.Width - 13 - self.AlarmLineDist - middle_bar_w, self.AlarmLineTick, self.Width - 13 - self.AlarmLineDist, self.AlarmLineTick) # top left
                
                painter.drawLine(13 + self.AlarmLineDist, self.Hight - self.AlarmLineTick, 13 + self.AlarmLineDist + middle_bar_w, self.Hight - self.AlarmLineTick) # bottom right
                painter.drawLine(self.Width - 13 - self.AlarmLineDist - middle_bar_w, self.Hight - self.AlarmLineTick, self.Width - 13 - self.AlarmLineDist, self.Hight - self.AlarmLineTick) # bottom left
        else:
            self.blink = False     
class SvgPump(ABCGraphicsSvgItem):
    def __init__(self, parent, args, widget_name=''):
        super().__init__(parent, widget_name)
        self.setSharedRenderer(QSvgRenderer('./Img/images.svg'))
        self.setScale(3.7795275591)
        assert args['direction'] == 'R' or args['direction'] == 'L', f'Pump direction error : {args["direction"]}'
        # ---------------------------
        self.setElementId('Pump_Off')
        self.Hight = self.sceneBoundingRect().height()
        self.Width = self.sceneBoundingRect().width()
        self.InPoint = QPointF(0, 0)
        self.OutPoint = QPointF(0, 0)
        self.direction = args['direction']
        self.update_direction(args['direction'])
        
    def update_direction(self, direction):
        if direction == 'R':
            trans_f = QTransform()
            trans_f.scale(-1, 1)
            trans_f.translate(- self.Width, 0)
            self.setTransform(trans_f)
        else:
            pass # Original image is left direction

    def update_InOutPoints(self):
        self.InPoint.setX(self.sceneBoundingRect().x() if self.direction == 'R' else self.Width + self.sceneBoundingRect().x())
        self.InPoint.setY(19.5 + self.sceneBoundingRect().y())
        self.OutPoint.setX(self.Width + self.sceneBoundingRect().x() if self.direction == 'R' else self.sceneBoundingRect().x())
        self.OutPoint.setY(8.5 + self.sceneBoundingRect().y())
        
    def update_state(self, state):
        state = "On" if state == 1 else "Off"
        self.setElementId(f'Pump_{state}')
class SvgImg(ABCGraphicsSvgItem):
    def __init__(self, parent, args, widget_name=''):
        super().__init__(parent, widget_name)
        self.setSharedRenderer(QSvgRenderer('./Img/images.svg'))
        self.setScale(3.7795275591)
        assert args['direction'] == 'V' or args['direction'] == 'H', f'Pump direction error : {args["direction"]}'
        # ---------------------------
        self.setElementId(f'{args["img_name"]}_{args["direction"]}')
        self.Hight = self.sceneBoundingRect().height()
        self.Width = self.sceneBoundingRect().width()
        self.InPoint = QPointF(0, 0)
        self.OutPoint = QPointF(0, 0)
        self.args = args
        self.direction = args['direction']
    
    def update_InOutPoints(self):
        if self.args['img_name'] == 'HX':
            self.InPoint.setX(self.sceneBoundingRect().x() + self.Width * 0.5 if self.direction == 'V' else 0)
            self.InPoint.setY(0 if self.direction == 'V' else self.sceneBoundingRect().y() + self.Hight * 0.5)
            self.OutPoint.setX(self.sceneBoundingRect().x() + self.Width * 0.5 if self.direction == 'V' else self.sceneBoundingRect().x() + self.Width)
            self.OutPoint.setY(self.sceneBoundingRect().y() + self.Hight if self.direction == 'V' else self.sceneBoundingRect().y() + self.Hight * 0.5)
    
# ==========================================================================================
#
# Comp package
#
# ==========================================================================================
class PumpG(ABCGraphicsItemGroup):
    def __init__(self, parent, args, widget_name=''):
        super().__init__(parent, widget_name='')
        self.DistCompToName = 1.5
        self.args = args
        self.compLabel = CompLabel(self, args)
        self.comp = SvgPump(self, args)
        #
        self.compLabel.setPos(0, self.comp.Hight + self.DistCompToName)
        x_ = 0 if self.comp.Width > self.compLabel.Width else (self.compLabel.Width - self.comp.Width) * 0.5
        self.comp.setPos(x_, 0)
        #        
        self.addToGroup(self.compLabel)
        self.addToGroup(self.comp)
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.setPos(self.args['x'], self.args['y'])
        #
        self.comp.update_InOutPoints()
        self.InPoint = self.comp.InPoint
        self.OutPoint = self.comp.OutPoint
    
    def update_state(self):
        val = self.inmem.ShMem.get_para_val(self.args['para_name'])
        self.comp.update_state(val)
        self.compLabel.update()
        if self.args['connected_id'] != []:
            for line_id in self.args['connected_id']:
                if line_id in self.inmem.widget_ids['MainMiddleMimicScene'].ItemBox.keys():
                    self.inmem.widget_ids['MainMiddleMimicScene'].ItemBox[line_id].flow = val
                else:
                    CPrint(f"{self.args['Id']}와 {line_id} 가 연결되지 않음. Json 파일 수정 필요함.")
    
    def mouseReleaseEvent(self, event: 'QGraphicsSceneMouseEvent') -> None:
        CPrint(f'{self.args["Id"]:_^50}')
        CPrint(f'이전 Pos  x: {self.args["x"]}, y: {self.args["y"]}')
        CPrint(f'최종 Pos  x: {self.pos().x()}, y: {self.pos().y()}')
        self.args["x"] = self.pos().x()
        self.args["y"] = self.pos().y()
        CPrint(f'입력 Pos  x: {self.InPoint.x()}, y: {self.InPoint.y()}')
        CPrint(f'출력 Pos  x: {self.OutPoint.x()}, y: {self.OutPoint.y()}')
        return super().mouseReleaseEvent(event)
    
    def move_pos(self, dx, dy):
        CPrint(f'{self.args["Id"]:_^50}')
        CPrint(f'이전 Pos  x: {self.args["x"]}, y: {self.args["y"]}')
        self.setPos(self.pos().x() + dx, self.pos().y() + dy)
        CPrint(f'최종 Pos  x: {self.pos().x()}, y: {self.pos().y()}')
        self.args["x"] = self.pos().x()
        self.args["y"] = self.pos().y()
        
class ImgG(ABCGraphicsItemGroup):
    def __init__(self, parent, args, widget_name=''):
        super().__init__(parent, widget_name)
        self.DistCompToName = 1.5
        self.args = args
        self.compLabel = CompLabel(self, args)
        self.comp = SvgImg(self, args)
        #
        if args["comp_name_direction"] == 'Right':
            self.comp.setPos(0, 0)
            self.compLabel.setPos(self.comp.Width + self.DistCompToName * 3, (self.comp.Hight - self.compLabel.Hight) * 0.5)
        #
        self.addToGroup(self.compLabel)
        self.addToGroup(self.comp)
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.setPos(self.args['x'], self.args['y'])
        #
        self.comp.update_InOutPoints()
        self.InPoint = self.comp.InPoint
        self.OutPoint = self.comp.OutPoint
    
    def update_state(self):
        self.compLabel.update()
    
    def mouseReleaseEvent(self, event: 'QGraphicsSceneMouseEvent') -> None:
        CPrint(f'{self.args["Id"]:_^50}')
        CPrint(f'이전 Pos  x: {self.args["x"]}, y: {self.args["y"]}')
        CPrint(f'최종 Pos  x: {self.pos().x()}, y: {self.pos().y()}')
        self.args["x"] = self.pos().x()
        self.args["y"] = self.pos().y()
        CPrint(f'입력 Pos  x: {self.InPoint.x()}, y: {self.InPoint.y()}')
        CPrint(f'출력 Pos  x: {self.OutPoint.x()}, y: {self.OutPoint.y()}')
        return super().mouseReleaseEvent(event)
    
    def move_pos(self, dx, dy):
        CPrint(f'{self.args["Id"]:_^50}')
        CPrint(f'이전 Pos  x: {self.args["x"]}, y: {self.args["y"]}')
        self.setPos(self.pos().x() + dx, self.pos().y() + dy)
        CPrint(f'최종 Pos  x: {self.pos().x()}, y: {self.pos().y()}')
        self.args["x"] = self.pos().x()
        self.args["y"] = self.pos().y()
# ==========================================================================================
#
# Line elements and package
#
# ==========================================================================================
class ArrowHead(ABCGraphicsPolygonItem):
    def __init__(self, parent, args, widget_name=''):
        super().__init__(parent, widget_name)
        if args['arrow']:
            self.setPolygon(QPolygonF([QPointF(-5, 0), QPointF(5, 0), QPointF(0, 10)]))
        self.setBrush(QBrush(rgb_to_qCOLOR(DarkGray), Qt.BrushStyle.SolidPattern))
        self.setPen(QPen(Qt.PenStyle.NoPen))
        self.setPos(QPointF(args['x2'], args['y2']))
        self.setRotation(- QLineF(QPointF(args['x1'], args['y1']), QPointF(args['x2'], args['y2'])).angle() - 90)
class PipeLines(ABCGraphicsLineItem):
    def __init__(self, parent, args, widget_name=''):
        super().__init__(parent, widget_name)
        self.setPen(QPen(rgb_to_qCOLOR(DarkGray), 3))
        self.setLine(QLineF(QPointF(args['x1'], args['y1']),
                            QPointF(args['x2'], args['y2'])))
class LineG(ABCGraphicsItemGroup):
    def __init__(self, parent, args, widget_name=''):
        super().__init__(parent, widget_name)
        self.args = args
        self.Pipe = PipeLines(self, args)
        self.Arrowhead = ArrowHead(self, args)
        self.addToGroup(self.Pipe)
        self.addToGroup(self.Arrowhead)
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.flow = 0
        
    def update_state(self):
        if self.flow > 0:
            self.Arrowhead.setBrush(QBrush(rgb_to_qCOLOR(LightBlue), Qt.BrushStyle.SolidPattern))
            self.Pipe.setPen(QPen(rgb_to_qCOLOR(LightBlue), 3))
        else:
            self.Arrowhead.setBrush(QBrush(rgb_to_qCOLOR(DarkGray), Qt.BrushStyle.SolidPattern))
            self.Pipe.setPen(QPen(rgb_to_qCOLOR(DarkGray), 3))
            
        self.update()
        
        if self.args['connected_id'] != []:
            for line_id in self.args['connected_id']:
                if line_id in self.inmem.widget_ids['MainMiddleMimicScene'].ItemBox.keys():
                    self.inmem.widget_ids['MainMiddleMimicScene'].ItemBox[line_id].flow = self.flow
                else:
                    CPrint(f"{self.args['Id']}와 {line_id} 가 연결되지 않음. Json 파일 수정 필요함.")
                    
    def mouseReleaseEvent(self, event: 'QGraphicsSceneMouseEvent') -> None:
        CPrint(f'{self.args["Id"]:_^50}')
        CPrint(f'이전 Pos  x1: {self.args["x1"]}, \
                           x2: {self.args["x2"]}, \
                           y1: {self.args["y1"]}, \
                           y2: {self.args["y2"]}, \
                           ')
        CPrint(f'최종 Pos  x1: {self.Pipe.line().p1().x() + self.pos().x()}, \
                           x2: {self.Pipe.line().p2().x() + self.pos().x()}, \
                           y1: {self.Pipe.line().p1().y() + self.pos().y()}, \
                           y2: {self.Pipe.line().p2().y() + self.pos().y()}, \
                           ')
        
        self.args["x1"] = self.Pipe.line().p1().x() + self.pos().x()
        self.args["x2"] = self.Pipe.line().p2().x() + self.pos().x()
        self.args["y1"] = self.Pipe.line().p1().y() + self.pos().y()
        self.args["y2"] = self.Pipe.line().p2().y() + self.pos().y()
        return super().mouseReleaseEvent(event)
    
    def move_pos(self, dx, dy):
        CPrint(f'{self.args["Id"]:_^50}')
        CPrint(f'이전 Pos  x1: {self.args["x1"]}, \
                           x2: {self.args["x2"]}, \
                           y1: {self.args["y1"]}, \
                           y2: {self.args["y2"]}, \
                           ')
        self.setPos(self.pos().x() + dx, self.pos().y() + dy)
        CPrint(f'최종 Pos  x1: {self.Pipe.line().p1().x() + self.pos().x()}, \
                           x2: {self.Pipe.line().p2().x() + self.pos().x()}, \
                           y1: {self.Pipe.line().p1().y() + self.pos().y()}, \
                           y2: {self.Pipe.line().p2().y() + self.pos().y()}, \
                           ')
        self.args["x1"] = self.Pipe.line().p1().x() + self.pos().x()
        self.args["x2"] = self.Pipe.line().p2().x() + self.pos().x()
        self.args["y1"] = self.Pipe.line().p1().y() + self.pos().y()
        self.args["y2"] = self.Pipe.line().p2().y() + self.pos().y()