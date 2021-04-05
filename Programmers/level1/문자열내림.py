# 문자열 내림차순으로 배치하기

def solution(s):
    answer = sorted(list(s), reverse=True)
    return ''.join(answer)