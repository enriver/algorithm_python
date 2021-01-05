# 수 정렬하기 3 - S4

import sys

num_li=[0]*10001

for i in range(int(sys.stdin.readline())):
    num_li[int(sys.stdin.readline())]+=1

for i in range(10001):
    if num_li[i]!=0:
        for j in range(num_li[i]):
            print(i)