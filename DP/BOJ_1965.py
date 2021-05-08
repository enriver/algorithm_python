# 상자넣기 - S2

import sys

if __name__=="__main__":
    n=int(sys.stdin.readline())
    box=list(map(int,sys.stdin.readline().split())) 

    dp=[0 for _ in range(n)]
    dp[0]=1

    for i in range(1,n):
        t=0

        while True:
            if t==i:
                break

            if box[t]<box[i]: # 현재 값보다 작은 박스들중 가장 큰 값을 가져옴
                dp[i]=max(dp[i],dp[t])

            t+=1

        dp[i]+=1

    print(max(dp))
