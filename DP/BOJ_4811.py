#알약

import sys


def pill(W,H):

    if dp[W][H]>0:
        return dp[W][H]
    
    if W==0:
        return 1
    
    if W>0 and H==0:
        dp[W][H]+=pill(W-1,H+1)
    elif W>0 and H>0:
        dp[W][H]+=pill(W-1,H+1)
        dp[W][H]+=pill(W,H-1)

    return dp[W][H]
    

while True:
    n=int(sys.stdin.readline())
    dp=[[0 for _ in range(31)] for _ in range(31)]

    if n==0:
        break
    else:
        print(pill(n,0))
        