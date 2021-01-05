#상수

num=input().split()

sangsoo=[]
for i in range(0,2):
    first=num[i][0]
    mid=num[i][1]
    last=num[i][2]
    sangsoo.append(last+mid+first)

sangsoo.sort()

print(int(sangsoo[1]))