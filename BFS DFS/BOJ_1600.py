#말이 되고픈 원숭이 DFS_BFS
import sys
from collections import deque

k = int(sys.stdin.readline())
w, h = map(int, sys.stdin.readline().split()) # h 행 w 렬
world = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
visit=[[[False for _ in range(w)] for _ in range(h)] for _ in range(k+1)]


dx1=[1,0,-1,0]
dy1=[0,1,0,-1]
dx2=[-2,1,2,1,-1,2,-1,-2]
dy2=[1,-2,1,2,2,-1,-2,-1]

def bfs(x,y,move,jump):
    que=deque()
    que.append((x,y,move,jump))

    while que:
        x,y,move,jump=que.popleft()

        if x==(h-1) and y==(w-1) :
            return move
        else:
            if jump>0:
                for i in range(8):
                    nx,ny=x+dx2[i],y+dy2[i]
                    if 0<=nx<h and 0<=ny<w :
                        if world[nx][ny]==0 and not visit[jump-1][nx][ny]:
                            visit[jump-1][nx][ny]=True
                            que.append((nx,ny,move+1,jump-1))
            for i in range(4):
                nx,ny=x+dx1[i],y+dy1[i]
                if 0<=nx<h and 0<= ny<w:
                    if world[nx][ny]==0 and not visit[jump][nx][ny]:
                        visit[jump][nx][ny]=True
                        que.append((nx,ny,move+1,jump))
            
        
    return -1

print(bfs(0,0,0,k))





# world = [[0 for col in range(w)] for row in range(h)]
# for i in range(h):
#     obstacle = list()
#     [obstacle.append(j) for j in map(int, sys.stdin.readline().split())]
#     for s in range(w):
#         world[i][s] = obstacle.pop(0)


# def bfs(move,x,y,jump):
#     que=deque()
#     que.append((x,y))

#     while que:
#         x,y = que.popleft()
#         if jump!=0:
#             for i in range(8):
#                 nx,ny=x+dx2[i],y+dy2[i]
#                 if 0<=nx<h and 0<=ny<w:
#                     if world[nx][ny]!=1 and not visit[jump][nx][ny]:
#                         visit[nx][ny][jump]=True
#                         jump-=1
#                         move+=1
#                         que.append((move,nx,ny,jump))
#             for i in range(4):
#                 nx,ny=x+dx[i],y+dy[i]
#                 if 0<=nx<h and 0<=ny<w:
#                     if world[nx][ny]!=1 and not visit[jump][nx][ny]:
#                         visit[nx][ny][jump]=True
#                         move+=1
#                         que.append((move,nx,ny,jump))   
                    
#         else:
#             for i in range(4):
#                 nx,ny=x+dx[i],y+dy[i]
#                 if 0<=nx<h and 0<=ny<w:
#                     if world[nx][ny]!=1 and not visit[jump][nx][ny]:
#                                 visit[nx][ny][jump]=True
#                                 move+=1
#                                 que.append((move,nx,ny,jump))
#     return move

