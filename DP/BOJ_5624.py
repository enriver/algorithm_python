# 좋은 수 - G5
'''
A+B+C=K -> A+B=K-C
'''
import sys

if __name__=="__main__":
    N=int(sys.stdin.readline())
    A=list(map(int,sys.stdin.readline().split()))

    one_set=set()
    two_set=set()

    ans=0
    for i in range(N):
        for one in one_set:
            if A[i]-one in two_set: # K-C
                ans+=1
                break # K가 여러번 체크되는 것을 방지하기 위함

        one_set.add(A[i])

        for one in one_set:
            if -100000<=one+A[i]<=100000: # 중복을 허용
                two_set.add(one+A[i]) # A+B

    print(ans)