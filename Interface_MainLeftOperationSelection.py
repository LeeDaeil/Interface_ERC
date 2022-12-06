from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Interface_ABCWidget import *
from Interface_QSS import qss


class OperationSelectionWindow(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setGeometry(584, 154, 300, 500)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 상단바 제거
        self.setAttribute(Qt.WA_TranslucentBackground)      # widget 투명화
        self.setStyleSheet(qss) # qss load
        self.m_flag = False

        vl = QVBoxLayout(self)
        title_bg = OperationSelectionTitle_BG(self)
        vl.addWidget(title_bg)
        self.op_tree = OperationSelectionTree(self)
        vl.addWidget(self.op_tree)
        vl.setSpacing(0)
        vl.setContentsMargins(0, 0, 0, 0)

        bottom_w = OperationSelectionBottom(self)
        hl = QHBoxLayout()
        hl.setContentsMargins(0, 0, 10, 10)
        hl.addStretch(1)
        hl.addWidget(OperationSelectionOk(self))
        hl.addWidget(OperationSelectionClose(self))
        hl.setSpacing(10)
        bottom_w.setLayout(hl)
        vl.addWidget(bottom_w)

    # window drag
    def mousePressEvent(self, event):        
        if (event.button() == Qt.LeftButton):
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 윈도우 position 변경
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))
        print(self.widget_name, self.geometry())

    def initiation(self):
        self.op_tree.initiation()

class OperationSelectionTitle_BG(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        layout = QHBoxLayout(self)
        layout.addWidget(OperationSelectionTitle(self))
        layout.setContentsMargins(5, 5, 5, 5)
        layout.addStretch(1)
        self.setFixedHeight(35)

class OperationSelectionTitle(ABCLabel):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setText('Operation Selection')
        self.setFixedSize(240, 25)

class OperationSelectionBottom(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)

class OperationSelectionTree(ABCTreeWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setContentsMargins(0, 0, 0, 0)
        self.setHeaderHidden(True)
        self.setColumnCount(1)
        self.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.setFocusPolicy(Qt.NoFocus)
        self.selected_operation_mode = ''
        self.procedure_names = {} # 
        self.procedure_nubs = {} #
        self.procedure_buts = []

        # make tree -----------------------------------------------------------------------------------------------
        # top
        self.btn_x_group = QButtonGroup()
        top_btn_list = [OperationSelectionTreeItem(self, in_text=_, top_item=True, fixwidth=200) for _ in ['Normal', 'Abnormal', 'Emergency']]
        [self.btn_x_group.addButton(btn_) for btn_ in top_btn_list]
        
        self.btn_xx_group = QButtonGroup()
        for i, btn_x in enumerate(self.btn_x_group.buttons()):
            item_top = QTreeWidgetItem()
            self.addTopLevelItem(item_top)
            self.setItemWidget(item_top, 0, btn_x)
            op_mode = {
                0: ['Refueling', 'Cold Shutdown', 'Hot Shutdown', 'Hot Standby', 'Startup', 'Power Operation'],
                1: ['Ab01', 'Ab02', 'Ab03', 'Ab04','Ab06'],
                2: ['LOCA', 'SGTR', 'MSLB', 'SBO', 'LOAF'],
            }
            btn_list = [OperationSelectionTreeItem(self, in_text=_, fixwidth=175) for _ in op_mode[i]]
            self.procedure_buts.append(btn_list)
            
            for btn_xx in btn_list:
                item = QTreeWidgetItem(item_top)
                self.addTopLevelItem(item)
                self.setItemWidget(item, 0, btn_xx)
                # 
                self.procedure_names[len(self.procedure_names)] = btn_xx.in_text
                self.procedure_nubs[btn_xx.in_text] = len(self.procedure_nubs)
                #
                self.btn_xx_group.addButton(btn_xx)
        self.initiation()

    def initiation(self):
        # 초기 상태 업데이트        
        for btn_group, top_btn in zip(self.procedure_buts, self.btn_x_group.buttons()):
            for btn in btn_group:
                if btn.in_text == self.transform_nub_to_procedure_name(self.inmem.ShMem.get_para_val('iFixOpMode')):
                    self.selected_operation_mode = btn.in_text
                    btn.setChecked(True)
                    top_btn.setChecked(True)

    def transform_nub_to_procedure_name(self, nub):
        return self.procedure_names[nub]
    
    def transform_name_to_procedure_nub(self, name):
        return self.procedure_nubs[name]

    def get_operation_mode_nub(self):
        return self.transform_name_to_procedure_nub(self.selected_operation_mode)

    def btn_changed(self):
        for btn_group, top_btn in zip(self.procedure_buts, self.btn_x_group.buttons()):
            for btn in btn_group:
                if btn.in_text == self.selected_operation_mode:
                    top_btn.setChecked(True)
                
class OperationSelectionTreeItem(ABCPushButton):
    def __init__(self, parent, widget_name='', in_text='', top_item=False, fixwidth=0):
        super().__init__(parent, widget_name)
        self.in_text = in_text
        self.top_item = top_item
        self.setText(in_text)
        self.setCheckable(True)
        self.setChecked(False)
        self.setFixedSize(fixwidth, 35)
    
    def mousePressEvent(self, e: QMouseEvent) -> None:
        if not self.top_item:
            self.inmem.widget_ids['OperationSelectionTree'].selected_operation_mode = self.in_text
            self.inmem.widget_ids['OperationSelectionTree'].btn_changed()
            super().mousePressEvent(e)

class OperationSelectionOk(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setFixedSize(80, 25)
        self.setText('확인')
    
    def mousePressEvent(self, e: QMouseEvent) -> None:
        self.inmem.ShMem.change_para_val('iFixOpMode', self.inmem.widget_ids['OperationSelectionTree'].get_operation_mode_nub())
        self.inmem.widget_ids['MainLeftTop2OperationSelectionBtn'].setText(self.inmem.widget_ids['OperationSelectionTree'].selected_operation_mode)
        self.inmem.widget_ids['OperationSelectionWindow'].close()
        return super().mousePressEvent(e)

class OperationSelectionClose(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setFixedSize(80, 25)
        self.setText('닫기')
    
    def mousePressEvent(self, e: QMouseEvent) -> None:
        self.inmem.widget_ids['OperationSelectionWindow'].close()
        return super().mousePressEvent(e)