### List

# Create a list of your favorite colors and print it.
list_of_colors = ['red', 'blue', 'green']
print(f"My favorite colors: {list_of_colors}")

# Given a list of three numbers, print the third number using indexing.
numbers = [10, 20, 30]
print(f"The original list of numbers: {numbers}")
print(f"The third number is: {numbers[2]}")

# Create a list of five animals and print the middle three using slicing.
animals = ['lion', 'tiger', 'elephant', 'giraffe', 'zebra']
print(f"The original list of animals: {animals}")
print(f"The middle three animals are: {animals[1:4]}")

# Given a list of four items, print the second to last item using negative indexing.
items = ['apple', 'banana', 'cherry', 'date']
print(f"The original list of items: {items}")
print(f"The second to last item is: {items[-2]}")

# Change the last element of a list numbers = [10, 20, 30] to 40 and print the list.
numbers = [10, 20, 30]
print(f"The original list is: {numbers}")
numbers[-1] = 40
print(f"The updated list is: {numbers}")

# Start with numbers = [1, 2, 3]. Use append to add 4 and print the list.
numbers = [1, 2, 3]
print(f"The original list is: {numbers}")
numbers.append(4)
print(f"The updated list is: {numbers}")

# Given letters = ['a', 'c', 'd'], insert 'b' at index 1 and print the list.
letters = ['a', 'c', 'd']
print(f"The original list is: {letters}")
letters.insert(1, 'b')
print(f"The updated list is: {letters}")

# Given nums = [1, 2, 3, 4], remove the number 3 and print the list.
nums = [1, 2, 3, 4]
print(f"The original list is of nums: {nums}")
nums.remove(3)
print(f"The updated list is of nums: {nums}")