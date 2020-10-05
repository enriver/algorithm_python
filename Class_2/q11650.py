# 11650 좌표 정렬하기 - S5

import sys

n=int(sys.stdin.readline())

check=[list() for _ in range(200001)]

for i in range(n):
    x,y=map(int,sys.stdin.readline().split())
    check[x].append(y)

for i in range(-100000,100001):
    if check[i]!=0:
        for j in sorted(check[i]):
            print(i,j)