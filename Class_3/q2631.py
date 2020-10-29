# 줄세우기 - G5

import sys

n=int(sys.stdin.readline())

children=list()

dp=[1]*n
for i in range(n):
    children.append(int(sys.stdin.readline()))


for i in range(n):
    for j in range(i):
        if children[i] > children[j]:
            dp[i]=max(dp[i],dp[j]+1)

#print(n-max(dp))
print(dp)