#알약

import sys


dp=[[0 for _ in range(31)] for _ in range(31)]


def pill(W,H):

        



while True:
    n=int(sys.stdin.readline())

    if n==0:
        break
    else:
        print(pill(n,0))
        