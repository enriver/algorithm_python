# 점프 게임 - S1 

import sys
from collections import deque

def solve(pos,line,cnt):
    que=deque()
    que.append((pos,line,cnt))

    while que:
        pos, line, cnt=que.popleft()

        for i in [pos+1, pos-1, pos+K]:
            if i==pos+1 or i==pos+K:
                if i>=N:
                    return 1

            if i==pos+K:
                if line==left:
                    line=right
                else:
                    line=left

            if line[i]==1 and i>cnt:
                que.append((i, line, cnt+1))

    return 0


if __name__=="__main__":
    N,K=map(int, sys.stdin.readline().split())

    left=list(map(int,sys.stdin.readline().rstrip()))
    right=list(map(int,sys.stdin.readline().rstrip()))

    if N==1:
        print(0)
    else:
        print(solve(0,left,0))

