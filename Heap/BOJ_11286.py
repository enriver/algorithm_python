# 절댓값 힙 - S1

import sys
import heapq as hq

if __name__=="__main__":
    N=int(sys.stdin.readline())
    heap=[]

    for _ in range(N):
        n=int(sys.stdin.readline())

        if n==0:
            if heap:
                print(hq.heappop(heap)[1])
            else:
                print(0)

        else:
            hq.heappush(heap, (abs(n), n))
