def calculator():
    print("=== Simple Calculator ===")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    print("\nChoose operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1/2/3/4): ").strip()
    if choice == '1':
        result = num1 + num2
    elif choice == '2':
        result = num1 - num2
    elif choice == '3':
        result = num1 * num2
    elif choice == '4':
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            return
        result = num1 / num2
    else:
        print("Invalid choice.")
        return

    print("Result:", result)

if __name__ == "__main__":
    calculator()
