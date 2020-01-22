import pyautogui
import win32com.client
import win32gui

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

        