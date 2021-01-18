# 열 개씩 끊어 출력하기 - B2

import sys
import math
word=sys.stdin.readline().strip()

length=math.ceil(len(word)/10)  
n=0
for i in range(length):
    print(word[n:n+10])
    n+=10