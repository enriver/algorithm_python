#맥주 마시면서 걸어가기 - S1

import sys
from collections import deque

#dfs 풀이

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
    
'''
# bfs 풀이

def bfs(x,y):
    global result
    que=deque()
    que.append((x,y))

    while que:
        x,y=que.popleft()

        if (x,y)==position[-1]:
            result='happy'
            return
        
        for i, value in enumerate(position):
            dx=abs(value[0]-x)
            dy=abs(value[1]-y)

            if dx+dy<=1000 and not visit[i]:
                visit[i]=True
                que.append((value[0],value[1]))
    return

t=int(sys.stdin.readline())
for _ in range(t):
    n=int(sys.stdin.readline())
    position=list()
    visit=[False for _ in range(n+2)]

    for _ in range(n+2):
        x,y=(map(int,sys.stdin.readline().split()))
        position.append((x,y))
    
    result='sad'
    bfs(position[0][0],position[0][1])

    print(result)
'''