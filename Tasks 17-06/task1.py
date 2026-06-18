### Q1.
# Write a program to divide 100 by a user-input number. Handle both zero and non-integer inputs.

try:
    n = int(input("Enter the number:"))
    res = 100/n
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Enter a valid number !")
else:
    print("Result is",res)