# 소수 부분 문자열 - G5

import sys
import math

def isPrime(number):
    if number<2 or number>100000:
        return False

    sqrt=int(math.sqrt(number))

    for k in range(2,sqrt+1):
        if number%k==0: return False

    return True

if __name__=="__main__":
    
    while True:
        num=sys.stdin.readline().rstrip()

        if num=='0':
            break
        else:
            ans=0

            for i in range(len(num)):
                for j in range(i+1,len(num)):
                    val=int(num[i:j])
                    if isPrime(val):
                        ans=max(ans,val)

            print(ans)

