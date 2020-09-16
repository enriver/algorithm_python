#조합

import sys

n,r=map(int, sys.stdin.readline().split())

dp=[0 for _ in range(n+1)]

dp[0]=1
dp[1]=1

def factorial(num):
    if num>1:
        for i in range(2,num+1):
            dp[i]=i*dp[i-1]

factorial(n)

print(dp[n]//(dp[n-r]*dp[r]))