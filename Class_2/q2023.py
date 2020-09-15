#신기한 소수

import sys
import math

n=int(sys.stdin.readline())


def isPrime(num):
    if num==1: return False

    sqrt=int(math.sqrt(num))

    for k in range(2, sqrt+1):
        if num % k==0: return False
    return True

def checkPrime(num):
    if len(num)==n:
        print(num)
    
    for i in ['1','3','5','7','9']:
        val=num+i
        if isPrime(int(val)):
            checkPrime(val)



for i in ['2','3','5','7']:
    checkPrime(i)