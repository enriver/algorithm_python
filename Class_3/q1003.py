# 피보나치 함수

import sys

n=int(sys.stdin.readline())

zero=0
one=0

def fibonacci(n):
    global zero
    global one
    if n==0:
        zero+=1
        return 0
    elif n==1:
        one+=1
        return 1
    else:
        return fibonacci(n-2)+fibonacci(n-1)

for _ in range(n):
    m=int(sys.stdin.readline())

    fibonacci(m)

    print(zero,one)
    zero=0
    one=0



