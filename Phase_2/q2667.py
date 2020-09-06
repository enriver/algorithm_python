#단지번호붙이기
import sys

n=int(sys.stdin.readline())
matrix=[[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    house=sys.stdin.readline()
    for j in range(n):
        matrix[i][j]=int(house[j])

print(matrix)