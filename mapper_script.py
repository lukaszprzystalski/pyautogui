import pyautogui as py
import time
import os
from datetime import datetime

''' script uses FFV2XML_COA_eCofA map from Mapper in order to process 
    automatically files located in mapper folder on desktop         '''


def moveAndClick(x,y, t1=0, t2=0):
    py.moveTo(x, y)
    time.sleep(t1)
    py.click()
    time.sleep(t2)

def twoKeys(x, y, klucz1, klucz2, t1=0):
    py.moveTo(x, y)
    py.click()
    time.sleep(t1)
    py.hotkey(klucz1, klucz2)

def typeWrite(klucz, t1=0):
    py.typewrite(klucz)
    time.sleep(t1)

def hotKey(klucz, t1=0):
    py.hotkey(klucz)
    time.sleep(t1)

def mapperPrep():
    #open mapper
    moveAndClick(661, 1068, 1, 5)
    moveAndClick(914, 358, 1, 2)

    #choose map
    #FFV2XML_COA_eCofa
    moveAndClick(340, 344, 1, 2)
    moveAndClick(791, 647, 1, 2)
    moveAndClick(315, 84, 1, 2)

    #pre set mapper
    #Advanced File Properties - Encoding: Eight-bit Unicode Transformation Format
    moveAndClick(157, 294, 1, 2)
    typeWrite('e', 1)
    typeWrite('e', 1)
    moveAndClick(1190, 612, 1, 2)

    moveAndClick(166, 387, 1, 2)
    typeWrite('e', 1)
    typeWrite('e', 1)
    moveAndClick(1190, 612, 1, 2)

def mapperClose():
    #close mapper
    time.sleep(2)
    moveAndClick(1897, 8, 1, 2)
    hotKey('TAB', 1)
    hotKey('RETURN', 1)
  
startTime = datetime.now()

workingDir = r'C:\Users\lukasz.przystalski\OneDrive - Avantor\Desktop\mapper'
time.sleep(3)

mapperPrep()

for root, dirs, files in os.walk(workingDir, topdown = False):
    for name in files:
        if name.split('.')[1] == 'txt':
            sourceFile = os.path.join(workingDir, name)
            targetFile = os.path.join(workingDir, name.split('.')[0]+'.xml')
            twoKeys(737,275,'CTRL', 'a', 1)
            typeWrite(sourceFile, 1)
            twoKeys(852,362,'CTRL', 'a', 1)
            typeWrite(targetFile, 1)
            moveAndClick(684,995,1,2)
            hotKey('RETURN', 1)

mapperClose()

print('czas wykonania operacji: ',datetime.now() - startTime)    