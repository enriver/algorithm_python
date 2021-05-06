#토마토 3차원 - S1
'''
visit 행렬을 만들어서 방문 체크를 해주지 않아도 됨
'''

import sys
from collections import deque

def bfs():
    dx=[-1,1,0,0,0,0]
    dy=[0,0,1,-1,0,0]
    dz=[0,0,0,0,1,-1]

    que=deque()
    day=0

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomato[i][j][k]==1:
                    que.append((i,j,k,day))
                if tomato[i][j][k]==-1:
                    tomato[i][j][k]=1 # 이미 지나간 자리라 바꿔줘도됨

    while que:
        x,y,z,day=que.popleft()

        for i in range(6):
            nx,ny,nz=x+dx[i], y+dy[i], z+dz[i]

            if 0<=nx<H and 0<=ny<N and 0<=nz<M:
                if tomato[nx][ny][nz]==0:
                    tomato[nx][ny][nz]=1
                    que.append((nx,ny,nz,day+1))

    return day
    

if __name__=="__main__":
    M,N,H=map(int, sys.stdin.readline().split()) # 가로, 세로, 높이
    tomato=[[list(map(int,sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]

    days=bfs()

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomato[i][j][k]==0:
                    print(-1)
                    sys.exit(0)

    print(days)
