# 현수막 - S1

import sys
from collections import deque

def bfs(x,y):
    dx=[1,-1,0,0, -1,-1,1,1] # x좌표 : 상하좌우, 대각선
    dy=[0,0,1,-1, -1,1,-1,1] # y좌표 : 상하좌우, 대각선 

    que=deque()
    que.append((x,y))

    while que:
        x,y=que.popleft()

        for i in range(8):
            nx,ny=x+dx[i], y+dy[i]

            if 0<=nx<M and 0<=ny<N:
                if not visit[nx][ny] and placard[nx][ny]==1:
                    visit[nx][ny]=True
                    que.append((nx,ny))

    return 1

if __name__=="__main__":
    M,N=map(int, sys.stdin.readline().split())

    placard=list()

    for _ in range(M):
        placard.append(list(map(int,sys.stdin.readline().split())))

    visit=[[False for _ in range(N)] for _ in range(M)]

    res=0
    for i in range(M):
        for j in range(N):
            if not visit[i][j] and placard[i][j]==1:
                res+=bfs(i,j)

    print(res)