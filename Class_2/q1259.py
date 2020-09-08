# 팰린드롬수
import sys

for _ in range(100):
    n=sys.stdin.readline()
    isP=True
    if int(n)==0:
        break
    else:
        val=list()
        re_val=list()

        for i in n:
            val.append(i)
            re_val.append(i)

        re_val.reverse()
   
        val.pop(-1)
        re_val.pop(0)
   
        for i in range(len(val)):
            if val[i]!=re_val[i]:
                isP=False

        if isP==False:
            print('no')
        else:
            print('yes')
        
    