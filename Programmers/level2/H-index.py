# 정렬 - H-index

def solution(citations):
    citations.sort()
    
    length=len(citations)
    
    for i in range(length):
        h=citations[i]
        
        if h>=length-i:
            return length-i
        
    return 0