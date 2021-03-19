# 전쟁 : 전투 - S1

import sys

def solve(x,y,cnt,color):
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]

        if 0<=nx<M and 0<=ny<N:
            if not visit[nx][ny] and soldiers[nx][ny]==color:
                visit[nx][ny]=True
                cnt=solve(nx,ny,cnt+1,color)

    return cnt

if __name__=="__main__":
    N,M = map(int, sys.stdin.readline().split()) # N 가로, M 세로

    soldiers=list()

    for _ in range(M):
        soldiers.append(list(sys.stdin.readline().rstrip()))

    visit=[[False for _ in range(N)] for _ in range(M)]
    
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    
    white=0
    blue=0

    for i in range(M):
        for j in range(N):
            if not visit[i][j]:
                visit[i][j]=True
                num=solve(i,j,1,soldiers[i][j])

                if soldiers[i][j]=='W':
                    white+=num**2
                else:
                    blue+=num**2

    print(white, blue)