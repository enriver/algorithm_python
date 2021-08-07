# DFS/BFS - 네트워크

from collections import deque
                
                
def solution(n, computers):
    visit=set()
    answer=0
    
    def bfs(node):
        que=deque()
        que.append(node)

        visit.add(node)
        while que:
            node=que.popleft()

            for idx,val in enumerate(computers[node]):
                if val==1 and idx not in visit:
                    visit.add(idx)
                    que.append(idx)

        return 1
    
    for i in range(n):
        for j in range(n):
            if computers[i][j]==1 and i not in visit:
                answer+=bfs(i)
                
    return answer