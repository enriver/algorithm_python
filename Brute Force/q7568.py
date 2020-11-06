#덩치

import sys

n=int(sys.stdin.readline())

weight=list()
height=list()

for _ in range(n):
    w,h=map(int,sys.stdin.readline().split())
    weight.append(w)
    height.append(h)

rank=list()

count=1
for i in range(n):
    for j in range(n):
        if weight[i]<weight[j] and height[i]<height[j]:
            count+=1
    rank.append(count)
    count=1

print(*rank)