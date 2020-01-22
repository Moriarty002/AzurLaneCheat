import pyautogui
import win32com.client
import win32gui
import numpy as np
from PIL import ImageGrab
'''
use check('pname') to check the target process is execute or not
'''
def check(pname='Nox.exe'):
    WMI = win32com.client.GetObject('winmgmts:')
    processCodeCov = WMI.ExecQuery('select * from Win32_Process where Name="%s"' % pname)

    if len(processCodeCov) > 0:
        return True
    else:
        return False

'''
use get() to get the point of nox
'''
def get():
    win32gui.EnumWindows(callback, None)

def callback(hwnd, extra):
    rect = win32gui.GetWindowRect(hwnd)
    x1 = rect[0]
    y1 = rect[1]
    x2 = rect[2]
    y2 = rect[3]
    name=win32gui.GetWindowText(hwnd)
    #print("%s:" %name)
    if(name=='夜神模擬器1'):
        print(x1,y1,x2,y2)
        return(x1,y1,x2,y2)

'''
use mclick(x,y) to click position (x,y) on screen 
'''
def mclick(x=0,y=0):
    pyautogui.click(x,y)
    
'''
cut the img in range(x1,y1,x2,y2)
save in test.jpg
'''
def mprtsc(x1=0,y1=0,x2=100,y2=100):
    img = ImageGrab.grab(bbox=(x1,y1,x2,y2))
    img.save('test.jpg','JPEG')

