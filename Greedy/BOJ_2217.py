# 로프 - S4

import sys

if __name__=="__main__":
    N=int(sys.stdin.readline())
    rope=list()

    for _ in range(N):
        rope.append(int(sys.stdin.readline()))

    rope.sort(reverse=True)

    answer=0

    for i in range(N):
        answer=max(answer,rope[i]*(i+1))

    print(answer)
