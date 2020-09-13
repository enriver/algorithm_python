#신기한 소수

import sys

n=int(sys.stdin.readline())


def isPrime(num):
    if num<2:
        return False
    else:
        for i in range(2,num):
            if num%i==0:
                return False
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