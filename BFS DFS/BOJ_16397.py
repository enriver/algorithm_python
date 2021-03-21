# 탈출 - G4

import sys
from collections import deque

def solve(n,cnt):
    que=deque()
    que.append((n, cnt))

    visit[n]=True

    while que:
        now, cnt=que.popleft()

        if cnt>T:
            print('ANG')
            return
        else:
            if now==G:
                print(cnt)
                return
            elif now>=0:
                if now+1<=99999:
                    if not visit[now+1]:
                        visit[now+1]=True
                        que.append((now+1, cnt+1))

                if now!=0:
                    now*=2

                    if now<=99999:
                        length=len(str(now))

                        if length==1:
                            now-=1
                        elif length==2:
                            now-=10
                        elif length==3:
                            now-=100
                        elif length==4:
                            now-=1000
                        elif length==5:
                            now-=10000

                        if not visit[now]:
                            visit[now]=True
                            que.append((now, cnt+1))
    
    print('ANG')
    return
                
if __name__=="__main__":
    N, T, G = map(int, sys.stdin.readline().split())

    visit=[False for _ in range(100000)]

    solve(N,0)