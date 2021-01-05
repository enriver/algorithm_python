# 단어 정렬 - S5

import sys

n=int(sys.stdin.readline())

num=set()
for i in range(n):
    num.add(sys.stdin.readline())

num_sort=list()

for i in num:
    num_sort.append((len(i),i))

num_sort.sort()

for i in num_sort:
    print(i[1], end='')