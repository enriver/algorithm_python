# 문자열 추측 - S1

import sys

if __name__=="__main__":
    N=int(sys.stdin.readline())

    ps=list()

    for _ in range(2*N-2):
        ps.append(sys.stdin.readline().rstrip());

    ps_sorted=sorted(ps, key=len)

    #print(ps_sorted)

    a,b=ps_sorted[-2], ps_sorted[-1]

    if a[1:]==b[:-1]:
        word=a+b[-1]
    else:
        word=b+a[-1]

    print(word)
    result=list()

    for i in ps:
        isStart=False
        isEnd=False

        if word.startswith(i):
            isStart=True
        if word.endswith(i):
            isEnd=True
        
        if isStart and isEnd:
            result.append('B')
        elif isStart:
            result.append('P')
        else:
            result.append('S')

    now='P'
    for i in range(len(result)):
        if result[i]=='B':
            if now=='P':
                result[i]=now
                now='S'
            else:
                result[i]=now
                now='P'

    print(''.join(result))