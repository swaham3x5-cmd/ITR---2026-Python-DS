### Q4.
# Ask the user to enter a number between 1 and 10. Keep retrying if the input is not a number or is out of range.

while True:
    try:
        num = int(input("Enter the number between 1 and 10: "))
        if ((num > 1) and (num < 10)):
            print("You entered:",num)
            break
    except ValueError:
        print("Invalid Input! Try again")
    