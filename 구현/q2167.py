# 2차원 배열의 합 - B1

import sys

N,M =map(int,sys.stdin.readline().split())

array=[list() for _ in range(N)]
for i in range(N):
    array[i].extend(map(int,sys.stdin.readline().split()))

dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = array[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

k = int(input())
for _ in range(k):
    i, j, y, x = map(int, input().split())
    ans = dp[y][x] - dp[y][j - 1] - dp[i - 1][x] + dp[i - 1][j - 1]
    print(ans)