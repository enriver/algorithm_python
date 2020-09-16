#정수 삼각형

import sys

n=int(sys.stdin.readline())

val=[]
for _ in range(n):
    val.append(list(map(int,sys.stdin.readline().split())))


val[1][0]=val[1][0]+val[0][0]
val[1][1]=val[1][1]+val[0][0]

k=3
for i in range(2,n):
    for j in range(k):
        if j==0:
            val[i][j]=val[i][j]+val[i-1][j]
        elif j==(k-1):
            val[i][-1]=val[i][-1]+val[i-1][-1]
        else:
            val[i][j]=max(val[i][j]+val[i-1][j-1],val[i][j]+val[i-1][j])
    k+=1

print(max(val[n-1]))