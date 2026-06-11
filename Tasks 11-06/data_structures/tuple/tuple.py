# Operations on tuple

# 1. Creating a tuple
coord = (10, 20)
print(f"coord: {coord}")  # Output: coord: (10, 20)

# 2. Accessing elements
print(f"coord[0]: {coord[0]}")  # Output: coord[0]: 10
print(f"coord[1]: {coord[1]}")  # Output: coord[1]: 20

# 3. Negative indexing
print(f"coord[-1]: {coord[-1]}")  # Output: coord[-1]: 20
print(f"coord[-2]: {coord[-2]}")  # Output: coord[-2]: 10

# 4. Slicing a tuple
print(f"coord[0:2]: {coord[0:2]}")  # Output: coord[0:2]: (10, 20)

# 6. Counting elements
print(f"coord.count(10): {coord.count(10)}")  # Output: coord.count(10): 1
print(f"coord.count(20): {coord.count(20)}")  # Output: coord.count(20): 1

# 7. Finding index of an element
print(f"coord.index(10): {coord.index(10)}")  # Output: coord.index(10): 0

# 8. Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5)
concatenated = tuple1 + tuple2 + coord
print(f"concatenated: {concatenated}")  # Output: concatenated: (1, 2, 3, 4, 5, 10, 20)