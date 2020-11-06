#토마토 - S1

import sys
from collections import deque

M,N =map(int, sys.stdin.readline().split())

visit=[[False for _ in range(M)] for _ in range(N)]
mat=[[False for _ in range(M)] for _ in range(N)]

for i in range(N):
    tomato=list(map(int,sys.stdin.readline().split()))
    for j in range(M):
        mat[i][j]=tomato[j]

dx=[1,-1,0,0]
dy=[0,0,-1,1]

def bfs():
    que=deque()
    day=-1
    for i in range(N):
        for j in range(M):
            if mat[i][j]==-1:
                visit[i][j]=True
            if mat[i][j]==1 and not visit[i][j]:
                visit[i][j]=True
                que.append((i,j,0))

    while que:
        x,y,day=que.popleft()

        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]

            if 0<=nx<N and 0<=ny<M:
                if mat[nx][ny]==0 and not visit[nx][ny]:
                    visit[nx][ny]=True
                    que.append((nx,ny,day+1))

    return day

def solve(days):
    for i in range(N):
        for j in range(M):
            if visit[i][j]==False:
                return -1
    return days

day=bfs()
print(solve(day))