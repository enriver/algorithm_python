#동전 0

import sys
from collections import deque

N,K = map(int, sys.stdin.readline().split())

coin=list()
for _ in range(N):
    coin.append(int(sys.stdin.readline()))


def min_coin(cnt,value):
    que=deque()
    que.append((cnt,value))

    while que:
        cnt,value=que.popleft()
    
        if value==0:
            break

        if len(coin)==1:
            cnt=value//coin[0]
            break

        else:
            for i in range(0,len(coin)):
                if coin[i]>value:
                    cnt+=value//coin[i-1]
                    value%=coin[i-1]
                    
                    que.append((cnt,value))
                    break

            cnt+=value//coin[-1]
            value%=coin[-1]
            que.append((cnt,value))
    return cnt


print(min_coin(0,K))