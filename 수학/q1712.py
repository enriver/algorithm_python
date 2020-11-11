#손익분기점

a,b,c=list(map(int,input().split()))


if c<=b :
    print(-1)
else :
    print(int(a/(c-b))+1)


#   n > a/(c-b)