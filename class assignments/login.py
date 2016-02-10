username = input("enter username: ")
password = input("enter password: ")

file = open("text.txt", "r")
info = file.readlines()
file.close()


list_info = []

for line in info:
    line = line.rstrip("\n")
    list_info.append(line)
print(list_info)

if username + ":" + password in list_info:
    print("YAY")
else:
    print(":(")

new_u = input("new username: ")
new_p = input("new password: ")

file = open("text.txt", "r")
info = file.readlines()
file.close()

list1 = []
list2 = []

for line in info:
    line = line.rstrip("\n").split(":")
    list1.append(line)
for r in range(len(list1)):
    for c in range(2):
        list2.append(list1[r][c])

if new_u in list2:
    print("Being used")
else:
    file = open("text.txt", "a")
    file.write(new_u + ":" + new_p + "\n")
    file.close()

