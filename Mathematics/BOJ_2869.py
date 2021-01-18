# 달팽이는 올라가고 싶다

A,B,V=map(int,input().split())

k=(V-B)/(A-B)

if k==int(k):
    print(int(k))
else:
    print(int(k)+1)
        