# 다이얼

word=input().lower()

score=0
for i in word :
    if i in ('a','b','c') :
        score+=3
    elif i in ('d','e','f'):
        score+=4
    elif i in ('g','h','i'):
        score+=5
    elif i in ('j','k','l'):
        score+=6
    elif i in ('m','n','o'):
        score+=7
    elif i in ('p','q','r','s'):
        score+=8
    elif  i in ('t','u','v'):
        score+=9
    else : 
        score+=10
    
print(score)