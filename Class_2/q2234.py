#성곽

import sys
from collections import deque

m,n=map(int, sys.stdin.readline().split()) #m 렬 n행

visit=[[[False for _ in range(m)] for _ in range(n)] for _ in range(5)]

dx=[0,0,1,-1]
dy=[1,-1,0,0]

mat=[[list() for _ in range(m)] for _ in range(n)]

direction={
    1:[0,1,0,0],
    2:[0,0,0,1],
    3:[0,1,0,1],
    4:[1,0,0,0],
    5:[1,1,0,0],
    6:[1,0,0,1],
    7:[1,1,0,1],
    8:[0,0,1,0],
    9:[0,1,1,0],
    10:[0,0,1,1],
    11:[0,1,1,1],
    12:[1,0,1,0],
    13:[1,1,1,0],
    14:[1,0,1,1],
    15:[1,1,1,1]
}


for i in range(n):
    dsnp=list(map(int, sys.stdin.readline().split()))
    for j in range(m):
        dir=direction[dsnp[j]]
        for k in range(4):
            mat[i][j].append(dir[k])



def bfs(cnt,x,y):
    li=[]
    for i in range(4):
        if mat[x][y][i]==0:
            li.append(i)
    for i in li:
        nx,ny=x+dx[i], y+dy[i]  # nx 동서, ny 남북
        if 0<=nx<n and 0<=ny<m:
            if not visit[i][nx][ny]:
                visit[i][nx][ny]=True
                cnt=bfs(cnt+1,nx,ny)
    return cnt


stack=[]
for i in range(n):
    for j in range(m):
        stack.append(bfs(0,i,j))

stack.sort()

print(len(stack))
print(stack)
