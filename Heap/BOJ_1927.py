# 최소 힙 - s1

import sys
import heapq

if __name__=="__main__":
    N=int(sys.stdin.readline())
    heap=[]

    for i in range(N):
        n=int(sys.stdin.readline())

        if n==0:
            if heap:
                print(heapq.heappop(heap))
            else:
                print(0)
        else:
            heapq.heappush(heap, n)