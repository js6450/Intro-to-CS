#assignment part 1 for 23-09-12

import random

list = []

for n in range(1,101):
    list.append(n)

print(list)
print("the first value in the list is", list[0])
print("the last value in the list is", list[-1])

rnum = random.randint(0, 100)
rannum = list[rnum]

print("random number is", rannum)

print("the total number of values in the list is", len(list))

list.remove(4)
print(list)

list.insert(3,400)
print(list)

print(id(list))

list.append('CS')
print(list)

list.reverse()
print(list)
