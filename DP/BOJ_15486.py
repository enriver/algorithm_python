# 퇴사 2 - S2

import sys

N=int(sys.stdin.readline())
counsel=list()

for _ in range(N):
    T,P=map(int,sys.stdin.readline().split())

    counsel.append((T,P))

dp=[0]*(N+1)

for i in range(N):
    if i+counsel[i][0]<=N: # 범위를 벗어나지 않을때
        dp[i+counsel[i][0]]=max(dp[i+counsel[i][0]], dp[i]+counsel[i][1])
    dp[i+1]=max(dp[i+1],dp[i])

print(dp[N])

'''
dp 의미 : 해당 날짜에 도달했을 때 벌 수 있는 최대금액
'''