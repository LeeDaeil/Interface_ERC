from time import sleep
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Interface_ABCWidget import *
from Interface_QSS import *
import typing

class OperationStrategyWindow(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setGeometry(640, 543, 1350, 890)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 상단바 제거
        self.setAttribute(Qt.WA_TranslucentBackground)  # widget 투명화
        self.setStyleSheet(qss) # qss load
        self.m_flag = False

        vl = QVBoxLayout(self)
        vl.setSpacing(0)
        vl.setContentsMargins(0, 0, 0, 0)
        self.title_label = OperationStrategyTitle_BG(self)
        vl.addWidget(self.title_label)
        vl.addWidget(OperationStrategyBoard_BG(self))
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
class OperationStrategyTitle_BG(ABCLabel):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setFixedHeight(25 + 10) # Title size + margin * 2
        hl = QHBoxLayout(self)
        hl.setContentsMargins(10, 5, 5, 5)
        hl.addWidget(OperationStrategyTitle(self))
        hl.addStretch(1)
class OperationStrategyTitle(ABCLabel):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setText('Operation Strategy')
        self.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)
        self.setFixedSize(240, 25)
class OperationStrategyBoard_BG(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        vl = QVBoxLayout(self)
        vl.setContentsMargins(10, 10, 10, 10)
        vl.addWidget(OperationStrategyBoard(self))
        hl = QHBoxLayout()
        hl.addStretch(1)
        hl.addWidget(OperationStrategyClose(self))
        vl.addLayout(hl)
class OperationStrategyBoard(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        vl = QVBoxLayout(self)
        self.GraphicsScene = OperationStrategyBoardScene(self)
        self.GraphicsView = OperationStrategyBoardView(self, scene=self.GraphicsScene)
        vl.addWidget(self.GraphicsView)

    def resizeEvent(self, a0: QResizeEvent) -> None:
        w, h = self.GraphicsView.size().width(), self.GraphicsView.size().height()
        self.GraphicsScene.setSceneRect(QRectF(0, 0, w, h))
class OperationStrategyBoardView(ABCGraphicsView):
    def __init__(self, parent, widget_name='', scene=None):
        super().__init__(parent, widget_name)
        self.setScene(scene)
        self.setStyleSheet("border: 0px")
class OperationStrategyBoardScene(ABCGraphicsScene):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setBackgroundBrush(rgb_to_qCOLOR(LightGray))
        
        self.item_w = 154
        self.item_h = 70
        self.item_m = 16
        self.item_m_multiple = 2
        
        self.items = {}
        # Box --------------------------------------------------------------------------------------------------
        if True:
            # Top
            self.items['t1']      = OperationStrategyBoardItem(self, 230, 0, self.item_w * 0.5, self.item_h * 0.5, in_text='Start')
            self.items['t2']      = OperationStrategyBoardItem(self, self.items['t1'].sx - self.items['t1'].w * 0.5, self.items['t1'].ey, in_text='Are alarms and\ntrip occur?', box=False)
            # Normal
            self.items['n1']      = OperationStrategyBoardItem(self, self.items['t2'].sx - self.item_w - self.item_m * self.item_m_multiple,
                                                        self.items['t2'].ey,  in_text='Normal\noperation strategy')
            self.items['n2']      = OperationStrategyBoardItem(self, self.items['n1'].sx, self.items['n1'].ey, in_text='Auto control RL')
            self.items['n3']      = OperationStrategyBoardItem(self, self.items['n2'].sx, self.items['n2'].ey, in_text='Are all the actions\nperformed?', box=False)
            # Abnormal
            self.items['a1']      = OperationStrategyBoardItem(self, self.items['t2'].sx, self.items['t2'].ey, in_text='Abnormal\noperation strategy')
            self.items['a2']      = OperationStrategyBoardItem(self, self.items['a1'].sx, self.items['a1'].ey, in_text='Is the scenario\ntrained?', box=False)
            self.items['a3']      = OperationStrategyBoardItem(self, self.items['a1'].sx, self.items['a2'].ey, in_text="Is the operator's\nintervention required?", box=False)
            self.items['a4']      = OperationStrategyBoardItem(self, self.items['a1'].sx, self.items['a3'].ey, in_text='Request for\noperator intervention')
            self.items['a5']      = OperationStrategyBoardItem(self, self.items['a1'].sx, self.items['a4'].ey, in_text='Auto control LSTM')
            self.items['a6']      = OperationStrategyBoardItem(self, self.items['a1'].sx, self.items['a5'].ey, in_text='Are all the actions\nperformed?', box=False)
            self.items['a7']      = OperationStrategyBoardItem(self, self.items['a1'].sx, self.items['a6'].ey, in_text='Manual control')

            self.items['a8']      = OperationStrategyBoardItem(self, self.items['a1'].sx + self.item_w + self.item_m * self.item_m_multiple, self.items['a4'].ey, in_text='Auto control LSTM')
            self.items['a9']      = OperationStrategyBoardItem(self, self.items['a8'].sx, self.items['a8'].ey, in_text='Are all the actions\nperformed?', box=False)
            
            self.items['a10']     = OperationStrategyBoardItem(self, self.items['a8'].sx + self.item_w + self.item_m * self.item_m_multiple, self.items['a2'].ey, in_text='Request for\noperator intervention')
            self.items['a11']     = OperationStrategyBoardItem(self, self.items['a10'].sx, self.items['a10'].ey, in_text='Auto control RL')
            self.items['a12']     = OperationStrategyBoardItem(self, self.items['a10'].sx, self.items['a11'].ey, in_text='Is the operator\ninvolved?', box=False)
            self.items['a13']     = OperationStrategyBoardItem(self, self.items['a10'].sx, self.items['a12'].ey, in_text='Manual control')
            # Emergency
            self.items['e1']      = OperationStrategyBoardItem(self, self.items['a10'].sx + self.item_w + self.item_m * self.item_m_multiple, self.items['t2'].ey, in_text='Emergency\noperation strategy')
            self.items['e2']      = OperationStrategyBoardItem(self, self.items['e1'].sx, self.items['e1'].ey, in_text='Is Tech Spec\ncomplied?', box=False)
            self.items['e3']      = OperationStrategyBoardItem(self, self.items['e1'].sx, self.items['a10'].ey, in_text='Is initiating event\nidentified?', box=False)
            self.items['e4']      = OperationStrategyBoardItem(self, self.items['e1'].sx, self.items['e3'].ey, in_text='Auto control LSTM')
            self.items['e5']      = OperationStrategyBoardItem(self, self.items['e1'].sx, self.items['e4'].ey, in_text='Is the status of all\nthe safety functions\nas expected?', box=False)

            self.items['e6']      = OperationStrategyBoardItem(self, self.items['e2'].sx + self.item_w + self.item_m * self.item_m_multiple, self.items['e1'].ey, in_text='Execute\nTech Spec action')
            self.items['e7']      = OperationStrategyBoardItem(self, self.items['e6'].sx, self.items['a10'].ey, in_text='Are all the safety\nfunctions normal?', box=False)
            self.items['e8']      = OperationStrategyBoardItem(self, self.items['e6'].sx, self.items['e4'].ey, in_text='Auto control ES')
            self.items['e9']      = OperationStrategyBoardItem(self, self.items['e6'].sx, self.items['e8'].ey, in_text='Is the status of all\nthe safety functions\nas expected?', box=False)
            
            self.items['e10']     = OperationStrategyBoardItem(self, self.items['e6'].sx + self.item_w + self.item_m * self.item_m_multiple, self.items['a10'].ey, in_text='Manual control')
            # End --------------------------------------------------------------------------------------------------
            self.items['ae']      = OperationStrategyBoardItem(self, self.items['a7'].sx + self.items['t1'].w*0.5, self.items['a7'].ey, self.items['t1'].w, self.items['t1'].h, in_text='End')
            self.items['ne']      = OperationStrategyBoardItem(self, self.items['n3'].sx + self.items['t1'].w*0.5, self.items['a7'].ey, self.items['t1'].w, self.items['t1'].h, in_text='End')
            self.items['ee']      = OperationStrategyBoardItem(self, self.items['e4'].sx + self.items['t1'].w*0.5, self.items['a7'].ey, self.items['t1'].w, self.items['t1'].h, in_text='End')
        # Box - Box line ---------------------------------------------------------------------------------------
        if True:
            self.items['t1_2']    = OperationStrategyBoardLineItem(self, self.items['t1'].BottomP, self.items['t2'].TopP)
            self.items['t2_n1']   = OperationStrategyBoardLineItem(self, self.items['t2'].LeftP, self.items['n1'].TopP, angle=10)
            self.items['n1_2']    = OperationStrategyBoardLineItem(self, self.items['n1'].BottomP, self.items['n2'].TopP)
            self.items['n2_31']   = OperationStrategyBoardLineItem(self, self.items['n2'].BottomP, self.items['n3'].TopP)
            self.items['n2_32']   = OperationStrategyBoardLineItem(self, self.items['n2'].RightP, self.items['n3'].RightP, angle=2)
            self.items['n3_e']    = OperationStrategyBoardLineItem(self, self.items['n3'].BottomP, self.items['ne'].TopP)

            self.items['t2_a1']   = OperationStrategyBoardLineItem(self, self.items['t2'].BottomP, self.items['a1'].TopP)
            self.items['a1_2']    = OperationStrategyBoardLineItem(self, self.items['a1'].BottomP, self.items['a2'].TopP)
            self.items['a2_3']    = OperationStrategyBoardLineItem(self, self.items['a2'].BottomP, self.items['a3'].TopP)
            self.items['a3_4']    = OperationStrategyBoardLineItem(self, self.items['a3'].BottomP, self.items['a4'].TopP)
            self.items['a4_5']    = OperationStrategyBoardLineItem(self, self.items['a4'].BottomP, self.items['a5'].TopP)
            self.items['a5_61']   = OperationStrategyBoardLineItem(self, self.items['a5'].BottomP, self.items['a6'].TopP)
            self.items['a5_62']   = OperationStrategyBoardLineItem(self, self.items['a5'].RightP, self.items['a6'].RightP, angle=2)
            self.items['a6_7']    = OperationStrategyBoardLineItem(self, self.items['a6'].BottomP, self.items['a7'].TopP)
            self.items['a8_a9']   = OperationStrategyBoardLineItem(self, self.items['a8'].RightP, self.items['a9'].RightP, angle=2)
            self.items['a7_e']    = OperationStrategyBoardLineItem(self, self.items['a7'].BottomP, self.items['ae'].TopP)
            
            self.items['a3_8']    = OperationStrategyBoardLineItem(self, self.items['a3'].RightP, self.items['a8'].TopP, angle=10)
            self.items['a8_9']    = OperationStrategyBoardLineItem(self, self.items['a8'].BottomP, self.items['a9'].TopP)
            self.items['a9_e1']   = OperationStrategyBoardLineItem(self, self.items['a9'].BottomP, self.items['ae'].TopP - QPointF(0, self.item_m*0.5), angle=11)

            self.items['a2_10']   = OperationStrategyBoardLineItem(self, self.items['a2'].RightP, self.items['a10'].TopP, angle=10)
            self.items['a10_11']  = OperationStrategyBoardLineItem(self, self.items['a10'].BottomP, self.items['a11'].TopP)
            self.items['a11_12']  = OperationStrategyBoardLineItem(self, self.items['a11'].BottomP, self.items['a12'].TopP)
            self.items['a12_131'] = OperationStrategyBoardLineItem(self, self.items['a12'].BottomP, self.items['a13'].TopP)
            self.items['a12_132'] = OperationStrategyBoardLineItem(self, self.items['a12'].RightP, self.items['a13'].RightP, angle=2)
            self.items['a13_e1']  = OperationStrategyBoardLineItem(self, self.items['a13'].BottomP, self.items['ae'].TopP - QPointF(0, self.item_m*0.5), angle=11)

            self.items['t2_e1']   = OperationStrategyBoardLineItem(self, self.items['t2'].RightP, self.items['e1'].TopP, angle=10)
            self.items['e1_2']    = OperationStrategyBoardLineItem(self, self.items['e1'].BottomP, self.items['e2'].TopP)
            self.items['e2_3']    = OperationStrategyBoardLineItem(self, self.items['e2'].BottomP, self.items['e3'].TopP)
            self.items['e3_4']    = OperationStrategyBoardLineItem(self, self.items['e3'].BottomP, self.items['e4'].TopP)
            self.items['e4_5']    = OperationStrategyBoardLineItem(self, self.items['e4'].BottomP, self.items['e5'].TopP)
            self.items['e5_e1']   = OperationStrategyBoardLineItem(self, self.items['e5'].BottomP, self.items['ee'].TopP)

            self.items['e2_e6']   = OperationStrategyBoardLineItem(self, self.items['e2'].RightP, self.items['e6'].LeftP)
            self.items['e6_e12']  = OperationStrategyBoardLineItem(self, self.items['e6'].RightP, self.items['e3'].TopP - QPointF(0, self.item_m*0.5), angle=2)

            self.items['e3_e7']   = OperationStrategyBoardLineItem(self, self.items['e3'].RightP, self.items['e7'].LeftP)
            self.items['e7_e4']   = OperationStrategyBoardLineItem(self, self.items['e7'].BottomP, self.items['e4'].RightP, angle=11)

            self.items['e5_e8']   = OperationStrategyBoardLineItem(self, self.items['e5'].RightP, self.items['e8'].LeftP)
            self.items['e8_e9']   = OperationStrategyBoardLineItem(self, self.items['e8'].BottomP, self.items['e9'].TopP)
            self.items['e9_ee']   = OperationStrategyBoardLineItem(self, self.items['e9'].BottomP, self.items['ee'].TopP - QPointF(0, self.item_m*0.5), angle=11)

            self.items['e7_e10']   = OperationStrategyBoardLineItem(self, self.items['e7'].RightP, self.items['e10'].LeftP)
            self.items['e10_e9']   = OperationStrategyBoardLineItem(self, self.items['e10'].BottomP, self.items['e9'].RightP, angle=11)
            self.items['e10_ee']   = OperationStrategyBoardLineItem(self, self.items['e10'].RightP, self.items['ee'].TopP - QPointF(0, self.item_m*0.5), angle=2)
        # NY ---------------------------------------------------------------------------------------------------
        if True:
            self.items['n3n']     = OperationStrategyBoardYNItem(self, self.items['n3'].RightP, 1, 'N')      
            self.items['n3y']     = OperationStrategyBoardYNItem(self, self.items['n3'].BottomP, 3, 'Y')      
            self.items['a2n']     = OperationStrategyBoardYNItem(self, self.items['a2'].RightP, 1, 'N')      
            self.items['a2y']     = OperationStrategyBoardYNItem(self, self.items['a2'].BottomP, 3, 'Y')      
            self.items['a3n']     = OperationStrategyBoardYNItem(self, self.items['a3'].RightP, 1, 'N')      
            self.items['a3y']     = OperationStrategyBoardYNItem(self, self.items['a3'].BottomP, 3, 'Y')      
            self.items['a6n']     = OperationStrategyBoardYNItem(self, self.items['a6'].RightP, 1, 'N')      
            self.items['a6y']     = OperationStrategyBoardYNItem(self, self.items['a6'].BottomP, 3, 'Y')     
            self.items['a9n']     = OperationStrategyBoardYNItem(self, self.items['a9'].RightP, 1, 'N')     
            self.items['a9y']     = OperationStrategyBoardYNItem(self, self.items['a9'].BottomP, 3, 'Y')     
            self.items['a12n']     = OperationStrategyBoardYNItem(self, self.items['a12'].RightP, 1, 'N')     
            self.items['a12y']     = OperationStrategyBoardYNItem(self, self.items['a12'].BottomP, 3, 'Y')
            self.items['e2n']     = OperationStrategyBoardYNItem(self, self.items['e2'].RightP, 1, 'N')
            self.items['e2y']     = OperationStrategyBoardYNItem(self, self.items['e2'].BottomP, 3, 'Y')
            self.items['e3n']     = OperationStrategyBoardYNItem(self, self.items['e3'].RightP, 1, 'N')
            self.items['e3y']     = OperationStrategyBoardYNItem(self, self.items['e3'].BottomP, 3, 'Y')
            self.items['e5n']     = OperationStrategyBoardYNItem(self, self.items['e5'].RightP, 1, 'N')
            self.items['e5y']     = OperationStrategyBoardYNItem(self, self.items['e5'].BottomP, 3, 'Y')
            self.items['e7n']     = OperationStrategyBoardYNItem(self, self.items['e7'].RightP, 1, 'N')
            self.items['e7y']     = OperationStrategyBoardYNItem(self, self.items['e7'].BottomP, 3, 'Y')
            self.items['e9n']     = OperationStrategyBoardYNItem(self, self.items['e9'].RightP, 1, 'N')
            self.items['e9y']     = OperationStrategyBoardYNItem(self, self.items['e9'].BottomP, 3, 'Y')
        [self.addItem(w) for w in self.items.values()]

    def update_boxs(self, v_, top_id, sub_ids=None):
        if sub_ids != None:
            [self.items[id].update_blinking(2) for id in sub_ids]
        self.items[top_id].update_blinking(1)

    def call_update(self):
        [self.items[id].update_blinking(0) for id in self.items.keys()]
        v_ = self.inmem.ShMem.get_para_val('iOpStrategy')
        if v_ == 0: self.update_boxs(v_, 't1', None),
        if v_ == 1: self.update_boxs(v_, 'n1', ['t1', 't2']),
        if v_ == 2: self.update_boxs(v_, 'n2', ['t1', 't2', 'n1']),
        if v_ == 3: self.update_boxs(v_, 'ne', ['t1', 't2', 'n1', 'n2', 'n3']),
        if v_ == 4: self.update_boxs(v_, 'a1', ['t1', 't2']),
        if v_ == 5: self.update_boxs(v_, 'a4', ['t1', 't2', 'a1', 'a2', 'a3']),
        if v_ == 6: self.update_boxs(v_, 'a5', ['t1', 't2', 'a1', 'a2', 'a3', 'a4']),
        if v_ == 7: self.update_boxs(v_, 'a7', ['t1', 't2', 'a1', 'a2', 'a3', 'a4', 'a5','a6']),
        if v_ == 8: self.update_boxs(v_, 'ae', ['t1', 't2', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7']),
        if v_ == 9: self.update_boxs(v_, 'a8', ['t1', 't2', 'a1', 'a2', 'a3']),
        if v_ == 10: self.update_boxs(v_, 'ae', ['t1', 't2', 'a1', 'a2', 'a3', 'a8', 'a9']),
        if v_ == 11: self.update_boxs(v_, 'a10', ['t1', 't2', 'a1', 'a2']),
        if v_ == 12: self.update_boxs(v_, 'a11', ['t1', 't2', 'a1', 'a2', 'a10']),
        if v_ == 13: self.update_boxs(v_, 'a13', ['t1', 't2', 'a1', 'a2', 'a10', 'a11', 'a12']),
        if v_ == 14: self.update_boxs(v_, 'ae', ['t1', 't2', 'a1', 'a2', 'a10', 'a11', 'a12', 'a13']),
        if v_ == 15: self.update_boxs(v_, 'e1', ['t1', 't2']),
        if v_ == 16: self.update_boxs(v_, 'e4', ['t1', 't2', 'e1', 'e2', 'e3']),
        if v_ == 17: self.update_boxs(v_, 'ee', ['t1', 't2', 'e1', 'e2', 'e3', 'e4', 'e5']),
        if v_ == 18: self.update_boxs(v_, 'e6', ['t1', 't2', 'e1', 'e2']),
        if v_ == 19: self.update_boxs(v_, 'e8', ['t1', 't2', 'e1', 'e2', 'e3', 'e4', 'e5']),
        if v_ == 20: self.update_boxs(v_, 'e10', ['t1', 't2', 'e1', 'e2', 'e3', 'e7']),
class OperationStrategyBoardItem(ABCGraphicsPolygonItem):
    def __init__(self, parent, x, y, w=None, h=None, in_text='', box=True, widget_name=''):
        super().__init__(parent, widget_name)
        self.setPos(QPointF(x, y))
        self.w = self.inmem.widget_ids['OperationStrategyBoardScene'].item_w if w is None else w
        self.h = self.inmem.widget_ids['OperationStrategyBoardScene'].item_h if h is None else h
        self.sx = x
        self.ey = self.h + y + self.inmem.widget_ids['OperationStrategyBoardScene'].item_m

        if box:
            self.rect_points = [QPoint(0, 0), QPoint(self.w, 0), QPoint(self.w, self.h), QPoint(0, self.h)]
        else:
            self.rect_points = [QPoint(self.w * 0.5, 0), QPoint(0, self.h * 0.5), QPoint(self.w * 0.5, self.h), QPoint(self.w, self.h * 0.5)]
            
        self.TopP = QPointF(self.w * 0.5, 0) + QPointF(x, y)
        self.RightP = QPointF(self.w, self.h * 0.5) + QPointF(x, y)
        self.LeftP = QPointF(0, self.h * 0.5) + QPointF(x, y)
        self.BottomP = QPointF(self.w * 0.5, self.h) + QPointF(x, y)
        
        self.setPolygon(QPolygonF(self.rect_points))
        self.in_text = in_text
        self.blinking = 0
        self.color_rule = {
            0: rgb_to_qCOLOR(LightWhite),
            1: rgb_to_qCOLOR(Yellow),
            2: rgb_to_qCOLOR(Gray),
        }
    
    def update_blinking(self, id):
        self.blinking = id

    def paint(self, painter: QPainter, option: 'QStyleOptionGraphicsItem', widget: typing.Optional[QWidget] = ...) -> None:
        painter.setPen(QPen(rgb_to_qCOLOR(DarkGray), 1))
        painter.setBrush(QBrush(self.color_rule[self.blinking]))
        painter.drawPolygon(QPolygonF(self.rect_points))
        #
        painter.setPen(QPen(rgb_to_qCOLOR(Black), 1))
        painter.setFont(QFont(Global_font, Content_font_size_nub,weight=QFont.Bold))
        painter.drawText(self.boundingRect(), Qt.AlignmentFlag.AlignCenter, self.in_text)
        #
        return super().paint(painter, option, widget)
class OperationStrategyBoardLineItem(ABCGraphicsPathItem):
    def __init__(self, parent, startp:QPointF, endp:QPointF, angle=0, widget_name=''):
        super().__init__(parent, widget_name)
        self.StartP = startp
        self.EndP = endp

        self.setPen(QPen(rgb_to_qCOLOR(DarkGray), 2))
        
        if angle == 0:
            points = [endp]
        elif angle == 10:
            points = [QPointF(endp.x(), startp.y()), endp]
        elif angle == 11:
            points = [QPointF(startp.x(), endp.y()), endp]
        elif angle == 2:
            p_1 = startp + QPointF(25, 0)
            points = [p_1, QPointF(p_1.x(),endp.y()), endp]

        path_ = QPainterPath()
        path_.moveTo(startp)
        [path_.lineTo(p) for p in points]
        self.setPath(path_)
    
    def update_blinking(self, id):
        pass
class OperationStrategyBoardYNItem(ABCGraphicsRectItem):
    def __init__(self, parent, fixpoint, position=0, in_text='', widget_name=''):
        super().__init__(parent, widget_name)
        # 0 | 1
        # 2 | 3
        w = 20
        start_points = {
            0: fixpoint - QPointF(w, w),
            1: fixpoint - QPointF(0, w),
            2: fixpoint - QPointF(w, 0),
            3: fixpoint,
        }
        self.setPos(start_points[position])
        self.setRect(QRectF(0, 0, w, w))
        self.in_text = in_text

    def update_blinking(self, id):
        pass

    def paint(self, painter: QPainter, option: 'QStyleOptionGraphicsItem', widget: typing.Optional[QWidget] = ...) -> None:
        #
        painter.setPen(QPen(rgb_to_qCOLOR(Black), 1))
        painter.setFont(QFont(Global_font, Content_font_size_nub, weight=QFont.Bold))
        painter.drawText(self.boundingRect(), Qt.AlignmentFlag.AlignCenter, self.in_text)
class OperationStrategyClose(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setFixedSize(160, 25)
        self.setText('닫기')

    def mousePressEvent(self, e: QMouseEvent) -> None:
        self.inmem.widget_ids['OperationStrategyWindow'].close()
        return super().mousePressEvent(e)