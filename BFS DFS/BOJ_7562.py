# 나이트의 이동 - S2

import sys
from collections import deque

dx=[-2,-1,-2,-1,1,2,2,1]
dy=[-1,-2,1,2,2,1,-1,-2]

def bfs(size,x,y,ggx,ggy,cnt):
    #chess=[[0 for _ in range(size)] for _ in range(size)]
    visit=[[False for _ in range(size)] for _ in range(size)]
    visit[x][y]=True

    que=deque()
    que.append((x,y,cnt))

    while que:
        x,y,cnt = que.popleft()

        if x==ggx and y==ggy:
            return cnt

        for i in range(8):
            nx,ny=x+dx[i], y+dy[i]

            if 0<=nx<size and 0<=ny<size:
                if not visit[nx][ny]:
                    visit[nx][ny]=True
                    que.append((nx,ny,cnt+1))
    
if __name__=="__main__":
    T=int(sys.stdin.readline())

    for _ in range(T):
        n=int(sys.stdin.readline())

        kx,ky=list(map(int,sys.stdin.readline().split()))
        gx,gy=list(map(int,sys.stdin.readline().split()))

        print(bfs(n, kx,ky, gx,gy, 0))
        
