### Dictionary

# Create a dictionary for a book with keys title, author, and year, then print it.
book = {"title": "Dead Person's Viewpoint", "author": "Swaham", "year": 2008}
print(f"The book dictionary is: {book}")

# Given student = {"id": 101, "grade": "A"}, print the student's grade.
student = {"id": 101, "grade": "A"}
print(f"The student's grade is: {student['grade']}")

# Start with d = {"a": 1}. Add a new key "b" with value 2 and print d.
d = {"a": 1}
d["b"] = 2
print(f"The updated dictionary is: {d}")

# Given d = {"x": 9, "y": 8}, change the value of "x" to 10 and print d.
d = {"x": 9, "y": 8}
d["x"] = 10
print(f"The updated dictionary is: {d}")

# Given d = {"a": 1, "b": 2}, remove key "a" using pop and print d.
d = {"a": 1, "b": 2}
d.pop("a")
print(f"The updated dictionary is: {d}")

# For d = {"a": 1, "b": 2}, print the list of keys and the list of values.
d = {"a": 1, "b": 2}
print(f"The keys are: {list(d.keys())}")
print(f"The values are: {list(d.values())}")