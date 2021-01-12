# 이모티콘 - G5

import sys
from collections import deque

S=int(sys.stdin.readline())

dp=[[0 for _ in range(S+1)] for _ in range(S+1)]
dp[1][0]=1

que=deque()
que.append((1,0))

while que:
    i,j = que.popleft()

    if i<=S+1:
        if dp[i][i]=0:
            dp[i][i]=dp[i][j]+1
            que.append((i,i))
    
    if i+j <=1000:
