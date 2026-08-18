print("Simple Calculator")
print("Enter two numbers and an operator (+, -, *, /) to perform the calculation.")
print("Example: 5 + 3 = 8" )

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print("Result:", num1 + num2)

elif operator == "-":
    print("Result:", num1 - num2)

elif operator == "*":
    print("Result:", num1 * num2)

elif operator == "/":
    print("Result:", num1 / num2)

else:
    print("Invalid operator")