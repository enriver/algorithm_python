#말이 되고픈 원숭이 DFS_BFS
import sys

k = int(sys.stdin.readline())
w, h = map(int, sys.stdin.readline().split())

# world = [[0 for col in range(w)] for row in range(h)]
# for i in range(h):
#     obstacle = list()
#     [obstacle.append(j) for j in map(int, sys.stdin.readline().split())]
#     for s in range(w):
#         world[i][s] = obstacle.pop(0)

world = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]

