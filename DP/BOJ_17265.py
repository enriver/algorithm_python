# 나의 인생에는 수학과 함께 - G5

import sys

N=int(sys.stdin.readline())

route=list()

for _ in range(N):
    route.append(sys.stdin.readline().split())

max_dp=[[0 for _ in range(N)] for _ in range(N)]
min_dp=[[0 for _ in range(N)] for _ in range(N)]

min_dp[0][0]=max_dp[0][0]=route[0][0]

for i in range(2,N,2):
    max_dp[0][i]=str(eval(max_dp[0][i-2]+route[0][i-1]+route[0][i]))
    min_dp[0][i]=str(eval(min_dp[0][i-2]+route[0][i-1]+route[0][i]))
    max_dp[i][0]=str(eval(max_dp[i-2][0]+route[i-1][0]+route[i][0]))
    min_dp[i][0]=str(eval(min_dp[i-2][0]+route[i-1][0]+route[i][0]))


for x in range(1, N):
    for y in range(1, N):
        if (x + y) % 2 == 1:
            continue
        max_dp[x][y] = max(eval(max_dp[x-1][y-1]+route[x-1][y]+route[x][y]), eval(max_dp[x-1][y-1]+route[x][y-1]+route[x][y]))
        min_dp[x][y] = min(eval(min_dp[x-1][y-1]+route[x-1][y]+route[x][y]), eval(min_dp[x-1][y-1]+route[x][y-1]+route[x][y]))

        if x > 1:
            max_dp[x][y] = max(max_dp[x][y], eval(max_dp[x-2][y] + route[x-1][y] + route[x][y]))
            min_dp[x][y] = min(min_dp[x][y], eval(min_dp[x-2][y] + route[x-1][y] + route[x][y]))
        if y > 1:
            max_dp[x][y] = max(max_dp[x][y], eval(max_dp[x][y-2] + route[x][y-1] + route[x][y]))
            min_dp[x][y] = min(min_dp[x][y], eval(min_dp[x][y-2] + route[x][y-1] + route[x][y]))

        max_dp[x][y] = str(max_dp[x][y])
        min_dp[x][y] = str(min_dp[x][y])
        
print(max_dp)
print(max_dp[-1][-1],min_dp[-1][-1])
        