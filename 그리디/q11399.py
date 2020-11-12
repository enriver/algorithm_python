# ATM - S3

import sys

N=int(sys.stdin.readline())

dp=[0]*N

time=list(map(int,sys.stdin.readline().split()))
time.sort()

dp[0]=time[0]
for i in range(1,N):
    dp[i]=dp[i-1]+time[i]

print(sum(dp))
