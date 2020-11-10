# 이진 검색 트리 - S1


import sys

def postorder(start, end):
    if start > end:     # 같은 키 없음
        return

    division = end + 1
    for i in range(start + 1, end + 1):
        if pre[start] < pre[i]:
            division = i
            break

    postorder(start + 1, division - 1)
    postorder(division, end)
    print(pre[start])

sys.setrecursionlimit(10 ** 8)

pre = []
count = 0
while count <= 10000:
    try:
        num = int(sys.stdin.readline())
    except:
        break
    pre.append(num)
    count += 1

postorder(0, len(pre) - 1)