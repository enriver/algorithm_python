# 톱니바퀴 - S1

import sys
from collections import deque


def rotate(num, direction):
    to_right=topni[num][2]
    to_left=topni[num][6]

    if direction==1:
        temp=topni[num][-1]
        topni[num][1:]=topni[num][:-1]
        topni[num][0]=temp

    else:
        temp=topni[num][0]
        topni[num][:-1]=topni[num][1:]
        topni[num][-1]=temp

    for x in [num+1, num-1]:
        if 0<=x<4 and not visit[x]:
            visit[x]=True
            if x==(num+1):
                if to_right!=topni[x][6]:
                    rotate(x,direction*-1)
                    
            else:
                if to_left!=topni[x][2]:
                    rotate(x,direction*-1)
                    

def check():
    ans=0

    for i in range(4):
        if topni[i][0]=='0':
            ans+=0
        else:
            if i==0:
                ans+=1
            elif i==1:
                ans+=2
            elif i==2:
                ans+=4
            else:
                ans+=8

    print(ans)

if __name__=="__main__":
    topni=list()
    for _ in range(4):
        topni.append(list(sys.stdin.readline().rstrip()))

    K=int(sys.stdin.readline())

    
    for _ in range(K):
        visit=[False for _ in range(4)]
        topni_num, way=map(int,sys.stdin.readline().split())
        visit[topni_num-1]=True
        rotate(topni_num-1,way)

    check()
