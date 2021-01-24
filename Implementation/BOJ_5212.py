# 지구 온난화  - S2

import sys

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def check(x,y):
    cnt=0
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]

        if 0<=nx<R and 0<=ny<C:
            if sea[nx][ny]=='X':
                cnt+=1
    
    return cnt


def sink(arr):
    for i in arr:
        sea[i[0]][i[1]]='.'


def after_50():
    for i in range(remain_min_r,remain_max_r+1):
        for j in range(remain_min_c,remain_max_c+1):
            print(sea[i][j], end='')

            if i==remain_max_r and j==remain_max_c:
                sys.exit(0)
            if j==remain_max_c:
                print()




if __name__=="__main__":
    R, C =map(int,sys.stdin.readline().split())

    sea=list()
    for i in range(R):
        sea.append(list(sys.stdin.readline().rstrip()))

    sink_idx=list()

    remain_min_r=10
    remain_max_r=-1
    remain_min_c=10
    remain_max_c=-1

    for i in range(R):
        for j in range(C):
            if sea[i][j]=='X':
                if check(i,j) < 2:
                    sink_idx.append((i,j))
                else:
                    remain_min_r=min(remain_min_r,i)
                    remain_max_r=max(remain_max_r,i)
                    remain_min_c=min(remain_min_c,j)
                    remain_max_c=max(remain_max_c,j)


    sink(sink_idx)
    after_50()

