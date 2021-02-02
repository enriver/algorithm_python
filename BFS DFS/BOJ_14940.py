# 쉬운 최단거리 - G5

import sys
from collections import deque

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def solve(x,y,cnt):
    que=deque()
    que.append((x,y,cnt))

    while que:
        x,y,cnt=que.popleft()

        distance[x][y]=cnt

        for i in range(4):
            nx,ny=x+dx[i], y+dy[i]

            if 0<=nx<n and 0<=ny<m and mapp[nx][ny]==1 and not visit[nx][ny]:
                visit[nx][ny]=True
                que.append((nx,ny,cnt+1))
                

if __name__=="__main__":
    n,m=map(int,sys.stdin.readline().split())

    mapp=list()
    distance=[[-1 for _ in range(m)] for _ in range(n)]
    visit=[[False for _ in range(m)] for _ in range(n)]

    for _ in range(n):
        mapp.append((list(map(int,sys.stdin.readline().split()))))
    
    for i in range(n):
        for j in range(m):
            if mapp[i][j]==2:
                solve(i,j,0)
            if mapp[i][j]==0:
                distance[i][j]=0
                
    for i in range(n):
        for j in range(m):
            print(distance[i][j], end=' ')
            
            if j==m-1:
                print()