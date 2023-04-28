##chh1hc: falsh SW
##
import os
import re
from Glib import *
import shutil
import hashlib 

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

def configIP(flashPath, sensorIP):    
    canIniPath = os.path.join(flashPath, "canape.ini")
    f = open(canIniPath, "r")
    data = f.read()

    #Change IP
    regex = r'\[module.*?radar.*?\][^`]+?(?=\[)'
    for tmatch in re.findall(regex, data, re.IGNORECASE):
        ipstr = search_f(tmatch, 'HOST=(.+?)\n')
        if ipstr != '':            
            tmatchK1 = tmatch
            tmatch = tmatch.replace(ipstr, 'HOST=' + sensorIP + '\n')
            data = data.replace(tmatchK1, tmatch)
            print('Correct IP ' + sensorIP + '\n') 
            
    #Write back
    f = open(canIniPath, "w")
    f.write(data)

def writeFlash(flashPath, sw_path, FlashFolder):
    # flashPath = ''
    executeFolder = findfolder('executables', sw_path)['path']    
    executeFile = findfile('signed', executeFolder, 'hex')
    # oldHexfile = findfile('signed_S', FlashFolder, 'hex')
    # if oldHexfile['name'] != '':
    #     if hashfile(oldHexfile['path']) != hashfile(executeFile['path']):
    #         os.remove(oldHexfile['path'])
    #         shutil.copyfile(executeFile['path'], os.path.join(FlashFolder, executeFile['name']))
    # else:
    #     shutil.copyfile(executeFile['path'], os.path.join(FlashFolder, executeFile['name']))
    # flashPath = findfolder("Canape", sw_path)['path']
    if flashPath != '':
        flashPath =  os.path.join(flashPath, "FSI_Flash.cns")
        #Write FSI_Flash.cns
        f = open(flashPath, "w")       
        f.writelines('//Get current_device;\nchar DeviceName[256];\nint index;\nGetDevice(0x00000100, index, DeviceName);\nSetCurrentDevice(DeviceName);')
        f.writelines('\n//Flash File\n')
        f.writelines('int result = 0;\n')
        f.writelines('ClearWriteWindow();\n')
        nvm = ''
        for root, dirs, files in os.walk(FlashFolder):
            for name in files:            
                if name.endswith('hex') == True and 'signed' not in name.lower():
                    if 'nvm' in name.lower():
                        nvm = name
                    else:
                        f.writelines('if(result == 0){\n')                    
                        f.writelines('\tWrite(\"----------FLASH: ' + name + ' ------------\");\n')
                        f.writelines('\tresult = result + current_device.DownloadFile(\"'+ os.path.join(FlashFolder, name).replace('\\', '/') +'\");\n')
                        f.writelines('\tsleep(500);\n')
                        f.writelines('}\n\n')
        f.writelines('if(result == 0){\n')                    
        f.writelines('\tWrite(\"----------FLASH: ' + executeFile['name'] + ' ------------\");\n')
        f.writelines('\tresult = result + current_device.DownloadFile(\"'+ executeFile['path'].replace('\\', '/') +'\");\n')
        f.writelines('\tsleep(500);\n')
        f.writelines('}\n\n')
        if nvm != '':
            f.writelines('if(result == 0){\n')                    
            f.writelines('\tWrite(\"----------FLASH: ' + nvm + ' ------------\");\n')
            f.writelines('\tresult = result + current_device.DownloadFile(\"'+ os.path.join(FlashFolder, nvm).replace('\\', '/') +'\");\n')
            f.writelines('\tsleep(500);\n')
            f.writelines('}\n\n')
        f.writelines('Write(\"---------- FINISH ------------\");\n')
        f.close
    
    return flashPath

def Flash(sw_path, flashPath, FlashFolder, IPChange, sensorIP = '133.65.1.1', canape_path = r'C:\Program Files\Vector CANape 17\Exec64\CANape64.exe'):
    #Config IP
    if IPChange:
        print('Config IP')
        configIP(flashPath, sensorIP)

    #Write Flash Script
    print('Write Flash Script')
    flashScript = writeFlash(flashPath, sw_path, FlashFolder)
    print('Flash SW')
    path, filename = os.path.split(flashScript)
    CMD = '\"' + canape_path + '\" -q -a -b \"' + filename + '\"'
    curdir = os.getcwd()
    os.chdir(path)
    # os.system('cmd /c \"' + CMD + '\"')
    os.chdir(curdir)
    
def copyUUT(sw_path):
    print('Copy UUT....')
    Folder = findfolder('measurement', sw_path)['path']
    File = findfile('Radar*', Folder, 'a2l')
    oldFile = findfile('Radar*', '../../../uut', 'a2l')
    if File['name'] != '':
        if oldFile['name'] != File['name'] or hashfile(File['path']) != hashfile(oldFile['path']):
            print('\tCopy: ' + File['name'])
            shutil.copyfile(File['path'], os.path.join('../../../uut', File['name']))            
        else:
            print('\tDone. ' + File['name'] + ' is already existing')
    else:
        print('\tCan not find a2L. Please check!')
    Folder = findfolder('Failure_Doc', sw_path)['path']
    File = findfile('Dem_Cfg_EventId', Folder, 'h')
    shutil.copyfile(File['path'], os.path.join('../../../uut', File['name']))
    print('\tCopy: ' + File['name'])

if __name__ == "__main__":  
    os.chdir(os.path.dirname(os.path.realpath(__file__)))    
    # <FlashSW>
    sw_path = r'D:\GEN5_FSI\CA C589_FR\BL02_RC00\Release_Radar_C2_ASIL_B_C589'
    FlashFolder = r'D:\GEN5_FSI\CA_C589_FR\FlashCommon'
    flashPath = r'D:\GEN5_FSI\00_FLASH_Canape'
    copyUUT(sw_path)
    Flash(sw_path, flashPath, FlashFolder, IPChange = False)
    print('Finished!')