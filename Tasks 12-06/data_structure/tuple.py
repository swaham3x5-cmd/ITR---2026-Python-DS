### Tuples

# Create a tuple with three elements (like (1, 2, 3)) and print it.
tuple_of_numbers = (1, 2, 3)
print(f"My tuple of numbers: {tuple_of_numbers}")

# Given t = (5, 6, 7, 8), print the third element.
t = (5, 6, 7, 8)
print(f"The original tuple is: {t}")
print(f"The third element is: {t[2]}")

# Given a tuple of four colors, print the second to last color using negative indexing.
colors = ('red', 'blue', 'green', 'yellow')
print(f"The original tuple of colors is: {colors}")
print(f"The second to last color is: {colors[-2]}")

# Slice the tuple (100, 200, 300, 400, 500) to get (200, 300).
sliced_tuple = (100, 200, 300, 400, 500)[1:3]
print(f"The original tuple is: {(100, 200, 300, 400, 500)}")
print(f"The sliced tuple is: {sliced_tuple}")

# Create a tuple (2, 3, 2, 2, 4) and print how many times 2 appears.
tuple_with_duplicates = (2, 3, 2, 2, 4)
print(f"The original tuple is: {tuple_with_duplicates}")
print(f"The number of times 2 appears is: {tuple_with_duplicates.count(2)}")

# Join (7, 8) and (9, 10) into one tuple and print it.
tuple1 = (7, 8)
print(f"The first tuple is: {tuple1}")
tuple2 = (9, 10)
print(f"The second tuple is: {tuple2}")
joined_tuple = tuple1 + tuple2
print(f"The joined tuple is: {joined_tuple}")