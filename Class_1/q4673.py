#셀프 넘버

number_set=set(range(1,10001))
generated_set=set()

for i in range(1,10001):
    for j in str(i):
        i+=int(j)
    generated_set.add(i)


self_num=number_set-generated_set

for i in sorted(self_num):
    print(i)