# 제로 - S4

import sys

n=int(sys.stdin.readline())

stack=[]
for _ in range(n):
    m= int(sys.stdin.readline())
    if m!=0:
        stack.append(m)
    else:
        stack.pop()
sum=0
for i in stack:
    sum+=i

print(sum)