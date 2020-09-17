#기타리스트

import sys
from collections import deque

N,S,M=map(int,sys.stdin.readline().split())
volume=list(map(int,sys.stdin.readline().split()))

dp=[[0 for _ in range(M+1)] for _ in range(N+1)]
dp[0][S]=1

for i in range(1,N+1):
    for j in range(M+1):
        if dp[i-1][j]==1:
            if j+volume[i-1]<=M:
                dp[i][j+volume[i-1]]=1
            if j-volume[i-1]>=0:
                dp[i][j-volume[i-1]]=1

def result():
    for i in range(M,-1,-1):
        if dp[N][i]==1:
            print(i)
            return
    print(-1)

result()
