# 백대열 - S3

import sys
import math

vs=sys.stdin.readline()

index=vs.find(':')

n1,n2=int(vs[:index]), int(vs[index+1:])

common=math.gcd(n1,n2)

n1,n2=n1//common, n2//common

print(str(n1)+":"+str(n2))