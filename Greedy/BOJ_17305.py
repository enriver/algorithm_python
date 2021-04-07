# 사탕 배달 - G4

import sys

if __name__=="__main__":
    N, W =map(int, sys.stdin.readline().split()) # N 사탕개수, W 무게제한

    three=list() # 무게가 3인 사탕의 당도 저장
    five=list() # 무게가 5인 사탕의 당도 저장

    for _ in range(N):
        t,s=map(int,sys.stdin.readline().split()) # 사탕종류, 당도
        
        if t==3:
            three.append(s)
        else:
            five.append(s)

    # 당도가 높은순으로 정렬 (insert(0,0) 는 해당 무게의 사탕 없는 경우)
    three.sort(reverse=True); three.insert(0,0)
    five.sort(reverse=True); five.insert(0,0)

    # 당도 누적 (핵심)
    for i in range(1,len(three)):
        three[i]+=three[i-1]
    for i in range(1,len(five)):
        five[i]+=five[i-1]
    print(three)
    print(five)
    answer=0

    for i in range(len(five)):
        if i*5>W: # 무게가 초과되는 경우
            break

        ## 미니멈 ##
        # W에서 i*5만큼 빼고 남은 무게 나누기 3 (해당 값의 목 만큼 누적값이 들어갈 수 있음)
        # 무게가 3인 사탕의 최대값
        threeIdx=min((W-i*5)//3, len(three)-1) 
        ## 맥시멈 ##
        # 무게가 5인 사탕을 i 누적값+무게가 3인 사탕을 (W-i*5)//3 누적값
        answer=max(answer, three[threeIdx]+five[i])
    
    print(answer)
        