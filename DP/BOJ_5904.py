# Moo 게임 - S2

import sys

# S_{0}='moo'
# S_{n+1}=S_{n}+'m'+'o'*(n+2)+S_{n}  (n>=0)
#        =S_{n}+(n+3)+S_{n}
#        =2*S_{n}+(n+3)

def solve(n,k): 
    if k==0:
        return 'moo'[n-1]
    
    if n<=dp[k-1]: # n<= S_{k-1} 인 경우
        return solve(n,k-1)
    elif n<=dp[k-1]+k+3: # n<=S_{k-1}+k+3 인 경우
        if n-dp[k-1]==1: # 남은 글자수가 1 : m
            return 'm'
        else: # else: o
            return 'o'
    else: # S_{k-1}+k+3< n 인 경우
        return solve(n-dp[k-1]-(k+3),k-1)

if __name__=="__main__":
    N=int(sys.stdin.readline())

    dp=[3] # 문자의 길이를 넣어주는 리스트
    K=0

    while dp[K]<N: # 조건 : S_{k}의 길이가 N보다 작을 때
        K+=1
        dp.append(2*dp[K-1]+K+3) #  K가 증가할때마다 생성되는 S_{k}의 길이 추가

    print(solve(N,K))