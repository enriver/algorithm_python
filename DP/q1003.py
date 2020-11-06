# 피보나치 함수

import sys

n=int(sys.stdin.readline())

dp=[[0]*2 for _ in range(41)]

dp[0]=[1,0]
dp[1]=[0,1]

dp[2][0]=dp[0][0]+dp[1][0]
dp[2][1]=dp[0][1]+dp[1][1]

def fibonacci(num):
    for i in range(2, num+1):
        dp[i][0]=dp[i-1][0]+dp[i-2][0]
        dp[i][1]=dp[i-1][1]+dp[i-2][1]


for _ in range(n):
    k=int(sys.stdin.readline())
    fibonacci(k)
    print(dp[k][0], end=' ')
    print(dp[k][1])