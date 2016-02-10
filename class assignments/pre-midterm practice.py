#Generating 1000 numbers between range 1 and 500 inclusive

import random

total = 0
list1 = []
for num in range(1, 1001):
    x = random.randint(1, 500)
    total += x
    list1.append(x)
print(list1)
print("The total is:", total)

average = total / 1000
print("The average is:", average)


    

