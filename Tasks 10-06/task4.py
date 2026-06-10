# Take a number as user input and print its multiplication table using a while loop with a single initialization.

num = int(input("Enter a number of which you want the table: "))
print(f"Table of {num} is:")

i = 1   #Initialization

while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1  # Incrementation