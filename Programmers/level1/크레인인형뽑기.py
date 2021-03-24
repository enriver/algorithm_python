# 크레인 인형 뽑기 게임

import sys

def solution(board, moves):
    answer = 0
    
    stack=list()
    
    for i in moves:
        k=0
        i=int(i)
        while k<len(board):
            if board[k][i-1]!='0':
                if len(stack)>0:
                    if stack[-1]!=board[k][i-1]:
                        stack.append(board[k][i-1])
                        board[k][i-1]='0'
                        break
                    else:
                        stack.pop()
                        board[k][i-1]='0'
                        answer+=2
                        break
                else:
                    stack.append(board[k][i-1])
                    board[k][i-1]='0'
                    break
            k+=1
            
    return answer

if __name__=="__main__":
    N=int(sys.stdin.readline())
    boards=list()

    for _ in range(N):
        boards.append(list(sys.stdin.readline().rstrip()))

    move=list(sys.stdin.readline().rstrip())

    print(solution(boards, move))

    
    