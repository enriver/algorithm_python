# Puyo Puyo - G5

import sys
from collections import deque

def fall(rgb_index,rgb_y):
    for x,y in rgb_index:
        puyo[x][y]='.'
    
    for y in rgb_y:
        for x in range(11,0,-1):
            if puyo[x][y]=='.':
                for k in range(x-1,-1,-1):
                    if puyo[k][y]!='.':
                        puyo[x][y]=puyo[k][y]
                        puyo[k][y]='.'
                        break

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs(x,y):
    que=deque()
    que.append((x,y))

    cnt=1
    
    color_index=set()
    color_y=set()
    while que:
        x,y=que.popleft()
        
        color_index.add((x,y))
        color_y.add(y)
        for i in range(4):
            nx,ny=x+dx[i], y+dy[i]

            if 0<=nx<12 and 0<=ny<6:
                if puyo[x][y]==puyo[nx][ny] and not visit[nx][ny]:
                    cnt+=1
                    visit[nx][ny]=True
                    que.append((nx,ny))
    if cnt>=4:
        fall(color_index,color_y)
        return 1
    else:
        return 0

if __name__=="__main__":
    puyo=list()

    for _ in range(12):
        puyo.append(list(sys.stdin.readline().rstrip()))

    ans=0
    while True:
        result=0
        visit=[[False for _ in range(6)] for _ in range(12)]
        for i in range(12):
            for j in range(6):
                if puyo[i][j]!='.' and not visit[i][j]:
                    visit[i][j]=True
                    result+=bfs(i,j)

        if result>0:
            ans+=1
        else:
            break

    print(ans)