# 분수찾기

n=int(input())

k=1
sum=0
j=n

while(n-k>0):
    n=n-k
    sum+=k
    k+=1

t2=j-sum
t1=k-(t2-1)

print(str(t1)+'/'+str(t2))
