# sqrt log sin - s1

import sys
import math

limit=1000001
dp=[0]*limit
dp[0]=1

i=1
while i<limit:
    sqrt=int(i-math.sqrt(i))
    log=int(math.log(i))
    sin=int(i*math.sin(i)**2)

    dp[i]=dp[sqrt]+dp[log]+dp[sin]

    i+=1

while True:
    num=int(sys.stdin.readline())

    if num==-1:
        break
    else:
        print(dp[num]%1000000)