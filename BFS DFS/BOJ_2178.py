#미로탐색

import sys
from collections import deque

n,m=map(int,sys.stdin.readline().split()) # n 행 m 렬

miro=[[0 for _ in range(m)] for _ in range(n)]
visit=[[False for _ in range(m)] for _ in range(n)]

for i in range(n):
    k=sys.stdin.readline()
    for j in range(m):
        miro[i][j]=int(k[j])

dx=[1,0,0,-1]
dy=[0,1,-1,0]

def bfs(x,y,move):
    que=deque()
    que.append((x,y,move))

    while que:
        x,y,move=que.popleft()

        if x==(n-1) and y==(m-1):
            return move

        for i in range(4):
            nx,ny=x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if miro[nx][ny]==1 and not visit[nx][ny]:
                    visit[nx][ny]=True
                    que.append((nx,ny,move+1))
                    
print(bfs(0,0,1))