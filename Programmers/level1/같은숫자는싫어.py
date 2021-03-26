# 같은 숫자는 싫어

def solution(arr):
    answer=list()
    
    for i in arr:
        if len(answer)>0:
            if answer[-1]!=i:
                answer.append(i)
        else:
            answer.append(i)
    
    return answer