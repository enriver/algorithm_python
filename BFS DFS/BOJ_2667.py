#단지번호붙이기
import sys

def dfs(depth,x,y,mat,n):
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            if mat[nx][ny]==1 and not visit[nx][ny]:
                visit[nx][ny]=True
                depth=dfs(depth+1, nx,ny,mat,n)
    return depth


dx=[-1,0,1,0] # x방향
dy=[0,1,0,-1] # y방향
size=[] #단지

n=int(sys.stdin.readline())
matrix=[[0 for _ in range(n)] for _ in range(n)]
visit=[[False for _ in range(n)] for _ in range(n)]

for i in range(n):
    house=sys.stdin.readline()
    for j in range(n):
        matrix[i][j]=int(house[j])

for i in range(n):
    for j in range(n):
        if matrix[i][j]==1 and not visit[i][j]:
            visit[i][j]=True
            size.append(dfs(1,i,j,matrix,n))

size.sort()

print(len(size))
for i in size:
    print(i)