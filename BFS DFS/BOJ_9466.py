# 텀 프로젝트 - G4

import sys

def solve(val): # partner[i]
    global res

    if val not in visit:
        visit.append(val)
        solve(partner[val])
    
    else:
        res+=len(visit)-visit.index(val)


if __name__=="__main__":
    T=int(sys.stdin.readline())

    for _ in range(T):
        num=int(sys.stdin.readline())

        partner=[0]
        partner.extend(list(map(int, sys.stdin.readline().split())))

        res=0
        visit=list()

        for i in range(1,num+1):
            if i not in visit and partner[i] not in visit:
                visit.append(i)
                solve(partner[i])

        print(num-res)