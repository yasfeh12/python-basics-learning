def calculate():
    try:
        num1 = float(input("Enter the first number: "))
        opp = input("Enter an operation (+, -, /, *): ").strip()
        num2 = float(input("Enter the second number: "))

        if opp == "+":
            result = num1 + num2
        elif opp == "-":
            result = num1 - num2
        elif opp == "/":
            if num2 == 0:
                return "Error: Division by zero is not allowed."
            result = num1 / num2
        elif opp == "*":
            result = num1 * num2
        else:
            return "Error: Please enter a valid operator (+, -, /, *)."

        return f"The result is: {result}"

    except ValueError:
        return "Error: Please enter valid numbers."

print(calculate())
