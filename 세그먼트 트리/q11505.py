#구간 곱 구하기 - P5

import sys

N,M,K=map(int,sys.stdin.readline().split())


def gugan(mat,start,end):
    sum=1
    for i in range(start,end+1):
        sum*=mat[i]

    return sum

num=[0]
for _ in range(N):
    n=int(sys.stdin.readline())
    num.append(n)


for _ in range(M+K):
    k=list(map(int,sys.stdin.readline().split()))
    if k[0]==1:
        num[k[1]]=k[2]
    elif k[0]==2:
        print(gugan(num,k[1],k[2]))



