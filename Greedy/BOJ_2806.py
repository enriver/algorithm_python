# DNA 발견 - G4
'''
<돌연변이 CASE>

1) A->B or B->A
2) 첫 K개의 글자를 모두 다른 글자로 바꾸는 것
'''

import sys

if __name__=="__main__":
    N=int(sys.stdin.readline())
    word=list(sys.stdin.readline().rstrip())

    a=[0]*(N+1) # 1~N의 자릿수까지 A로 만드는 최소 돌연변이 횟수
    b=[0]*(N+1) # 1~N의 자릿수까지 B로 만드는 최소 돌연변이 횟수

    for i in range(1,N+1):
        if word[i-1]=='A': # 현재 위치한 값이 A 일때
            a[i]=min(a[i-1], b[i-1]+1) # i번째 위치한 곳까지 A로 만들기 위해서는
            b[i]=min(a[i-1], b[i-1])+1 # i번째 위치한 곳까지 B로 만들기 위해서는
        else: # 현재 위치한 값이 B 일때
            a[i]=min(a[i-1], b[i-1])+1 # i번째 위치한 곳까지 A로 만들기 위해서는
            b[i]=min(a[i-1]+1, b[i-1]) # i번째 위치한 곳까지 B로 만들기 위해서는

    print(a[-1])
    
