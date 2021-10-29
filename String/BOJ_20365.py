# 블로그 - S2

import sys

if __name__=="__main__":
    N=int(sys.stdin.readline()) # 색을 칠해야 하는 문제의 수
    problem=list(sys.stdin.readline().rstrip())

    origin=problem[0]
    count=1

    for i in range(1,N):
        if problem[i]==origin:
            pass
        else:
            current=problem[i]
            count+=1

    print(count)