# 케빈 베이컨의 6단계 법칙 - S1

import sys
from collections import deque

def solve(num,order):
    count=0

    que=deque()
    que.append((num,order))
    
    visit=set()
    visit.add(num)

    while que:
        num,order=que.popleft()

        count+=order

        for i in range(1,N+1):
            if friend[num][i]==1 and i not in visit:
                visit.add(i)
                que.append((i,order+1))

    return count

if __name__=="__main__":
    N,M=map(int,sys.stdin.readline().split())

    friend=[[0 for _ in range(N+1)] for _ in range (N+1)]

    for _ in range(M):
        A,B=map(int, sys.stdin.readline().split())

        friend[A][B]=1
        friend[B][A]=1

    result=list()
    for i in range(1,N+1):
        result.append(solve(i,0))

    print(result.index(min(result))+1)
    