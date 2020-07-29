#설탕 배달
a=3
b=5

n=int(input())


if n%3==0 and n%5 == 0 :
    print(n//5)
elif n%3!=0 and n%5==0:
    print(n//5)
elif n%5!=0 and n%3==0 and n%5!=3:
    print(n//3)
elif n%5==3:
    print((n//5)+1)
elif n%3==2:
    print(n//3)
else :
    print(-1)