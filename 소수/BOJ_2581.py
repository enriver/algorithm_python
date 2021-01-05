# 소수 - S4

import math
import sys


def isPrime(num):
    if num==1: return False

    sqrt=int(math.sqrt(num))

    for k in range(2, sqrt+1):
        if num % k==0: return False
    return True

M=int(sys.stdin.readline())
N=int(sys.stdin.readline())

prime_list=list()
for i in range(M,N+1):
    if isPrime(i)==True:
        prime_list.append(i)
        
if len(prime_list)==0:
    print(-1)
else:
    print(sum(prime_list))
    print(prime_list[0])
