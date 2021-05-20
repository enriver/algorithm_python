# 좁은 미술전시관 - G5
'''
https://www.acmicpc.net/source/10611809 참고

dp[N+1][K+1][3]= N번째 줄까지 닫았을 경우의 Max값

모두 열었을때, 왼쪽만 닫았을 때, 오른쪽만 닫았을 때  모두 고려해줘야함
'''

import sys

if __name__=="__main__":
    N,K=map(int,sys.stdin.readline().split()) # N 세로줄, k 닫을 방

    room=[(0,0)]
    for n in range(N+1):
        i,j=map(int,sys.stdin.readline().split())

        if n==N:
            break
        room.append((i,j))

    dp=[[[0 for _ in range(3)] for _ in range(K+1)] for _ in range(N+1)] 

    dp[1][0][0]=room[1][0]+room[1][1]

    if K!=0:
        dp[1][1][1]=room[1][1] # 왼쪽이 열려있으면 -> 왼쪽 방 닫은 경우
        dp[1][1][2]=room[1][0] # 오른쪽이 열려있으면 -> 왼쪽 방 닫은 경우

    for i in range(2,N+1):
        for k in range(K+1):
            if i!=k: # k를 다 소모하지 않음
                dp[i][k][0]=max(dp[i-1][k][0], dp[i-1][k][1], dp[i-1][k][2])+sum(room[i])

            if k>=1:
                dp[i][k][1]=max(dp[i-1][k-1][0], dp[i-1][k-1][1])+room[i][1]
                dp[i][k][2]=max(dp[i-1][k-1][0], dp[i-1][k-1][2])+room[i][0]

    print(max(dp[N][K]))