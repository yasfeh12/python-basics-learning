# Tuples are immutable - they cannot be modified after creation.
coordinates = (4, 5)
print("First element:", coordinates[0])  # Accessing elements in a tuple

# Tuple packing and unpacking
point = 4, 5  # Packing without parentheses
x, y = point  # Unpacking tuple
print("x:", x, "y:", y)

# Single-element tuple (note the comma)
single_element_tuple = (42,)
print(type(single_element_tuple))  # Output: <class 'tuple'>

# Tuple methods: count and index
nums = (1, 2, 2, 3)
print("Count of 2:", nums.count(2))
print("Index of 3:", nums.index(3))
