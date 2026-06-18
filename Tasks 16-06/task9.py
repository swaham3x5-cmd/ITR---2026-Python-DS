while True:
    try:
        num=int(input("Enter the number: "))
        print("You entered:",num)
        break
    except ValueError:
        print("Invalid input. Try again.")
