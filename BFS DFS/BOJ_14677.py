# 병약한 윤호 - G5

import sys
from collections import deque

def bfs():
    que=deque()
    que.append((0,0))
    
    day=-1
    order=0

    while que:
        size=len(que)

        while True:
            if size==0:
                break
            left, right=que.popleft()

            if left+right<T: 
                if pill[left]==BLD[order] and dp[left+1][right]==0:
                    que.append((left+1,right))
                    dp[left+1][right]=1
                
                if pill[T-1-right]==BLD[order] and dp[left][right+1]==0:
                    que.append((left, right+1))
                    dp[left][right+1]=1

            size-=1

        order=(order+1)%3
        day+=1

    return day


if __name__=="__main__":                 
    N=int(sys.stdin.readline())
    T=3*N

    BLD=['B','L','D']

    pill=list(sys.stdin.readline().rstrip())

    dp=[[0 for _ in range(T+1)] for _ in range(T+1)]
    dp[0][0]=1

    print(bfs())