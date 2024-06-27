calculator1 = float(input("hello enter first number"))
calculator2 = float(input("second number"))
calculator3 = input("Enter +, -, *, / ")
if calculator3 == '+':
    calculator = calculator1 + calculator2
elif calculator3 == '-':
    calculator = calculator1 - calculator2
elif calculator3 == '*':
    calculator = calculator1 * calculator2
elif calculator3 == '/':
    if calculator2 != 0:
        calculator = calculator1 / calculator2
    else:
        calculator = "Error Division by zero"
else:
    calculator = ("invalid")

print(f"The result is: {calculator}")



