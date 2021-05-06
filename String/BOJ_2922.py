# 즐거운 단어 - G4

import sys

def dfs(idx, moeum, jaeum, containL):
    cnt=0

    if moeum>=3 or jaeum>=3: # 모음이나 자음이 연속해서 3번 나왔는지 체크
        return 0

    if idx==len(word): # 모든 인덱스를 돌았을 때 'L'을 포함했는가
        if containL:
            return 1
        else:
            return 0

    if word[idx]=="_":
        cnt+=5*dfs(idx+1, moeum+1, 0, containL) # 모음
        cnt+=20*dfs(idx+1,0,jaeum+1,containL) # 'L'을 제외한 자음
        cnt+=dfs(idx+1,0,jaeum+1,True) # 'L'을 포함한 자음

    elif word[idx] in 'AEIOU':
        cnt+=dfs(idx+1, moeum+1, 0, containL)

    elif word[idx] not in 'AEIOU':
        if word[idx]=='L':
            cnt+=dfs(idx+1,0,jaeum+1,True)
        else:
            cnt+=dfs(idx+1,0,jaeum+1,containL)

    return cnt

if __name__=="__main__":
    word=sys.stdin.readline().rstrip();

    print(dfs(0,0,0,False))