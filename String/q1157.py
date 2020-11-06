#단어 공부

from collections import Counter

word=input().upper()

word_cnt=Counter(word)

freq_word=[]
for k,v in word_cnt.items() :
    if v==max(word_cnt.values()):
        freq_word.append(k)
        if len(freq_word)>1:
            break

if len(freq_word) > 1:
    print('?')
else:
    print(freq_word[0])