# 텀 프로젝트 - G4

import sys
from collections import deque

sys.setrecursionlimit(10**9)

def solve(val): 
    global res
    
    visit.add(val)
    stack.append(val)

    if partner[val] not in visit:
        solve(partner[val])

    else:
        if partner[val] in stack:
            res+=len(stack)-stack.index(partner[val])

if __name__=="__main__":
    T=int(sys.stdin.readline())

    for _ in range(T):
        num=int(sys.stdin.readline())

        partner=[0]
        partner.extend(list(map(int, sys.stdin.readline().split())))

        res=0
        visit=set()

        for i in range(1, num+1):
            if i not in visit:
                stack=list()
                solve(i)

        print(num-res)