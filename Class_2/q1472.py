#소트인사이드

import sys

word=sys.stdin.readline()

li=[]
for i in word[:-1]:
    li.append(int(i))

li=sorted(li,reverse=True)

for i in li:
    print(i, end="")