# 안정적인 문자열 - S1

import sys

def stable(data,num):
    ans=0
    stack=list()

    for i in data:
        if i=='{':
            stack.append(i)
        else:
            if len(stack)==0 or stack[-1]=='}':
                stack.append(i)
            else:
                stack.pop()

    if len(stack)>0:
        for i in range(0,len(stack),2):
            w1,w2=stack[i], stack[i+1]

            if w1==w2:
                ans+=1
            else:
                ans+=2
    
    print(str(num)+'.',ans)


if __name__=="__main__":  
    case=1

    while True:
        sentence=sys.stdin.readline().rstrip();

        if '-' in sentence:
            break
        else:
            stable(sentence,case)
            case+=1
            