#숨바꼭질3 - G5

import sys
from collections import deque

N,K=map(int,sys.stdin.readline().split())

limit=100001
visit=[False]*limit

answer=float('inf')

def bfs(start,move):
    global answer
    que=deque()
    que.append((start,move))
    visit[start]=True

    while que:
        x,move=que.popleft()
        visit[x]=True

        if x==K:
            answer=min(answer,move)

        for i in [2*x,x+1,x-1]:
            if 0<=i<limit and not visit[i]:
                if i==2*x:
                    que.appendleft((i,move))
                else:
                    que.append((i,move+1))
            
bfs(N,0)
print(answer)
