#Exception handling
try:
    num=int(input("Enter the no:"))
    print(100/num)
except ZeroDivisionError:
    print("Cannot divide by zero")