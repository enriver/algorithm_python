# 문자열 집합 - S3

import sys

N,M=map(int,sys.stdin.readline().split())

s=set()
for _ in range(N):
    s.add(sys.stdin.readline().strip())

count=0

for _ in range(M):
    word=sys.stdin.readline().strip()
    if word in s:
        count+=1

print(count)