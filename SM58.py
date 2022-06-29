import pyautogui as py
import time
from datetime import datetime

'''
script will run SAP, then will run SM58 code and will check if any transaction threw an error
If Any transactions appear here in “Red” you will need to select these and press F6 to reprocess them.
In next step it will run SM59 code and will perform connection test
'''

def moveAndClick(x, y, t1=0, t2=0):
    py.moveTo(x, y)
    time.sleep(t1)
    py.click()
    time.sleep(t2)
def hotKey(klucz, t1=0):
    py.hotkey(klucz)
    time.sleep(t1)
def typeWrite(klucz, t1=0):
    py.typewrite(klucz)
    time.sleep(t1)
def twoKeys(klucz1, klucz2, t1=1):
    time.sleep(t1)
    py.hotkey(klucz1, klucz2)
def dateMod():
    dt = datetime.today()
    year = dt.year
    month = dt.month
    day = dt.day

    if day == 28 or 29 and month == 2:
        day = 1
        month += 1
        # print('if day = 28')
    elif day == 30 and month in(4, 6, 9, 11):
        day = 1
        month += 1
        # print('if day = 30')
    elif day == 31 and month in(1, 3, 5, 7, 8, 10):
        day = 1
        month += 1
        # print('if day = 31')
    elif day == 31 and month == 12:
        day = 1
        month = 1
        year += 1
        # print('day = 31 and month = 12')
    else:
        day += 1
        # print('else')

    if month <= 9:
        month = '0' + str(month)
        # print('month + 0')
    if day <= 9:
        day = '0' + str(day)
        # print('day + 0')

    # print(day, month, year)
    
    return day, month, year

def loginSAP():
    #starting sap
    time.sleep(5)   
    moveAndClick(410, 1054, 0, 5)
    #running sap
    hotKey('RETURN', 7)
    
def chooseCode(code):
    moveAndClick(80, 50, 0, 2)
    typeWrite(code, 3)
    hotKey('RETURN', 2)
def SM58Details():
    twoKeys('CTRL', 'a', 1)
    hotKey('delete')
    hotKey('TAB',1)

    #deal with dates
    z = dateMod()
    typeWrite(str(z[1]) + '/' + str(z[0]) + '/' + str(z[2]))

    #rest of fields
    hotKey('TAB',1)
    hotKey('TAB',1)

    twoKeys('CTRL', 'a', 1)
    hotKey('delete')

    hotKey('TAB',1)
    hotKey('TAB',1)
    hotKey('TAB',1)
    hotKey('TAB',1)
    hotKey('TAB',1)
    hotKey('TAB',1)

    twoKeys('CTRL', 'a', 1)
    typeWrite('GXS*')

    hotKey('F8', 1)
    time.sleep(2)
def SM59Details():
    moveAndClick(27,336,1,2)
    moveAndClick(87,697,1,2)
    hotKey('F2', 2)
    moveAndClick(76,120,1,2)
    time.sleep(2)
def quitSAP():
    twoKeys('alt', 'F4', 2)
    hotKey('TAB',2)
    hotKey('RETURN', 2)

def main():

    loginSAP()
    chooseCode('SM58')
    SM58Details()
    # quitSAP()
    hotKey('F3', 1)
    hotKey('F3', 1)
    hotKey('F3', 1)
    print('SM58 completed')

    chooseCode('SM59')
    SM59Details()
    print('SM59 completed')
    hotKey('F3', 1)
    hotKey('F3', 1)
    hotKey('F3', 1)
    hotKey('F3', 1)


main()
