# 피자 굽기 - G5

import sys

D,N=map(int,sys.stdin.readline().split())

depth=list(map(int,sys.stdin.readline().split()))
pizza=list(map(int,sys.stdin.readline().split()))

for i in range(1,D):
    if depth[i]>depth[i-1]:
        depth[i]=depth[i-1]

index=0
right=D-1

while index<N:
    result=0
    for i in range(right,-1,-1):
        if depth[i]>=pizza[index]:
            result=i+1
            right=i-1
            break
    if result==0:
        break
    index+=1

print(result)