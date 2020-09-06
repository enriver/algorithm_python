# 바이러스
import sys
from collections import deque

def bfs(graph, start):    
    visit=[]
    que=deque([start])

    while que:
        now=que.popleft()
        if now not in visit:
            visit.append(now)
            que.extend((graph[now]))

    return visit


node=int(sys.stdin.readline())
edge=int(sys.stdin.readline())

graph=[set([]) for _ in range(node+1)]

for _ in range(edge):
    x,y = map(int, sys.stdin.readline().split())
    graph[x].add(y)
    graph[y].add(x)

print(len(bfs(graph,1))-1)