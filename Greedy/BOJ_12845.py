# 모두의 마블 - S2

import sys

if __name__=="__main__":
    n=int(sys.stdin.readline())
    cards=list(map(int,sys.stdin.readline().split()))

    gold=0
    maxVal=max(cards)
    idx=cards.index(maxVal)

    for i in range(n):
        if i!=idx:
            gold+=cards[i]+maxVal

    print(gold)