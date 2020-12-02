# 가르침 - G4
'''
순규님 코드.. 그는 천재다
'''
import sys

def solve(k,prev): # 어려운걸
    global answer

    if k==K:
        n=0
        for word in words:
            flag=True
            for ch in word:
                if not include[ord(ch)-ord('a')]:
                    flag=False
                    break
            if flag:
                n+=1
        answer=max(answer,n)
        return
    
    for i in range(prev+1,26):
        if not include[i]:
            include[i]=True
            solve(k+1,i)
            include[i]=False

N,K=map(int,sys.stdin.readline().split())

if K<5:
    print(0)
elif K==26:
    print(N)
else:
    words=list()
    include=[False]*26
    answer=0

    for _ in range(N):
        words.append(sys.stdin.readline()[4:-5]) # 접두사와 접미사를 제외한 부분

    # 값이 존재하는것을 ord('a')를 빼주어서 index로 활용
    include[ord('a')-ord('a')] = True
    include[ord('c')-ord('a')] = True
    include[ord('i')-ord('a')] = True
    include[ord('n')-ord('a')] = True
    include[ord('t')-ord('a')] = True

    solve(5,-1)

    print(answer)