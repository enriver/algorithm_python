#음식물 피하기 DFS_BFS

import sys


n, m, k =map(int,sys.stdin.readline().split())

table=[[0 for _ in range(m)] for _ in range(n)]

for i in range(k):
    x,y=map(int, sys.stdin.readline().split())
    table[x-1][y-1]=1

print(table)
    

