import sys
from collections import deque


n=int(sys.stdin.readline())

que=deque()
for i in range(1,n+1):
    que.append(i)

while len(que)>1:
    que.popleft()
    k=que.popleft()
    que.append(k)

print(que.pop())
