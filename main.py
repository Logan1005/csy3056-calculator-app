
# Purpose: Interface for user interaction with the calculator
# Dependencies: Calculator module
# Description: This script uses the calculator module to perform arithmetic operations based on user input

from calculator import add, subtract, multiply, divide

if __name__ == "__main__":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operation (+, -, *, /): ")

    if op == "+":
        print(add(a, b))
    elif op == "-":
        print(subtract(a, b))
    elif op == "*":
        print(multiply(a, b))
    elif op == "/":
        print(divide(a, b))
    else:
        print("Invalid operation")