# 가장 큰 정사각형 - G5

import sys

n,m=map(int, sys.stdin.readline().split())
dp=[[0 for _ in range(m)] for _ in range(n)]

array=list()
for _ in range(n):
    array.append(list(map(int,list(sys.stdin.readline().strip()))))

side=0
for i in range(1,n):
    for j in range(1,m):
        if array[j][j]==1:
            dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
            side=max(side,dp[i][j])
            
print(side**2)
    
