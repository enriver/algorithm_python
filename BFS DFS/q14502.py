# 연구소 - S5

import sys
from collections import deque
from copy import deepcopy
from itertools import combinations

sys.setrecursionlimit(10**9)

def bfs(x,y):
    que=deque()
    que.append((x,y))

    while que:
        x,y=que.popleft()

        for i in range(4):
            nx,ny=x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<M and temp_lab[nx][ny]==0 and not visit[nx][ny]:
                visit[nx][ny]=True
                temp_lab[nx][ny]=2
                que.append((nx,ny))

N,M=map(int,sys.stdin.readline().split()) # row n , col m
dx=[-1,0,1,0]
dy=[0,1,0,-1]

lab=list()
virus=list()
empty=list()
area=-1

for _ in range(N):
    lab.append(list(map(int,sys.stdin.readline().split())))

for i in range(N):
    for j in range(M):
        if lab[i][j]==2:
            virus.append((i,j))
        elif lab[i][j]==0:
            empty.append((i,j))

cases=list(combinations(empty,3))

for k in range(len(cases)):
    temp_lab=deepcopy(lab) # 그냥 copy는 안되고 deepcopy 를 써야함
    visit=[[False for _ in range(M)] for _ in range(N)]

    for i in range(3): # 벽세우기
        temp_lab[cases[k][i][0]][cases[k][i][1]]=1

    for p,q in virus: # 바이러스 퍼뜨리기
        bfs(p,q)

    cnt=0

    for x in range(N):
        for y in range(M):
            if temp_lab[x][y]==0:
                cnt+=1

    area=max(area, cnt)

print(area)