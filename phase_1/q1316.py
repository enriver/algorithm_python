#그룹 단어 체커

n=int(input())

series=True
word_list=[]
for i in range(0, n):
    word=input()

    for j in word :
        if j not in word_list :
            word_list.append(j)
            series=False
        else :
            if series==True :
                continue