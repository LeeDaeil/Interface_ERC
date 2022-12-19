from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Function_Mem_ShMem import *
from TOOL_CSF import *
from TOOL_PTCurve import *
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
                self.Inmem.widget_ids['MainLeftTop2OperationSelectionBtn'].update_text()

        if self.ShMem.get_para_val('iFixOpMode') == 14: # Abnormal - AB 23-01
            if self.ShMem.get_para_val("KCNTOMS") == 170: self.add_des('Charging Valve Open', show_total_his=False)
            if self.ShMem.get_para_val("KCNTOMS") == 170: self.add_des('Charging Pump 2 Start', show_total_his=False)
            if self.ShMem.get_para_val("KCNTOMS") == 525:
                self.add_des('Reactor trip', show_total_his=False)
                self.add_des('Operation Strategy : Auto Control ES', show_control_his=False)
                self.add_des('Operation Condition : Abnormal -> Emergency', show_control_his=False)
                self.ShMem.change_para_val('iFixOpMode', 15)
                self.ShMem.change_para_val('iOpStrategy', 19) # Auto Control ES
                self.ShMem.change_para_val('iOpHistory', 2)  # Emergency
                self.ShMem.change_para_val('iDigBLK', 0)
                self.Inmem.widget_ids['MainLeftTop2OperationSelectionBtn'].update_text()

        if self.ShMem.get_para_val('iFixOpMode') == 15: # Emergency LOCA
            # CSF Tree
            trip = self.ShMem.get_para_val("KLAMPO9")
            p_range = self.ShMem.get_para_val("ZINST1")
            i_range = self.ShMem.get_para_val("ZINST2")
            s_range = self.ShMem.get_para_val("ZINST3")
            CoreExitTemp = self.ShMem.get_para_val("UUPPPL")
            PTcurve = PTCureve().Check(self.ShMem.get_para_val("UAVLEG2"), self.ShMem.get_para_val("ZINST65"))

            SG1Nar = self.ShMem.get_para_val('ZINST78') 
            SG2Nar = self.ShMem.get_para_val('ZINST77')
            SG3Nar = self.ShMem.get_para_val('ZINST76')
            SG1Pres = self.ShMem.get_para_val('ZINST75')
            SG2Pres =  self.ShMem.get_para_val('ZINST74')
            SG3Pres = self.ShMem.get_para_val('ZINST73')
            SG1Feed = self.ShMem.get_para_val('WFWLN1')
            SG2Feed = self.ShMem.get_para_val('WFWLN2')
            SG3Feed = self.ShMem.get_para_val('WFWLN3')
            AllSGFeed = self.ShMem.get_para_val('WFWLN1') + self.ShMem.get_para_val('WFWLN2') + self.ShMem.get_para_val('WFWLN3')

            SG1Wid = self.ShMem.get_para_val('ZINST72') 
            SG2Wid = self.ShMem.get_para_val('ZINST71')
            SG3Wid = self.ShMem.get_para_val('ZINST70')
            SG123Wid = [self.ShMem.get_para_val('ZINST72'), self.ShMem.get_para_val('ZINST71'), self.ShMem.get_para_val('ZINST70')]

            # CSF 4 Value RCS 건전성 상태 추적도
            RCSColdLoop1 = self.ShMem.get_para_val('UCOLEG1') 
            RCSColdLoop2 = self.ShMem.get_para_val('UCOLEG2')
            RCSColdLoop3 = self.ShMem.get_para_val('UCOLEG3') 
            RCSPressure = self.ShMem.get_para_val('ZINST65')
            CNSTimeL = self.ShMem.get_para_val('KCNTOMS')  # PTCurve: ...
            # CSF 5 Value 격납용기 건전성 상태 추적도
            CTMTPressre = self.ShMem.get_para_val('ZINST26')
            CTMTSumpLevel = self.ShMem.get_para_val('ZSUMP')
            CTMTRad = self.ShMem.get_para_val('ZINST22')
            # CSF 6 Value RCS 재고량 상태 추적도
            PZRLevel = self.ShMem.get_para_val('ZINST63')

            self.ShMem.change_para_val('iCSFReactivity', CSFTree.CSF1(trip, p_range, i_range, s_range)['L'])
            self.ShMem.change_para_val('iCSFCoreHeat',   CSFTree.CSF2(trip, CoreExitTemp, PTcurve)['L'])
            self.ShMem.change_para_val('iCSFRCSHeat',    CSFTree.CSF3(trip, SG1Nar, SG2Nar, SG3Nar, SG1Pres, SG2Pres, SG3Pres, SG1Feed, SG2Feed, SG3Feed)['L'])
            # self.ShMem.change_para_val('iCSFRCSPres',    CSFTree.CSF4(trip, RCSColdLoop1, RCSColdLoop2, RCSColdLoop3, RCSPressure, PTcurve, CNSTimeL)['L'])
            self.ShMem.change_para_val('iCSFCTMT',       CSFTree.CSF5(trip, CTMTPressre, CTMTSumpLevel, CTMTRad)['L'])
            self.ShMem.change_para_val('iCSFRCSInvt',    CSFTree.CSF6(trip, PZRLevel)['L'])
            # ==============================================================================================
            if self.ShMem.get_para_val("KCNTOMS") == 590: self.add_des('SI Valve Open', show_total_his=False)
            if self.ShMem.get_para_val("KCNTOMS") == 590: self.add_des('Containment ISO', show_total_his=False)
            if self.ShMem.get_para_val("KCNTOMS") == 590: self.add_des('Feedwater ISO', show_total_his=False)
            if self.ShMem.get_para_val("KCNTOMS") == 590: self.add_des('Aux feed pump 1 start', show_total_his=False)
            if self.ShMem.get_para_val("KCNTOMS") == 590: self.add_des('Aux feed pump 2 start', show_total_his=False)
            if self.ShMem.get_para_val("KCNTOMS") == 595: self.add_des('Charging pump 3 start', show_total_his=False)
            if self.ShMem.get_para_val("KCNTOMS") == 700: self.add_des('Aux feed pump 3 start', show_total_his=False)
            if self.ShMem.get_para_val("KCNTOMS") == 900: self.add_des('Main steam line ISO', show_total_his=False)
            if self.ShMem.get_para_val("KCNTOMS") == 900: self.add_des('RCP 1 stop', show_total_his=False)
            if self.ShMem.get_para_val("KCNTOMS") == 900: self.add_des('RCP 2 stop', show_total_his=False)
            if self.ShMem.get_para_val("KCNTOMS") == 900: self.add_des('RCP 3 stop', show_total_his=False)

        # Call Update

        self.Inmem.widget_ids['MainLeftTop1ReactorPower'].call_update()
        self.Inmem.widget_ids['MainLeftTop1Electric'].call_update()
        self.Inmem.widget_ids['MainLeftTop2OperationControllerBtnM'].call_update()
        self.Inmem.widget_ids['MainLeftTop2OperationControllerBtnA'].call_update()
        self.Inmem.widget_ids['MainLeftTop3PreTrip'].call_update()
        self.Inmem.widget_ids['MainLeftTop3Signal'].call_update()
        self.Inmem.widget_ids['MainLeftTop3CSF'].call_update()
        self.Inmem.widget_ids['MainLeftTop3Diagnosis'].call_update()
        self.Inmem.widget_ids['MainMiddleMimicScene'].call_update()
        self.Inmem.widget_ids['MainRightTop1'].call_update()
        self.Inmem.widget_ids['ControlWindow'].call_update()
        if self.ShMem.get_para_val('iFixOpMode') == 4:
            self.Inmem.widget_ids['ControlTrendStartUpPowerWidget'].call_update()
            self.Inmem.widget_ids['ControlTrendStartUpTemperatureWidget'].call_update()
        if self.ShMem.get_para_val('iFixOpMode') == 14 or self.ShMem.get_para_val('iFixOpMode') == 15:
            self.Inmem.widget_ids['ControlTrendEmergencyGPWidget'].call_update()

        self.Inmem.widget_ids['OperationStrategyBoardScene'].call_update()
        self.Inmem.widget_ids['MainTopBarTimer'].call_update()

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
