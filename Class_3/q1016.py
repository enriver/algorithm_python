#제곱 ㄴㄴ수

import sys

min,max=map(int,sys.stdin.readline().split())

eratos=[False for _ in range(min,max+1)]

cnt=max-min+1
i=2
while i**2 <=max:
    s=min//(i**2)

    if min%(i**2)!=0:
        s+=1

    while s*(i**2)<=max:
        if not eratos[s*(i**2) - min]:
            eratos[s*(i**2)-min]=True
            cnt-=1
        s+=1
    i+=1

print(cnt)