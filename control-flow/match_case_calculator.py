num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        addition = num1 + num2
        print(f"The result is {addition}.")
    case "-":
        subtract = num1 - num2
        print(f"The result is {subtract}.")
    case "*":
        multiply = num1 * num2
        print(f"The result is {multiply}.")
    case "/":
        if num2 != 0:
            divide = num1 / num2
            print(f"The result is {divide}.")
        else:
            print("Cannot divide by zero.")
    case _:
        print("Invalid input")