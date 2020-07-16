# OX퀴즈


def scoreSum(inputVal):
    score=0
    isO=False
    sum=0
    for i in range(0,len(inputVal)):
        if isO==True:
            if inputVal[i]=="O":
                isO=True
                score+=1
                sum+=score
            else:
                isO=False
                score=0
        else :
            if inputVal[i]=="O":
                isO=True
                score+=1
                sum+=score
            else:
                isO=False
                score=0
    return sum


for i in range(0,int(input())):
    y=input()
    print(scoreSum(y))