# 신나는 함수 실행 - S2

import sys

def w(x,y,z):
    if x<=0 or y<=0 or z<=0:
        return 1
    
    if x>20 or y>20 or z>20:
        return w(20,20,20)

    if dp[x][y][z]!=0:
        return dp[x][y][z]

    if x<y and y<z:
        dp[x][y][z]=w(x,y,z-1)+w(x,y-1,z-1)-w(x,y-1,z)

    else:
        dp[x][y][z]=w(x-1,y,z)+w(x-1,y-1,z)+w(x-1,y,z-1)-w(x-1,y-1,z-1)

    return dp[x][y][z]
    

if __name__=="__main__":
    dp=[[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]
    
    while True:
        a,b,c=map(int,sys.stdin.readline().split())

        if a==-1 and b==-1 and c==-1:
            break
        else:
            print('w('+str(a)+', '+str(b)+', '+str(c)+') = '+str(w(a,b,c)))