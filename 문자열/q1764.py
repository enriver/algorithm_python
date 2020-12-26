# 듣보잡 - S4

import sys

N,M=map(int,sys.stdin.readline().split())

hear=set()
for _ in range(N):
    hear.add(sys.stdin.readline().rstrip())

see=set()
for _ in range(M):
    see.add(sys.stdin.readline().rstrip())

res=sorted(list(hear.intersection(see)))
print(len(res))
for i in res:
    print(i)
