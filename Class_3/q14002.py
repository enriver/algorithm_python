# 가장 긴 증가하는 부분수열4 - G4   

import sys

n=int(sys.stdin.readline())

num_arr=list(map(int,sys.stdin.readline().split()))

dp=[1 for _ in range(n)]
route=[0 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if num_arr[i]>num_arr[j]:
            if dp[i]>dp[j]+1:
                continue
            else:
                dp[i]=dp[j]+1
                route[i]=j


print(max(dp))
back=dp.index(max(dp))

result=list()

for i in range(max(dp)):
    result.append(num_arr[back])
    back=route[back]

print(*sorted(result))