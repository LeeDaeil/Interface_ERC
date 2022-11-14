from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSvg import QGraphicsSvgItem, QSvgRenderer
from Function_Mem_ShMem import ShMem, InterfaceMem



class TOOL:   
    @staticmethod
    def make_shmem(parent, child, widget_name):
        """새롭게 명명된 위젯을 widget_id에 저장

        Args:
            parent (_type_): 부모의 inmem 주소값
            child (_type_): 새롭게 생성된 widget id
            widget_name (_type_): widget class name

        Returns:
            _type_: 업데이트된 inmem
        """
        result = parent.inmem
        result.add_widget_id(child, widget_name)
        return result

class ABCWidget(QWidget, TOOL):
    def __init__(self, parent, widget_name=''):
        super(ABCWidget, self).__init__()
        self.inmem: InterfaceMem = TOOL.make_shmem(parent, self, widget_name)
        self.widget_name=type(self).__name__ if widget_name == '' else widget_name
        self.setObjectName(self.widget_name)
        self.setAttribute(Qt.WA_StyledBackground, True)

    def mousePressEvent(self, a0: QMouseEvent) -> None:
        print(f'This is {self.widget_name}')
        return super().mousePressEvent(a0)

class ABCPushButton(QPushButton, TOOL):
    def __init__(self, parent, widget_name=''):
        super(ABCPushButton, self).__init__()
        self.inmem: InterfaceMem = TOOL.make_shmem(parent, self, widget_name)
        self.widget_name=type(self).__name__ if widget_name == '' else widget_name
        self.setObjectName(self.widget_name)
        self.setAttribute(Qt.WA_StyledBackground, True)

    def mousePressEvent(self, e: QMouseEvent) -> None:
        print(f'This is {self.widget_name}')
        return super().mousePressEvent(e)

class ABCLabel(QLabel, TOOL):
    def __init__(self, parent, widget_name=''):
        super(ABCLabel, self).__init__()
        self.inmem: InterfaceMem = TOOL.make_shmem(parent, self, widget_name)
        self.widget_name=type(self).__name__ if widget_name == '' else widget_name
        self.setObjectName(self.widget_name)
        self.setAttribute(Qt.WA_StyledBackground, True)
    
    def mousePressEvent(self, ev: QMouseEvent) -> None:
        print(f'This is {self.widget_name}')
        return super().mousePressEvent(ev)

class ABCTabWidget(QTabWidget, TOOL):
    def __init__(self, parent, widget_name=''):
        super(ABCTabWidget, self).__init__()
        self.inmem: InterfaceMem = TOOL.make_shmem(parent, self, widget_name)
        self.widget_name=type(self).__name__ if widget_name == '' else widget_name
        self.setObjectName(self.widget_name)
        self.setAttribute(Qt.WA_StyledBackground, True)
    
    def mousePressEvent(self, a0: QMouseEvent) -> None:
        print(f'This is {self.widget_name}')
        return super().mousePressEvent(a0)

class ABCText(QTextEdit, TOOL):
    def __init__(self, parent, widget_name=''):
        super(ABCText, self).__init__()
        self.inmem: InterfaceMem = TOOL.make_shmem(parent, self, widget_name)
        self.widget_name=type(self).__name__ if widget_name == '' else widget_name
        self.setObjectName(self.widget_name)
        self.setAttribute(Qt.WA_StyledBackground, True)

    def mousePressEvent(self, e: QMouseEvent) -> None:
        print(f'This is {self.widget_name}')
        return super().mousePressEvent(e)

class ABCTableWidget(QTableWidget, TOOL):
    def __init__(self, parent, widget_name=''):
        super(ABCTableWidget, self).__init__()
        self.inmem: InterfaceMem = TOOL.make_shmem(parent, self, widget_name)
        self.widget_name=type(self).__name__ if widget_name == '' else widget_name
        self.setObjectName(self.widget_name)
        self.setAttribute(Qt.WA_StyledBackground, True)

    def mousePressEvent(self, e: QMouseEvent) -> None:
        print(f'This is {self.widget_name}')
        return super().mousePressEvent(e)

class ABCStackWidget(QStackedWidget, TOOL):
    def __init__(self, parent, widget_name=''):
        super(ABCStackWidget, self).__init__()
        self.inmem: InterfaceMem = TOOL.make_shmem(parent, self, widget_name)
        self.widget_name=type(self).__name__ if widget_name == '' else widget_name
        self.setObjectName(self.widget_name)
        self.setAttribute(Qt.WA_StyledBackground, True)

class ABCGraphicsScene(QGraphicsScene, TOOL):
    def __init__(self, parent, widget_name=''):
        super(ABCGraphicsScene, self).__init__()
        self.inmem: InterfaceMem = TOOL.make_shmem(parent, self, widget_name)
        self.widget_name=type(self).__name__ if widget_name == '' else widget_name
        self.setObjectName(self.widget_name)

    def mousePressEvent(self, event: 'QGraphicsSceneMouseEvent') -> None:
        print(f'This is {self.widget_name}')
        return super().mousePressEvent(event)
class ABCGraphicsView(QGraphicsView, TOOL):
    def __init__(self, parent, widget_name=''):
        super(ABCGraphicsView, self).__init__()
        self.inmem: InterfaceMem = TOOL.make_shmem(parent, self, widget_name)
        self.widget_name=type(self).__name__ if widget_name == '' else widget_name
        self.setObjectName(self.widget_name)
class ABCGraphicsRectItem(QGraphicsRectItem, TOOL):
    def __init__(self, parent, widget_name=''):
        super(ABCGraphicsRectItem, self).__init__()
        self.inmem: InterfaceMem = TOOL.make_shmem(parent, self, widget_name)
        self.widget_name=type(self).__name__ if widget_name == '' else widget_name
class ABCGraphicsTextItem(QGraphicsTextItem, TOOL):
    def __init__(self, parent, widget_name=''):
        super(ABCGraphicsTextItem, self).__init__()
        self.inmem: InterfaceMem = TOOL.make_shmem(parent, self, widget_name)
        self.widget_name=type(self).__name__ if widget_name == '' else widget_name
class ABCGraphicsPolygonItem(QGraphicsPolygonItem, TOOL):
    def __init__(self, parent, widget_name=''):
        super(ABCGraphicsPolygonItem, self).__init__()
        self.inmem: InterfaceMem = TOOL.make_shmem(parent, self, widget_name)
        self.widget_name=type(self).__name__ if widget_name == '' else widget_name
class ABCGraphicsPathItem(QGraphicsPathItem, TOOL):
    def __init__(self, parent, widget_name=''):
        super(ABCGraphicsPathItem, self).__init__()
        self.inmem: InterfaceMem = TOOL.make_shmem(parent, self, widget_name)
        self.widget_name=type(self).__name__ if widget_name == '' else widget_name
class ABCGraphicsLineItem(QGraphicsLineItem, TOOL):
    def __init__(self, parent, widget_name=''):
        super(ABCGraphicsLineItem, self).__init__()
        self.inmem: InterfaceMem = TOOL.make_shmem(parent, self, widget_name)
        self.widget_name=type(self).__name__ if widget_name == '' else widget_name
class ABCGraphicsSvgItem(QGraphicsSvgItem, TOOL):
    def __init__(self, parent, widget_name=''):
        super(ABCGraphicsSvgItem, self).__init__()
        self.inmem: InterfaceMem = TOOL.make_shmem(parent, self, widget_name)
        self.widget_name=type(self).__name__ if widget_name == '' else widget_name
class ABCGraphicsItemGroup(QGraphicsItemGroup, TOOL):
    def __init__(self, parent, widget_name=''):
        super(ABCGraphicsItemGroup, self).__init__()
        self.inmem: InterfaceMem = TOOL.make_shmem(parent, self, widget_name)
        self.widget_name=type(self).__name__ if widget_name == '' else widget_name
class ABCTreeWidget(QTreeWidget, TOOL):
    def __init__(self, parent, widget_name=''):
        super(ABCTreeWidget, self).__init__()
        self.inmem: InterfaceMem = TOOL.make_shmem(parent, self, widget_name)
        self.widget_name=type(self).__name__ if widget_name == '' else widget_name
        self.setObjectName(self.widget_name)
class ABCScrollBar(QScrollBar, TOOL):
    def __init__(self, parent, widget_name=''):
        super(ABCScrollBar, self).__init__()
        self.inmem: InterfaceMem = TOOL.make_shmem(parent, self, widget_name)
        self.widget_name=type(self).__name__ if widget_name == '' else widget_name
        self.setObjectName(self.widget_name)