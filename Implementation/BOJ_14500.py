# 테트로미노 - G5

import sys

def type1(x,y):
    if x+3<N and y+3<M:
        return max(tet[x][y]+tet[x+1][y]+tet[x+2][y]+tet[x+3][y],tet[x][y]+tet[x][y+1]+tet[x][y+2]+tet[x][y+3])

    elif x+3<N and y+3>=M:
        return tet[x][y]+tet[x+1][y]+tet[x+2][y]+tet[x+3][y]

    elif x+3>=N and y+3<M:
        return tet[x][y]+tet[x][y+1]+tet[x][y+2]+tet[x][y+3]
    else:
        return 0

def type2(x,y):
    val=0
    if x+1<N and y+1<M:
        val=tet[x][y]+tet[x+1][y]+tet[x][y+1]+tet[x+1][y+1]

    return val

def type3(x,y):
    val1,val2,val3,val4=0,0,0,0
    val5,val6,val7,val8=0,0,0,0

    if x+2<N and y+1<M:
        val1=tet[x][y]+tet[x+1][y]+tet[x+2][y]+tet[x+2][y+1]
    
    if x+1<N and y+2<M:
        val2=tet[x][y]+tet[x][y+1]+tet[x][y+2]+tet[x+1][y+2]

    if x+2<N and y-1>=0:
        val3=tet[x][y]+tet[x+1][y]+tet[x+2][y]+tet[x+2][y-1]

    if x-1>=0 and y+2<M:
        val4=tet[x][y]+tet[x][y+1]+tet[x][y+2]+tet[x-1][y+2]

    if x-2>=0 and y+1<M:
        val5=tet[x][y]+tet[x-1][y]+tet[x-2][y]+tet[x-2][y+1]

    if x-2>=0 and y-1>=0:
        val6=tet[x][y]+tet[x-1][y]+tet[x-2][y]+tet[x-2][y-1]

    if x+1<N and y-2>=0:
        val7=tet[x][y]+tet[x][y-1]+tet[x][y-2]+tet[x+1][y-2]

    if x-1>=0 and y-2>=0:
        val8=tet[x][y]+tet[x][y-1]+tet[x][y-2]+tet[x-1][y-2]

    return max(val1,val2,val3,val4,val5,val6,val7,val8)

def type4(x,y):
    val1,val2,val3,val4=0,0,0,0
    val5,val6,val7,val8=0,0,0,0

    if x+1<N and y+2<M:
        val1=tet[x][y]+tet[x][y+1]+tet[x+1][y+1]+tet[x+1][y+2]

    if x-1>=0 and y+2<M:
        val2=tet[x][y]+tet[x][y+1]+tet[x-1][y+1]+tet[x-1][y+2]

    if x+2<N and y+1<M:
        val3=tet[x][y]+tet[x+1][y]+tet[x+1][y+1]+tet[x+2][y+1]

    if x+2<N and y-1>=0:
        val4=tet[x][y]+tet[x+1][y]+tet[x+1][y-1]+tet[x+2][y-1]

    if x-2>=0 and y+1<M:
        val5=tet[x][y]+tet[x-1][y]+tet[x-1][y+1]+tet[x-2][y+1]

    if x-2>=0 and y-1>=0:
        val6=tet[x][y]+tet[x-1][y]+tet[x-1][y-1]+tet[x-2][y-1]

    if x-1>=0 and y-2>=0:
        val7=tet[x][y]+tet[x][y-1]+tet[x-1][y-1]+tet[x-1][y-2]

    if x+1<N and y-2>=0:
        val8=tet[x][y]+tet[x][y-1]+tet[x+1][y-1]+tet[x+1][y-2]

    return max(val1,val2,val3,val4,val5,val6,val7,val8)

def type5(x,y):
    val1,val2,val3,val4=0,0,0,0
    val5,val6,val7,val8=0,0,0,0

    if x-1>=0 and y+2<M:
        val1=tet[x][y]+tet[x][y+1]+tet[x-1][y+1]+tet[x][y+2]

    if x+1<N and y+2<M:
        val2=tet[x][y]+tet[x][y+1]+tet[x+1][y+1]+tet[x][y+2]

    if x-1>=0 and y-2>=0:
        val3=tet[x][y]+tet[x][y-1]+tet[x-1][y-1]+tet[x][y-2]

    if x+1<N and y-2>=0:
        val4=tet[x][y]+tet[x][y-1]+tet[x+1][y-1]+tet[x][y-2]

    if x-2>=0 and y+1<M:
        val5=tet[x][y]+tet[x-1][y]+tet[x-1][y+1]+tet[x-2][y]

    if x-2>=0 and y-1>=0:
        val6=tet[x][y]+tet[x-1][y]+tet[x-1][y-1]+tet[x-2][y]

    if x+2<N and y+1<M:
        val7=tet[x][y]+tet[x+1][y]+tet[x+1][y+1]+tet[x+2][y]

    if x+2<N and y-1>=0:
        val8=tet[x][y]+tet[x+1][y]+tet[x+1][y-1]+tet[x+2][y]

    return max(val1,val2,val3,val4,val5,val6,val7,val8)

if __name__=="__main__":
    N,M = map(int, sys.stdin.readline().split())

    tet=list()
    for _ in range(N):
        tet.append(list(map(int,sys.stdin.readline().split())))

    ans=0
    for i in range(N):
        for j in range(M):
            ans=max(ans, type1(i,j), type2(i,j), type3(i,j), type4(i,j), type5(i,j))


    print(ans)


