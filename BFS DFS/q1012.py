#유기농 배추 - S2

import sys
from collections import deque

T=int(sys.stdin.readline())

dx=[1,-1,0,0]
dy=[0,0,-1,1]

def bfs(x,y,size,row,col,matrix,visited):
    que=deque()
    que.append((x,y,size))

    while que:
        x,y,size=que.popleft()

        for i in range(4):
            nx,ny=x+dx[i], y+dy[i]
            if 0<=nx<row and 0<=ny<col:
                if matrix[nx][ny]==1 and not visited[nx][ny]:
                    visited[nx][ny]=True
                    que.append((nx,ny,size+1))

    return 1



for _ in range(T):
    N,M,K=map(int,sys.stdin.readline().split()) # M 렬 N행 K 배추개수

    visit=[[False for _ in range(M)] for _ in range(N)]
    mat=[[0 for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        i,j=map(int, sys.stdin.readline().split())
        mat[i][j]=1

    sum=0
    for i in range(N):
        for j in range(M):
            if mat[i][j]==1 and not visit[i][j]:
                sum+=(bfs(i,j,1,N,M,mat,visit))
    print(sum)