#미친로봇 DFS_BFS

import sys

num, d,s,n,p=map(int,sys.stdin.readline().split())

visit=[[False for _ in range(30)] for _ in range(30)]
direction=[d/100,s/100,n/100,p/100]

dx=[0,0,1,-1]
dy=[1,-1,0,0]

result=0

def dfs(x,y,pob,count):
    global result

    if count==num:
        result +=pob
        return
    
    for i in range(4):   # 행 값은 북/남,  열 값은 동/서
        nx,ny=x+dx[i], y+dy[i]
        if not visit[nx][ny]:
            visit[nx][ny]=True
            dfs(nx,ny,pob*direction[i],count+1)
            visit[nx][ny]=False
        
   

visit[15][15]=True
dfs(15,15,1,0)

print(result)

