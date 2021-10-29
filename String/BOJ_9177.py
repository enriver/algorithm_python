# 단어 섞기 - G5

import sys

def isPossible(word1, word2, objective):
    stack=list()
    w1=0
    w2=0

    length=len(objective)
    i=0

    while i<length:
        word=objective[i]
        print(i)
        print(w1,'w1')
        print(w2,'w2')
        '''
        if word==word1[w1] and word==word2[w2]:
            i+=1
            w1+=1
        '''
        if word==word1[w1] and word!=word2[w2]: # word1 만
            i+=1
            w1+=1

        elif word!=word1[w1] and word==word2[w2]: # word2 만
            i+=1
            w2+=1

        else:
            return "no"
        
    return "yes"

if __name__=="__main__":
    n=int(sys.stdin.readline())

    for  i in range(n):
        first_one,seconde_one,obj_one=sys.stdin.readline().split()

        print('Data set {}: {}'.format(i+1,isPossible(first_one,seconde_one,obj_one)))