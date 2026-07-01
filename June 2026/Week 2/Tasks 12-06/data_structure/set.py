### Sets

# Create a set of three letters, e.g., {'a', 'b', 'c'}, and print it.
s = {'a', 'b', 'c'}
print(f"The set is: {s}")

# Start with s = {'x', 'y'}. Add 'z' to the set and print it.
s = {'x', 'y'}
s.add('z')
print(f"The updated set is: {s}")

# Given s = {'a', 'b', 'c'}, remove 'b' and print the set.
s = {'a', 'b', 'c'}
s.remove('b')
print(f"The updated set is: {s}")  

# Given a = {10, 20} and b = {20, 30}, print the union of a and b.
a = {10, 20}
b = {20, 30}
print(f"The union of a and b is: {a.union(b)}")

# Given a = {5, 6} and b = {6, 7}, print the intersection of a and b.
a = {5, 6}
b = {6, 7}
print(f"The intersection of a and b is: {a.intersection(b)}")

# Check if 'x' is in the set {'x', 'y', 'z'} and print the result.
s = {'x', 'y', 'z'}
print(f"Is 'x' in the set? {'x' in s}")