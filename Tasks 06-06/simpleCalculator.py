# Day 1 Assignment – Creating a simple calculator

# Menu
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice = int(input("Enter choice (1/2/3/4): "))

if choice == 1 or (choice > 1 and choice < 5):
    # Take input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Perform the chosen operation
    if choice == 1:
        print(num1, "+", num2, "=", num1 + num2)
    elif choice == 2:
        print(num1, "-", num2, "=", num1 - num2)
    elif choice == 3:
        print(num1, "*", num2, "=", num1 * num2)
    elif choice == 4:
        if num2 != 0:
            print(num1, "/", num2, "=", num1 / num2)
        else:
            print("Error: Division by zero is not allowed.")
            
else:
    print("Invalid input")