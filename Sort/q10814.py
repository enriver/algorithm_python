# 나이순 정렬 - S5

import sys

n=int(sys.stdin.readline())

member=list()
for i in range(n):
    age,name=sys.stdin.readline().split()
    member.append((int(age),i,name))

member.sort()

for i in member:
    print(i[0],i[2])