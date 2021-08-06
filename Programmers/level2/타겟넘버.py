# DFS/BFS 타켓 넘버

from collections import deque

def solution(numbers, target):
    answer=0
    
    que=deque()
    que.append((0, 0)) # cumsum, idx
    
    while que:
        cumsum, idx=que.popleft()
        
        if idx==len(numbers):
            if cumsum==target:
                answer+=1
        else:  
            number=numbers[idx]

            que.append((cumsum+number, idx+1))
            que.append((cumsum-number, idx+1))
                
    return answer