from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Function_Mem_ShMem import *
import pandas as pd
import numpy as np


class CNS(QWidget):
    def __init__(self, w):
        super(CNS, self).__init__()
        self.ShMem: ShMem = w.inmem.ShMem
        self.Inmem: InterfaceMem = w.inmem
        self.setGeometry(50, 50, 300, 100)

        lay = QVBoxLayout(self)
        one_step_btn = QPushButton('OneStep', self)
        one_step_btn.clicked.connect(self.one_step)

        lay2 = QHBoxLayout()
        change_val_btn = QPushButton('ChangeVal', self)
        change_val_btn.clicked.connect(self.change_val)
        self.paraname = QLineEdit('para_name')
        self.paraval = QLineEdit('para_val')
        lay2.addWidget(change_val_btn)
        lay2.addWidget(self.paraname)
        lay2.addWidget(self.paraval)

        lay3 = QHBoxLayout()        
        self.tape_start = QPushButton('Start')
        self.tape_start.clicked.connect(lambda _:self.change_tape(state='Start'))
        self.tape_stop = QPushButton('Stop')
        self.tape_stop.clicked.connect(lambda _:self.change_tape(state='Stop'))
        lay3.addWidget(self.tape_start)
        lay3.addWidget(self.tape_stop)
        self.tape_state = 'Stop'
        
        self.mes = QLabel('')

        lay.addWidget(one_step_btn)
        lay.addLayout(lay2)
        lay.addLayout(lay3)
        lay.addWidget(self.mes)
        
        self.shortcut_run = QShortcut(Qt.Key.Key_F1, self, self.change_tape_auto)        

        self.startTimer(300)

    def timerEvent(self, a0: 'QTimerEvent') -> None:
        if self.tape_state == 'Start':
            self.one_step()
        return super().timerEvent(a0)

    def change_tape(self, state):
        self.tape_state = state

    def change_tape_auto(self):
        self.tape_state = 'Stop' if self.tape_state == 'Start' else 'Start'

    def one_step(self):
        # self.ShMem.change_para_val('KCNTOMS', self.ShMem.get_para_val('KCNTOMS') + 5)
        self.ShMem.one_step_tape()
        self.ShMem.add_val_to_list()
        self.ShMem.update_alarmdb()
        self.mes.setText(f'OneStep 진행함. [KCNTOMS: {self.ShMem.get_para_val("KCNTOMS")}]')
        # Start-up His =======================================================================
        if self.ShMem.get_para_val('iFixOpMode') == 4: # Start-up
            if self.ShMem.get_para_val("KCNTOMS") == 610: 
                self.add_des('Start : StartUp Operation')
                self.add_des('Operation Strategy : Auto Control RL', show_control_his=False)
                self.add_des('Withdraw Control Rods', show_total_his=False)
                self.ShMem.change_para_val('iOpStrategy', 2) # Auto control RL
            if self.ShMem.get_para_val("KCNTOMS") == 1330:
                self.add_des('Increase : Boron Concentration', show_total_his=False)
            if self.ShMem.get_para_val("KCNTOMS") == 24623:
                self.add_des('Start : Power Increase Operation')
            if self.ShMem.get_para_val("KCNTOMS") == 28835:
                self.add_des('Decrease : Boron Concentration', show_total_his=False)
            if self.ShMem.get_para_val("KCNTOMS") == 29069: self.add_des('Set-up : Turbine 1800 RPM', show_total_his=False)
            if self.ShMem.get_para_val("KCNTOMS") == 40184: self.add_des('Generate : Electric Power', show_total_his=False)
            if self.ShMem.get_para_val("KCNTOMS") == 65924: self.add_des('Run : Main FeedWater Pump #2', show_total_his=False)
            if self.ShMem.get_para_val("KCNTOMS") == 75518: self.add_des('Run : Condenser Pump #3', show_total_his=False)
            if self.ShMem.get_para_val("KCNTOMS") == 111437: self.add_des('Run : Main FeedWater Pump #3', show_total_his=False)
            if self.ShMem.get_para_val("KCNTOMS") == 144620: 
                self.add_des('Done : Power Increase Operation')
                self.change_tape_auto()
        # Abnormal + Emergency His =======================================================================
        if self.ShMem.get_para_val('iFixOpMode') == 5: # Power Operation
            if self.ShMem.get_para_val("KCNTOMS") == 170:
                self.ShMem.change_para_val('iFixOpMode', 14)
                self.ShMem.change_para_val('iOpStrategy', 9) # Auto control LSTM
                self.ShMem.change_para_val('iOpHistory', 1)  # Abnormal
                self.ShMem.change_para_val('iDABNub', 17)   # Abnormal

                self.ShMem.change_para_val('iDAB00', 0) 
                self.ShMem.change_para_val('iDAB01', 0) 
                self.ShMem.change_para_val('iDAB02', 0) 
                self.ShMem.change_para_val('iDAB03', 0) 
                self.ShMem.change_para_val('iDAB04', 0) 
                self.ShMem.change_para_val('iDAB05', 0) 
                self.ShMem.change_para_val('iDAB06', 0.1) 
                self.ShMem.change_para_val('iDAB07', 0) 
                self.ShMem.change_para_val('iDAB08', 0) 
                self.ShMem.change_para_val('iDAB09', 0) 
                self.ShMem.change_para_val('iDAB10', 0) 
                self.ShMem.change_para_val('iDAB11', 0) 
                self.ShMem.change_para_val('iDAB12', 0) 
                self.ShMem.change_para_val('iDAB13', 0) 
                self.ShMem.change_para_val('iDAB14', 0) 
                self.ShMem.change_para_val('iDAB15', 0.1) 
                self.ShMem.change_para_val('iDAB16', 0.1) 
                self.ShMem.change_para_val('iDAB17', 99.5) 
                self.ShMem.change_para_val('iDAB18', 0.1) 
                self.ShMem.change_para_val('iDAB19', 0.1) 
                self.ShMem.change_para_val('iDAB20', 0) 
                
                self.ShMem.change_para_val('iDigBLK', 1) 
                
                self.add_des('Operation Strategy : Auto Control LSTM', show_control_his=False)
                self.add_des('Operation Condition : Normal -> Abnormal', show_control_his=False)
                self.Inmem.widget_ids['OperationSelectionOk'].call_OK()
        if self.ShMem.get_para_val('iFixOpMode') == 14: # Abnormal - AB 23-01
            pass


    def add_des(self, txt, show_control_his=True, show_total_his=True):
        if show_control_his:
            self.Inmem.widget_ids['ControlHistoryTable'].add_new_item(txt)
        if show_total_his:
            self.Inmem.widget_ids['MainRightTop2TimeTable'].add_new_item('C', txt)

    def change_val(self):
        if self.ShMem.check_para_name(self.paraname.text()):
            self.mes.setText(f'{self.paraname.text()} 변수 있음.')
            if self.paraval.text().isdigit():
                self.mes.setText(f'{self.paraname.text()} 변수는 {self.paraval.text()} 로 변경됨.')
                o = int(self.paraval.text()) if self.ShMem.check_para_type(self.paraname.text()) == 0 else float(self.paraval.text())
                self.ShMem.change_para_val(self.paraname.text(), o)
            else:
                self.mes.setText(f'{self.paraval.text()} 은 숫자가 아님.')
        else:
            self.mes.setText(f'{self.paraname.text()} 변수 없음.')

        self.paraname.setText('para_name')
        self.paraval.setText('para_val')
