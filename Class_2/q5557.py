# 1학년 - G5

import sys

n=int(sys.stdin.readline())

num=list(map(int,sys.stdin.readline().split()))

dp=[[0 for _ in range(21)] for _ in range(n-1)]

dp[0][num[0]]=1

for i in range(1,n-1):
    for j in range(21):
        if dp[i-1][j]>0:
            if j+num[i]>=0 and j+num[i]<=20:
                dp[i][j+num[i]]+=dp[i-1][j]
            if j-num[i]>=0 and j-num[i]<=20:
                dp[i][j-num[i]]+=dp[i-1][j]
 
print(dp[n-2][num[-1]])