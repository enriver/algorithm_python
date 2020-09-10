#그림

import sys
from collections import deque
sys.setrecursionlimit(1000000)

n,m=map(int,sys.stdin.readline().split())

mat=[[0 for _ in range(m)] for _ in range(n)]
visit=[[False for _ in range(m)] for _ in range(n)]

for i in range(n):
    k=list(map(int,sys.stdin.readline().split()))
    for j in range(m):
        mat[i][j]=k[j]

dx=[0,1,0,-1]
dy=[1,0,-1,0]

def dfs(x,y,depth):
    for i in range(4):
        nx,ny=x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if not visit[nx][ny] and mat[nx][ny]==1:
                visit[nx][ny]=True
                depth=dfs(nx,ny,depth+1)
    return depth
    

stack=[]

isZero=True

for i in range(n):
    for j in range(m):
        if not visit[i][j] and mat[i][j]==1:
            isZero=False
            visit[i][j]=True
            stack.append(dfs(i,j,1))

if isZero==True:
    print(0)
    print(0)
else:
    stack.sort()

    print(len(stack))
    print(stack[-1])