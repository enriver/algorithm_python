# 접미사 배열 - S4

import sys

word=sys.stdin.readline().strip()

word_li=list()
for i in range(0,len(word)):
    word_li.append(word[i:])

for i in sorted(word_li):
    print(i)