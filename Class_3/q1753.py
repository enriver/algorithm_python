# 최단경로

import sys
from collections import deque
#정점개수 v 간선개수 e

v, e = map(int, sys.stdin.readline().split())

k=int(sys.stdin.readline()) #시작번호

world=[[0 for _ in range(v+1)] for _ in range(v+1)]
store=[0 for _ in range(v+1)]

for _ in range(e):
    start,end,weight=map(int,sys.stdin.readline().split())
    world[start][end]=weight

store=world[k]

check=set()
isExist=True

while isExist==True:
    isExist=False
    que=deque()

    for i in range(1,len(store)):
        if store[i]!=0:
            if i not in check:
                check.add(i)
                isExist=True
                que.append(i)
    for i in range(1, len(store)):
        for j in que:
            if world[j][i]!=0 and store[i]!=0:
                store[i]=min(store[i],j+world[j][i])
            elif world[j][i]!=0 and store[i]==0:
                store[i]=j+world[j][i]


for i in range(1,len(store)):
    if i==k:
        print(0)
    elif store[i]==0:
        print('Inf')
    else:
        print(store[i])