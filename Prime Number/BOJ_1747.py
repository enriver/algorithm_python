# 소수 & 팰린드롬 - G5

import sys
import math

def isPrime(num):
    if num==1: return False

    sqrt=int(math.sqrt(num))

    for k in range(2, sqrt+1):
        if num % k==0: return False
    return True

n=int(sys.stdin.readline())

def isPalindrome(num):
    li=list(num)
    li.reverse()
    val=''.join(li)

    if num==val:
        return True
    else:
        return False

while True:
    if isPrime(n)==True:
        if isPalindrome(str(n))==True:
            break
        else:
            n+=1
    else:
        n+=1

print(n)