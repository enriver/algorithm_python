# 트리의 부모 찾기 - S2

import sys

n=int(sys.stdin.readline())

tree=[[] for _ in range(n+1)]
for _ in range(n-1):
    a,b=map(int,sys.stdin.readline().split())
    
    tree[a].append(b)
    tree[b].append(a)

print(tree)