# 좌표 압축 - S2

import sys

if __name__=="__main__":
    N=int(sys.stdin.readline())
    index=list(map(int,sys.stdin.readline().split()))
    
    index2=sorted(list(set(index)))
    index_dict=dict()

    for i in range(len(index2)):
        index_dict[index2[i]]=i

    for i in index:
        print(index_dict[i], end=' ')