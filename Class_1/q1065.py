#한수

import sys

N=int(sys.stdin.readline())

count=0

for i in range(1,N+1):
    if i<=99:
        count+=1

    else:
        num=list(map(int,str(i)))
        if num[0] - num[1] == num[1] - num[2]:
            count+=1

print(count)