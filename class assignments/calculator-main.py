
from calculator import *
import calculator


def main():
    op = input("enter op.: +, -, *, /: ")
    num1 = int(input("enter a number: "))
    num2 = float(input("enter a decimal number: "))

    if op == "+":
        result = calculator.add(num1, num2)
    elif op == "-":
        result = calculator.sub(num1, num2)
    elif op == "*":
        result = calculator.mult(num1, num2)
    elif op == "/":
        result = calculator.div(num1, num2)
    else:
        print("Invalid operation")
    print(result)

main()
