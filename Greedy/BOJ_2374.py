# 같은 수로 만들기 - G5

import sys

if __name__=="__main__":
    n=int(sys.stdin.readline())

    number=list()

    for _ in range(n):
        number.append(int(sys.stdin.readline()))

    cnt=0
    maxVal=max(number)

    while min(number)!=maxVal:
        minVal=maxVal+1
        for i in range(n):
            if minVal>number[i]:
                minVal=number[i]
                idx=i

        for i in range(idx,n):
            if minVal<number[i]:
                break
            else:
                number[i]+=1
        cnt+=1

    print(cnt)