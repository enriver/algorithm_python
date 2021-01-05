#그룹 단어 체커

import sys

def check(word):
    ch=1
    group=set()
    now=word[0]
    group.add(now)
    for i in word[1:]:
        if i not in group:
            group.add(i)
            now=i
        else:
            if i!=now:
                ch=0
                break
            else:
                ch= 1
    return ch


n=int(sys.stdin.readline())
word_list=[]

for _ in range(n):
    word=sys.stdin.readline()
    word_list.append(word)

num=0
for i in word_list:
    num+=check(i)

print(num)

