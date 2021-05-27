# 여왕벌 - G4

import sys

if __name__=="__main__":
    M,N=map(int,sys.stdin.readline().split()) # 가로세로크기, 날짜수
    
    bees=[[1 for _ in range(M)] for _ in range(M)]
    add=[0 for _ in range(2*M-1)]
    
    for _ in range(N):
        zero,one,two=map(int,sys.stdin.readline().split())

        for i in range(zero, zero+one):
            add[i]+=1
        for i in range(zero+one, zero+one+two):
            add[i]+=2

    for i in range(2*M-1):
        if i<M:
            bees[M-1-i][0]+=add[i]
        elif i==M-1:
            bees[0][0]+=add[i]
        else:
            bees[0][i-M+1]+=add[i]

    for i in range(1,M):
        for j in range(1,M):
            bees[i][j]=bees[i-1][j]

    for i in range(M):
        print(*bees[i])
    
    '''
    저장해서 출력하는게 더 빠름
    
    for i in range(M):
        for j in range(M):
            if j>=1:
                print(bees[0][j],end=' ')
            else:
                print(bees[i][j],end=' ')
        print()
    '''