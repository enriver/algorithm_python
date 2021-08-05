#정수 삼각형 - S1

import sys

n=int(sys.stdin.readline())

val=[]
for _ in range(n):
    val.append(list(map(int,sys.stdin.readline().split())))

for i in range(1,n):
    for j in range(i+1):
        if j==0: # 맨 왼쪽인 경우
            val[i][j]+=val[i-1][j] 
        elif j==i: # 맨 오른쪽인 경우
            val[i][j]+=val[i-1][j-1]
        else:
            val[i][j]+=max(val[i-1][j-1], val[i-1][j])

print(max(val[n-1]))