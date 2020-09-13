#소수 찾기

import sys

n=int(sys.stdin.readline())

li=list(map(int,sys.stdin.readline().split()))


def isPrime(num):
    if num<2:
        return False
    else:
        for i in range(2,num):
            if num%i==0:
                return False
        return True

count=0
for i in li:
    if isPrime(i)==True:
        count+=1

print(count)