# 2020 카카오 인턴십 - 경주로 건설

import sys
from collections import deque

def dfs(x,y,won,direction):
    global result

    dx=[0,0,1,-1] # 동서남북
    dy=[1,-1,0,0]

    que=deque()
    pairs=list()

    que.append((x,y,won,direction))

    while que:
        x,y,won,direction=que.popleft()

        if x==N-1 and y==N-1:
            for pair in pairs:
                visit[pair[0]][pair[1]]=False

            result.append(won)

        for i in range(4):
            nx,ny=x+dx[i], y+dy[i]

            if 0<=nx<N and 0<=ny<N:
                if board[nx][ny]==0 and not visit[nx][ny]:
                    visit[nx][ny]=True
                    pairs.append((nx,ny))
                    
                    if direction==i:
                        que.append((nx,ny,won+100, i))
                    else:
                        que.append((nx,ny,won+600, i))


def solve(board):
    won=float('inf')
    visit[0][0]=True

    for i in [(0,1),(1,0)]:
        ax,ay=i[0],i[1]

        if 0<=ax<N and 0<=ay<N:
            if board[ax][ay]==0 and not visit[ax][ay]:
                visit[ax][ay]=True  
                dfs(ax,ay,100,i)

if __name__=="__main__":
    N=int(sys.stdin.readline())
    visit=[[False for _ in range(N)] for _ in range(N)]
    board=[]

    for i in range(N):
        board.append(list(map(int,sys.stdin.readline().split())))

    result=list()
    solve(board)

    print(result)