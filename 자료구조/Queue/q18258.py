# 큐2 - S4

import sys
from collections import deque

que=deque()

for i in range(int(sys.stdin.readline())):
    word=sys.stdin.readline().split()

    if len(word)>1:
        if word[0]=='push':
            que.append(word[1])

    else:
        if word[0]=='front':
            if len(que)>0:
                k=que[0]
                print(k)
            else:
                print(-1)

        elif word[0]=='size':
            print(len(que))

        elif  word[0]=='empty':
            if len(que)>0:
                print(0)
            else:
                print(1)

        elif word[0]=='back':
            if len(que)>0:
                k=que[-1]
                print(k)
            else:
                print(-1)

        elif word[0]=='pop':
            if len(que)>0:
                k=que.popleft()
                print(k)
            else:
                print(-1)