# 검증수

import sys

num=list(map(int,sys.stdin.readline().split()))

sum=0

for i in num:
    sum+=i**2

print(sum%10)