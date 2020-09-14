#신기한 소수

import sys

n=int(sys.stdin.readline())


def isPrime(num):
    if num==1: return False

    sqrt=int(math.sqrt(num))

    for k in range(2, sqrt+1):
        if num % k==0: return False
    return True

def mysterious(num):
    val=num
    while val>0:
        if isPrime(val)==True:
            continue
        else:
            return False
        val=val/10
    return True


now=int('9'*(n-1))+1
primeStack=list()

while now<=int('9'*n):
    if mysterious(now) == True:
        primeStack.append(now)
    now+=1

print(primeStack)