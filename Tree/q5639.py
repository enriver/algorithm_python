# 이진 검색 트리 - S1


import sys

def postorder(start, end):
    if start > end:     # 같은 키 없음
        return

    division = end + 1
    for i in range(start + 1, end + 1):
        if node[start] < node[i]:
            division = i
            break

    postorder(start + 1, division - 1)
    postorder(division, end)
    print(node[start])

sys.setrecursionlimit(10 ** 8)

node = []
while True:
    try:
        node.append(int(sys.stdin.readline()))
    except:
        break

postorder(0, len(node) - 1)