# 두 동전 - G4

import sys
from collections import deque

def solve(coins):
    que=deque()
    que.append(coins[0])
    que.append(coins[1])
    que.append(1)

    while que:
        coin_1=que.popleft()
        coin_2=que.popleft()
        cnt=que.popleft()

        for i in range(4):
            ax,ay=coin_1[0]+dx[i], coin_1[1]+dy[i]
            bx,by=coin_2[0]+dx[i], coin_2[1]+dy[i]

            if 0<=ax<N and 0<=ay<M:
                if not visit[0][ax][ay] and board[ax][ay]!='#':
                    if 0>bx or N<=bx or 0>by or M<=by:
                        print(cnt)
                        return
            if 0<=bx<N and 0<=by<M:
                if not visit[1][bx][by] and board[bx][by]!='#':
                    if 0>ax or N<=ax or 0>ay or M<=ay:
                        print(cnt)
                        return

            if 0<=ax<N and 0<=ay<M and 0<=bx<N and 0<=by<M:
                if board[ax][ay]!='#' and board[bx][by]!='#': # 둘다 #이 아닌 경우 -> 둘중 하나라도 움직일 수 있는 상황
                    if not visit[0][ax][ay] and not visit[1][bx][by]:
                        visit[0][ax][ay]=True
                        visit[1][bx][by]=True

                        que.append((ax,ay))
                        que.append((bx,by))
                        que.append(cnt+1)

                if board[ax][ay]!='#' and board[bx][by]=='#':
                    que.append((ax,ay))
                    que.append((coin_2[0],coin_2[1]))
                    que.append(cnt+1)

                if board[bx][by]!='#' and board[ax][ay]=='#':
                    que.append((coin_1[0], coin_1[1]))
                    que.append((bx,by))
                    que.append(cnt+1)

    print(-1)
    return

if __name__=="__main__":
    N,M=map(int,sys.stdin.readline().split()) # N세로, M가로

    board=list()
    visit=[[[False for _ in range(M)] for _ in range(N)] for _ in range(2)]

    for _ in range(N):
        board.append(list(sys.stdin.readline().rstrip()))

    coin=list()
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]

    k=0
    for i in range(N):
        for j in range(M):
            if board[i][j]=='o':
                coin.append((i,j))
                visit[k][i][j]=True
                k+=1
    solve(coin)
