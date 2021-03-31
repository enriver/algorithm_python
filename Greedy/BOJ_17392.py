# 우울한 방학 - S1

import sys

if __name__=="__main__":
    N,M=map(int,sys.stdin.readline().split()) # 약속 N, 방학일수 M

    happiness=list(map(int,sys.stdin.readline().split()))

    for i in happiness:
        M-=i+1

    feel=0
    
    if M>0:
        q=M//(N+1)
        r=M%(N+1)
        
        for i in range(q):
            feel+=(i+1)**2*(N+1)
        for _ in range(r):
            feel+=(q+1)**2

    print(feel)

    