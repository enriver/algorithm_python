#격자상의 경로

import sys

N,M,K = map(int,sys.stdin.readline().split())

mat=[[1 for _ in range(M+1)] for _ in range(N+1)]


if K==0:
    for i in range(1,N+1):
        for j in range(1,M+1):
            mat[i][j]=mat[i-1][j]+mat[i][j-1]

else:
    number=1

    for i in range(N):
        for j in range(M):
            if number==K:
                x,y=i,j
            number+=1

    for i in range(1,x+1):
        for j in range(1,y+1):
            mat[i][j]=mat[i-1][j]+mat[i][j-1]

    mid=mat[x][y]

    for i in range(y,M):
        mat[x][i]=mid
    for j in range(x,N):
        mat[j][y]=mid

    for i in range(x+1,N+1):
        for j in range(y+1,M+1):
            mat[i][j]=mat[i-1][j]+mat[i][j-1]

print(mat[N-1][M-1])