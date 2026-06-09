num = int(input("Enter a number of which you want the table: "))
print(f"Table of {num} is:")
i = 1
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1