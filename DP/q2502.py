# 떡 먹는 호랑이 - S1

import sys

D,K = map(int,sys.stdin.readline().split())

i,j=1,1
dp=[0]*D

while True:
    dp[0]=i
    dp[1]=j
    day=2
    while day<D:
        dp[day]=dp[day-1]+dp[day-2]
        day+=1
    
    if dp[D-1]==K:
        print(i)
        print(j)
        break
    elif dp[D-1]>K:
        i+=1
        j=1
    else:
        j+=1

    