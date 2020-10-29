# 줄세우기 - G5

import sys

n=int(sys.stdin.readline())

arr=list(map(int,sys.stdin.readline().split()))

dp=[0]*(n+1)

for i in range(n):
    dp[arr[i]]=dp[arr[i]-1]+1

print(dp)
print(n-max(dp))