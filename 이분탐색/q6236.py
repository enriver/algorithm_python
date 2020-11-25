# 용돈 관리 - S3

import sys

N,M =map(int,sys.stdin.readline().split())

plan=list()
for _ in range(N):
    money=int(sys.stdin.readline())
    plan.append(money)

left=max(plan)
right=sum(plan)

while left<right:
    mid=(left+right)//2
    count=1
    now=0

    for i in plan:
        if now+i>mid:
            count+=1
            now=i
        else:
            now+=i
    
    if count>M:
        left=mid+1
    else:
        right=mid

print(right)