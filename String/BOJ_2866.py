# 문자열 잘라내기 - G5

import sys

if __name__=="__main__":
    R,C=map(int,sys.stdin.readline().split()) # R,C 입력 받기

    table=list()
    for i in range(R):
        table.append(list(sys.stdin.readline().rstrip()))


    count=0
    r=1

    while r<R:
        word_set=set()
        for j in range(C):
            word=''
            for i in range(r,R):
                word+=table[i][j]

            if word not in word_set:
                word_set.add(word)
            else:
                print(count)
                sys.exit(0)

        r+=1
        count+=1

    print(count)