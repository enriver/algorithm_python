# 숨바꼭질

import sys
from collections import deque

n,k=map(int,sys.stdin.readline().split())

limit=100001

visit=[False]*limit

def bfs(start, move):
    que=deque()
    que.append((start,move))
    visit[start]=True

    while que:
        x, move=que.popleft()

        if x==k:
            return move
        else:
            for i in list([x+1,x-1,2*x]):
                if 0<=i<limit and not visit[i]:
                    visit[i]=True
                    que.append((i,move+1))

print(bfs(n,0))