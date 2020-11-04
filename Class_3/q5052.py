# 전화번호목록 - G4

'''
풀이 1 : 시간초과로 실패

import re
import sys

sys.setrecursionlimit(30000)

T=int(sys.stdin.readline())

def find_prefix(val_list, sentence):
    yn='YES'

    for i in val_list:
        for a in re.finditer(i, sentence):
            pos=a.start()
            if sentence[pos+len(i)] != '/':
                yn='NO'
                break
    
    return yn

for _ in range(T):
    n=int(sys.stdin.readline())
    val=list()
    word='/'
    for _ in range(n):
        num=sys.stdin.readline().rstrip()
        val.append(num)
        word+=num+'/'
    
    result=find_prefix(val,word)
    print(result)
'''

'''
풀이 2 : 시간초과로 실패

import sys

sys.setrecursionlimit(10000)

def find_prefix(sentence):
    temp=sentence.copy()

    for i in sentence:
        sentence.remove(i)
        for j in sentence:
            if j.startswith(i)==True:
                print('NO')
                return
        sentence=temp

    print('YES')

T=int(sys.stdin.readline())

for _ in range(T):
    n=int(sys.stdin.readline())
    word=list()
    for _ in range(n):
        num=sys.stdin.readline().rstrip()
        word.append(num)

    find_prefix(word)

'''

'''
풀이 3 - 완전탐색을 하지않고, 문자열의 특성상 글자순으로 정렬된다는것을 이용하여 풀이
'''

import sys

T=int(sys.stdin.readline())

def find_prefix(sentence):
    sentence.sort()

    for i in range(len(sentence)-1):
        if sentence[i+1].startswith(sentence[i])==True:
            print('NO')
            return
    
    print('YES')

for _ in range(T):
    n=int(sys.stdin.readline())
    word=list()
    for _ in range(n):
        num=sys.stdin.readline().rstrip()
        word.append(num)

    find_prefix(word)