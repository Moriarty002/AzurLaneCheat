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

def callback(hwnd, extra):
    rect = win32gui.GetWindowRect(hwnd)
    x = rect[0]
    y = rect[1]
    w = rect[2] - x
    h = rect[3] - y
    print("Window %s:" % win32gui.GetWindowText(hwnd))
    print("\tLocation: (%d, %d)" % (x, y))
    print("\t    Size: (%d, %d)" % (w, h))

if __name__ == '__main__':
    win32gui.EnumWindows(callback, None)

        