# 텔레포트 정거장 - S2

import sys
from collections import deque

def solve(s):
    que=deque()
    que.append((s,0))

    visit[s]=True

    while que:
        s,cnt=que.popleft()

        if s==E:
            break

        if s in tp.keys():
            for i in tp[s]:
                if not visit[i]:
                    visit[i]=True
                    que.append((i, cnt+1))

        for i in [s+1, s-1]:
            if 1<=i<N+1 and not visit[i]:
                visit[i]=True
                que.append((i, cnt+1))

    return cnt

if __name__=="__main__":
    N,M = map(int, sys.stdin.readline().split())
    S,E = map(int, sys.stdin.readline().split())

    visit=[False for _ in range(N+1)]

    tp=dict()
    for _ in range(M):
        x,y=map(int,sys.stdin.readline().split())
        
        if x not in tp.keys():
            tp[x]=list()
        if y not in tp.keys():
            tp[y]=list()

        tp[x].append(y)
        tp[y].append(x)

    print(solve(S))