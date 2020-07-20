#문자열 반복

a=int(input())

for i in range(0,a):
    num, word = input().split()
    text=""
    for j in word:
        text +=int(num)*j
    print(text)