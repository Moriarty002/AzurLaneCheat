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

'''
map generate
'''

'''
map caculate
map_cac(map,tpos,epos) >> args: map(ndarray),tpos==team1 position(tupple),epos==enemy position(tupple array)
'''
def bfs(omap,nmap,vmap,start):
    x=start[0]
    y=start[1]
    if x<0 or x>=omap.shape[0]:
        return nmap
    elif y<0 or y>=omap.shape[1]:
        return nmap
    if vmap[x,y] == 1:
        return nmap
    vmap[x,y]=1
    nmap[x,y]=0
    if omap[x,y] == 0 :
        nmap[x,y]=1
        nmap=bfs(omap,nmap,vmap,(x+1,y))
        nmap=bfs(omap,nmap,vmap,(x-1,y))
        nmap=bfs(omap,nmap,vmap,(x,y+1))
        nmap=bfs(omap,nmap,vmap,(x,y-1))
    elif omap[x,y] == 1:
        nmap[x,y]=1
    return nmap
def add_enymy(mmap,pos):
    mmap[pos[0],pos[1]]=1
    return mmap
def map_cac(map,tpos,epos):
    #map_3_4 0=通道 -1=路障 1=敵人
    #abmap 0=無法到達 1=可到達
    #tmap 2=點擊目標 其他=非必要點擊
    abmap=np.zeros_like(map)
    vmap=abmap
    for i in epos:
        map=add_enymy(map,i)
    abmap=bfs(map,abmap,vmap,tpos)
    tmap=abmap+map
    return tmap ,map


