# 신입사원 - S1

import sys

T=int(sys.stdin.readline())

for _ in range(T):
    N=int(sys.stdin.readline())

    employee=list()
    for _ in range(N):
        r1,r2=map(int,sys.stdin.readline().split())
        employee.append((r1,r2))
    
    employee.sort()

    count=1
    standard=employee[0][1]

    for i in range(1,N):
        if employee[i][1]<standard:
            standard=employee[i][1]
            count+=1

    print(count)