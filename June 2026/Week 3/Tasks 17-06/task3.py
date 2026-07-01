### Q3.
# Catch non-integer inputs and print *"Invalid input"* if the user enters letters.

try:
    n = int(input("Enter the number:"))
except ValueError:
    print("Invalid input")
else:
    print("Entered Value is",n)