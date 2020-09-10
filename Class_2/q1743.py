#음식물 피하기 DFS_BFS
import sys
from collections import deque

sys.setrecursionlimit(100000)

n,m,k =map(int, sys.stdin.readline().split()) # n 행 m 열 k 쓰레기

matrix=[[0 for _ in range(m)] for _ in range(n)]
visit=[[False for _ in range(m)] for _ in range(n)]

for _ in range(k):
    x,y=map(int,sys.stdin.readline().split())
    matrix[x-1][y-1]=1

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def dfs(depth, x,y):
    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if matrix[nx][ny]==1 and not visit[nx][ny]:
                visit[nx][ny]=True
                depth=dfs(depth+1,nx,ny)
    return depth

stack=[]
for i in range(n):
    for j in range(m):
        if not visit[i][j] and matrix[i][j]==1:
            visit[i][j]=True
            stack.append(dfs(1,i,j))

stack.sort()

print(stack[-1])