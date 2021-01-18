#통계학

import sys
from collections import Counter

n=int(sys.stdin.readline())


def avg(li):
    sum=0

    for i in li:
        sum+=i

    return round(sum/len(li))

def median(li):
    if len(li)%2==0:
        return (li[int((len(li)/2))-1]+li[int((len(li)/2))])/2

    else:
        return li[int((len(li)+1)/2)-1]

def mode(li):
    mode_dict = Counter(li) 
    modes = mode_dict.most_common()
    
    if len(li) > 1 : 
        if modes[0][1] == modes[1][1]:
            mod = modes[1][0]
        else : 
            mod = modes[0][0]
    else : 
        mod = modes[0][0]

    return mod


def rrange(li):
    return li[-1]-li[0]


num=[]

for _ in range(n):
    num.append(int(sys.stdin.readline()))

num.sort()

print(avg(num))
print(median(num))
print(mode(num))
print(rrange(num))