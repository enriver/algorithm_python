# 괄호 - S4

import sys

n=int(sys.stdin.readline())

stack=[]
check='YES'
for _ in range(n):
    bracket=sys.stdin.readline()
    for j in bracket:
        if j=='(':
            stack.append(j)
        elif j==')':
            if '(' in stack:
                stack.remove('(')
            else:
                check='NO'

    if len(stack)>0:
        check='NO'
    print(check)
    
    stack=[]
    check='YES'