total = students = grade = 0
while (grade != -1):
    grade = int(input("enter grade or type -1 to exit"))
    total += grade
    students += 1
avg = total / students
print("the average is", avg)
