from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import pandas as pd
import numpy as np


class CNS(QWidget):
    def __init__(self, ShMem):
        super(CNS, self).__init__()
        self.ShMem: ShMem = ShMem
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
        
        self.startTimer(600)

    def timerEvent(self, a0: 'QTimerEvent') -> None:
        if self.tape_state == 'Start':
            self.one_step()
        return super().timerEvent(a0)

    def change_tape(self, state):
        self.tape_state = state

    def one_step(self):
        # self.ShMem.change_para_val('KCNTOMS', self.ShMem.get_para_val('KCNTOMS') + 5)
        self.ShMem.one_step_tape()
        self.ShMem.add_val_to_list()
        self.ShMem.update_alarmdb()
        self.mes.setText(f'OneStep 진행함. [KCNTOMS: {self.ShMem.get_para_val("KCNTOMS")}]')

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
