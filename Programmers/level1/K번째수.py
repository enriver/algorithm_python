# 정렬 K번째수

def solution(array, commands):
    answer = []
    
    for command in commands:
        start,end,order=command
        
        temp=array[start-1:end]
        temp.sort()
        
        answer.append(temp[order-1])
    return answer