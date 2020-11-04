# java vs c++ - S5

import sys

val=sys.stdin.readline()

def to_java(word):
    index=len(word)-1

    while index>-1:
        if word[index].isupper()==True:
            word=word.replace(word[index],'_'+word[index].lower())
        index-=1
    
    return word

def to_cpp(word):
    word=word.replace('_',' ').title().replace(' ','')

    return word

error=True

ver=0

if '_' in val:
    result=to_cpp(val)
    ver=1
elif val.islower()==False:
    result=to_java(val)
    ver=2
elif val.islower()==True:
    result=val
    error=False

if ver==1:
    if '_' in result:
        error=True
    else:
        error=False
elif ver==2:
    if result.islower()==False:
        error=True
    else:
        error=False

if error==True:
    print('Error!')
else:
    print(result)