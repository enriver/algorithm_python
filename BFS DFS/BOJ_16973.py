import sys
from collections import deque

# 동서남북
dx=[0,0,1,-1]
dy=[1,-1,0,0]

def solve(x,y,cnt):
    que=deque()
    que.append((x,y,cnt))

    while que:
        x,y,cnt=que.popleft()

        if x==Fr-1 and y==Fc-1:
            return cnt

        for i in range(4):
            nx,ny=x+dx[i], y+dy[i]

            if 0<=nx<N and 0<=ny<M and 0<=nx+H-1<N and 0<=ny+W-1<M and check(nx,ny,i)==True:
                if not visit[nx][ny]:
                    visit[nx][ny]=True
                    que.append((nx,ny,cnt+1))

    return -1

def check(x,y,direction): # 동서남북
    if direction==0:
        for k in range(x,x+H):
            if pan[k][y+W-1]==1:
                return False
    elif direction==1:
        for k in range(x,x+H):
            if pan[k][y]==1:
                return False
    elif direction==2:
        for k in range(y,y+W):
            if pan[x+H-1][k]==1:
                return False
    elif direction==3:
        for k in range(y,y+W):
            if pan[x][k]==1:
                return False
    
    return True

if __name__=="__main__":
    N,M=map(int,sys.stdin.readline().split())

    pan=list()
    visit=[[False for _ in range(M)] for _ in range(N)]

    for _ in range(N):
        pan.append(list(map(int,sys.stdin.readline().split())))

    H,W,Sr,Sc,Fr,Fc=map(int,sys.stdin.readline().split())

    print(solve(Sr-1,Sc-1,0))
