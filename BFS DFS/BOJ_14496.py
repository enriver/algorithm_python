# 그대, 그머가 되어 - S1

import sys
from collections import deque

def solve(now,cnt):
    que=deque()
    que.append((now,cnt))

    while que:
        now, cnt=que.popleft()
        
        if now==b:
            return cnt

        for i in range(N+1):
            if wordSet[now][i]==1 and not visit[i]:
                visit[i]=True
                que.append((i,cnt+1))

    return -1


if __name__=="__main__":
    a,b=map(int,sys.stdin.readline().split())

    N,M=map(int,sys.stdin.readline().split())

    wordSet=[[0 for _ in range(N+1)] for _ in range(N+1)]
    visit=[False]*(N+1)
    
    visit[a]=True
    for _ in range(M):
        w1,w2=map(int,sys.stdin.readline().split()) 

        wordSet[w1][w2]=1
        wordSet[w2][w1]=1

    print(solve(a,0))
