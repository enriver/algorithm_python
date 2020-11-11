#직사각형에서 탈출

import sys

x,y,w,h=map(int,sys.stdin.readline().split())

x_list=[0,w]
y_list=[0,h]

min=1000000

for i in range(2):
    if x>x_list[i]:
        if min>x-x_list[i]:
            min=x-x_list[i]
    else:
        if min>x_list[i]-x:
            min=x_list[i]-x

    if y>y_list[i]:
        if min>y-y_list[i]:
            min=y-y_list[i]
    else:
        if min>y_list[i]-y:
            min=y_list[i]-y

print(min)