# 문자열 추측 - S1

import sys

def find_ps(word):
    result=['' for _ in range(2*N-2)]
    
    for i in range(0,len(ps),2):
        (w1, idx1),(w2, idx2)=ps[i],ps[i+1]
        p1, s1=word.startswith(w1), word.endswith(w1)
        p2, s2=word.startswith(w2), word.endswith(w2)

        if p1 and s2:
            result[idx1]='P'
            result[idx2]='S'
        elif p2 and s1:
            result[idx1]='S'
            result[idx2]='P'
        else:
            return

    print(word)
    print(''.join(result))
    sys.exit(0)

if __name__=="__main__":
    N=int(sys.stdin.readline())

    ps=list()

    for i in range(2*N-2):
        ps.append((sys.stdin.readline().rstrip(),i));

    ps.sort(key=lambda x:len(x[0]))

    a=ps[-2][0]
    b=ps[-1][0]

    if a[1:]==b[:-1]:
        find_ps(a+b[-1])
    if b[1:]==a[:-1]:
        find_ps(b+a[-1])