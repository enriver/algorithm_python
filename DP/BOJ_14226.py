# 이모티콘 - G5

import sys
from collections import deque

S=int(sys.stdin.readline())

visit=[[0 for _ in range(S+1)] for _ in range(S+1)]

def bfs():
    que=deque()
    que.append((1,0))

    while que:
        w,c=que.popleft()

        if w==S:
            print(visit[w][c])
            return
        
        for nx,ny in [(w,w),(w+c,c),(w-1,c)]:
            if nx<0 or nx>S:
                continue
            if not visit[nx][ny]:
                que.append((nx,ny))
                visit[nx][ny]=visit[w][c]+1

bfs()