# 거북이 - S2

import sys

def check(mv):
    x=0
    y=0

    min_x=501
    max_x=-501
    min_y=501
    max_y=-501

    direction=0 # 0:북, 1:서, 2:남, 3:동

    for i in mv:
        if i=='L':
            direction+=1
        elif i=='R':
            direction-=1

        if direction==4:
            direction=0
        elif direction==-1:
            direction=3

        if i=='F':
            if direction==0:
               y=y+1
            elif direction==1:
               x=x-1
            elif direction==2:
               y=y-1
            else:
               x=x+1

        elif i=='B':
            if direction==0:
              y=y-1
            elif direction==1:
              x=x+1
            elif direction==2:
              y=y+1
            else:
              x=x-1

        min_x=min(min_x,x,0)
        max_x=max(max_x,x,0)
        min_y=min(min_y,y,0)
        max_y=max(max_y,y,0)

    print(abs(max_x-min_x)*abs(max_y-min_y))


if __name__=="__main__":
    T=int(sys.stdin.readline())

    for _ in range(T):
        move=list(sys.stdin.readline().rstrip())

        check(move)