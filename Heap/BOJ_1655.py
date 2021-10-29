# 가운데를 말해요 - G2

import sys
import heapq as hq

if __name__=="__main__":
    N=int(sys.stdin.readline())
    min_h, max_h=list(), list()

    for _ in range(N):
        n=int(sys.stdin.readline())

        if len(min_h) == len (max_h):
            hq.heappush(min_h, -n)
        else:
            hq.heappush(max_h, n)

        if len(min_h) > 0 and len(max_h) > 0:
            if -min_h[0] > max_h[0]:
                min_val=-hq.heappop(min_h)
                max_val=hq.heappop(max_h)

                hq.heappush(min_h, -max_val)
                hq.heappush(max_h, min_val)

        print(-min_h[0])