# 풍선 공장 - S2

import sys

sys.setrecursionlimit(10**9)
N,M = map(int,sys.stdin.readline().split())

time=list(map(int,sys.stdin.readline().split()))

left=min(time) # 아무리 빨라도 이 시간만큼 걸렸을때 풍선 생성
right=min(time)*M # 아무리 늦어도 이 시간만큼 걸렸을때 전부 생성 가능

while left<right:
    mid=(left+right)//2 # 해당 시간초안에 구하겠다
    count=0 # 풍선을 만드는 개수

    for i in time:
        count+=mid//i
    
    if count>=M: # 주어진 시간내에 풍선을 모두 만들었거나 더 만든 경우
        right=mid # 오래걸리는 시간을 단축
    else:
        left=mid+1 # 덜 생성했을 경우 mid를 키워주기 위해, left값 을 늘림

print(right)