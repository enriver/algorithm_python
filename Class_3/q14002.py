# 가장 긴 증가하는 부분수열4 - G4   

import sys

n=int(sys.stdin.readline())

num_arr=list(map(int,sys.stdin.readline().split()))

dp=[0 for _ in range(n)]
asc=[[x] for x in num_arr]

for i in range(n):
    for j in range(i):
        if num_arr[i]>num_arr[j]:
            if dp[i]>dp[j]+1:
                continue
            else:
                dp[i]=dp[j]+1
                asc[i]=asc[j]+[num_arr[i]]

length=0
for i in range(len(asc)):
    if len(asc[i])>length:
        length=len(asc[i])
        position=i

#print(dp)
#print(asc)
print(length)
print(*asc[position])