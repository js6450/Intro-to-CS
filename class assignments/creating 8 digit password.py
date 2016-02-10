import random

def rand(n1, n2):
    value = random.randint(n1, n2)
#random.randint is between and equal to n1 and n2
    return value

def main():
    password = ""
    for i in range(5):
        bit = rand(97,122)
        letter = chr(bit)
        password += letter
    for i in range(2):
        bit = rand(65,90)
        letter = chr(bit)
        password += letter
    for i in range(1):
        bit = rand(1,9)
        number = str(bit)
        password += number
    print(password)

main()
