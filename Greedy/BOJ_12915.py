# 대회 개최 - S2

import sys

if __name__=="__main__":
    E,EM,M,MH,H=map(int,sys.stdin.readline().split())

    count=0

    while True:
        check=[False]*3

        if E>0:
            E-=1
            check[0]=True
        else:
            if EM>0:
                EM-=1
                check[0]=True
            else:
                break

        if M>0:
            M-=1
            check[1]=True
        else:
            if EM>0 and MH>0:
                if EM>=MH:
                    EM-=1
                else:
                    MH-=1
            elif EM==0 and MH>0:
                MH-=1
            elif EM>0 and MH==0:
                EM-=1
            else:
                break
            
            check[1]=True

        if H>0:
            H-=1
            check[2]=True
        else:
            if MH>0:
                MH-=1
                check[2]=True
            else:
                break

        if False in check:
            break

        count+=1

    print(count)