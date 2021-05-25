# 로마 숫자 - S1

import sys

def toNumeric(arab):
    num=0
    iv,ix,xl,xc,cd,cm=1,1,1,1,1,1
    isPass=False
    for i in range(len(arab)):
        if isPass:
            isPass=False
            continue

        if arab[i]=='I':
            if i!=len(arab)-1:
                if arab[i+1]=='V' and iv>0:
                    num+=4
                    iv-=1
                    isPass=True
                elif arab[i+1]=='X' and ix>0:
                    num+=9
                    ix-=1
                    isPass=True
                else:
                    num+=1
            else:
                num+=1

        if arab[i]=='V':
            num+=5

        if arab[i]=='X':
            if i!=len(arab)-1:
                if arab[i+1]=='L' and xl>0:
                    num+=40
                    xl-=1
                    isPass=True
                elif arab[i+1]=='C' and xc>0:
                    num+=90
                    xc-=1
                    isPass=True
                else:
                    num+=10
            else:
                num+=10

        if arab[i]=='L':
            num+=50

        if arab[i]=='C':
            if i!=len(arab)-1:
                if arab[i+1]=='D' and cd>0:
                    num+=400
                    cd-=1
                    isPass=True
                elif arab[i+1]=='M' and cm>0:
                    num+=900
                    cm-=1
                    isPass=True
                else:
                    num+=100
            else:
                num+=100

        if arab[i]=='D':
            num+=500

        if arab[i]=='M':
            num+=1000

    return num

def toArabic(number):
    arabic=''

    iv,ix,xl,xc,cd,cm=1,1,1,1,1,1
    while True:
        if number>=1000:
            arabic+='M'; number-=1000
        elif number>=900 and cm>0:
            arabic+='CM'; number-=900
            cm-=1; cd-=1
        elif number>=500:
            arabic+='D'; number-=500
        elif number>=400 and cd>0:
            arabic+='CD'; number-=400
            cd-=1; cm-=1
        elif number>=100:
            arabic+='C'; number-=100
        elif number>=90 and xc>0:
            arabic+='XC'; number-=90
            xc-=1; xl-=1
        elif number>=50:
            arabic+='L'; number-=50
        elif number>=40 and xl>0:
            arabic+='XL'; number-=40
            xl-=1; xc-=1
        elif number>=10:
            arabic+='X'; number-=10
        elif number>=9 and ix>0:
            arabic+='IX'; number-=9
            ix-=1; iv-=1
        elif number>=5:
            arabic+='V'; number-=5
        elif number>=4 and iv>0:
            arabic+='IV'; number-=4
            iv-=1; ix-=1
        elif number>=1:
            arabic+='I'; number-=1
        else:
            break

    return arabic
    
if __name__=="__main__":
    arab1=sys.stdin.readline().rstrip()
    arab2=sys.stdin.readline().rstrip()

    num=toNumeric(arab1)+toNumeric(arab2)
    arabic=toArabic(num)
    print(num)
    print(arabic)

    