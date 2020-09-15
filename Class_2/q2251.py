#물통

import sys
from collections import deque

A,B,C=map(int,sys.stdin.readline().split())
visit=[[False for _ in range(201)] for _ in range(201)]


def check(a,b,c):
    que=deque()
    que.append((a,b,c))

    while que:
        aa,bb,cc=que.popleft()

        if not visit[aa][bb]:
            visit[aa][bb]=True

            if aa==0:
                val.add(cc)
        
            # C->A
            if cc+aa<=A:
                que.append((aa+cc,bb,0))
            else:
                que.append((A,bb,cc+aa-A))
            
            # C->B
            if cc+bb<=B:
                que.append((aa,cc+bb,0))
            else:
                que.append((aa,B,cc+bb-B))

            # A->B
            if aa+bb<=B:
                que.append((0,aa+bb,cc))
            else:
                que.append((aa+bb-B,B,cc))
            
            # A->C
            if aa+cc<=C:
                que.append((0,b,aa+cc))
            else:
                que.append((aa+cc-C,b,C))

            # B->A
            if bb+aa<=A:
                que.append((bb+aa,0,c))
            else:
                que.append((A,bb+aa-A,c))
            
            # B->C
            if bb+cc<=C:
                que.append((aa,0,bb+cc))
            else:
                que.append((aa,bb+cc-C,C))
        

val=set()
check(0,0,C)

val_li=list(val)

print(*sorted(val_li))