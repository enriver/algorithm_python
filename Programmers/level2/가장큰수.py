# 정렬 - 가장 큰 수

def solution(numbers):
    
    numbers=[str(i) for i in numbers]
    numbers=sorted(numbers, key=lambda x:x*3, reverse=True)
    
    answer=str(int(''.join(numbers)))
    
    return answer