# IOIOI - S2

# KMP - Knuth Morris-Pratt 알고리즘
# https://www.youtube.com/watch?v=-AjGdS-eKGE


import sys

N=int(sys.stdin.readline())
M=int(sys.stdin.readline())
S=sys.stdin.readline().strip()

index=0
count=0
result=0

while index < M :
    if S[index:index+3]=='IOI':
        count+=1
        index+=2 # M 길이 만큼 탐색하기 위해서 마지막 I 값으로 이동
        if count>=N:
            result+=1
    else:
        count=0
        index+=1

print(result)


'''
# DP 풀이

import sys

N=int(sys.stdin.readline())

M=int(sys.stdin.readline())

S=sys.stdin.readline().strip()

dp = [0 for _ in range(M)]

for i in range(2, M):
    if S[i] == "O":
        continue
    if S[i-1] == "O" and S[i-2] == "I":
        dp[i] = dp[i-2] + 1

result = 0
for val in dp:
    if val >= N:
        result += 1

print(result)

'''