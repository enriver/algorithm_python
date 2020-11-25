# 강의실 배정 - G5

import heapq
import sys

N=int(sys.stdin.readline())

time=list()
standard=list()

for _ in range(N):
    S,T=map(int,sys.stdin.readline().split())
    time.append((S,T))

time.sort()

for i in range(N):
    if len(standard) != 0 and standard[0]<= time[i][0]:
        heapq.heappop(standard)
    heapq.heappush(standard,time[i][1])
    
print(len(standard))