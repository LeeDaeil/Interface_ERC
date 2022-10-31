# ref : https://het.as.utexas.edu/HET/Software/html/stylesheet-reference.html
# ref : https://doc.qt.io/archives/qt-4.8/stylesheet-examples.html#customizing-qgroupbox
# ref : https://wikidocs.net/book/2957
# Qss builder -------------------------------------------------
def builder(objecttype:str, objectname:str, contents:list):
    qss_info = f'{objecttype}#{objectname}' + '{'
    
    for content in contents:
        qss_info += f'{content};'
    
    qss_info += '}'
    
    return qss_info

# Color Table -------------------------------------------------
DarkGray = 'rgb(78, 78, 78)'
Gray = 'rgb(181, 181, 181)'
LightGray = 'rgb(231, 231, 231)'
LightWhite = 'rgb(255, 255, 255)'
LightBlue = 'rgb(0, 178, 216)'
DarkRed = 'rgb(192, 0, 0)'
Yellow = 'rgb(249, 249, 0)'
Black = 'rgb(0, 0, 0)'
# Font Table --------------------------------------------------
Global_font = '함초롬돋움'
Global_font_size = '15pt'
Content_font_size = '12pt'
# Qss ---------------------------------------------------------
QssMain = ''.join(
    builder('QWidget', 'Main', [
        f'background-color: {Gray};',
        ]),
)
QssMainLeft = ''.join([
    builder('QWidget', 'MainLeft', [
        f'background-color: {Gray};',
        ]),
    # ---------------------------------------------------
    builder('QWidget', 'MainLeftTop1', [
        f'background-color: {LightGray};',
        'border-radius: 5px;'
        ]),
    builder('QLabel', 'MainLeftTop1ReactorPower', [
        f'font-family: {Global_font};',
        f'font-size: {Global_font_size};',
        "qproperty-alignment: 'AlignCenter';",
        'font-weight: bold;'
        ]),
    builder('QLabel', 'MainLeftTop1Electric', [
        f'font-family: {Global_font};',
        f'font-size: {Global_font_size};',
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
        f'font-size: {Global_font_size};',
        "qproperty-alignment: 'AlignCenter';",
        'font-weight: bold;',
        'border-radius: 5px;'
        ]),
    builder('QPushButton', 'MainLeftTop2OperationSelectionBtn', [
        f'background-color: {LightWhite};',
        f'font-family: {Global_font};',
        f'font-size: {Content_font_size};',
        'text-align:center;',
        'font-weight: bold;'
        ]),
    builder('QPushButton', 'MainLeftTop2OperationSelectionBtn:hover', [
        f'background-color: {LightBlue};',
        ]),
    builder('QLabel', 'MainLeftTop2OperationController', [
        f'background-color: {LightGray};',
        f'font-family: {Global_font};',
        f'font-size: {Global_font_size};',
        "qproperty-alignment: 'AlignCenter';",
        'font-weight: bold;',
        'border-radius: 5px;'
        ]),
    builder('QPushButton', 'MainLeftTop2OperationControllerBtnM', [
        f'background-color: {LightWhite};',
        f'font-family: {Global_font};',
        f'font-size: {Content_font_size};',
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
        f'font-size: {Content_font_size};',
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
    builder('QWidget', 'OperationSelectionWindow', [
        f'background-color: {LightGray};',
        'border-radius: 5px;'
        ]),
    builder('QLabel', 'OperationSelectionTitle', [
        f'background-color: {DarkGray};',
        f'font-family: {Global_font};',
        f'font-size: {Global_font_size};',
        "qproperty-alignment: 'AlignLeft';",
        'font-weight: bold;',
        'padding: 5px;',
        'border-top-left-radius: 5px;',
        'border-top-right-radius: 5px;'
        ]),
    builder('QTreeWidget', 'OperationSelectionTree', [
        f'background-color: {LightGray};',
        f'font-family: {Global_font};',
        f'font-size: {Global_font_size};',
        "text-align: 'AlignRight';",
        'font-weight: bold;',
        'border: none;',
        ]),
    builder('QTreeWidget', 'OperationSelectionTree:item', [
        f'background-color: {LightGray};',
        f'font-family: {Global_font};',
        f'font-size: {Global_font_size};',
        'font-weight: bold;',
        'border: none;',
        'padding: 8px 0px 0px 0px;', 
        ]),
    builder('QTreeWidget', 'OperationSelectionTree::branch:has-siblings:!adjoins-item', [
        f'border-image: url(Img/branch-vline.png) 0;',
        ]),
    builder('QTreeWidget', 'OperationSelectionTree::branch:has-siblings:adjoins-item', [
        f'border-image: url(Img/branch-more.png) 0;',
        ]),
    builder('QTreeWidget', 'OperationSelectionTree::branch:!has-children:!has-siblings:adjoins-item', [
        f'border-image: url(Img/branch-end.png) 0;',
        ]),
    builder('QTreeWidget', 'OperationSelectionTree::branch:has-children:!has-siblings:closed,QTreeWidget#OperationSelectionTree::branch:closed:has-children:has-siblings', [
        'border-image: none;',
        'image: url(Img/branch-closed.png);'
        ]),
    builder('QTreeWidget', 'OperationSelectionTree::branch:open:has-children:!has-siblings,QTreeWidget#OperationSelectionTree::branch:open:has-children:has-siblings', [
        'border-image: none;',
        'image: url(Img/branch-open.png);'
        ]),
    builder('QPushButton', 'OperationSelectionTreeItem', [
        f'background-color: {LightWhite};',
        f'font-family: {Global_font};',
        f'font-size: {Content_font_size};',
        'border: none;'
        'text-align:left;',
        'padding: 8px 0px 0px 0px;',
        'font-weight: bold;',
        ]),
    builder('QPushButton', 'OperationSelectionTreeItem:checked', [
        f'background-color: {LightBlue};',
        ]),
    builder('QPushButton', 'OperationSelectionOk', [
        f'background-color: {LightWhite};',
        f'font-family: {Global_font};',
        f'font-size: {Content_font_size};',
        'border: none;'
        'text-align:center;',
        'font-weight: bold;',
        'border-radius: 5px;'
        ]),
    builder('QPushButton', 'OperationSelectionClose', [
        f'background-color: {LightWhite};',
        f'font-family: {Global_font};',
        f'font-size: {Content_font_size};',
        'border: none;'
        'text-align:center;',
        'font-weight: bold;',
        'border-radius: 5px;'
        ]),    
    # Pre-trip/Signal/CSFMonitoring -----------------------
    builder('QWidget', 'MainLeftTop3', [
        f'background-color: {Gray};',
        ]),
    builder('QPushButton', 'MainLeftTop3PreTrip', [
        f'background-color: {LightWhite};',
        f'font-family: {Global_font};',
        f'font-size: {Content_font_size};',
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
    builder('QPushButton', 'MainLeftTop3Signal', [
        f'background-color: {LightWhite};',
        f'font-family: {Global_font};',
        f'font-size: {Content_font_size};',
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
    builder('QPushButton', 'MainLeftTop3CSF', [
        f'background-color: {LightWhite};',
        f'font-family: {Global_font};',
        f'font-size: {Content_font_size};',
        'border: none;',
        'text-align:center;',
        'font-weight: bold;',
        ]),
    builder('QPushButton', 'MainLeftTop3CSF[blinking="true"]', [
        f'background-color: {Yellow};'
        ]),
    builder('QPushButton', 'MainLeftTop3CSF[blinking="false"]', [
        f'background-color: {LightWhite};'
        ]),
    builder('QPushButton', 'MainLeftTop3CSF:hover', [
        f'background-color: {LightBlue};',
        ]),
    # Alarm -----------------------------------------------
    builder('QWidget', 'MainLeftTop4_1', [
        f'background-color: {Gray};',
        ]),
    builder('QWidget', 'MainLeftTop4_2', [
        f'background-color: {Gray};',
        f'border: 2px solid {DarkRed};'
        ]),
    builder('QPushButton', 'MainLeftTop4Alarm', [
        f'background-color: {LightGray};',
        f'font-family: {Global_font};',
        f'font-size: {Content_font_size};',
        'border: none;',
        'text-align:center;',
        ]),
    builder('QPushButton', 'MainLeftTop4Alarm[blinking="true"]', [
        f'background-color: {Yellow};'
        ]),
    builder('QPushButton', 'MainLeftTop4Alarm[blinking="false"]', [
        f'background-color: {LightGray};'
        ]),
])
QssMainTop = ''.join([
    builder('QWidget', 'MainTopBar', [
        f'background-color: {DarkGray};',
        'border-radius: 5px;'
        ]),
    builder('QLabel', 'MainTopBarTimer', [
        f'background-color: {LightGray};',
        f'font-family: {Global_font};',
        f'font-size: {Global_font_size};',
        "qproperty-alignment: 'AlignCenter';",
        'border-radius: 5px;'
        ]),
    builder('QPushButton', 'MainTopBarClose', [
        f'border-image: url(Img/close.png);',
        'border-radius: 5px;'
        ]),
])
# final qss !! 
qss = ''.join(
    [QssMain, QssMainLeft, QssMainTop]
)