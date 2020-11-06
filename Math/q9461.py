#파도반 수열

import sys

n=int(sys.stdin.readline())

pp=[0]*101

pp[1]=1
pp[2]=1
pp[3]=1

def pado(num):
    if num>3:
        for i in range(4,num+1):
            pp[i]=pp[i-2]+pp[i-3]

for _ in range(n):
    k=int(sys.stdin.readline())
    pado(k)
    print(pp[k])