#성곽

import sys

m,n=map(int, sys.stdin.readline().split()) #m 렬 n행

visit=[[False for _ in range(m)] for _ in range(n)]

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

room_num=0
room_size=0
after_crash=-1

depth=0

for i in range(n):
    dsnp=list(map(int, sys.stdin.readline().split()))
    for j in range(m):
        dir=direction[dsnp[j]]
        for k in range(4):
            mat[i][j].append(dir[k])

def dfs(x,y):
    global depth
    visit[x][y]=True
    stack.append([x,y])
    depth+=1
    pos=list()
  
    for i in range(4):
        if mat[x][y][i]==0:
            pos.append(i)
        
    for k in pos:
        nx,ny=x+dx[k], y+dy[k]       
        if 0<=nx<n and 0<=ny<m:
            if not visit[nx][ny]:
                dfs(nx,ny)
                

for i in range(n):
    for j in range(m):
        if not visit[i][j]:
            stack=list()
            dfs(i,j)
            room_size=max(room_size,depth)
            room_num+=1
            for k in range(len(stack)):
                mat[stack[k][0]][stack[k][1]]=depth
            depth=0
                      

print(room_num)
print(room_size)

for i in range(n):
    for j in range(m):
        for t in range(4):
            ni,nj=i+dx[t],j+dy[t]
            if 0<=ni<n and 0<=nj<m:
                if mat[i][j]!=mat[ni][nj]:
                    after_crash=max(after_crash,mat[i][j]+mat[ni][nj])

if after_crash==-1:
    if room_num>1:
        print(2*mat[0][0])
    else:
        print(1)
else:
    print(after_crash)
