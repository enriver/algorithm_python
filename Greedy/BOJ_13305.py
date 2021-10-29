# 주유소 - S4

import sys

if __name__=="__main__":
    N=int(sys.stdin.readline())
    dist=list(map(int,sys.stdin.readline().split()))
    oil=list(map(int,sys.stdin.readline().split()))

    stack=oil[0]
    ans=oil[0]*dist[0]

    for i in range(1,N-1):
        if stack > oil[i]:
            stack=oil[i]

        ans+=stack*dist[i]

    print(ans)