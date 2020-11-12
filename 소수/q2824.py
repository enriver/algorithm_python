# 최대공약수 - G5

import sys
import math

N=int(sys.stdin.readline())
n_li=map(int,sys.stdin.readline().split())

M=int(sys.stdin.readline())
m_li=map(int,sys.stdin.readline().split())

a,b=1,1

for i in n_li:
    a*=i
for j in m_li:
    b*=j

answer=str(math.gcd(a,b))

if len(answer)>9:
    print(answer[len(answer)-9:])
else:
    print(answer)