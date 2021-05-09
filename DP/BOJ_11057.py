# 오르막 수 - S1

import sys

if __name__=="__main__":
    N=int(sys.stdin.readline())
    dp=[[0 for _ in range(11)] for _ in range(N)]

    dp[0]=[1 for _ in range(11)]
    dp[0][10]=10
    
    for i in range(1,N):
        for j in range(11):
            if j==0:
                dp[i][j]=dp[i-1][10]
            elif j==10:
                dp[i][j]=sum(dp[i])
            else:
                dp[i][j]=dp[i][j-1]-dp[i-1][j-1]
           
    print(dp[N-1][10]%10007)