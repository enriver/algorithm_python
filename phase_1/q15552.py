import sys

x=sys.stdin.readline()

for i in range(0,int(x)):
    numA, numB=map(int,sys.stdin.readline().split(' '))
    print(numA+numB)