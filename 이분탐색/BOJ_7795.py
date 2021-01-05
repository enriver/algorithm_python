# 먹을 것인가 먹힐 것인가 - S3

import sys

T=int(sys.stdin.readline())

'''
이분탐색 풀이
'''
for _ in range(T):
    N,M=map(int,sys.stdin.readline().split())
    A=list(map(int,sys.stdin.readline().split()))
    B=list(map(int,sys.stdin.readline().split()))

    A.sort()
    count=0

    for i in B:
        left=0
        right=N-1

        if i < A[-1]:     
            while left<right:
                mid=(left+right)//2

                if A[mid]>i:
                    right=mid
                else:
                    left=mid+1
            count+=N-right

    print(count)


#더 좋은 효율 풀이

'''
import sys

T=int(sys.stdin.readline())

for _ in range(T):
    N,M=map(int,sys.stdin.readline().split())
    A=list(map(int,sys.stdin.readline().split()))
    B=list(map(int,sys.stdin.readline().split()))

    A.sort()
    B.sort()
    count=0
    i=0
    j=0

    while i<N and j<M:
        if A[i]>B[j]:
            count+=N-i
            j+=1
        else:
            i+=1

    print(count)
'''