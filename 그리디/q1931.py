# 회의실배정 - S2

import sys

N=int(sys.stdin.readline()) # 회의의 수

time=list()

for _ in range(N):
    t1, t2=map(int,sys.stdin.readline().split())
    time.append((t1,t2))

time.sort(key=lambda x:(x[1],x[0]))


count=1
standard=time[0][1]

for i in range(1,N):
    if time[i][0] >= standard:
        standard=time[i][1]
        count+=1

print(count)