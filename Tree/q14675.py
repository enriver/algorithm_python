# 단절점과 단절선 - G5

import sys

N=int(sys.stdin.readline())

graph=dict()
for _ in range(N-1):
    a,b=map(int,sys.stdin.readline().split())

    if a not in graph.keys():
        graph[a]=set()
    if b not in graph.keys():
        graph[b]=set()

    graph[a].add(b)
    graph[b].add(a)


q=int(sys.stdin.readline())

for _ in range(q):
    t,k=map(int,sys.stdin.readline().split())

    if t==1:
        if len(graph[k])==1:
            print('no')
        else:
            print('yes')
    else:
        print('yes')