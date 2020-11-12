# 가르침 - G4

import sys
from collections import Counter

N,K=map(int,sys.stdin.readline().split())

word=list()
for _ in range(N):
    word.extend(sys.stdin.readline().strip().replace('a','').replace('n','').replace('t','').replace('i','').replace('c',''))

print(Counter(word).most_common())


# k가 6보다 커야 o 5보다 작으면 x