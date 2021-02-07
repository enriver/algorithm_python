# 윌리암슨수액빨이딱따구리가 정보섬에 올라온 이유 - G5

import sys
from collections import deque

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def solve(x,y,cnt):
    que=deque()
    que.append((x,y,cnt))

    while que:
        x,y,cnt=que.popleft()

        if food[x][y] in [3,4,5]:
            return cnt

        for i in range(4):
            nx,ny=x+dx[i], y+dy[i]
            
            if 0<=nx<n and 0<=ny<m and food[nx][ny]!=1 and not visit[nx][ny]:
                visit[nx][ny]=True
                que.append((nx,ny,cnt+1))

    return -1

if __name__=="__main__":
    n,m=map(int,sys.stdin.readline().split())

    food=list()
    visit=[[False for _ in range(m)] for _ in range(n)]

    for i in range(n):
        food.append(list(map(int,sys.stdin.readline().rstrip())))

    for i in range(n):
        for j in range(m):
            if food[i][j]==2:
                visit[i][j]=True
                ans=solve(i,j,0)
                break

    if ans>0:
        print('TAK')
        print(ans)
    else:
        print('NIE')