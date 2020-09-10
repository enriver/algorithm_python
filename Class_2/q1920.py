#수 찾기

import sys

n=sys.stdin.readline()
num=set(sys.stdin.readline().split())
m=sys.stdin.readline()
compare=sys.stdin.readline().split()


for j in compare:
    if j in num:
        print(1)
    else:
        print(0)
