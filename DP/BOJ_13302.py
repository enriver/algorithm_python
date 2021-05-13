# 리조트 - G5
'''
dp 는 어렵다. 근데 DFS와 함께하니 더 모르겠다
java팀의 풀이방법을 들어보자...!
'''
import sys

def solve(day,coupon):
    if day>N:
        return 0

    if dp[day][coupon]!=INF:
        return dp[day][coupon]

    if day in rest: # 요기 이해안됨
        dp[day][coupon]=solve(day+1,coupon)
        return dp[day][coupon]

    dp[day][coupon]=min(dp[day][coupon], solve(day+1, coupon)+10000) # 하루
    dp[day][coupon]=min(dp[day][coupon], solve(day+3, coupon+1)+25000) # 3일
    dp[day][coupon]=min(dp[day][coupon], solve(day+5, coupon+2)+37000) # 5일

    if coupon>=3: # 쿠폰사용
        dp[day][coupon]=min(dp[day][coupon], solve(day+1, coupon-3))

    return dp[day][coupon]

if __name__=="__main__":
    N,M = map(int, sys.stdin.readline().split()) # N 여름방학 일 수, M 리조트 못가는 날 수
    
    INF=float('inf')

    dp=[[INF for _ in range(N+1)] for _ in range(N+1)]
    rest=list(map(int,sys.stdin.readline().split()))

    print(solve(1,0))