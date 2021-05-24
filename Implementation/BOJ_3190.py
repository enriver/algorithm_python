# 뱀 - G5

import sys
from collections import deque

def solve(x,y,sec,move_x,move_y):
    que=deque()
    que.append((x,y,sec,move_x,move_y))

    visit[x][y]=True

    snake=[(x,y)] #머리겸 꼬리
    while que:
        x,y,sec,move_x,move_y=que.popleft()

        nx,ny=x+move_x, y+move_y
        
        if sec in rotate.keys():
            direction=rotate[sec]
            if move_x==0:
                if direction=='L':
                    move_x,move_y=-move_y,move_x
                else:
                    move_x,move_y=move_y,move_x
            else: # move_x가 1일때
                if direction=='L':
                    move_x,move_y=move_y,move_x
                else:
                    move_x,move_y=move_y,-move_x

        if 0<=nx<N and 0<=ny<N:
            if visit[nx][ny]:
                break
            else:
                if board[nx][ny]==1: # 사과가 있다
                    snake.append((nx,ny)) # 머리추가
                    visit[nx][ny]=True
                    que.append((nx,ny,sec+1,move_x,move_y))
                    board[nx][ny]=0

                else: # 사과가 없다
                    snake.append((nx,ny))
                    visit[nx][ny]=True
                    tail=snake.pop(0)
                    visit[tail[0]][tail[1]]=False
                    que.append((nx,ny,sec+1,move_x,move_y))

        else:
            break

    return sec

if __name__=="__main__":
    N=int(sys.stdin.readline()) # 보드의 크기 N*N
    K=int(sys.stdin.readline()) # 사과의 개수

    board=[[0 for _ in range(N)] for _ in range(N)]
    visit=[[False for _ in range(N)] for _ in range(N)]

    for _ in range(K): # 사과의 위치
        x,y=map(int, sys.stdin.readline().split())
        board[x-1][y-1]=1

    L=int(sys.stdin.readline()) # 뱀의 방향 변환 횟수

    rotate=dict()
    for _ in range(L):
        sec,direction=sys.stdin.readline().split()
        rotate[int(sec)]=direction

    print(solve(0,0,1,0,1))

    