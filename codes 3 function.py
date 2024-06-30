def calculator(a, b):
    return a + b

def calculator1(a, b):
    return a - b

def calculator2(a, b):
    return a * b

def calculator3(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero"
num1 = float(input("Enter the first number"))
num2 = float(input("Enter the second number"))
num3 = input("Enter + - / *")
if num3 == '+':
    print("the result=",calculator(num1, num2))
elif num3 == '-':
    print("the result=",calculator1(num1, num2))
elif num3 == '*':
    print("the result=", calculator2(num1, num2))
elif num3 == '/':
    print("the result=",calculator3(num1, num2))
else:
    print("invalid operation")
