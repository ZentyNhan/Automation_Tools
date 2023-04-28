from DBC import *
from GEN_XCP import *
import re
import os
import multiprocessing
from multiprocessing import Process
import threading
import concurrent.futures
import time

alv = ['RLC','ALV','ALIVECOUNT','ALIVECTR','MSGCOUNT''_COUNTER', 'MSGCNTR', 'MESSAGECOUNTER', '_COUNTER', 'MsgCounter', 'ROLLING', 'MSGCTR', 'ALIVERCTR']
crc = ['CHK','CHECKSUM','CHKSUM','CRC']
listIgnore = ['BLOCKC','SYNC_FC','ADS_SYNC_']
listIgnore.extend(alv)
listIgnore.extend(crc)
msgIgnore = ['NM', 'Diag']

def searchXCP(argurments):	
    MSG = argurments['MSG']
    SIGNAL = argurments['SIGNAL']
    XCP = argurments['XCP']

    lisIntVar = []                      
    internalVar = ''
    SignalName = ''

    if "VFC_ObjHdr" in SIGNAL:
        tstr = re.findall('VFC_ObjHdr_(\w+)', SIGNAL)[-1]
        SignalName = "_m_VFC_ObjHdr._" + tstr
        # SignalName = "VFC_OBJECT_HDR._" + tstr
    elif "VFC_LineHdr" in SIGNAL:
        tstr = re.findall('VFC_LineHdr_(\w+)', SIGNAL)[-1]
        SignalName = "_m_VFC_LineHdr._" + tstr
        # SignalName = "VFC_LINE_HEADER._" + tstr
    elif "VFC_ADAS" in SIGNAL:
        tstr = re.findall('VFC_ADAS_(\w+)', SIGNAL)[-1]
        #SignalName = tstr
        SignalName = "_m_VFC_ADAS._" + tstr
        
    elif re.match('VFC_Line(\d+)_(\w+)', SIGNAL):
        tstr = re.findall('VFC_Line(\d+)_(\w+)', SIGNAL)[0]
        line_num = str(int(tstr[0]) - 1)
        SignalName = "VFC_LineInfo._" + line_num + '_._' + tstr[1]
        # SignalName = "VFC_LINE_LISTS._" + line_num + '_._' + tstr[1]
    elif re.match('VFC_Obj(\d+)\w?_(\w+)', SIGNAL):
        tstr = re.findall('VFC_Obj(\d+)\w?_(\w+)', SIGNAL)[0]
        obj_num = str(int(tstr[0]))
        SignalName = "_m_VFC_ObjInfo._" + obj_num + '_._' + tstr[1]
        # SignalName = "VFC_OBJECTS._" + obj_num + '_._' + tstr[1]
    else:                    
        SignalName = SIGNAL

    lisIntVar = [t for t in XCP if (re.search('(netsig)?' + SignalName + '$', t, re.IGNORECASE) != None)]
    #for exception
    # if len(lisIntVar) == 0:
    #     lisIntVar = [t for t in XCP if (re.search('(netsig)?' + SignalName + "_RX", t, re.IGNORECASE) != None)]
    if len(lisIntVar) > 0:
        internalVar = lisIntVar[-1] 
    result = {}
    result['SIGNAL'] = SIGNAL
    result['MSG'] = MSG
    result['XCP'] = internalVar
    return result

def GENCOM(DBC, Channel, tPath, Variant):
    if Channel == '1':
        DictName = "SignalsDict"
    else:
        DictName = "PriSignalsDict"
        
    FileData = "import os\nimport re\n\n" + DictName + " = {}\n"+\
            "Signals = {\n" +\
            "\t'Variant' : '',\n" +\
            "\t'MSG' : '',\n" +\
            "\t'Name' : '',\n" +\
            "\t'Length' : '',\n" +\
            "\t'Min' : '',\n" +\
            "\t'Max' : '',\n" +\
            "\t'Offset' : '',\n" +\
            "\t'Factor' : '',\n" +\
            "\t'FullName' : '',\n" +\
            "\t'XCP' : '',\n" +\
            "}\n\n"

    msgK1 = ''
    #Sort MSG
    ignorelist = []
    errlist = []
    TX_MSG = []
    TX_ALV = []
    TX_CRC = []

    RX_MSG = []
    RX_ALV = []
    RX_CRC = []

    for tMSG in sorted(DBC.keys()):
        tSignals = DBC[tMSG]
        #Sort Name
        for SignalName in sorted(tSignals.keys()):
            tSignal = tSignals[SignalName]
            if tSignal['Dir'] != 'RX':# and tSignal['Node'] == 'RadarFrontCenter':
                if not any(s for s in msgIgnore if s.upper() in tSignal['MSG'].upper()):
                    if not any(s for s in listIgnore if s.upper() in tSignal['Signal'].upper()):  
                        if tSignal['MSG'] != msgK1:
                            msgK1 = tSignal['MSG']
                            FileData = FileData + '################## ' + tSignal['MSG'] + ' ##################\n' 						
                        if tSignal['XCP'] == '':
                            errlist.append(tSignal['Signal'])
                        FileData = FileData +\
                            DictName + "['" + tSignal['Signal'] + "'] = dict(Signals)\n" +\
                            DictName + "['" + tSignal['Signal'] + "'].update({\n" +\
                                "\t\t'Variant' : ['" + Variant + "'],\n" +\
                                "\t\t'MSG' : '" + tSignal['MSG'] + "',\n" +\
                                "\t\t'Name' : '" + tSignal['Signal'] + "',\n" +\
                                "\t\t'Length' : '" + tSignal['Length'] + "',\n" +\
                                "\t\t'Min' : '" + tSignal['Min'] + "',\n" +\
                                "\t\t'Max' : '" + tSignal['Max'] + "',\n" +\
                                "\t\t'Offset' : '" + tSignal['Offset'] + "',\n" +\
                                "\t\t'Factor' : '" + tSignal['Factor'] + "',\n" +\
                                "\t\t'XCP' : '" + tSignal['XCP'] + "',\n" +\
                                "\t})\n\n" 
                    else:
                        ignorelist.append(tSignal['Signal'])
                else:
                    ignorelist.append(tSignal['Signal'])
                
                #RX message
                if tSignal['MSG'] not in RX_MSG and 'DIAG' not in tSignal['MSG'].upper():
                    RX_MSG.append(tSignal['MSG'])
                if any(s for s in alv if s.upper() in tSignal['Signal'].upper()):
                    RX_ALV.append(tSignal['MSG'] + "." + tSignal['Signal'])
                if any(s for s in crc if s.upper() in tSignal['Signal'].upper()):
                    RX_CRC.append(tSignal['MSG'] + "." + tSignal['Signal'])
            else:
                #TX message
                if tSignal['MSG'] not in TX_MSG and 'DIAG' not in tSignal['MSG'].upper():
                    TX_MSG.append(tSignal['MSG'])
                if any(s for s in alv if s.upper() in tSignal['Signal'].upper()):
                    TX_ALV.append(tSignal['MSG'] + "." + tSignal['Signal'])
                if any(s for s in crc if s.upper() in tSignal['Signal'].upper()):
                    TX_CRC.append(tSignal['MSG'] + "." + tSignal['Signal'])
            
    if ignorelist != []:         
        print("########################## Ignore: ############################\n") 
        print(ignorelist)
    if errlist != []:  
        print("########################## Error: ############################\n") 
        print(errlist)

    FileData = FileData +\
        "for tSignal in " + DictName + ":\n" +\
        "\t" + DictName + "[tSignal]['FullName'] = " + DictName + "[tSignal]['MSG'] + '.' + " + DictName + "[tSignal]['Name']\n"

    FileData = FileData + "\n#TX Define:\n"
    FileData = FileData + "TX_MSG = " + str(TX_MSG) + "\n"
    FileData = FileData + "TX_ALV = " + str(TX_ALV)+ "\n"
    FileData = FileData + "TX_CRC = " + str(TX_CRC) + "\n"

    FileData = FileData + "\n#RX Define:\n"
    FileData = FileData + "RX_MSG = " + str(RX_MSG) + "\n"
    FileData = FileData + "RX_ALV = " + str(RX_ALV)+ "\n"
    FileData = FileData + "RX_CRC = " + str(RX_CRC) + "\n"

    myFile = open(tPath, "w") 
    myFile.write(FileData)
    myFile.close       

def GEN_TX_Init(DBC, tPath):
    FileData = '\tdefaultRawValue = [\n'
    msgK1 = ''
    for tMSG in sorted(DBC.keys()):
        tSignals = DBC[tMSG]
        #Sort Name        
        for SignalName in sorted(tSignals.keys()):
            tSignal = tSignals[SignalName]
            if tSignal['Dir'] == 'RX':
                if not any(s for s in msgIgnore if s.upper() in tSignal['MSG'].upper()):
                    if not any(s for s in listIgnore if s.upper() in tSignal['Signal'].upper()):
                        if tSignal['MSG'] != msgK1:
                            msgK1 = tSignal['MSG']
                            FileData = FileData + '\n\t\t################## ' + tSignal['MSG'] + ' ##################\n' 	
                        FileData = FileData + "\t\t{'signal' :'" + tSignal['MSG'] + '.' + tSignal['Signal'] + "', 'value' : 0},\n"
    FileData += '\t[\n'
    tPath = tPath.replace('.py', '_Init.py')
    myFile = open(tPath, "w") 
    myFile.write(FileData)
    myFile.close
if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))

    DBCs = [
        {'path' : r'..\Database\0ADASCAN_C589_V2.1_CC_ACC.dbc', 'node' : 'ACC', 'filePath' : '../GEN/DBCCOM_Public.py', 'channel' : '1'},
        # {'path' : '..\Database\ADASCAN_S202_ICAR_ADASCAN_20201026_FR_TGU_BL04.dbc', 'node' : 'ACC', 'filePath' : '../GEN/DBCCOM_Public2.py', 'channel' : '1'},
        # {'path' : '..\Database\CA_1R1V_privatecan_V1.6.dbc', 'node' : 'RadarFrontCenter', 'filePath' : '../GEN/DBCCOM_Private.py', 'channel' : '2'},
        # {'path' : '..\Database\S202_L2.9_PrivateCAN_20201029_V2_Bosch_FR_BL04.dbc', 'node' : 'FR', 'filePath' : '../GEN/DBCCOM_Private2.py', 'channel' : '2'}
    ]
    start_time = time.time()
    a2lPath = r"..\..\..\uut\RadarFC.a2l"
    XCPData = getAtoL(a2lPath)
    Variant = ''
    for DBC in DBCs:
        DBCData = GetDBCInfo(DBC['path'], DBC['node'])
        futures= []

        argurments = []
        for tMSG in sorted(DBCData.keys()):				
            tSignals = DBCData[tMSG]
            for tSig in tSignals:
                if tSignals[tSig]['Dir'] != 'RX':
                    if not any(s for s in msgIgnore if s.upper() in tSignals[tSig]['MSG'].upper()):
                        if not any(s for s in listIgnore if s.upper() in tSignals[tSig]['Signal'].upper()):
                            argurments.append({'MSG': tMSG, 'SIGNAL': tSig, 'XCP':XCPData})

        with multiprocessing.Pool() as pool:
            return_list = pool.map(searchXCP, argurments)

        for ret in return_list:
            DBCData[ret['MSG']][ret['SIGNAL']]['XCP'] = ret['XCP']

        GENCOM(DBCData, DBC['channel'], DBC['filePath'], Variant)
        GEN_TX_Init(DBCData, DBC['filePath'])

    end_time = time.time()
    print(f'Total time: {end_time - start_time:2f}s')

