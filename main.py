def calculator():
    print("=== Simple Calculator ===")
    print("Operations: +, -, *, /, **")
    
    while True:
        try:
            user_input = input("Enter first number (or 'quit' to exit): ").strip()
            if user_input.lower() == 'quit':
                print("Goodbye!")
                break
            num1 = float(user_input)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        operation = input("Enter operation (+, -, *, /, **): ").strip()
        if operation not in ['+', '-', '*', '/', '**']:
            print("Invalid operation. Please use +, -, *, /, or **")
            continue
        
        try:
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Cannot divide by zero!")
                continue
            result = num1 / num2
        elif operation == '**':
            result = num1 ** num2
        
        print(f"\n{num1} {operation} {num2} = {result}\n")

if __name__ == "__main__":
    calculator()