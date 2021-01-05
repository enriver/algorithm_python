# 벽 부수고 이동하기

import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())

mat=[[0 for _ in range(m)] for _ in range(n)]
visit=[[[False for _ in range(m)] for _ in range(n)] for _ in range(2)]

for i in range(n):
    word=sys.stdin.readline()
    for j in range(m):
        mat[i][j]=int(word[j])

dx=[1,-1,0,0]
dy=[0,0,-1,1]


def bfs(x,y,move,crash):
    que=deque()
    que.append((x,y,move,crash))

    while que:
        x,y,move,crash=que.popleft()

        if x==(n-1) and y==(m-1):
            return move

        for i in range(4):
            nx,ny=x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if crash>0:
                    if mat[nx][ny]==1 and not visit[crash][nx][ny]:
                        visit[crash][nx][ny]=True
                        que.append((nx,ny,move+1,crash-1))
                        
                if mat[nx][ny]==0 and not visit[crash][nx][ny]:
                    visit[crash][nx][ny]=True
                    que.append((nx,ny,move+1,crash))
    return -1

    

print(bfs(0,0,1,1))