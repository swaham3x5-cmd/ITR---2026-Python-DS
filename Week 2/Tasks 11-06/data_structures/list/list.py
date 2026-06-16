# Operations on Lists

# 1. Creating a list
fruits = ["apple", "banana", "cherry"]
print(f"fruits: {fruits}")  # Output: fruits: ['apple', 'banana', 'cherry']

# 2. Accessing elements
print(f"fruits[0]: {fruits[0]}")  # Output: fruits[0]: apple
print(f"fruits[1]: {fruits[1]}")  # Output: fruits[1]: banana
print(f"fruits[2]: {fruits[2]}")  # Output: fruits[2]: cherry

# 3. Slicing a list
print(f"fruits[0:2]: {fruits[0:2]}")  # Output: fruits[0:2]: ['apple', 'banana']
print(f"fruits[1:3]: {fruits[1:3]}")  # Output: fruits[1:3]: ['banana', 'cherry']

# 4. Negative indexing
print(f"fruits[-1]: {fruits[-1]}")  # Output: fruits[-1]: cherry
print(f"fruits[-2]: {fruits[-2]}")  # Output: fruits[-2]: banana
print(f"fruits[-3]: {fruits[-3]}")  # Output: fruits[-3]: apple

# 5. Changing element
fruits[0] = "orange"
print(f"fruits: {fruits}")  # Output: fruits: ['orange', 'banana', 'cherry']

# 6. Adding elements with append()
fruits.append("orange")
print(f"fruits: {fruits}")  # Output: fruits: ['orange', 'banana', 'cherry', 'orange']

# 7. Inserting elements
fruits.insert(1, "kiwi")
print(f"fruits: {fruits}")  # Output: fruits: ['orange', 'kiwi', 'banana', 'cherry', 'orange']

# 8. Removing elements
fruits.remove("banana")
print(f"fruits: {fruits}")  # Output: fruits: ['orange', 'kiwi', 'cherry', 'orange']