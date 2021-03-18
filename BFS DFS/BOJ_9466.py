# 텀 프로젝트 - G4

import sys

sys.setrecursionlimit(10**9)

def solve(val): 
    global res
    
    if val not in visit:
        visit.add(val)
        
        stack.append(val)
        solve(partner[val])

    else:
        if val in stack:
            res+=len(stack)-stack.index(val)

if __name__=="__main__":
    T=int(sys.stdin.readline())

    for _ in range(T):
        num=int(sys.stdin.readline())

        partner=[0]
        partner.extend(list(map(int, sys.stdin.readline().split())))

        res=0
        visit=set()

        for i in range(1, num+1):
            if i not in visit and partner[i] not in visit:
                visit.add(i)

                stack=[i]
                solve(partner[i])

        print(num-res)