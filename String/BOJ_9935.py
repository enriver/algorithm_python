#문자열 폭발 - G4

import sys

word=sys.stdin.readline().strip()
bomb=sys.stdin.readline().strip()

lastChar = bomb[-1] # 폭발 문자열의 마지막 글자
stack = []
length = len(bomb)  # 폭발 문자열의 길이

for char in word:
    stack.append(char)
    if char == lastChar and ''.join(stack[-length:]) == bomb:
        del stack[-length:]

answer = ''.join(stack)

if answer == '':
    print("FRULA")
else:
    print(answer)