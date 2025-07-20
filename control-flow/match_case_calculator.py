num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operations = input("Choose the operation (+, -, *, /):")

match operations:
    case "+":
        result = num1 + num2
        print(f"The result is {result}.")
    case "-":
        result = num1 - num2
        print(f"The result is {result}.")
    case "*":
        result = num1 * num2
        print(f"The result is {result}.")
    case "/":
        if num2 != 0:
            result = num1 / num2
            print(f"The result is {result}.")
        else:
            print("Error: division by zero is not allowed.")
    case _:
        print("unknown operation")
        
