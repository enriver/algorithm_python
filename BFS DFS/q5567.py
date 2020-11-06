#결혼식 DFS_BFS
import sys

n=int(sys.stdin.readline())
m=int(sys.stdin.readline())

graph=dict()

for i in range(0, m):
    key,item=map(int,sys.stdin.readline().split())
    if key not in graph:
        graph[key]=list()
    if item not in graph:
        graph[item]=list()
    graph[key].append(item)
    graph[item].append(key)
  
invite=set()
invite.update(graph.get(1))

for i in list(graph.get(1)):
    try:
        invite.update(graph.get(i))
    except:
        invite.add(graph.get(i))
invite.remove(1)

print(len(invite))