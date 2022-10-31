from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Interface_ABCWidget import *
from Interface_QSS import qss


class OperationSelectionWindow(ABCWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setGeometry(0, 0, 300, 500)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 상단바 제거
        self.setStyleSheet(qss) # qss load
        self.m_flag = False

        vl = QVBoxLayout(self)
        vl.addWidget(OperationSelectionTitle(self))
        vl.addWidget(OperationSelectionTree(self))
        hl = QHBoxLayout()
        hl.addStretch(1)
        hl.addWidget(OperationSelectionOk(self))
        hl.addWidget(OperationSelectionClose(self))
        vl.addLayout(hl)

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

class OperationSelectionTitle(ABCLabel):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setText('Operation Selection')
        self.setFixedHeight(30)

class OperationSelectionTree(ABCTreeWidget):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setHeaderHidden(True)
        self.setColumnCount(1)
        self.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

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
            btn_list = [OperationSelectionTreeItem(self, in_text=_, fixwidth=150) for _ in op_mode[i]]
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
        self.setFixedWidth(fixwidth)
    
    def mousePressEvent(self, e: QMouseEvent) -> None:
        if not self.top_item:
            self.inmem.widget_ids['OperationSelectionTree'].selected_operation_mode = self.in_text
            self.inmem.widget_ids['OperationSelectionTree'].btn_changed()
            super().mousePressEvent(e)
        else:
            print('do')

class OperationSelectionOk(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setText('확인')
    
    def mousePressEvent(self, e: QMouseEvent) -> None:
        self.inmem.ShMem.change_para_val('iFixOpMode', self.inmem.widget_ids['OperationSelectionTree'].get_operation_mode_nub())
        self.inmem.widget_ids['MainLeftTop2OperationSelectionBtn'].setText(self.inmem.widget_ids['OperationSelectionTree'].selected_operation_mode)
        self.inmem.widget_ids['OperationSelectionWindow'].close()
        return super().mousePressEvent(e)

class OperationSelectionClose(ABCPushButton):
    def __init__(self, parent, widget_name=''):
        super().__init__(parent, widget_name)
        self.setText('닫기')
    
    def mousePressEvent(self, e: QMouseEvent) -> None:
        self.inmem.widget_ids['OperationSelectionWindow'].close()
        return super().mousePressEvent(e)