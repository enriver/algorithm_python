# 스택
import sys

def stack(world,li):

    if len(world)==2:
        li.append(int(world[1]))
    else:
        if world[0]=='pop':
            if(len(li)==0):
                print(-1)
            else:
                print(li.pop())
        elif world[0]=='size':
            print(len(li))
        elif world[0]=='empty' :
            if(len(li)==0):
                print(1)
            else:
                print(0)
        elif world[0]=='top':
            if(len(li)==0):
                print(-1)
            else: 
                print(li[-1])
    return li
            

stack_val=[]

n=int(sys.stdin.readline())

for _ in range(n):
    val=list(sys.stdin.readline().split())
    stack(val,stack_val)
    # print(val)

