# 문자열 잘라내기 - G5

import sys

if __name__=="__main__":
    R,C=map(int,sys.stdin.readline().split()) # R,C 입력 받기

    table=list()
    for i in range(R):
        table.append(list(sys.stdin.readline().rstrip()))


    word_li=list()

    for j in range(C):
        word=''
        for i in range(R):
            word+=table[i][j]

        word_li.append(word)

    count=0
    r=1

    while r<R:
        temp=set()
        for i in word_li:
            if i[r:] not in temp:
                temp.add(i[r:])
            else:
                print(count)
                sys.exit(0)

        r+=1
        count+=1

    print(count)