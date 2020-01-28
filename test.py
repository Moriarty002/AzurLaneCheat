import win32gui
import os
import time
while(True):
    os.system('cls||clear')
    x,y=win32gui.GetCursorPos()
    print(x)
    print(y)
    time.sleep(1)