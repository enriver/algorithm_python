# 음계

import sys

scale_num = list(map(int, sys.stdin.readline().split()))
if scale_num == [1,2,3,4,5,6,7,8]:
    print("ascending")
elif scale_num == [8,7,6,5,4,3,2,1]:
    print("descending")
else:
    print("mixed")