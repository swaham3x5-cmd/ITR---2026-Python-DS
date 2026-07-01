# Perform addition to each element of array without ventorization
numbers = [1,2,3,4]
result = []
for i in range(len(numbers)):
     result.append(numbers[i] + 5)
print(f"Result = {result}")

# Perform addition to each element of array with ventorization
import numpy as np

numbers = np.array([1,2,3,4])
print(numbers + 5)