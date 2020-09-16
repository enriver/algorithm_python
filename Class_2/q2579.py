#계단 오르기

import sys

N=int(sys.stdin.readline())

stairs=[0]

for _ in range(N):
    stairs.append(int(sys.stdin.readline()))

dp=[[0 for _ in range(2)] for _ in range(301)]

dp[1][0]=dp[1][1]=stairs[1]

def climing(num):
    if num>1:
        for i in range(2, num+1):
            dp[i][0]=max(stairs[i]+dp[i-2][0],stairs[i]+dp[i-2][1])
            dp[i][1]=stairs[i]+dp[i-1][0]

climing(N)

print(max(dp[N]))