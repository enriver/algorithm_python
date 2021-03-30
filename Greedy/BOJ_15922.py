# 아우으 우아으이야!! - G5

import sys

if __name__=="__main__":
    N=int(sys.stdin.readline())
    
    dx=list()
    dy=list()

    for _ in range(N):
        x,y=map(int,sys.stdin.readline().split())
        dx.append(x)
        dy.append(y)

    length=dy[0]-dx[0]

    ymax=dy[0]

    for i in range(1,N):
        if dx[i]<ymax and dy[i]<ymax:
            continue
        elif dx[i]<ymax and dy[i]>=ymax:
            length+=dy[i]-ymax
            ymax=dy[i]
        elif dx[i]==ymax:
            length+=dy[i]-ymax
            ymax=dy[i]
        elif dx[i]>ymax:
            length+=dy[i]-dx[i]
            ymax=dy[i]

    print(length)