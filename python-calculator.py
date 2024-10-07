def calculator():
    print("Simple Calculator")
    
    # Input first number
    num1 = float(input("Enter First Number: "))
    
    # Input second number
    num2 = float(input("Enter Second Number: "))
    
    # Choose operation
    print("Choose Operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    operation = input("Enter operation number (1-4): ")
    
    # Perform calculation based on chosen operation
    if operation == '1':
        result = num1 + num2
        operator = '+'
    elif operation == '2':
        result = num1 - num2
        operator = '-'
    elif operation == '3':
        result = num1 * num2
        operator = '*'
    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            operator = '/'
        else:
            return "Error: Division by zero!"
    else:
        return "Invalid operation selected!"
    
    # Display result
    print(f"Result: {num1} {operator} {num2} = {result}")

# Run the calculator
if __name__ == "__main__":
    calculator()
