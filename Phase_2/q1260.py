#DFS와 BFS
import sys
from collections import deque
"""
n: 정점개수
m: 간선개수
v: 시작노드
"""

def dfs(graph,start):
    visit={}
    stack=[start]

    while stack:
        now=stack.pop()
        if now not in visit:
            visit[now]=True
            stack.extend(sorted(graph[now], reverse=True))

    return visit.keys()

def bfs(graph,start):
    visit={}
    que=deque([start])

    while que:
        now=que.popleft()
        if now not in visit:
            visit[now]=True
            que.extend(sorted(graph[now]))

    return visit.keys()

n, m, v =map(int, sys.stdin.readline().split()) 

# graph=dict()

# for _ in range(m):
#     a,b = map(int, sys.stdin.readline().split())
#     if a not in graph.keys():
#         graph[a]=list()
#     if b not in graph.keys():
#         graph[b]=list()
#     graph[a].append(b)
#     graph[b].append(a)

graph=[set([]) for _ in range(n+1)]
for _ in range(m):
    a,b=map(int, sys.stdin.readline().split())
    graph[a].add(b)
    graph[b].add(a)

print(*dfs(graph,v))
print(*bfs(graph,v))