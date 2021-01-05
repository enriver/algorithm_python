# 좌표 정렬하기 2 - S5

import sys

check=[list() for _ in range(200001)]

for i in range(int(sys.stdin.readline())):
    x,y=map(int,sys.stdin.readline().split())

    check[y].append(x)

for i in range(-100000,100001):
    if check[i]!=0:
        for j in sorted(check[i]):
            print(j,i)