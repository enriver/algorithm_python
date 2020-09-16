#덱

import sys
from collections import deque

que=deque()
for _ in range(int(sys.stdin.readline())):
    a=list(sys.stdin.readline().split())
    
    if a[0]=='push_back':
        que.append(int(a[1]))
    
    elif a[0]=='push_front':
        que.appendleft(int(a[1]))
    
    elif a[0]=='pop_front':
        if len(que)==0:
            print(-1)
        else:
            x=que.popleft()
            print(x)
    elif a[0]=='pop_back':
        if len(que)==0:
            print(-1)
        else:
            x=que.pop()
            print(x)
    elif a[0]=='size':
        print(len(que))
    elif a[0]=='empty':
        if len(que)==0:
            print(1)
        else:
            print(0)
    elif a[0]=='front':
        if len(que)==0:
            print(-1)
        else:
            print(que[0])
    elif a[0]=='back':
        if len(que)==0:
            print(-1)
        else:
            print(que[-1])