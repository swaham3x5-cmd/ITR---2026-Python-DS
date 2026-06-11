# Operations on Dictionaries

# 1. Creating a dictionary
person = {"name": "Swaham", "age": 17}
print(person)

# 2. Accessing values
print(person["name"])  # Output: Swaham
print(person["age"])   # Output: 17

# 3. Adding a new key-value pair
person["city"] = "Dombivli"
print(person)

# 4. Changing values
person["age"] = 18
print(person)

# 5. Removing a key-value pair
person.pop("city")
print(person)

# 6. Keys and Values
print(person.keys())   # Output: dict_keys(['name', 'age'])
print(person.values()) # Output: dict_values(['Swaham', 18])

# 8. Checking key existance
print(f"Checking if 'name' exists in person? {'name' in person}")  # Output: True