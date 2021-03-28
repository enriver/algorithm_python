# 문자열 내 p와 y의 개수

import sys

def solution(s):    
    s=s.lower()

    p=s.count('p')
    y=s.count('y')
    
    if p==None or y==None:
        return True
    if p==y:
        return True
    else:
        return False

if __name__=="__main__":
    word=sys.stdin.readline().rstrip()

    print(solution(word))