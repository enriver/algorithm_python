# 회문 - S1

import sys

def pseudo(words):
    left=0
    right=len(words)-1

    while left<right:
        if words[left]!=words[right]:
            # 오른쪽 하나 줄인 경우 (left~right-1)
            if words[left:right]==words[left:right][::-1]:
                return 1
            # 왼쪽 하나 늘인 경우 (left+1~right)
            elif words[left+1:right+1]==words[left+1:right+1][::-1]:
                return 1
            else:
                return 2
        else:
            left+=1
            right-=1

if __name__=="__main__":
    T=int(sys.stdin.readline())

    for _ in range(T):
        word=list(sys.stdin.readline().rstrip())

        if word==word[::-1]:
            print(0)
        else:
            print(pseudo(word))