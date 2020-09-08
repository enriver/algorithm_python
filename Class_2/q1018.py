#체스판 다시 칠하기

import sys

n,m = map(int,sys.stdin.readline().split()) # n 행 m 렬

board=[[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    word=sys.stdin.readline()
    for j in range(m):
        board[i][j]=word[j]

print(board)