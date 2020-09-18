#숨바꼭질2 - G5

import sys
from collections import deque

N,K = map(int,sys.stdin.readline().split())

limit=100001

visit=[False]*limit

def bfs(now,move):
    global stack
    que=deque()
    que.append((now,move))

    while que:
        now,move=que.popleft()
        visit[now]=True

        if now==K:
            stack.append(move)

        li=[now-1,now+1,2*now]
        for i in li:
            if 0<=i<limit and not visit[i]:
                que.append((i,move+1))
    
stack=[]
bfs(N,0)
print(stack[0])

count=1
for i in stack[1:]:
    if stack[0]==i:
        count+=1

print(count)