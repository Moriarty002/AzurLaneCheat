#algorithm of searching map
import numpy as np
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
if __name__ == "__main__":
    #map_3_4 0=通道 -1=路障 1=敵人
    #abmap 0=無法到達 1=可到達
    #tmap 2=點擊目標 其他=非必要點擊
    map_3_4=np.array([[0,0,0,0,0,-1,-1,-1],[0,0,0,0,0,0,-1,-1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]])
    abmap=np.zeros_like(map_3_4)
    vmap=abmap
    abmap=bfs(map_3_4,abmap,vmap,(1,2))
    tmap=abmap+map_3_4
    print(tmap)
    for i in range(1,4):
        map_3_4=add_enymy(map_3_4,(i,5))
        abmap=np.zeros_like(map_3_4)
        vmap=abmap
        abmap=bfs(map_3_4,abmap,vmap,(1,2))
        tmap=abmap+map_3_4
        print(tmap)