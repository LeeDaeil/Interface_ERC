class AlarmDB:
    def __init__(self, Shmem):
        self.ShMem = Shmem
        self.alarmdb = self.init_alarm_db()

    def update_alarmdb_from_ShMem(self):
        self.alarmdb = self.update_alarm(self.ShMem.get_mem(), self.alarmdb)

    def init_alarm_db(self):
        alarm_dict = {
            'KLAMPO251': {'Val': 0, 'Em':False, 'Des': 'INTMD RANGE HI FLUX ROD STOP'},
            'KLAMPO252': {'Val': 0, 'Em':False, 'Des': 'POWER RANGE OVERPOWER ROD STOP'},
            'KLAMPO253': {'Val': 0, 'Em':False, 'Des': 'CONT BANK D FULL ROD WITHDRAWAL'},
            'KLAMPO254': {'Val': 0, 'Em':False, 'Des': 'CONT BANK LO-LO LIMIT'},
            'KLAMPO255': {'Val': 0, 'Em':False, 'Des': 'TWO OR MORE ROD AT BOTTOM'},
            'KLAMPO256': {'Val': 0, 'Em':False, 'Des': 'AXIAL POWER DISTRIBUTION LIMIT'},
            'KLAMPO257': {'Val': 0, 'Em':False, 'Des': 'CCWS OUTLET TEMP HI'},
            'KLAMPO258': {'Val': 0, 'Em':False, 'Des': 'INSTRUMENT AIR PRESS LO'},
            'KLAMPO259': {'Val': 0, 'Em':False, 'Des': 'RWST LEVEL LO-LO'},
            'KLAMPO260': {'Val': 0, 'Em':False, 'Des': 'L/D HX OUTLET FLOW LO'},
            'KLAMPO261': {'Val': 0, 'Em':False, 'Des': 'L/D HX outlet temp hi'},
            'KLAMPO262': {'Val': 0, 'Em':False, 'Des': 'RHX L/D OUTLET TEMP HI'},
            'KLAMPO263': {'Val': 0, 'Em':False, 'Des': 'VCT LEVEL LO'},
            'KLAMPO264': {'Val': 0, 'Em':False, 'Des': 'VCT PRESS LO'},
            'KLAMPO265': {'Val': 0, 'Em':False, 'Des': 'RCP SEAL INJ WTR FLOW LO'},
            'KLAMPO266': {'Val': 0, 'Em':False, 'Des': 'CHARGING FLOW CONT FLOW LO'},
            # 'KLAMPO267': {'Val': 0, 'Em':False, 'Des': ''}, # Not used
            'KLAMPO268': {'Val': 0, 'Em':False, 'Des': 'L/D HX OUTLET FLOW HI'},
            'KLAMPO269': {'Val': 0, 'Em':False, 'Des': 'PRZ PRESS LO SI'},
            'KLAMPO270': {'Val': 0, 'Em':False, 'Des': 'CTMT SPRAY ACTUATED'},
            'KLAMPO271': {'Val': 0, 'Em':False, 'Des': 'VCT LEVEL HI'},
            'KLAMPO272': {'Val': 0, 'Em':False, 'Des': 'VCT PRESS HI'},
            'KLAMPO273': {'Val': 0, 'Em':False, 'Des': 'CTMT PHASE B ISO ACTUATED'},
            'KLAMPO274': {'Val': 0, 'Em':False, 'Des': 'CHARGING FLOW CONT FLOW HI'},
            
            'KLAMPO275': {'Val': 0, 'Em':True, 'Des': 'OT△T RCT TRIP'},
            'KLAMPO276': {'Val': 0, 'Em':True, 'Des': 'OP△P RCT TRIP'},
            'KLAMPO277': {'Val': 0, 'Em':True, 'Des': 'CTMT PRESS HI SI RCT TRIP'},
            'KLAMPO278': {'Val': 0, 'Em':True, 'Des': 'MANUAL RCT TRIP'},
            'KLAMPO279': {'Val': 0, 'Em':True, 'Des': 'MANUAL SI RCT TRIP'},
            'KLAMPO280': {'Val': 0, 'Em':True, 'Des': 'PRZ HI LEVEL RCT TRIP'},
            'KLAMPO281': {'Val': 0, 'Em':True, 'Des': 'PRZ HI PRESS RCT TRIP'},
            'KLAMPO282': {'Val': 0, 'Em':True, 'Des': 'PRZ LO PRESS & P-7 RCT TRIP'},
            'KLAMPO283': {'Val': 0, 'Em':True, 'Des': 'SOURCE RANGE HI FLUX RCT TRIP'},
            'KLAMPO284': {'Val': 0, 'Em':True, 'Des': 'INTMD RANGE HI FLUX RCT TRIP'},
            'KLAMPO285': {'Val': 0, 'Em':True, 'Des': 'PWR RANGE HI FLUX HI SETPT RCT TRIP'},
            'KLAMPO286': {'Val': 0, 'Em':True, 'Des': 'PWR RANGE LO FLUX HI SETPT RCT TRIP'},
            'KLAMPO287': {'Val': 0, 'Em':True, 'Des': 'PWR RANGE HI FLUX HI RATE RCT TRIP'},
            'KLAMPO288': {'Val': 0, 'Em':True, 'Des': 'RCS FLOW LO AT HI PWR RCT TRIP'},
            'KLAMPO289': {'Val': 0, 'Em':True, 'Des': 'RCS FLOW LO AT LO PWR RCT TRIP'},
            'KLAMPO290': {'Val': 0, 'Em':True, 'Des': 'SG 1,2,3 WTR LEVEL LO-LO RCT TRIP'},
            'KLAMPO291': {'Val': 0, 'Em':True, 'Des': 'TBN TRIP & P-7 RCT TRIP'},
            'KLAMPO292': {'Val': 0, 'Em':True, 'Des': 'MSL PRESS LO SI RCT TRIP'},
            
            'KLAMPO295': {'Val': 0, 'Em':False, 'Des': 'CTMT SUMP LEVEL HI'},
            'KLAMPO296': {'Val': 0, 'Em':False, 'Des': 'CTMT SUMP LEVEL HI-HI'},
            'KLAMPO297': {'Val': 0, 'Em':False, 'Des': 'CTMT AIR TEMP HI'},
            'KLAMPO298': {'Val': 0, 'Em':False, 'Des': 'CTMT MOISTURE HI'},
            'KLAMPO301': {'Val': 0, 'Em':False, 'Des': 'RAD HI ALARM'},
            'KLAMPO302': {'Val': 0, 'Em':False, 'Des': 'CTMT PRESS HI 1 ALERT'},
            'KLAMPO303': {'Val': 0, 'Em':False, 'Des': 'CTMT PRESS HI 2 ALERT'},
            'KLAMPO304': {'Val': 0, 'Em':False, 'Des': 'CTMT PRESS HI 3 ALERT'},
            'KLAMPO305': {'Val': 0, 'Em':False, 'Des': 'ACCUM TK PRESS LO'},
            'KLAMPO306': {'Val': 0, 'Em':False, 'Des': 'ACCUM TK PRESS HI'},
            'KLAMPO307': {'Val': 0, 'Em':False, 'Des': 'PRZ PRESS HI ALERT'},
            'KLAMPO308': {'Val': 0, 'Em':False, 'Des': 'PRZ PRESS LO ALERT'},
            'KLAMPO309': {'Val': 0, 'Em':False, 'Des': 'PRZ PORV OPENING'},
            'KLAMPO310': {'Val': 0, 'Em':False, 'Des': 'PRZ CONT LEVEL HI HEATER ON'},
            'KLAMPO311': {'Val': 0, 'Em':False, 'Des': 'PRZ CONT LEVEL LO HEATER OFF'},
            'KLAMPO312': {'Val': 0, 'Em':False, 'Des': 'PRZ PRESS LO BACK-UP HEATER ON'},
            'KLAMPO313': {'Val': 0, 'Em':False, 'Des': 'Tref/AUCT Tavg DEVIATION'},
            'KLAMPO314': {'Val': 0, 'Em':False, 'Des': 'RCS 1,2,3 Tavg HI'},
            'KLAMPO315': {'Val': 0, 'Em':False, 'Des': 'RCS 1,2,3 Tavg/AUCT Tavg HI/LO'},
            'KLAMPO316': {'Val': 0, 'Em':False, 'Des': 'RCS 1,2,3 LO FLOW ALERT'},
            'KLAMPO317': {'Val': 0, 'Em':False, 'Des': 'PRT TEMP HI'},
            'KLAMPO318': {'Val': 0, 'Em':False, 'Des': 'PRT PRESS HI'},
            'KLAMPO319': {'Val': 0, 'Em':False, 'Des': 'SG 1,2,3 LEVEL LO'},
            'KLAMPO320': {'Val': 0, 'Em':False, 'Des': 'SG 1,2,3 STM/FW FLOW DEVIATION'},
            'KLAMPO321': {'Val': 0, 'Em':False, 'Des': 'RCP 1,2,3 TRIP'},
            'KLAMPO322': {'Val': 0, 'Em':False, 'Des': 'CONDENSATE STOR TK LEVEL LO'},
            'KLAMPO323': {'Val': 0, 'Em':False, 'Des': 'CONDENSATE STOR TK LEVEL LO-LO'},
            'KLAMPO324': {'Val': 0, 'Em':False, 'Des': 'CONDENSATE STOR TK LEVEL HI'},
            'KLAMPO325': {'Val': 0, 'Em':False, 'Des': 'MSIV TRIPPED'},
            'KLAMPO326': {'Val': 0, 'Em':False, 'Des': 'MSL PRESS RATE HI STEAM ISO'},
            'KLAMPO327': {'Val': 0, 'Em':False, 'Des': 'MSL 1,2,3 PRESS RATE HI'},
            'KLAMPO328': {'Val': 0, 'Em':False, 'Des': 'MSL 1,2,3 PRESS LOW'},
            'KLAMPO329': {'Val': 0, 'Em':False, 'Des': 'AFW(MD) ACTUATED'},
            'KLAMPO330': {'Val': 0, 'Em':False, 'Des': 'CONDENSER LEVEL LO'},
            'KLAMPO331': {'Val': 0, 'Em':False, 'Des': 'FW PUMP DISCHARGE HEADER PRESS HI'},
            'KLAMPO332': {'Val': 0, 'Em':False, 'Des': 'FW PUMP TRIP'},
            'KLAMPO333': {'Val': 0, 'Em':False, 'Des': 'FW temp hi'},
            'KLAMPO334': {'Val': 0, 'Em':False, 'Des': 'CONDENSATE PUMP FLOW LO'},
            'KLAMPO335': {'Val': 0, 'Em':False, 'Des': 'CONDENSER ABS PRESS HI'},
            'KLAMPO336': {'Val': 0, 'Em':False, 'Des': 'CONDENSER LEVEL HI'},
            'KLAMPO337': {'Val': 0, 'Em':False, 'Des': 'TBN TRIP P-4'},
            'KLAMPO338': {'Val': 0, 'Em':False, 'Des': 'SG 1,2,3 WTR LEVEL HI-HI TBN TRIP'},
            'KLAMPO339': {'Val': 0, 'Em':False, 'Des': 'CONDENSER VACUUM LO TBN TRIP'},
            'KLAMPO340': {'Val': 0, 'Em':False, 'Des': 'TBN OVERSPEED HI TBN TRIP'},
            'KLAMPO341': {'Val': 0, 'Em':False, 'Des': 'GEN BRK OPEN'},
            'iEmptyAlnon': {'Val': 0, 'Em':False, 'Des': ''},
            'iEmptyAlem': {'Val': 0, 'Em':True, 'Des': ''},
        }
        return alarm_dict

    def update_alarm(slef, mem, alarm_dict):
        """
                현재 파라 메터가 알람관련 변수라면 입력된 값을 Overwrite
                # -----------  Left panel : KLARML(3,II) -----------------------------------------------------------------------
                #
                #           ---------------------------------------------------
                #           | II = 1 |   9    |   17   |   25   |   33   |  41 |
                #           ---------------------------------------------------
                #           |   2    |   10   |   18   |   26   |   34   |  42|
                #           ---------------------------------------------------
                #           |   3    |   11   |   19   |   27   |   35   |  43 |
                #           ---------------------------------------------------
                #           |   4    |   12   |   20   |   28   |   36   |  44 |
                #           ---------------------------------------------------
                #           |   5    |   13   |   21   |   29   |   37   |  45 |
                #           ---------------------------------------------------
                #           |   6    |   14   |   22   |   30   |   38   |  46 |
                #           ---------------------------------------------------
                #           |   7    |   15   |   23   |   31   |   39   |  47 |
                #           ---------------------------------------------------
                #           |   8    |   16   |   24   |   32   |   40   |  48 |
                #           ---------------------------------------------------
                #
                # ==============================================================================================================
                # -----------  Right panel : KLARMR(3,IJ)
                #
                #       -----------------------------------------------------------------
                #       | IJ=1  |   7   |  13   |  18   |  21   |  26   |  32   |  38   |
                #       -----------------------------------------------------------------
                #       |   2   |   8   |  14   |  19   |  22   |  27   |  33   |  39   |
                #       -----------------------------------------------------------------
                #       |   3   |   9   |  15   |  20   |       |  28   |  34   |  40   |
                #       -----------------------------------------------------------------
                #       |   4   |   10  |  16   |       |  23   |  29   |  35   |  41   |
                #       -----------------------------------------------------------------
                #       |   5   |   11  |       |       |  24   |  30   |  36   |       |
                #       -----------------------------------------------------------------
                #       |   6   |   12  |  17   |       |  25   |  31   |  37   |  42   |
                #       -----------------------------------------------------------------
                #
                # ==============================================================================================================

                """
        #
        # Left panel
        #
        # --------- L1  Intermediate range high flux rod stop(20% of FP)
        if mem['XPIRM']['Val'] > mem['CIRFH']['Val']:
            alarm_dict['KLAMPO251']['Val'] = 1
        else:
            alarm_dict['KLAMPO251']['Val'] = 0
        # --------- L2  Power range overpower rod stop(103% of FP)
        if mem['QPROREL']['Val'] > mem['CPRFH']['Val']:
            alarm_dict['KLAMPO252']['Val'] = 1
        else:
            alarm_dict['KLAMPO252']['Val'] = 0
        # --------- L3  Control bank D full rod withdrawl(220 steps)
        if mem['KZBANK4']['Val'] > 220:
            alarm_dict['KLAMPO253']['Val'] = 1
        else:
            alarm_dict['KLAMPO253']['Val'] = 0
        # --------- L4  Control bank lo-lo limit
        # ******* Insertion limit(Reference : KNU 5&6 PLS)
        #
        if mem['UMAXDT']['Val'] == 0 or mem['CDT100']['Val'] == 0:
            RDTEMP = 0
        else:
            RDTEMP = (mem['UMAXDT']['Val'] / mem['CDT100']['Val']) * 100.0
        if RDTEMP >= 100.0: RDTEMP = 100.
        if RDTEMP <= 0.0: RDTEMP = 0.
        if True:
            CRIL = {1: 1.818, 2: 1.824, 3: 1.818, 4: 208.0,
                    5: 93.0, 6: -22.0, 7: 12.0}
            # Control A
            KRIL1 = 228
            # Control B
            KRIL2 = int(CRIL[1] * RDTEMP + CRIL[4])
            if KRIL2 >= 228: KRIL2 = 228
            # Control C
            KRIL3 = int(CRIL[2] * RDTEMP + CRIL[5])
            if KRIL3 >= 228: KRIL3 = 228
            # Control D
            if RDTEMP >= CRIL[7]:
                KRIL4 = int(CRIL[3] * RDTEMP + CRIL[6])
                if KRIL4 >= 160: KRIL4 = 160
                if KRIL4 <= 0: KRIL4 = 0
            else:
                KRIL4 = 0

            if mem['KBNKSEL']['Val'] == 1:
                KRILM = KRIL1
            elif mem['KBNKSEL']['Val'] == 2:
                KRILM = KRIL2
            elif mem['KBNKSEL']['Val'] == 3:
                KRILM = KRIL3
            elif mem['KBNKSEL']['Val'] == 4:
                KRILM = KRIL4
            else:
                KRILM = 0

            if ((mem['KZBANK1']['Val'] < KRIL1) or (mem['KZBANK2']['Val'] < KRIL2)
                    or (mem['KZBANK3']['Val'] < KRIL3) or (mem['KZBANK4']['Val'] < KRIL4)):
                alarm_dict['KLAMPO254']['Val'] = 1
            else:
                alarm_dict['KLAMPO254']['Val'] = 0
        # --------- L5  Two or more rod at bottom(ref:A-II-8 p.113 & KAERI87-39)
        IROD = 0
        for _ in range(1, 53):
            if mem[f'KZROD{_}']['Val'] < 0.0:
                IROD += 1
        if IROD > 2:
            alarm_dict['KLAMPO255']['Val'] = 1
        else:
            alarm_dict['KLAMPO255']['Val'] = 0
        # --------- L6  Axial power distribution limit(3% ~ -12%)
        if (mem['CAXOFF']['Val'] >= mem['CAXOFDL']['Val']) or \
                (mem['CAXOFF']['Val'] <= (mem['CAXOFDL']['Val'] - 0.75)):
            alarm_dict['KLAMPO256']['Val'] = 1
        else:
            alarm_dict['KLAMPO256']['Val'] = 0
        # --------- L7  CCWS outlet temp hi(49.0 deg C)
        if mem['UCCWIN']['Val'] >= mem['CUCCWH']['Val']:
            alarm_dict['KLAMPO257']['Val'] = 1
        else:
            alarm_dict['KLAMPO257']['Val'] = 0
        # --------- L8  Instrument air press lo(6.3 kg/cm2)
        if mem['PINSTA']['Val'] <= (mem['CINSTP']['Val'] - 1.5):
            alarm_dict['KLAMPO258']['Val'] = 1
        else:
            alarm_dict['KLAMPO258']['Val'] = 0
        # --------- L9  RWST level lo-lo(5%)
        if mem['ZRWST']['Val'] <= mem['CZRWSLL']['Val']:
            alarm_dict['KLAMPO259']['Val'] = 1
        else:
            alarm_dict['KLAMPO259']['Val'] = 0
        # --------- L10  L/D HX outlet flow lo(15 m3/hr)
        if mem['WNETLD']['Val'] < mem['CWLHXL']['Val']:
            alarm_dict['KLAMPO260']['Val'] = 1
        else:
            alarm_dict['KLAMPO260']['Val'] = 0
        # --------- L11  L/D HX outlet temp hi(58 deg C)
        if mem['UNRHXUT']['Val'] > mem['CULDHX']['Val']:
            alarm_dict['KLAMPO261']['Val'] = 1
        else:
            alarm_dict['KLAMPO261']['Val'] = 0
        # --------- L12  RHX L/D outlet temp hi(202 deg C)
        if mem['URHXUT']['Val'] > mem['CURHX']['Val']:
            alarm_dict['KLAMPO262']['Val'] = 1
        else:
            alarm_dict['KLAMPO262']['Val'] = 0
        # --------- L13  VCT level lo(20 %)
        if mem['ZVCT']['Val'] < mem['CZVCT2']['Val']:
            alarm_dict['KLAMPO263']['Val'] = 1
        else:
            alarm_dict['KLAMPO263']['Val'] = 0
        # --------- L14  VCT press lo(0.7 kg/cm2)
        if mem['PVCT']['Val'] < mem['CPVCTL']['Val']:
            alarm_dict['KLAMPO264']['Val'] = 1
        else:
            alarm_dict['KLAMPO264']['Val'] = 0
        # --------- L15  RCP seal inj wtr flow lo(1.4 m3/hr)
        if (mem['WRCPSI1']['Val'] < mem['CWRCPS']['Val'] or
                mem['WRCPSI2']['Val'] < mem['CWRCPS']['Val'] or
                mem['WRCPSI2']['Val'] < mem['CWRCPS']['Val']):
            alarm_dict['KLAMPO265']['Val'] = 1
        else:
            alarm_dict['KLAMPO265']['Val'] = 0
        # --------- L16  Charging flow cont flow lo(5 m3/hr)
        if mem['WCHGNO']['Val'] < mem['CWCHGL']['Val']:
            alarm_dict['KLAMPO266']['Val'] = 1
        else:
            alarm_dict['KLAMPO266']['Val'] = 0
        # --------- R17  Not used
        # alarm_dict['KLAMPO267']['Val'] = 0
        # --------- L18  L/D HX outlet flow hi (30  m3/hr)
        if mem['WNETLD']['Val'] > mem['CWLHXH']['Val']:
            alarm_dict['KLAMPO268']['Val'] = 1
        else:
            alarm_dict['KLAMPO268']['Val'] = 0
        # --------- L19  PRZ press lo SI
        CSAFEI = {1: 124.e5, 2: 40.3e5}
        if (mem['PPRZN']['Val'] < CSAFEI[1]) and (mem['KSAFEI']['Val'] == 1):
            alarm_dict['KLAMPO269']['Val'] = 1
        else:
            alarm_dict['KLAMPO269']['Val'] = 0
        # --------- L20 CTMT spray actuated
        if mem['KCTMTSP']['Val'] == 1:
            alarm_dict['KLAMPO270']['Val'] = 1
        else:
            alarm_dict['KLAMPO270']['Val'] = 0
        # --------- L21  VCT level hi(80 %)
        if mem['ZVCT']['Val'] > mem['CZVCT6']['Val']:
            alarm_dict['KLAMPO271']['Val'] = 1
        else:
            alarm_dict['KLAMPO271']['Val'] = 0
        # --------- L22 VCT press hi (4.5 kg/cm2)
        if mem['PVCT']['Val'] > mem['CPVCTH']['Val']:
            alarm_dict['KLAMPO272']['Val'] = 1
        else:
            alarm_dict['KLAMPO272']['Val'] = 0
        # --------- L23  CTMT phase B iso actuated
        if mem['KCISOB']['Val'] == 1:
            alarm_dict['KLAMPO273']['Val'] = 1
        else:
            alarm_dict['KLAMPO273']['Val'] = 0
        # --------- L24  Charging flow cont flow hi(27 m3/hr)
        if mem['WCHGNO']['Val'] > mem['CWCHGH']['Val']:
            alarm_dict['KLAMPO274']['Val'] = 1
        else:
            alarm_dict['KLAMPO274']['Val'] = 0
        # --------- L25  OT delta-T Reactor trip
        alarm_dict['KLAMPO275']['Val'] = 1 if mem['UNORDT']['Val'] > mem['UOVER']['Val'] else 0
        # --------- L26  OP delta-T Reactor trip
        alarm_dict['KLAMPO276']['Val'] = 1 if mem['UNORDT']['Val'] > mem['QOVER']['Val'] else 0
        # --------- L27  CTMT press hi SI Reactor trip
        rule1 = mem['PCTMT']['Val']*mem['PAKGCM']['Val'] > mem['QOVER']['Val']
        rule2 = mem['KSAFEI']['Val'] == 1
        alarm_dict['KLAMPO277']['Val'] = 1 if rule1 and rule2 else 0
        # --------- L28  Manual Reactor trip
        alarm_dict['KLAMPO278']['Val'] = 1 if mem['KMANRX']['Val'] == 1 else 0
        # --------- L29  Manual SI Reactor trip
        alarm_dict['KLAMPO279']['Val'] = 1 if mem['KMANSI']['Val'] == 1 else 0
        # --------- L30  PRZ hi level Reactor trip( 92% of span )
        alarm_dict['KLAMPO280']['Val'] = 0  # BLock
        # --------- L31  PRZ hi press Reactor trip( 167.72 kg/cm*2 )
        alarm_dict['KLAMPO281']['Val'] = 1 if mem['PPRZ']['Val'] > 164.E5 else 0
        # --------- L32  PRZ lo press & P-7 Reactor trip(136.78 kg/cm*2)
        alarm_dict['KLAMPO282']['Val'] = 0  # Block 1 if mem['PPRZ']['Val'] < 134.E5 else 0
        # --------- L33  Source range hi flux Reactor trip(1.0E5 cps)
        alarm_dict['KLAMPO283']['Val'] = 0  # Block 1 if mem['XPSRM']['Val'] > 5.0 else 0
        # --------- L34  Intermediate range hi flux Reactor trip(25% of FP)
        alarm_dict['KLAMPO284']['Val'] = 0  # Block 1 if mem['XPIRM']['Val'] > 2.083E-4 else 0
        # --------- L35  Pwr range hi flux hi setpt Reactor trip(109% of FP)
        alarm_dict['KLAMPO285']['Val'] = 1 if mem['QPROREL']['Val'] > 1.09 else 0
        # --------- L36  Pwr range hi flux lo setpt Reactor trip(25%of FP)
        alarm_dict['KLAMPO286']['Val'] = 0  # Block 1 if mem['QPROREL']['Val'] > 0.25 else 0
        # --------- L37  Pwr range hi flux rate Reactor trip(+/- 5%/sec)
        alarm_dict['KLAMPO287']['Val'] = 0  # Block
        # --------- L38  RCS flow lo at hi pwr Reactor trip(90% of normal flow)
        alarm_dict['KLAMPO288']['Val'] = 0  # Block
        # --------- L39  RCS flow lo at lo pwr Reactor trip(90% of normal flow)
        alarm_dict['KLAMPO289']['Val'] = 0  # Block
        # --------- L40  SG 1,2,3 wtr level lo-lo Reactor trip(17%)
        rule1 = mem['ZSGNOR1']['Val'] < 0.17
        rule2 = mem['ZSGNOR2']['Val'] < 0.17
        rule3 = mem['ZSGNOR3']['Val'] < 0.17
        alarm_dict['KLAMPO290']['Val'] = 1 if rule1 or rule2 or rule3 else 0
        # --------- L41  TBN trip & P-7 Reactor trip
        alarm_dict['KLAMPO291']['Val'] = 0 # Block
        # --------- L42  MSL press low SI Reactor trip
        rule1 = mem['PSG1']['Val'] < 40.3E5
        rule2 = mem['PSG2']['Val'] < 40.3E5
        rule3 = mem['PSG3']['Val'] < 40.3E5
        rule4 = mem['KSIBPS']['Val'] == 0
        rule5 = mem['KSAFEI']['Val'] == 1
        alarm_dict['KLAMPO292']['Val'] = 1 if (rule1 or rule2 or rule3) and rule4 and rule5 else 0

        # --------- R43  Not used
        # alarm_dict['KLAMPO293']['Val'] = 0
        # --------- R44  Not used
        # alarm_dict['KLAMPO294']['Val'] = 0
        # --------- L45  CTMT sump level hi
        CZSMPH = {1: 2.492, 2: 2.9238}
        if mem['ZSUMP']['Val'] > CZSMPH[1]:
            alarm_dict['KLAMPO295']['Val'] = 1
        else:
            alarm_dict['KLAMPO295']['Val'] = 0
        # --------- L46 CTMT sump level hi-hi
        if mem['ZSUMP']['Val'] > CZSMPH[2]:
            alarm_dict['KLAMPO296']['Val'] = 1
        else:
            alarm_dict['KLAMPO296']['Val'] = 0
        # --------- L47  CTMT air temp hi(48.89 deg C)
        if mem['UCTMT']['Val'] > mem['CUCTMT']['Val']:
            alarm_dict['KLAMPO297']['Val'] = 1
        else:
            alarm_dict['KLAMPO297']['Val'] = 0
        # --------- L48  CTMT moisture hi(70% of R.H.)
        if mem['HUCTMT']['Val'] > mem['CHCTMT']['Val']:
            alarm_dict['KLAMPO298']['Val'] = 1
        else:
            alarm_dict['KLAMPO298']['Val'] = 0
        #
        # Right panel
        #
        # --------- R1  Rad hi alarm
        if (mem['DCTMT']['Val'] > mem['CRADHI']['Val']) or \
                (mem['DSECON']['Val'] >= 3.9E-3):
            alarm_dict['KLAMPO301']['Val'] = 1
        else:
            alarm_dict['KLAMPO301']['Val'] = 0
        # --------- R2  CTMT press hi 1 alert
        CPCMTH = {1: 0.3515, 2: 1.02, 3: 1.62}
        if mem['PCTMT']['Val'] * mem['PAKGCM']['Val'] > CPCMTH[1]:
            alarm_dict['KLAMPO302']['Val'] = 1
        else:
            alarm_dict['KLAMPO302']['Val'] = 0
        # --------- R3  CTMT press hi 2 alert
        if mem['PCTMT']['Val'] * mem['PAKGCM']['Val'] > CPCMTH[2]:
            alarm_dict['KLAMPO303']['Val'] = 1
        else:
            alarm_dict['KLAMPO303']['Val'] = 0
        # --------- R4  CTMT press hi 3 alert
        if mem['PCTMT']['Val'] * mem['PAKGCM']['Val'] > CPCMTH[3]:
            alarm_dict['KLAMPO304']['Val'] = 1
        else:
            alarm_dict['KLAMPO304']['Val'] = 0
        # --------- R5  Accum. Tk press lo (43.4 kg/cm2)
        if mem['PACCTK']['Val'] < mem['CPACCL']['Val']:
            alarm_dict['KLAMPO305']['Val'] = 1
        else:
            alarm_dict['KLAMPO305']['Val'] = 0
        # --------- R6  Accum. Tk press hi ( /43.4 kg/cm2)
        if mem['PACCTK']['Val'] > mem['CPACCH']['Val']:
            alarm_dict['KLAMPO306']['Val'] = 1
        else:
            alarm_dict['KLAMPO306']['Val'] = 0
        # --------- R7  PRZ press hi alert(162.4 kg/cm2)
        if mem['PPRZ']['Val'] > mem['CPPRZH']['Val']:
            alarm_dict['KLAMPO307']['Val'] = 1
        else:
            alarm_dict['KLAMPO307']['Val'] = 0
        # --------- R8  PRZ press lo alert(153.6 kg/cm2)
        if mem['PPRZ']['Val'] < mem['CPPRZL']['Val']:
            alarm_dict['KLAMPO308']['Val'] = 1
        else:
            alarm_dict['KLAMPO308']['Val'] = 0
        # --------- R9  PRZ PORV opening(164.2 kg/cm2)
        if mem['BPORV']['Val'] > 0.01:
            alarm_dict['KLAMPO309']['Val'] = 1
        else:
            alarm_dict['KLAMPO309']['Val'] = 0
        # --------- R10 PRZ cont level hi heater on(over 5%) !%deail....
        DEPRZ = mem['ZINST63']['Val'] / 100
        if (DEPRZ > (mem['ZPRZSP']['Val'] + mem['CZPRZH']['Val'])) and (
                mem['QPRZB']['Val'] > mem['CQPRZP']['Val']):
            alarm_dict['KLAMPO310']['Val'] = 1
        else:
            alarm_dict['KLAMPO310']['Val'] = 0
        # --------- R11  PRZ cont level lo heater off(17%) !%deail....
        if (DEPRZ < mem['CZPRZL']['Val']) and (mem['QPRZ']['Val'] >= mem['CQPRZP']['Val']):
            alarm_dict['KLAMPO311']['Val'] = 1
        else:
            alarm_dict['KLAMPO311']['Val'] = 0
        # --------- R12  PRZ press lo back-up heater on(153.6 kg/cm2)
        if (mem['PPRZN']['Val'] < mem['CQPRZB']['Val']) and (mem['KBHON']['Val'] == 1):
            alarm_dict['KLAMPO312']['Val'] = 1
        else:
            alarm_dict['KLAMPO312']['Val'] = 0
        # --------- R13  Tref/Auct. Tavg Deviation(1.67 deg C)
        if ((mem['UAVLEGS']['Val'] - mem['UAVLEGM']['Val']) > mem['CUTDEV']['Val']) or \
                ((mem['UAVLEGM']['Val'] - mem['UAVLEGS']['Val']) > mem['CUTDEV']['Val']):
            alarm_dict['KLAMPO313']['Val'] = 1
        else:
            alarm_dict['KLAMPO313']['Val'] = 0
        # --------- R14 RCS 1,2,3 Tavg hi(312.78 deg C)
        if mem['UAVLEGM']['Val'] > mem['CUTAVG']['Val']:
            alarm_dict['KLAMPO314']['Val'] = 1
        else:
            alarm_dict['KLAMPO314']['Val'] = 0
        # --------- R15  RCS 1,2,3 Tavg/auct Tavg hi/lo(1.1 deg C)
        RUAVMX = max(mem['UAVLEG1']['Val'], mem['UAVLEG2']['Val'],
                     mem['UAVLEG3']['Val'])
        RAVGT = {1: abs((mem['UAVLEG1']['Val']) - RUAVMX),
                 2: abs((mem['UAVLEG2']['Val']) - RUAVMX),
                 3: abs((mem['UAVLEG3']['Val']) - RUAVMX)}
        if max(RAVGT[1], RAVGT[2], RAVGT[3]) > mem['CUAUCT']['Val']:
            alarm_dict['KLAMPO315']['Val'] = 1
        else:
            alarm_dict['KLAMPO315']['Val'] = 0
        # --------- R16  RCS 1,2,3 lo flow alert(92% from KAERI87-37)
        CWSGRL = {1: 4232.0, 2: 0.0}
        if ((mem['WSGRCP1']['Val'] < CWSGRL[1] and mem['KRCP1']['Val'] == 1) or
                (mem['WSGRCP1']['Val'] < CWSGRL[1] and mem['KRCP1']['Val'] == 1) or
                (mem['WSGRCP1']['Val'] < CWSGRL[1] and mem['KRCP1']['Val'] == 1)):
            alarm_dict['KLAMPO316']['Val'] = 10
        else:
            alarm_dict['KLAMPO316']['Val'] = 900
        # --------- R17  PRT temp hi(45deg C )
        if mem['UPRT']['Val'] > mem['CUPRT']['Val']:
            alarm_dict['KLAMPO317']['Val'] = 1
        else:
            alarm_dict['KLAMPO317']['Val'] = 0
        # --------- R18  PRT  press hi( 0.6kg/cm2)
        if (mem['PPRT']['Val'] - 0.98E5) > mem['CPPRT']['Val']:
            alarm_dict['KLAMPO318']['Val'] = 1
        else:
            alarm_dict['KLAMPO318']['Val'] = 0
        # --------- R19  SG 1,2,3 level lo(25% of span)
        if (mem['ZINST78']['Val'] * 0.01 < mem['CZSGW']['Val']) \
                or (mem['ZINST77']['Val'] * 0.01 < mem['CZSGW']['Val']) \
                or (mem['ZINST76']['Val'] * 0.01 < mem['CZSGW']['Val']):
            alarm_dict['KLAMPO319']['Val'] = 1
        else:
            alarm_dict['KLAMPO319']['Val'] = 0
        # --------- R20  SG 1,2,3 stm/FW flow deviation(10% of loop flow)
        RSTFWD = {1: mem['WSTM1']['Val'] * 0.1,
                  2: mem['WSTM2']['Val'] * 0.1,
                  3: mem['WSTM3']['Val'] * 0.1}
        if (((mem['WSTM1']['Val'] - mem['WFWLN1']['Val']) > RSTFWD[1]) or
                ((mem['WSTM2']['Val'] - mem['WFWLN2']['Val']) > RSTFWD[2]) or
                ((mem['WSTM3']['Val'] - mem['WFWLN3']['Val']) > RSTFWD[3])):
            alarm_dict['KLAMPO320']['Val'] = 1
        else:
            alarm_dict['KLAMPO320']['Val'] = 0
        # --------- R21 RCP 1,2,3 trip
        if mem['KRCP1']['Val'] + mem['KRCP2']['Val'] + mem['KRCP3']['Val'] != 3:
            alarm_dict['KLAMPO321']['Val'] = 1
        else:
            alarm_dict['KLAMPO321']['Val'] = 0
        # --------- R22  Condensate stor Tk level  lo
        CZCTKL = {1: 8.55, 2: 7.57}
        if mem['ZCNDTK']['Val'] < CZCTKL[1]:
            alarm_dict['KLAMPO322']['Val'] = 1
        else:
            alarm_dict['KLAMPO322']['Val'] = 0
        # --------- R23  Condensate stor Tk level lo-lo
        if mem['ZCNDTK']['Val'] < CZCTKL[2]:
            alarm_dict['KLAMPO323']['Val'] = 1
        else:
            alarm_dict['KLAMPO323']['Val'] = 0
        # --------- R24  Condensate stor Tk level hi
        if mem['ZCNDTK']['Val'] > mem['CZCTKH']['Val']:
            alarm_dict['KLAMPO324']['Val'] = 1
        else:
            alarm_dict['KLAMPO324']['Val'] = 0
        # --------- R25  MSIV tripped
        if mem['BHV108']['Val'] == 0 or mem['BHV208']['Val'] == 0 or mem['BHV308']['Val'] == 0:
            alarm_dict['KLAMPO325']['Val'] = 1
        else:
            alarm_dict['KLAMPO325']['Val'] = 0
        # --------- R26  MSL press rate hi steam iso
        if len(mem['KLAMPO325']['List']) >= 3:
            PSGLP = {1: mem['PSG1']['List'][-2],
                     2: mem['PSG2']['List'][-2],
                     3: mem['PSG3']['List'][-2]}
            RMSLPR = {1: abs((PSGLP[1] - mem['PSG1']['List'][-1]) * 5.0),
                      2: abs((PSGLP[2] - mem['PSG2']['List'][-1]) * 5.0),
                      3: abs((PSGLP[3] - mem['PSG3']['List'][-1]) * 5.0)}

            if (((RMSLPR[1] >= mem['CMSLH']['Val']) or
                 (RMSLPR[2] >= mem['CMSLH']['Val']) or
                 (RMSLPR[3] >= mem['CMSLH']['Val'])) and (mem['KMSISO']['Val'] == 1)):
                alarm_dict['KLAMPO326']['Val'] = 1
            else:
                alarm_dict['KLAMPO326']['Val'] = 0
            # --------- RK27  MSL 1,2,3 press rate hi(-7.03 kg/cm*2/sec = 6.89E5 Pa/sec)
            if ((RMSLPR[1] >= mem['CMSLH']['Val']) or
                    (RMSLPR[2] >= mem['CMSLH']['Val']) or
                    (RMSLPR[3] >= mem['CMSLH']['Val'])):
                alarm_dict['KLAMPO327']['Val'] = 1
            else:
                alarm_dict['KLAMPO327']['Val'] = 0
        # --------- R28  MSL 1,2,3 press low(41.1 kg/cm*2 = 0.403E7 pas)
        if ((mem['PSG1']['Val'] < mem['CPSTML']['Val']) or
                (mem['PSG2']['Val'] < mem['CPSTML']['Val']) or
                (mem['PSG3']['Val'] < mem['CPSTML']['Val'])):
            alarm_dict['KLAMPO328']['Val'] = 1
        else:
            alarm_dict['KLAMPO328']['Val'] = 0
        # --------- R29  AFW(MD) actuated
        if (mem['KAFWP1']['Val'] == 1) or (mem['KAFWP3']['Val'] == 1):
            alarm_dict['KLAMPO329']['Val'] = 1
        else:
            alarm_dict['KLAMPO329']['Val'] = 0
        # --------- R30  Condenser level lo(27")
        if mem['ZCOND']['Val'] < mem['CZCNDL']['Val']:
            alarm_dict['KLAMPO330']['Val'] = 1
        else:
            alarm_dict['KLAMPO330']['Val'] = 0
        # --------- R31  FW pump discharge header press hi
        if mem['PFWPOUT']['Val'] > mem['CPFWOH']['Val']:
            alarm_dict['KLAMPO331']['Val'] = 1
        else:
            alarm_dict['KLAMPO331']['Val'] = 0
        # --------- R32  FW pump trip
        if (mem['KFWP1']['Val'] + mem['KFWP2']['Val'] + mem['KFWP3']['Val']) == 0:
            alarm_dict['KLAMPO332']['Val'] = 1
        else:
            alarm_dict['KLAMPO332']['Val'] = 0
        # --------- R33  FW temp hi(231.1 deg C)
        if mem['UFDW']['Val'] > mem['CUFWH']['Val']:
            alarm_dict['KLAMPO333']['Val'] = 1
        else:
            alarm_dict['KLAMPO333']['Val'] = 0
        # --------- R34  Condensate pump flow lo(1400 gpm=88.324 kg/s)
        if mem['WCDPO']['Val'] * 0.047 > mem['CWCDPO']['Val']:
            alarm_dict['KLAMPO334']['Val'] = 1
        else:
            alarm_dict['KLAMPO334']['Val'] = 0
        # --------- R35  Condenser abs press hi(633. mmmHg)
        if mem['PVAC']['Val'] < mem['CPVACH']['Val']:
            alarm_dict['KLAMPO335']['Val'] = 1
        else:
            alarm_dict['KLAMPO335']['Val'] = 0
        # --------- R36  Condenser level hi (45" )
        if mem['ZCOND']['Val'] > mem['CZCNDH']['Val']:
            alarm_dict['KLAMPO336']['Val'] = 1
        else:
            alarm_dict['KLAMPO336']['Val'] = 0
        # --------- R37  TBN trip P-4
        if (mem['KTBTRIP']['Val'] == 1) and (mem['KRXTRIP']['Val'] == 1):
            alarm_dict['KLAMPO337']['Val'] = 1
        else:
            alarm_dict['KLAMPO337']['Val'] = 0
        # --------- R38  SG 1,2,3 wtr level hi-hi TBN trip
        CPERMS8 = 0.78
        if (mem['ZSGNOR1']['Val'] > CPERMS8) or \
                (mem['ZSGNOR2']['Val'] > CPERMS8) or \
                (mem['ZSGNOR3']['Val'] > CPERMS8):
            alarm_dict['KLAMPO338']['Val'] = 1
        else:
            alarm_dict['KLAMPO338']['Val'] = 0
        # --------- R39 Condenser vacuum lo TBN trip
        if (mem['PVAC']['Val'] < 620.0) and (mem['KTBTRIP']['Val'] == 1):
            alarm_dict['KLAMPO339']['Val'] = 1
        else:
            alarm_dict['KLAMPO339']['Val'] = 0
        # --------- R40  TBN overspeed hi TBN trip
        if (mem['FTURB']['Val'] > 1980.0) and (mem['KTBTRIP']['Val'] == 1):
            alarm_dict['KLAMPO340']['Val'] = 1
        else:
            alarm_dict['KLAMPO340']['Val'] = 0
        # --------- R42  Gen. brk open
        if mem['KGENB']['Val'] == 0:
            alarm_dict['KLAMPO341']['Val'] = 1
        else:
            alarm_dict['KLAMPO341']['Val'] = 0

        return alarm_dict
    
    def get_on_alarms(self):
        alarms = [k if self.alarmdb[k]['Val'] == 1 else 0 for k in self.alarmdb.keys()]
        return [] if alarms is None else [i for i in alarms if i != 0]

    def get_on_alarms_des(self):
        return [self.alarmdb[k]['Des'] for k in self.get_on_alarms()]

    def get_alarm_des(self, para):
        return self.alarmdb[para]['Des']
    
    def get_alarm_para(self, type_:str):
        para_alllist = []
        para_em_list = []
        para_nonem_list = []
        
        for alarm_para in self.alarmdb.keys():
            if self.alarmdb[alarm_para]['Em']:
                para_em_list.append(alarm_para)
            else:
                para_nonem_list.append(alarm_para)
            para_alllist.append(alarm_para)
        
        if type_ == 'all':
            return para_alllist
        elif type_ == 'em':
            return para_em_list
        elif type_ == 'nonem':
            return para_nonem_list
        else:
            print('Error! in Alarm DB')