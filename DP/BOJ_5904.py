# Moo 게임 - S2

import sys


def solve(n,k):
    if k==0:
        return 'moo'[n-1]
    
    if n<=dp[k-1]:
        return solve(n,k-1)
    elif n<=dp[k-1]+k+3:
        if n-dp[k-1]-1==0:
            return 'm'
        else:
            return 'o'
    else:
        return solve(n-dp[k-1]-(k+3),k-1)

if __name__=="__main__":
    N=int(sys.stdin.readline())

    dp=[3]
    K=0

    while dp[K]<N:
        K+=1
        dp.append(2*dp[K-1]+K+3)

    print(solve(N,K))