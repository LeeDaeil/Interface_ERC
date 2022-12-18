"""

Run_Run

"""

from multiprocessing.managers import BaseManager
from multiprocessing import Process
import sys
from PyQt5.QtWidgets import *

from Function_Mem_ShMem import ShMem
from Function_SimulatorCNS import CNS
from Interface_Main import Main


class Run:
    def __init__(self):
        pass

    def make_shmem(self):
        BaseManager.register('ShMem', ShMem)
        manager = BaseManager()
        manager.start()
        mem = manager.ShMem(recode_tape='./DUMY_ALL_ROD2.csv')
        return mem

    def start_process(self):
        """ MainProcess 동작 """
        mem = self.make_shmem()
        
        mem.change_para_val('iFixOpMode', 4) # 'Startup
        
        p_list = [InterfaceRun(mem)]
        [pr_.start() for pr_ in p_list]
        [pr_.join() for pr_ in p_list]  # finished at the same time

class InterfaceRun(Process):
    def __init__(self, mem):
        super(InterfaceRun, self).__init__()
        app = QApplication(sys.argv)
        app.setStyle('Windows')
        w = Main(mem)
        w.show()
        cns = CNS(w)
        cns.show()
        sys.exit(app.exec_())
class FastRun:
    def __init__(self) -> None:
        # Start-up
        mem = ShMem(recode_tape='./DUMY_ALL_ROD2.csv')
        mem.change_para_val('iFixOpMode', 4) # 'Startup
        # Abnormal + Emergency
        mem = ShMem(recode_tape='./DUMP_AB_EM.csv')
        mem.change_para_val('iFixOpMode', 5) # 'Power Operation
        InterfaceRun(mem)

if __name__ == '__main__':
    # MainProcess = Run()
    # MainProcess.start_process()
    FastRun()
