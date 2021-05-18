# 암호코드 - S1

import sys

if __name__=="__main__":
    ciphertext=sys.stdin.readline().rstrip();

    dp=[0]*(len(ciphertext)+1)

    if ciphertext[0]=='0':
        print(0)
    else:
        dp[0]=1

        for i in range(1,len(ciphertext)+1):
            if ciphertext[i-1]!='0': # 한자리수
                dp[i]+=dp[i-1]

            if '10'<=ciphertext[i-2:i]<'27': # 두자리수
                dp[i]+=dp[i-2]

        print(dp[-1]%1000000)