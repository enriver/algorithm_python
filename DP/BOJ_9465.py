# 스티커 - S2

import sys

T=int(sys.stdin.readline())

for _ in range(T):
    n=int(sys.stdin.readline())
    sticker=list()
    for i in range(2):
        sticker.append(list(map(int,sys.stdin.readline().split())))

    sticker[0][1]+=sticker[1][0]
    sticker[1][1]+=sticker[0][0]

    for j in range(2,n):
        sticker[0][j]=max(sticker[1][j-1],sticker[1][j-2])+sticker[0][j]
        sticker[1][j]=max(sticker[0][j-1],sticker[0][j-2])+sticker[1][j]

    print(max(sticker[0][-1],sticker[1][-1]))