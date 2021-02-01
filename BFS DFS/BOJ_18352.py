# 특정 거리의 도시 찾기 - S2

import sys
from collections import deque

                       
if __name__=="__main__":
    N,M,K,X=map(int,sys.stdin.readline().split())
    visit=[False]*(N+1)

    city=dict()
    for _ in range(M):
        A,B=map(int,sys.stdin.readline().split())

        if A not in city.keys():
            city[A]=list()

        city[A].append(B)

    result=set()

    que=deque()
    que.append((X,0))
    visit[X]=True

    while que:
        start,time=que.popleft()

        if time==K:
            result.add(start)
        elif time<K:
            if start in city.keys():
                for i in city[start]:
                    if not visit[i]:
                        visit[i]=True
                        que.append((i,time+1))

    if len(result)==0:
        print(-1)
    else:
        result=list(result)
        result.sort()
        for i in result:
            print(i)