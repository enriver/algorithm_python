# 괄호의 값 - S2

import sys

def get_mul(c:str):
    if c == ')':
        return 2
    if c == ']':
        return 3
    return 0

def solve(string):
    pairs={')':'(',']':'['}
    stack = []
    value = []
    ans = 0

    for c in string:
        if c in '([':
            stack.append(c)
            value.append(0)
        else:
            if not stack: # 스택에 아무런 요소가 없는데, 닫히는 괄호를 받은경우
                return 0
            if stack[-1] != pairs[c]: # stack의 마지막요소와 서로 짝이 맞지 않을경우
                return 0

            stack.pop()
            v = value.pop() # 가장 최근 value 가져오기

            if v == 0: 
                v = 1
            v *= get_mul(c)

            if not value: # value에 남은 값이 없다
                ans += v
            else:
                v+= value.pop() # 값이 존재하는 경우 더해줌 -> ()[] 같은 케이슨
                value.append(v)
    if stack:
        return 0
    return ans

if __name__=="__main__":
    bracket=sys.stdin.readline().strip()
    print(solve(bracket))