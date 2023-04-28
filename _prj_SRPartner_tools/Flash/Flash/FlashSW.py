from ast import Global
import os
import subprocess
import hashlib
import re
import shutil
import getpass
import win32com.client
from threading import Thread
import time
# from pywinauto.application import Application
import datetime
import telnetlib
from lib import lib
# from DGui import Ui_CLARAToolChain

# os.chdir(os.path.dirname(__file__))
# import snippet 
telnet = telnetlib.Telnet()
host = '192.168.2.1'
telnetPort = '23'
login = 'root'
passwd = 'clarax'
claraPort = '4242' 
def waitcmd( strmark, to = 10):
    if strmark.encode('ascii') in telnet.read_until(strmark.encode('ascii'), timeout=to):
        return strmark
    return ''

def sendcmd( cmd):
    telnet.write(cmd.encode('ascii') + b"\r")

def writeLog( type, message ):
    x = datetime.datetime.now()
    if type == '':
        type = 'Info'
    logFile = open("Flash/log/DataLog.log", 'a')
    logContent = '[{0}-{1}-{2}][{3}:{4}:{5}]-[{6}]: {7}'.format(x.day, x.month, x.year, x.hour, x.minute, x.second, str(type), str(message))
    logFile.write(logContent)
    logFile.write("\n")
    logFile.close()

def write(str):
    print('## ' + str + ' ##\n', flush=True)


def terAll():
    lib.terCanape()
    usename = os.getlogin()
    if usename.lower != 'gnh7hc':
        lib.terCANalyzer()

def hashfile(path):
    BUF_SIZE = 65536  # lets read stuff in 64kb chunks!
    md5 = hashlib.md5()

    with open(path, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            md5.update(data)
    return md5.hexdigest()

def findfolder(pattern, path):
    result = {'path': '', 'name': ''}
    for root, dirs, files in os.walk(path):
        for name in dirs:
            if lib.Search_f(name, pattern):
                result['path'] = os.path.join(root, name).replace('\\', '/')
                result['name'] = name
                return result
    return result

def findfile(pattern, path, extension=''):
    result = {'path': '', 'name': ''}
    for root, dirs, files in os.walk(path):
        for name in files:
            if extension != '':
                if name.endswith(extension) == False:
                    continue
            if lib.Search_f(name, pattern):
                result['path'] = os.path.join(root, name).replace('\\', '/')
                result['name'] = name
                break
    return result

def copy_UUT_DemEvent(radar_type, prj_folder_name, locsw_path):

    if radar_type == 'Front' or (radar_type == 'Corner' and not os.path.exists
            (r"X:\claraVR\{0}\{0}_FL".format(prj_folder_name))):
        writeLog('Info','Copy UUT....')
        uutFolder = findfolder(prj_folder_name, r"X:\claraVR")['path']
        uutFolder = findfolder('uut', uutFolder)['path']
        Folder = findfolder('measurement', locsw_path)['path']
        File = findfile('Radar*', Folder, 'a2l')
        oldFile = findfile('Radar*', uutFolder, 'a2l')
        if File['name'] != '':
            if oldFile['name'] != File['name'] or hashfile(File['path']) != hashfile(oldFile['path']):
                writeLog('Info','\tCopy: ' + File['name'])
                shutil.copyfile(File['path'], os.path.join(uutFolder, File['name']))
            else:
                writeLog('Info','\tDone. ' + File['name'] + ' is already existing')
        else:
            writeLog('Warning','\tCan not find a2L. Please check!')
        Folder = findfolder('Failure_Doc', locsw_path)['path']
        File = findfile('Dem_Cfg_EventId', Folder, 'h')
        shutil.copyfile(File['path'], os.path.join(uutFolder, File['name']))
        writeLog('Info','\tCopy: ' + File['name'])

    else:
        writeLog('Info','Copy UUT....')

        for radar in ['_FL', '_FR', '_RL', '_RR']:
            uutFolder = findfolder(prj_folder_name, r"X:\claraVR")['path']
            uutFolder = findfolder(prj_folder_name + radar, uutFolder)['path']
            uutFolder = findfolder('uut', uutFolder)['path']
            Folder = findfolder('measurement', locsw_path)['path']
            File = findfile('Radar*', Folder, 'a2l')
            oldFile = findfile('Radar*', uutFolder, 'a2l')
            if File['name'] != '':
                if oldFile['name'] != File['name'] or hashfile(File['path']) != hashfile(oldFile['path']):
                    writeLog('Info','\tCopy: ' + File['name'])
                    shutil.copyfile(File['path'], os.path.join(uutFolder, File['name']))
                else:
                    writeLog('Info','\tDone. ' + File['name'] + ' is already existing')
            else:
                writeLog('Info','\tCan not find a2L. Please check!')
            Folder = findfolder('Failure_Doc', locsw_path)['path']
            File = findfile('Dem_Cfg_EventId', Folder, 'h')
            shutil.copyfile(File['path'], os.path.join(uutFolder, File['name']))
            writeLog('Info','\tCopy: ' + File['name'])


def openCanalyzer(CANalyzer_path):
    writeLog('Info','Start CANalyzer')
    path = CANalyzer_path
    try:
        write('Open CANalyzer: ' + path)
        canalyzerApp = win32com.client.Dispatch('CANalyzer.Application')
        canalyzerApp.Open(path, True, True)
        canalyzerApp.Measurement.Start() 
    except:
        writeLog('Info','Faied to open CANalyzer: ' + path)
        pass


def trigger_restbus(radar_type, prj_folder_name):
    try:
        telnet.close()
    except:
        pass
    telnet.open(host, telnetPort, timeout=4)
    
    line = waitcmd('login: ')
    if ("login: " not in line):
        telnet.close()
        # return setStatus([-1, 'Login'])
    sendcmd(login)

    line = waitcmd('Password: ') 
    if ("Password: " not in line):
        telnet.close()
        # return setStatus([-1, 'Password'])
    sendcmd(passwd)
    sendcmd('killall -s SIGINT -w clara')
    time.sleep(3)
    sendcmd('cd /usr/claraVR/{}'.format(prj_folder_name))
    if radar_type == 'Front':
        sendcmd(r'DISPLAY=:0 ./clara')
    elif radar_type == 'Front' and 'FRRR' in prj_folder_name:
        sendcmd(r'DISPLAY=:0 ./claraRR')
    else:
        sendcmd(r'DISPLAY=:0 ./claraRR')
    line = waitcmd('$$ claraX started $$',3)
    if '$$ claraX started $$' not in str(line) :
        sendcmd('su clara')
        sendcmd('DISPLAY=":0.0" setsid ' + '/usr/claraVR/{}/clara'.format(prj_folder_name))
        line1 = waitcmd('$$ claraX started $$',3)


def close_restbus(radar_type, prj_folder_name):
    try:
        telnet.close()
    except:
        pass
    telnet.open(host, telnetPort, timeout=4)
    
    line = waitcmd('login: ')
    if ("login: " not in line):
        telnet.close()
        # return setStatus([-1, 'Login'])
    sendcmd(login)

    line = waitcmd('Password: ') 
    if ("Password: " not in line):
        telnet.close()
        # return setStatus([-1, 'Password'])
    sendcmd(passwd)

    if radar_type == 'Front':
        sendcmd('killall -s SIGINT -w clara')
    ## with project have front and back radar, or corner
    sendcmd('killall -s SIGINT -w claraRR')
    telnet.close()


def process_exists(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    # use buildin check_output right away
    output = subprocess.check_output(call).decode()
    # check in last line for process name
    last_line = output.strip().split('\r\n')[-1]
    # because Fail message could be translated
    return last_line.lower().startswith(process_name.lower())


def searchError():
    timeout = 10 * 60  # s
    count = 0
    while count < timeout:
        WinTitle = "Error"
        WinTitle2 = "Vector CANape"
        try:
            appPath = r"canape32.exe"
            app = Application().connect(path=appPath)
            app[WinTitle2].send_keystrokes("{ENTER}")
            app[WinTitle].set_focus()
            app[WinTitle].send_keystrokes("{ENTER}")
            write('##close Error success')
        except:
            pass
        if not process_exists('canape32.exe'):
            break
        time.sleep(1)
        count = count + 1


def callScript(canape_path, scriptPath):
    path, filename = os.path.split(scriptPath)
    writeLog('Info','Call flash: ' + filename)
    curdir = os.getcwd()
    CMD = '\"' + canape_path + '\" -q -a -b \"' + filename + '\"'
    os.chdir(path)
    
    os.system('cmd /c \"' + CMD + '\"')
    # print('belloooooooooooooooooo')

    os.chdir(curdir)

def replace_f(strInput, Pattern, strRplace):
    if re.search(Pattern, strInput, re.IGNORECASE) != None:
        return re.sub(Pattern, strRplace, re.search(Pattern, strInput, re.IGNORECASE).group(), re.IGNORECASE)

def getFlashCounter(tNumFlashFile, ObjResult):
    flash_path      = r"D:\Flash_Database_CT\00_FLASH_Canape"
    path = flash_path
    path = os.path.join(path, 'FSI_Report1')
    f = open(path, "w")
    f.writelines(r'')
    f.close()
    ret = '0'
    tempRet = '0'
    pattern = 'count.*?\|\d+'

    # Get each test case
    while tNumFlashFile > int(ret):
        tFlagDone1Element = False
        f = open(path, "r")
        data = f.read()
        time.sleep(0.5)
        # print('ret: %s'%ret )
        # print('tempRet: %s'%tempRet )
        for tmatch in re.findall(pattern, data, re.IGNORECASE):
            ret = replace_f(tmatch, 'count.*?\|(\d+)', r'\1')
            
            if ret != tempRet:
                tempRet = ret
                tFlagDone1Element = True
                print('emiiittttttttt   ----> %s\n'%ret)
        ObjResult.emit(int(ret), tNumFlashFile, tFlagDone1Element)


def getFlashResult(flash_path):
    path = flash_path
    path = os.path.join(path, 'FSI_Report')
    f = open(path, "r")
    data = f.read()
    ret = '1'
    pattern = 'result.*?\|\d+'
    # Get each test case
    for tmatch in re.findall(pattern, data, re.IGNORECASE):
        ret = replace_f(tmatch, 'result.*?\|(\d+)', r'\1')
        break
    if ret != '0':
        return "Error"
    else:
        return "Done"



def writeFlash(flash_path, hexfiles):

    t_flashPath = os.path.join(flash_path, "FSI_Flash.cns")
    # Write FSI_Flash.cns
    f = open(t_flashPath, "w")
    f.writelines('Stop();\n')
    f.writelines('sleep(5000);\n\n')
    f.writelines(
        '//Get current_device;\nchar DeviceName[256];\nint index;\nGetDevice(0x00000100, index, DeviceName);\nSetCurrentDevice(DeviceName);')
    f.writelines('\n//Flash File\n')
    f.writelines('int result = 0;\n')
    f.writelines('int count = 0;\n')
    f.writelines('ClearWriteWindow();\n')
    f.writelines('char fileName1[] = "./FSI_Report1";\n')
    f.writelines('long hFile1;\n')
    for item in hexfiles:
        name = os.path.split(item)[1]
        f.writelines('if(result == 0){\n')
        f.writelines('\tWrite(\"----------FLASH: ' + name + ' ------------\");\n')
        f.writelines('\tresult = result + current_device.DownloadFile(\"' + item.replace('\\', '/') + '\");\n')
        f.writelines('\tsleep(500);\n')
        f.writelines('\tif(result == 0){\n')
        f.writelines('\t\tcount = count + 1;\n')
        f.writelines('\t}\n')
        f.writelines('\thFile1 = OpenFile(fileName1, "w");\n')
        f.writelines('\tFprint(hFile1, "count|%d", count);\n')
        f.writelines('\tCloseFile(hFile1);\n')
        f.writelines('}\n\n')
    f.writelines('Write(\"---------- FINISH ------------\");\n')
    f.writelines('char fileName[] = "./FSI_Report";\n')
    f.writelines('long hFile;\n')
    f.writelines('hFile = OpenFile(fileName, "w");\n')
    f.writelines('Fprint(hFile, "result|%d", result);\n')
    f.writelines('CloseFile(hFile);\n')

    terPath = os.path.abspath('./Flash/snippet/terCANape.bat').replace('\\', '/')
    f.writelines(r'CallExecutable("' + terPath + '");')
    f.close()
    return t_flashPath


# def ExcuseFlashSW(flash_path, hexfiles, canape_path, locsw_path, is_restbus_open, radarType, prj_folder_name):
def ExcuseFlashSW(SwInfo, hexfiles, is_restbus_open, radarType, ObjResult):
    flash_path      = r"D:\Flash_Database_CT\00_FLASH_Canape"
    canape_path     = r"C:\Program Files\Vector CANape 17\Exec64\CANape64.exe"
    locsw_path      = SwInfo['SwPath']
    prj_folder_name = SwInfo['LinuxPath'].split('\\')[-1]

    current_dir = os.getcwd()
    terAll()
    close_restbus(radarType, prj_folder_name)
    time.sleep(1)
    os.chdir(current_dir)

    # <copyUUT>
    if SwInfo['FlagCopy']:
        copy_UUT_DemEvent(radarType, prj_folder_name, locsw_path)
    time.sleep(2)

    # if not is_restbus_open:
    #     openCanalyzer(SwInfo['CANalyzerPath'])
    # else:
    # Open restbus incase no canalyzer available
    trigger_restbus(radarType, prj_folder_name)
    time.sleep(1)
    os.chdir(current_dir)

    # openCanalyzer(SwInfo['CANalyzerPath'])
    # Write Flash Script
    write('Write Flash Script')
    ret = writeFlash(flash_path, hexfiles)
    result = "Error"

    flashScript = ret
    callScript(canape_path, flashScript)
    result = getFlashResult(flash_path)
    if result == "Error":
        recoveryScript = flashScript.replace('FSI_Flash.cns', 'FSI_Recovery.cns')
        # Call recovery
        callScript(canape_path, recoveryScript)
        # Try to flash again
        callScript(canape_path, flashScript)
        result = getFlashResult(flash_path)
    if result != "Error":
        writeLog('Info','Flash Result: ' + result)
    else:
        writeLog('Error','Flash Result: ' + result)
    # return flashScript
    time.sleep(3)
    telnet.close()
    ObjResult.emit('Flash', result, True)
    # terAll()
    close_restbus(radarType, prj_folder_name)
    os.chdir(current_dir)

# a = r"D:\Flash_Database_CT\00_FLASH_Canape"
# b = [r"D:\GEN5\CHJ\FR\00_UCB_19_20_21____HSM_disable_ORIG.hex", r"D:\GEN5\CHJ\FR\01_ALL_IN_ONE_HEX_CHARLIE5_BM_V4.hex", r"D:\GEN5\CHJ\FR\BL06_V3\release\executables\Radar_C2_ASIL_B_signed.hex"]
# c = r"C:\Program Files\Vector CANape 17\Exec64\CANape64.exe"
# d = r"D:\GEN5\CHJ\FR\BL06_V3"
# e = True
# f = 'Front'
# g = '_prj_CHJ_X01_FR'

# ExcuseFlashSW(a, b, c, d, e, f, g)
## folder Flash: local D:
## Folder flash common theo variant project