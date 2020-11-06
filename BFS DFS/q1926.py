#그림

import sys

sys.setrecursionlimit(1000000)
n,m = map(int,sys.stdin.readline().split()) # n행 m렬


visit=[[False for _  in range(501)] for _ in range(501)]
mat=[[0 for _ in range(501)] for _ in range(501)]

for i in range(n):
    val=list(map(int , sys.stdin.readline().split()))
    for j in range(m):
        mat[i][j]=val[j]

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def dfs(cnt,x,y):

    for i in range(4):
        nx,ny=x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if not visit[nx][ny] and mat[nx][ny]==1:
                visit[nx][ny]=True
                cnt=dfs(cnt+1,nx,ny)

    return cnt


picture_num=0
picture_size=0

for i in range(n):
    for j in range(m):
        if not visit[i][j] and mat[i][j]==1:
            visit[i][j]=True
            picture_num+=1
            picture_size=max(picture_size,dfs(1,i,j))
           
print(picture_num)
print(picture_size)

