# Operations on set

# 1. Creating a set
from typing import Union


nums = {1, 2, 3, 4}
print(f"nums: {nums}")  # Output: nums: {1, 2, 3, 4}

# 2. Adding elements
nums.add(5)
print(f"nums after adding 5: {nums}")  # Output: nums after adding 5: {1, 2, 3, 4, 5}

# 3. Removing elements
nums.remove(2)
print(f"nums after removing 2: {nums}")  # Output: nums after removing 2: {1, 3, 4, 5}  

# 4. Union
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(f"set1:{set1} set2:{set2} Union: {set1 | set2}")  # Output: Union: {1, 2, 3, 4, 5, 6}

# 5. Intersection
print(f"set1:{set1} set2:{set2} Intersection: {set1 & set2}")  # Output: Intersection: {3}

# 6. Difference
print(f"set1:{set1} set2:{set2} Difference (set1 - set2): {set1 - set2}")  # Output: Difference (set1 - set2): {1, 2, 6}
print(f"set1:{set1} set2:{set2} Difference (set2 - set1): {set2 - set1}")  # Output: Difference (set2 - set1): {4, 5}

# 7. Membership
nums1 = {1, 2, 3, 6}
print(f"Membership: 2 in nums1: {2 in nums1}")  # Output: Membership: 2 in nums1: True