#맥주 마시면서 걸어가기 - S1

import sys
from collections import deque


def dfs(num):
    global result
    visit[num]=1
    if num==(n+1):
        result='happy'
        return

    for i in range(n+2):
        dx=abs(position[num][0]-position[i][0])
        dy=abs(position[num][1]-position[i][1])

        if dx+dy<=1000 and not visit[i]:
            dfs(i)

t=int(sys.stdin.readline())
for _ in range(t):
    n=int(sys.stdin.readline())
    position=list()
    visit=[False for _ in range(n+2)]

    for _ in range(n+2):
        x,y=(map(int,sys.stdin.readline().split()))
        position.append((x,y))
    
    result='sad'
    dfs(0)

    print(result)
    