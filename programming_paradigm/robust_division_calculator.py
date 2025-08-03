def safe_divide(float(numerator), float(denominator)):
    try:
        result = numerator / denominator
    
    except (ValueError, TypeError):
        print("Error: Please enter numeric values only.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    else:
        print(f"The result of the division is {result}")

