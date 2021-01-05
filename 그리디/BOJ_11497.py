# 통나무 건너뛰기 - S2

import sys
from collections import deque

T=int(sys.stdin.readline())

for _ in range(T):
    new_log=deque()
    N=int(sys.stdin.readline())
    log=list(map(int,sys.stdin.readline().split()))
    log.sort()
    
    new_log.append(log[-1])
    for i in range(N-2,-1,-1):
        if i%2==0:
            new_log.appendleft(log[i])
        else:
            new_log.append(log[i])

    difficulty=list()
    difficulty.append(abs(new_log[-1]-new_log[0]))
    
    for i in range(1,N):
        difficulty.append(abs(new_log[i]-new_log[i-1]))

    print(max(difficulty))