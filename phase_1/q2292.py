#벌집

n=int(input())

k=1
if n==1 :
    print(1)
else:
    while(True):
        if 3*(k**2-k)+1<=n<=3*(k**2+k)+1 :
            print(k+1)
            break
        k+=1
