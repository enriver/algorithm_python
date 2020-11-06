#분해합

import sys

n=int(sys.stdin.readline())


result=0

for i in range(n):
    now=i
    for j in str(i):
        i+=int(j)
    if i==n:
        result=now
        break

print(result)