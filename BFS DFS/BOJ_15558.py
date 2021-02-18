# 점프 게임 - S1 

import sys
from collections import deque

def solve(pos,line,num,time): # 현재위치, 현재라인, 라인넘버(0:left, right=1), 진행시간
    que=deque()
    que.append((pos,line,num,time))
    
    visit[num][pos]=True
    while que:
        pos,line,num,time=que.popleft()

        for i in [pos+1, pos-1, pos+K]:
            if i <= time:
                continue

            if i>=N:
                return 1

            if i==pos+K:
                if num==0:
                    line=right
                    num=1
                else:
                    line=left
                    num=0

            if line[i]==1 and not visit[num][i]:
                visit[num][i]=True
                que.append((i, line, num, time+1))

    return 0


if __name__=="__main__":
    N,K=map(int, sys.stdin.readline().split())
    visit=[[False for _ in range(N)] for _ in range(2)] # 0-> left, 1-> right 방문 체크

    left=list(map(int,sys.stdin.readline().rstrip()))
    right=list(map(int,sys.stdin.readline().rstrip()))


    print(solve(0,left,0,0))

