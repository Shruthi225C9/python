num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+ for addition, - for subtraction, * for multiplication, / for division): ")


if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 == 0:
        print("Division by zero is not allowed.")
    else:
        result = num1 / num2
else:
    print("Invalid operator choice. Please use +, -, *, or /.")


if operator in ('+', '-', '*', '/'):
    print(f"Result: {num1} {operator} {num2} = {result}")