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

        if cnt>10:
            break

        for i in range(4):
            ax,ay=coin_1[0]+dx[i], coin_1[1]+dy[i]
            bx,by=coin_2[0]+dx[i], coin_2[1]+dy[i]

            if 0<=ax<N and 0<=ay<M:
                if 0>bx or N<=bx or 0>by or M<=by:
                    print(cnt)
                    return

            if 0<=bx<N and 0<=by<M:
                if 0>ax or N<=ax or 0>ay or M<=ay:
                    print(cnt)
                    return

            if 0<=ax<N and 0<=ay<M and 0<=bx<N and 0<=by<M:
                if board[ax][ay]!='#' and board[bx][by]=='#': # 첫번째 동전만 움직이는 경우
                    
                    que.append((ax,ay))
                    que.append((coin_2[0], coin_2[1]))
                    que.append(cnt+1)

                if board[ax][ay]=='#' and board[bx][by]!='#': # 두번째 동전만 움직이는 경우

                    que.append((coin_1[0], coin_1[1]))
                    que.append((bx,by))
                    que.append(cnt+1)

                if board[ax][ay]!='#' and board[bx][by]!='#' : # 두 동전 모두 움직이는 경우
                
                    que.append((ax,ay))
                    que.append((bx,by))
                    que.append(cnt+1)

    print(-1)
    return

if __name__=="__main__":
    N,M=map(int,sys.stdin.readline().split()) # N세로, M가로

    board=list()

    for _ in range(N):
        board.append(list(sys.stdin.readline().rstrip()))

    coin=list()
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]

    for i in range(N):
        for j in range(M):
            if board[i][j]=='o':
                coin.append((i,j))                
                
    solve(coin)
