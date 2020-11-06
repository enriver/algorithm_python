#토마토 3차원 - S1

import sys
from collections import deque

M,N,H=map(int,sys.stdin.readline().split())

visit=[[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]
mat=[[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]

for i in range(H):
    for j in range(N):
        tomato=list(map(int,sys.stdin.readline().split()))
        for k in range(M):
            mat[i][j][k]=tomato[k]

dx=[0,0,0,0,1,-1]
dy=[0,0,1,-1,0,0]
dz=[1,-1,0,0,0,0]

def bfs():
    que=deque()
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if mat[i][j][k]==-1:
                    visit[i][j][k]=True
                if mat[i][j][k]==1 and not visit[i][j][k]:
                    visit[i][j][k]=True
                    que.append((i,j,k,0))

    while que:
        z,x,y,day=que.popleft()

        for i in range(6):
            nz,nx,ny=z+dz[i],x+dx[i],y+dy[i]

            if 0<=nz<H and 0<=nx<N and 0<=ny<M:
                if mat[nz][nx][ny]==0 and not visit[nz][nx][ny]:
                    visit[nz][nx][ny]=True
                    que.append((nz,nx,ny,day+1))

    return day

def solve(days):
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if visit[i][j][k]==False:
                    return -1
    return days

print(solve(bfs()))
