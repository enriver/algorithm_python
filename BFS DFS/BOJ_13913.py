#숨바꼭질4 - G4

import sys
from collections import deque

N,K=map(int,sys.stdin.readline().split())
limit=100001

visit=[False]*limit
path=[0]*limit

def bfs():
    move=0
    que=deque()
    que.append((N,move))

    while que:
        x,move=que.popleft()

        if x==K: 
            print(move)
            p=[]
            
            while x!=N:
                p.append(x)
                x=path[x]
            p.append(N)
            p.reverse()
            print(*p)

            return

        for i in [x+1,x-1,2*x]:
            if 0<=i<limit and not visit[i]:
                visit[i]=True
                path[i]=x
                que.append((i,move+1))
            
bfs()