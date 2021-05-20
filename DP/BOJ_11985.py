# 오렌지 출하 - G5

import sys

if __name__=="__main__":
    N,M,K=map(int,sys.stdin.readline().split()) # 오렌지 갯수, 들어가는 갯수, 포장 비용
    A=[0]

    for _ in range(N):
        A.append(int(sys.stdin.readline()))

    dp=[0 for _ in range(N+1)]
    dp[1]=K

    for i in range(2,N+1):
        dp[i]=K*i # 각자 넣는 경우

        minVal=A[i]
        maxVal=A[i]
        for j in range(1,M+1):
            if (i-j)<0:
                break
            
            minVal=min(minVal,A[i-j+1])
            maxVal=max(maxVal,A[i-j+1])

            cost=K+j*(maxVal-minVal)
            dp[i]=min(dp[i], dp[i-j]+cost)
    
    print(dp[-1])