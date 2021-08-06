# 해시 - 위장

def solution(clothes):
    costume = dict()

    for _, type in clothes:
        if type not in costume:
            costume[type]=2
        else:
            costume[type]+=1
    
    answer=1
    
    for v in costume.values():
        answer*=v
        
    return answer-1