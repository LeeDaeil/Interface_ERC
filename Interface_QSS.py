# ref : https://het.as.utexas.edu/HET/Software/html/stylesheet-reference.html
# ref : https://doc.qt.io/archives/qt-4.8/stylesheet-examples.html#customizing-qgroupbox
# ref : https://wikidocs.net/book/2957
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
# Qss builder -------------------------------------------------
def builder(objecttype:str, objectname:str, contents:list):
    qss_info = f'{objecttype}#{objectname}' + '{'
    
    for content in contents:
        qss_info += f'{content};'
    
    qss_info += '}'
    
    return qss_info
def rgb_to_qCOLOR(color_code:str):
    color_code = color_code.replace('rgb(', '').replace(')', '').replace(' ', '').split(',')
    return QColor(int(color_code[0]), int(color_code[1]), int(color_code[2]))

# Color Table -------------------------------------------------
DarkGray = 'rgb(80, 80, 80)'
Gray = 'rgb(181, 181, 181)'
LightGray = 'rgb(231, 231, 234)'
LightWhite = 'rgb(255, 255, 255)'
LightBlue = 'rgb(0, 178, 216)'
DarkRed = 'rgb(192, 0, 0)'
Yellow = 'rgb(249, 249, 0)'
DarkYellow = 'rgb(255, 192, 0)'
Black = 'rgb(0, 0, 0)'
Green = 'rgb(0, 170, 0)'
Orange = 'rgb(255, 192, 0)'
# Font Table --------------------------------------------------
Content_font_size_nub = 12
Mimic_font_size_nub = 12
Title_font_size1_nub = 25
Title_font_size2_nub = 20
Title_font_size3_nub = 15
Alarm_font_size_nub = 10
Content_font_size = f'{Content_font_size_nub}pt'
Title_font_size1 = f'{Title_font_size1_nub}pt'
Title_font_size2 = f'{Title_font_size2_nub}pt'
Title_font_size3 = f'{Title_font_size3_nub}pt'
Alarm_font_size = f'{Alarm_font_size_nub}pt'
Global_font = 'Arial'
Global_font2 = '맑은 고딕'

for font_size in range(0, 5):
    # globals()['Global_font_size%d'%font_size] = f'{font_size * 3 + 12}pt'
    globals()['Global_font_size{}'.format(font_size)] = f'{font_size * 3 + 10}pt'

# Qss ---------------------------------------------------------
QssMain = ''.join(
    builder('QWidget', 'Main', [
        f'background-color: {Gray};',
        ]),
)
QssMainLeft = ''.join([
    builder('QWidget', 'MainLeft', [
        f'background-color: transparent;',
        ]),
    # ---------------------------------------------------
    builder('QWidget', 'MainLeftTop1', [
        f'background-color: {LightGray};',
        'border-radius: 5px;'
        ]),
    builder('QLabel', 'MainLeftTop1ReactorPower', [
        f'font-family: {Global_font};',
        f'font-size: {Title_font_size2};',
        "qproperty-alignment: 'AlignCenter';",
        'font-weight: bold;'
        ]),
    builder('QLabel', 'MainLeftTop1Electric', [
        f'font-family: {Global_font};',
        f'font-size: {Title_font_size2};',
        "qproperty-alignment: 'AlignCenter';",
        'font-weight: bold;'
        ]),
    # ---------------------------------------------------
    builder('QWidget', 'MainLeftTop2', [
        f'border: 2px solid {DarkGray};'
        ]),
    builder('QLabel', 'MainLeftTop2OperationSelection', [
        f'background-color: {LightGray};',
        f'font-family: {Global_font};',
        f'font-size: {Title_font_size3};',
        "qproperty-alignment: 'AlignCenter';",
        'font-weight: bold;',
        'border-radius: 5px;'
        ]),
    builder('QPushButton', 'MainLeftTop2OperationSelectionBtn', [
        f'background-color: {LightWhite};',
        f'font-family: {Global_font};',
        f'font-size: {Title_font_size3};',
        'border: none;',
        'text-align:center;',
        'font-weight: bold;'
        ]),
    builder('QPushButton', 'MainLeftTop2OperationSelectionBtn:hover', [
        f'background-color: {LightBlue};',
        ]),
    builder('QLabel', 'MainLeftTop2OperationController', [
        f'background-color: {LightGray};',
        f'font-family: {Global_font};',
        f'font-size: {Title_font_size3};',
        "qproperty-alignment: 'AlignCenter';",
        'font-weight: bold;',
        'border-radius: 5px;'
        ]),
    builder('QPushButton', 'MainLeftTop2OperationControllerBtnM', [
        f'background-color: {LightWhite};',
        f'font-family: {Global_font};',
        f'font-size: {Title_font_size3};',
        'border: none;',
        'text-align:center;',
        'font-weight: bold;',
        ]),
    builder('QPushButton', 'MainLeftTop2OperationControllerBtnM[blinking="true"]', [
        f'background-color: {Yellow};'
        ]),
    builder('QPushButton', 'MainLeftTop2OperationControllerBtnM[blinking="false"]', [
        f'background-color: {LightWhite};'
        ]),
    builder('QPushButton', 'MainLeftTop2OperationControllerBtnM:hover', [
        f'background-color: {LightBlue};',
        ]),
    builder('QPushButton', 'MainLeftTop2OperationControllerBtnM:checked', [
        f'background-color: {DarkRed};',
        ]),
    builder('QPushButton', 'MainLeftTop2OperationControllerBtnM:checked::hover', [
        f'background-color: {LightBlue};',
        ]),
    builder('QPushButton', 'MainLeftTop2OperationControllerBtnA', [
        f'background-color: {LightWhite};',
        f'font-family: {Global_font};',
        f'font-size: {Title_font_size3};',
        'border: none;',
        'text-align:center;',
        'font-weight: bold;',
        ]),
    builder('QPushButton', 'MainLeftTop2OperationControllerBtnA[blinking="true"]', [
        f'background-color: {Yellow};'
        ]),
    builder('QPushButton', 'MainLeftTop2OperationControllerBtnA[blinking="false"]', [
        f'background-color: {LightWhite};'
        ]),
    builder('QPushButton', 'MainLeftTop2OperationControllerBtnA:hover', [
        f'background-color: {LightBlue};',
        ]),
    builder('QPushButton', 'MainLeftTop2OperationControllerBtnA:checked', [
        f'background-color: {DarkRed};',
        ]),
    builder('QPushButton', 'MainLeftTop2OperationControllerBtnA:checked::hover', [
        f'background-color: {LightBlue};',
        ]),
    ## Selection part
    builder('QWidget', 'OperationSelectionWindow', [
        f'background-color:transparent;',
        'border-top-left-radius: 10px;',
        'border-top-right-radius: 10px;',
        ]),
    builder('QWidget', 'OperationSelectionBottom', [
        f'background-color: {LightGray};',
    ]),
    builder('QWidget', 'OperationSelectionTitle_BG', [
        f'background-color: {DarkGray};',
        'border-top-left-radius: 10px;',
        'border-top-right-radius: 10px;'
    ]),
    builder('QLabel', 'OperationSelectionTitle', [
        f'background-color: {LightGray};',
        f'font-family: {Global_font};',
        f'font-size: {Global_font_size2};',
        "text-align: Left;",
        'font-weight: bold;',
        'padding-left: 3px;',
        'border-radius: 10px;',
        ]),
    builder('QTreeWidget', 'OperationSelectionTree', [
        f'background-color: {LightGray};',
        f'font-family: {Global_font};',
        f'font-size: {Global_font_size2};',
        "text-align: 'AlignRight';",
        'font-weight: bold;',
        'border: none;',
        ]),
    builder('QTreeWidget', 'OperationSelectionTree:item', [
        f'background-color: {LightGray};',
        f'font-family: {Global_font};',
        f'font-size: {Global_font_size2};',
        'font-weight: bold;',
        'border: none;',
        'padding-left: 5px;',
    ]),
    builder('QPushButton', 'OperationSelectionTreeItem', [
        f'background-color: {LightWhite};',
        f'font-family: {Global_font};',
        f'font-size: {Global_font_size2};',
        'border: none;'
        "text-align:left;",
        'padding-left: 5px;',
        'margin-bottom: 5px;',
        'margin-top: 5px;',
        'font-weight: bold;',
        ]),
    builder('QPushButton', 'OperationSelectionTreeItem:checked', [
        f'background-color: {LightBlue};',
        ]),
    builder('QPushButton', 'OperationSelectionOk', [
        f'background-color: {LightWhite};',
        f'font-family: {Global_font2};',
        f'font-size: {Content_font_size};',
        'border: none;'
        'text-align: center;',
        'font-weight: bold;',
        'border-radius: 10px;'
        ]),
    builder('QPushButton', 'OperationSelectionClose', [
        f'background-color: {LightWhite};',
        f'font-family: {Global_font2};',
        f'font-size: {Content_font_size};',
        'border: none;'
        'text-align: center;',
        'font-weight: bold;',
        'border-radius: 10px;'
        ]),    
    # Pre-trip/Signal/CSFMonitoring -----------------------
    builder('QWidget', 'MainLeftTop3', [
        f'background-color: {Gray};',
        ]),
    builder('QPushButton', 'MainLeftTop3PreTrip', [
        f'background-color: {LightWhite};',
        f'font-family: {Global_font};',
        f'font-size: {Title_font_size2};',
        'border: none;',
        'text-align:center;',
        'font-weight: bold;',
        ]),
    builder('QPushButton', 'MainLeftTop3PreTrip[blinking="true"]', [
        f'background-color: {Yellow};'
        ]),
    builder('QPushButton', 'MainLeftTop3PreTrip[blinking="false"]', [
        f'background-color: {LightWhite};'
        ]),
    builder('QPushButton', 'MainLeftTop3PreTrip:hover', [
        f'background-color: {LightBlue};',
        ]),
    # MainLeftTop3Signal ----------------------------------
    builder('QPushButton', 'MainLeftTop3Signal', [
        f'background-color: {LightWhite};',
        f'font-family: {Global_font};',
        f'font-size: {Title_font_size2};',
        'border: none;',
        'text-align:center;',
        'font-weight: bold;',
        ]),
    builder('QPushButton', 'MainLeftTop3Signal[blinking="true"]', [
        f'background-color: {Yellow};'
        ]),
    builder('QPushButton', 'MainLeftTop3Signal[blinking="false"]', [
        f'background-color: {LightWhite};'
        ]),
    builder('QPushButton', 'MainLeftTop3Signal:hover', [
        f'background-color: {LightBlue};',
        ]),
    builder('QWidget', 'SignalWindow', [
        f'background-color: {LightGray};',
        'border-top-left-radius: 10px;',
        'border-top-right-radius: 10px;',
        ]),
    builder('QWidget', 'SignalTitle_BG', [
        f'background-color: {DarkGray};',
        'border-top-left-radius: 10px;',
        'border-top-right-radius: 10px;'
    ]),
    builder('QLabel', 'SignalTitle', [
        f'background-color: {LightGray};',
        f'font-family: {Global_font};',
        f'font-size: {Global_font_size2};',
        "text-align: Left;",
        'font-weight: bold;',
        'padding-left: 3px;',
        'border-radius: 10px;',
        ]),
    builder('QWidget', 'SignalBackground', [
        f'background-color: {LightGray};',
    ]),
    builder('QWidget', 'SignalResultWidget', [
        f'background-color: {LightGray};',
        f'border: 2px solid {Gray};'
        'border-radius: 10px;'
        ]),
    builder('QLabel', 'SignalResultWidgetTitle', [
        'background-color: None;',
        f'font-family: {Global_font};',
        f'font-size: {Global_font_size3};',
        "text-align: Left;",
        'font-weight: bold;',
        'padding-left: 3px;',
        'border-radius: 10px;',
        ]),
    builder('QLabel', 'SignalResultWidgetResult', [
        f'font-family: {Global_font};',
        f'font-size: {Global_font_size2};',
        "qproperty-alignment: 'AlignLeft';",
        'font-weight: bold;',
        'border: none;',
        ]),
    builder('QWidget', 'SignalResultAlarmWidget', [
        f'background-color: {LightGray};',
        f'border: 3px solid {Gray};'
        'border-radius: 10px;'
        ]),
    builder('QLabel', 'SignalResultAlarmItem', [
        f'background-color: {LightGray};',        
        f'font-family: {Global_font};',
        f'font-size: {Global_font_size1};',
        "qproperty-alignment: 'AlignCenter';",
        'font-weight: bold;',
        ]),
    builder('QLabel', 'SignalResultAlarmItem[blinking="true"]', [f'background-color: {Yellow};']),
    builder('QLabel', 'SignalResultAlarmItem[coner="TopR"]', [f'border: 1px solid {Gray};', 'border-top-right-radius: 10px;']),
    builder('QLabel', 'SignalResultAlarmItem[coner="TopL"]', [f'border: 1px solid {Gray};', 'border-top-left-radius: 10px;']),
    builder('QLabel', 'SignalResultAlarmItem[coner="BotR"]', [f'border: 1px solid {Gray};', 'border-bottom-right-radius: 10px;']),
    builder('QLabel', 'SignalResultAlarmItem[coner="BotL"]', [f'border: 1px solid {Gray};', 'border-bottom-left-radius: 10px;']),
    builder('QLabel', 'SignalResultAlarmItem[coner="In"]', [f'border: 1px solid {Gray};']),
    builder('QLabel', 'SignalResultAlarmItem[blinking="false"]', [f'background-color: {LightGray};']),
    builder('QPushButton', 'SignalResultClose', [
        f'background-color: {LightWhite};',
        f'font-family: {Global_font};',
        f'font-size: {Global_font_size1};',
        'border: none;'
        'text-align:center;',
        'font-weight: bold;',
        'border-radius: 5px;'
        ]),
    # MainLeftTop3CSF -------------------------------------
    builder('QPushButton', 'MainLeftTop3CSF', [
        f'background-color: {LightWhite};',
        f'font-family: {Global_font};',
        f'font-size: {Title_font_size2};',
        'border: none;',
        'text-align:center;',
        'font-weight: bold;',
        ]),
    builder('QPushButton', 'MainLeftTop3CSF[blinking="true"]', [f'background-color: {Yellow};']),
    builder('QPushButton', 'MainLeftTop3CSF[blinking="false"]', [f'background-color: {LightWhite};']),
    builder('QPushButton', 'MainLeftTop3CSF:hover', [f'background-color: {LightBlue};']),
    builder('QWidget', 'CSFMonitoringTitle_BG', [f'background-color: {DarkGray};', 'border-top-left-radius: 10px;', 'border-top-right-radius: 10px;']),
    builder('QLabel', 'CSFMonitoringTitle', [
        f'background-color: {LightGray};',
        f'font-family: {Global_font};',
        f'font-size: {Global_font_size2};',
        'font-weight: bold;',
        'border-radius: 10px;'
        'padding-left: 3px;',
        ]),
    builder('QWidget', 'CSFMonitoringAlarmWidget_BG', [f'background-color: {LightGray};']),
    builder('QWidget', 'CSFMonitoringAlarmWidget', [f'background-color: {LightGray};']),
    builder('QLabel', 'CSFMonitoringAlarmLabel', [
        f'background-color: {LightWhite};',
        f'font-family: {Global_font};',
        f'font-size: {Global_font_size2};',
        "qproperty-alignment: 'AlignCenter';",
        'font-weight: bold;',
        ]),
    builder('QPushButton', 'CSFMonitoringAlarmLevel1Item', [
        f'background-color: {LightGray};',
        f'font-family: {Global_font};',
        f'font-size: {Global_font_size2};',
        'font-weight: bold;',
        f'border: 1px solid {Gray};'
        ]),
    builder('QPushButton', 'CSFMonitoringAlarmLevel1Item:checked', [
        f'background-color: {Green};',
        ]),
    builder('QPushButton', 'CSFMonitoringAlarmLevel2Item', [
        f'background-color: {LightGray};',
        f'font-family: {Global_font};',
        f'font-size: {Global_font_size2};',
        'font-weight: bold;',
        f'border: 1px solid {Gray};'
        ]),
    builder('QPushButton', 'CSFMonitoringAlarmLevel2Item:checked', [
        f'background-color: {Yellow};',
        ]),
    builder('QPushButton', 'CSFMonitoringAlarmLevel3Item', [
        f'background-color: {LightGray};',
        f'font-family: {Global_font};',
        f'font-size: {Global_font_size2};',
        'font-weight: bold;',
        f'border: 1px solid {Gray};'
        ]),
    builder('QPushButton', 'CSFMonitoringAlarmLevel3Item:checked', [
        f'background-color: {Orange};',
        ]),
    builder('QPushButton', 'CSFMonitoringAlarmLevel4Item', [
        f'background-color: {LightGray};',
        f'font-family: {Global_font};',
        f'font-size: {Global_font_size2};',
        'font-weight: bold;',
        f'border: 1px solid {Gray};'
        ]),
    builder('QPushButton', 'CSFMonitoringAlarmLevel4Item:checked', [
        f'background-color: {DarkRed};',
        ]),
    builder('QPushButton', 'CSFMonitoringClose', [
        f'background-color: {LightWhite};',
        f'font-family: {Global_font};',
        f'font-size: {Content_font_size};',
        'border: none;'
        'text-align:center;',
        'font-weight: bold;',
        'border-radius: 5px;'
        ]),
    # Diagnosis ---------------------------------------------------------------------
    builder('QPushButton', 'MainLeftTop3Diagnosis', [
        f'background-color: {LightWhite};',
        f'font-family: {Global_font};',
        f'font-size: {Title_font_size2};',
        'border: none;',
        'text-align:center;',
        'font-weight: bold;',
        ]),
    builder('QPushButton', 'MainLeftTop3Diagnosis[blinking="true"]', [f'background-color: {Yellow};']),
    builder('QPushButton', 'MainLeftTop3Diagnosis[blinking="false"]', [f'background-color: {LightWhite};']),
    builder('QPushButton', 'MainLeftTop3Diagnosis:hover', [f'background-color: {LightBlue};']),
    builder('QWidget', 'DiagnosisWindow', [
        f'background-color: {LightGray};',
        'border-radius: 5px;'
        ]),
    builder('QLabel', 'DiagnosisTitle', [
        f'background-color: {DarkGray};',
        f'font-family: {Global_font};',
        f'font-size: {Global_font_size2};',
        'font-weight: bold;',
        'padding-left: 3px;',
        'border-top-left-radius: 5px;',
        'border-top-right-radius: 5px;'
        ]),
    builder('QWidget', 'DiagnosisResultWidget_BG', [f'background-color: {LightGray};']),
    builder('QWidget', 'DiagnosisResultWidget', [f'background-color: {LightGray};']),
    builder('QLabel', 'DiagnosisResultWidgetTitle', [
        f'font-family: {Global_font};',
        f'font-size: {Global_font_size2};',
        "qproperty-alignment: 'AlignLeft';",
        'font-weight: bold;',
        'border: none;',
        ]),
    builder('QLabel', 'DiagnosisResultWidgetResult', [
        f'font-family: {Global_font};',
        f'font-size: {Global_font_size2};',
        "qproperty-alignment: 'AlignLeft';",
        'font-weight: bold;',
        'border: none;',
        ]),
    builder('QWidget', 'DiagnosisResultAlarmWidget', [
        f'background-color: {LightGray};',
        f'border: 2px solid {Gray};'
        'border-radius: 5px;'
        ]),
    builder('QLabel', 'DiagnosisResultAlarmItem', [
        f'background-color: {LightGray};',        
        f'font-family: {Global_font};',
        f'font-size: {Global_font_size2};',
        "qproperty-alignment: 'AlignCenter';",
        'font-weight: bold;',
        f'border: 1px solid {Gray};'
        ]),    
    builder('QLabel', 'DiagnosisResultAlarmItem[blinking="true"]', [
        f'background-color: {Yellow};'
        ]),
    builder('QLabel', 'DiagnosisResultAlarmItem[blinking="false"]', [
        f'background-color: {LightGray};'
        ]),
    builder('QPushButton', 'DiagnosisResultClose', [
        f'background-color: {LightWhite};',
        f'font-family: {Global_font};',
        f'font-size: {Content_font_size};',
        'border: none;'
        'text-align:center;',
        'font-weight: bold;',
        'border-radius: 5px;'
        ]),
    # Alarm -----------------------------------------------
    builder('QWidget', 'MainLeftTop4_1', [
        f'background-color: {Gray};',
        ]),
    builder('QWidget', 'MainLeftTop4_2', [
        f'background-color: {Gray};',
        ]),
    builder('QLabel', 'MainLeftTop4Alarm', [
        f'background-color: {LightGray};',
        f'font-family: {Global_font};',
        f'font-size: {Alarm_font_size};',
        'border: none;',
        'font-weight: bold;',
        'text-align:center;',
        ]),
    builder('QLabel', 'MainLeftTop4Alarm[blinking="true"]', [
        f'background-color: {Yellow};'
        ]),
    builder('QLabel', 'MainLeftTop4Alarm[blinking="false"]', [
        f'background-color: {LightGray};'
        ]),
])
QssMainTop = ''.join([
    builder('QWidget', 'MainTopBar', [
        f'background-color: {DarkGray};',
        ]),
    builder('QLabel', 'MainTopBarTimer', [
        f'background-color: {LightGray};',
        f'font-family: {Global_font};',
        f'font-size: {Title_font_size1};',
        'font-weight: bold;',
        "qproperty-alignment: 'AlignCenter';",
        'border-radius: 10px;'
        ]),
    builder('QPushButton', 'MainTopBarClose', [
        f'border-image: url(Img/close.png);',
        'border-radius: 5px;'
        ]),
])
QssMainMiddle = ''.join([
    builder('QWidget', 'MainMiddle', [
        f'background-color: {Gray};',
        f'border: 3px solid {DarkGray};',
        'border-radius: 10px;',
        ]),
])
QssMainRight = ''.join([
    builder('QWidget', 'MainRight', [
        f'background-color: {Gray};',
        ]),
    # MainRightTop1 -----------------------------------------------------------------
    builder('QLabel', 'MainRightTop1Title', [
        f'background-color: {LightGray};',
        f'font-family: {Global_font};',
        f'font-size: {Title_font_size1};',
        "qproperty-alignment: 'AlignCenter';",
        'border-radius: 5px;',
        'font-weight: bold;',
        ]),
    builder('QPushButton', 'MainRightTop1Normal', [
        f'background-color: {LightGray};',
        f'font-family: {Global_font};',
        f'font-size: {Title_font_size2};',
        'border: none;',
        'text-align:center;',
        'font-weight: bold;',
        ]),
    builder('QPushButton', 'MainRightTop1Normal:checked', [
        f'background-color: {Green};',
        ]),
    builder('QPushButton', 'MainRightTop1Abnormal', [
        f'background-color: {LightGray};',
        f'font-family: {Global_font};',
        f'font-size: {Title_font_size2};',
        'border: none;',
        'text-align:center;',
        'font-weight: bold;',
        ]),
    builder('QPushButton', 'MainRightTop1Abnormal:checked', [
        f'background-color: {Yellow};',
        ]),
    builder('QPushButton', 'MainRightTop1Emergency', [
        f'background-color: {LightGray};',
        f'font-family: {Global_font};',
        f'font-size: {Title_font_size2};',
        'border: none;',
        'text-align:center;',
        'font-weight: bold;',
        ]),
    builder('QPushButton', 'MainRightTop1Emergency:checked', [
        f'background-color: {DarkRed};',
        ]),
    # MainRightTop2 -----------------------------------------------------------------
    builder('QTableWidget', 'MainRightTop2TimeTable', [
        f'background-color: {LightWhite};',
        f'font-family: {Global_font};',
        f'font-size: {Title_font_size3};',
        'font-weight: bold;',
        'border: none;',
        'border-bottom-left-radius: 10px;',
        'border-bottom-right-radius: 10px;',
        ]),
    builder('QTableWidget', 'MainRightTop2TimeTable QHeaderView::section', [
        f'background-color: {LightGray};',
        f'font-family: {Global_font};',
        f'font-size: {Title_font_size3};',
        'font-weight: bold;',
        'border: none;',
        'padding-top: 3px;',
        'padding-left: 3px;',
        ]),
    builder('QTableWidget', 'MainRightTop2TimeTable:item', [
        f'background-color: {LightWhite};',
        f'font-family: {Global_font};',
        f'font-size: {Title_font_size3};',
        'text-align: left;',
        'font-weight: bold;',
        'border: none;',
        'padding-left: 3px;',
        ]),
    # MainRightTop3 -----------------------------------------------------------------
    builder('QPushButton', 'MainRightTop3OperationStrategy', [
        f'background-color: {LightWhite};',
        f'font-family: {Global_font};',
        f'font-size: {Title_font_size2};',
        'border: none;',
        'text-align:center;',
        'font-weight: bold;',
        ]),
    builder('QLabel', 'OperationStrategyTitle', [
        f'background-color: {DarkGray};',
        f'font-family: {Global_font};',
        f'font-size: {Title_font_size2};',
        "qproperty-alignment: 'AlignLeft';",
        'font-weight: bold;',
        'padding-left: 3px;',
        'border-top-left-radius: 5px;',
        'border-top-right-radius: 5px;'
        ]),
    builder('QWidget', 'OperationStrategyBoard', [
        f'background-color: {LightGray};',
        'border: none;'
        ]),
    # OperationStrategyBoardScene -> py 파일에서 수정
    builder('QPushButton', 'OperationStrategyClose', [
        f'background-color: {LightWhite};',
        f'font-family: {Global_font};',
        f'font-size: {Content_font_size};',
        'border: none;'
        'text-align:center;',
        'font-weight: bold;',
        'border-radius: 5px;'
        ]),
    builder('QPushButton', 'MainRightTop3LCO', [
        f'background-color: {LightWhite};',
        f'font-family: {Global_font};',
        f'font-size: {Title_font_size2};',
        'border: none;',
        'text-align:center;',
        'font-weight: bold;',
        ]),
    builder('QPushButton', 'MainRightTop3ListAlarm', [
        f'background-color: {LightWhite};',
        f'font-family: {Global_font};',
        f'font-size: {Title_font_size2};',
        'border: none;',
        'text-align:center;',
        'font-weight: bold;',
        ]),
    builder('QPushButton', 'MainRightTop3Control', [
        f'background-color: {LightWhite};',
        f'font-family: {Global_font};',
        f'font-size: {Title_font_size2};',
        'border: none;',
        'text-align:center;',
        'font-weight: bold;',
        ]),
    

])
# final qss !! 
qss = ''.join(
    [QssMain, QssMainLeft, QssMainTop, QssMainMiddle, QssMainRight]
)
