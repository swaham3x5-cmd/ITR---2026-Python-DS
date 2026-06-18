### Q2.
# Add a finally block to print *"Operation complete"* no matter what happens.

try:
    n = int(input("Enter the number:"))
except ValueError:
    print("Enter a valid number !")
else:
    print("Entered Value is",n)
finally:
    print("Execution completed.")