# Example 1: Creating a new array by extracting a portion of an existing array
numbers = [1, 2, 3, 4, 5]
print("Creating a new array by extracting a portion of an existing array:")
extracted_values = numbers[2:4]   # slice(startIndex:endIndex)
print(extracted_values)           # Output: [3, 4]


# Example 2: Slice from index 1 to 3 (end is exclusive)
numbers_exmp_two = [10, 20, 30, 40, 50]
part = numbers_exmp_two[1:4]
print(part)                       # Output: [20, 30, 40]

# Slice with negative index
last_two = numbers_exmp_two[-2:]
print(last_two)                   # Output: [40, 50]


# Example 3: String slicing
text = "PythonScript"

# Slice from index 0 to 7
first_part = text[0:6]
print(first_part)                 # Output: "Python"

# Slice with negative index
last_part = text[-6:]
print(last_part)                  # Output: "Script"


# Example 4: Comparing slice and substring
# In Python, substring is achieved using slice itself
str_val = "Interview"
print(str_val[2:5])               # Output: "ter"
# No separate substring() method in Python, slicing covers it
