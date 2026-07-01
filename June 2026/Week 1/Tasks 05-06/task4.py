# Check for negative even and negative odd.

number = -51

if number < 0:
    if number % 2 == 0:
        print("Number is negative even")
    else:
        print("Number is negative odd")
else:
    print("Number is positive or zero")