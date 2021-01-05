# 가르침 - G4

import sys
from itertools import combinations

N,K=map(int,sys.stdin.readline().split())

if K < 5:
    print(0)
elif K==26:
    print(N)
else:    
    text = []
    alpha = set('acint')
    check = set()

    for _ in range(N):
        word = set(sys.stdin.readline().strip())
        text.append(word)
        check = check.union(word)
    
    check = check - alpha
    
    answer = 0
    for c in combinations(check, min(K-5, len(check))):
        count = 0
        subset = set(c).union(alpha)
        for word in text:
            if word.issubset(subset):
                count += 1
        
        answer=max(answer,count)
    print(answer)