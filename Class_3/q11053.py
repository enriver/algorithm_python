# 가장 긴 증가하는 부분 수열 - S2

import sys

N=int(sys.stdin.readline())
array=list(map(int,sys.stdin.readline().split()))

dp=[0 for _ in range(N)]


for i in range(N):
    for j in range(i):
        if array[i]>array[j]:
            dp[i]=max(dp[i],dp[j]+1)

print(max(dp)+1)