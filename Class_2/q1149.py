#RGB 거리

import sys
from collections import deque

n=int(sys.stdin.readline())
house=[[0 for _ in range(3)] for _ in range(n)]
result=[[[False for _ in range(3)] for _ in range(3)] for _ in range(3)]

for i in range(n):
    R,G,B=map(int,sys.stdin.readline().split())
    house[i][0]=R
    house[i][1]=G
    house[i][2]=B

