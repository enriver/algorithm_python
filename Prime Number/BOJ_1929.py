# 소수 구하기

import sys
import math

n,m=map(int,sys.stdin.readline().split())

def isPrime(num):
    if num==1: return False

    sqrt=int(math.sqrt(num))

    for k in range(2, sqrt+1):
        if num % k==0: return False
    return True

for i in range(n,m+1):
    if isPrime(i)==True:
        print(i)