# 시그널 - S2
'''
https://www.acmicpc.net/source/27187949 참고
'''
import sys

if __name__=="__main__":
    N=int(sys.stdin.readline()) # 시그널의 길이
    M=N//5

    signal=sys.stdin.readline().rstrip()

    num_dict={
    '######...######':'0',
    '#####':'1',
    '#.####.#.####.#':'2',
    '#.#.##.#.######':'3',
    '###....#..#####':'4',
    '###.##.#.##.###':'5',
    '######.#.##.###':'6',
    '#....#....#####':'7',
    '######.#.######':'8',
    '###.##.#.######':'9'
    }

    answer=''
    now=''
    for i in range(M): # N//5
        temp=''
        for j in range(5):
            temp+=signal[i+j*M]

        if temp=='.....': #공백
            if now: # 값이 끝난 후의 공백인가
                answer+=num_dict[now]
                now=''
        else: # 공백이 아닌경우
            now+=temp

    if now: # 예외 처리
        answer+=num_dict[now]

    print(answer)

