# array function 

fruits = ["Apple","Banana","Cherry"]
numbers = [1,2,3,4,5]

print(fruits)
print(numbers)


# 2. Accessing list elements
print("Accessing list elements:")

fruits = ["Apple", "Banana", "Cherry"]
numbers = [1, 2, 3, 4, 5]

print(fruits[1])   # Output: Banana
print(numbers[3])  # Output: 4

print(fruits[-1])  # Last element → Cherry
print(fruits[-2])  # Second last element → Banana
print(numbers[-3]) # Third last element → 3

print(fruits[0:2])   # First two elements → ['Apple', 'Banana']
print(numbers[2:])   # From index 2 onwards → [3, 4, 5]
print(numbers[:3])   # First three elements → [1, 2, 3]
print(fruits[::2])  # Every second element → ['Apple', 'Cherry']

print(numbers[::2])   # Every second element → [1, 3, 5]
print(numbers[1::2])  # Every second element starting at index 1 → [2, 4]

numbers = [1, 2, 3, 4, 5]
print(numbers[1::2])  # Output: [2, 4]

numbers = [1, 2, 3, 4, 5]

print(numbers[::2])   # [1, 3, 5] → step of 2, starting at index 0
print(numbers[1::2])  # [2, 4]   → step of 2, starting at index 1
print(numbers[::3])   # [1, 4]   → step of 3, starting at index 0
print(numbers[1::3])  # [2, 5]   → step of 3, starting at index 1

# 3. Adding additional values to the existing list at the end
print("Adding additional values to the existing list at the end:")

numbers = [1, 2, 3, 4, 5]
numbers.append(6)   # append() adds a single element at the end
print(numbers)      # Output: [1, 2, 3, 4, 5, 6]
numbers.extend([7, 8])  # extend() adds multiple elements at the end
print(numbers)          # Output: [1, 2, 3, 4, 5, 6, 7, 8]

numbers.insert(0, 0)     # Insert at index 0
print(numbers)           # [0, 1, 2, 3, 4, 5, 6, 7, 8]
numbers.insert(3, 2.5)   # Insert 2.5 at index 3
print(numbers)           # [0, 1, 2, 2.5, 3, 4, 5, 6, 7, 8]

numbers.insert(3, 99)    # Insert at index 3
print(numbers)           # [0, 1, 2, 99, 3, 4, 5, 6, 7, 8]
numbers.insert(0, -1)   # Insert at the beginning
print(numbers)           # [-1, 0, 1, 2, 99, 3, 4, 5, 6, 7, 8]

more_numbers = [100, 200]
combined = numbers + more_numbers
print(combined)          # [0, 1, 2, 99, 3, 4, 5, 6, 7, 8, 100, 200]

# 4. Removing the last element from the array.
print("Removing the last element from the array:")

numbers = [1, 2, 3, 4, 5]  # Example array
print(numbers)
numbers.pop()
print(numbers)

numbers = [1, 2, 3]
numbers = [10, 20] + numbers   # prepend multiple values
print(numbers)  # [10, 20, 1, 2, 3]
numbers = [1, 2, 3]
numbers = [0] + numbers        # prepend a single value 
print(numbers)  # [0, 1, 2, 3]  

# 6. Removing the first element from the array.
print("Removing the first element from the array:")

numbers = [1, 2, 3, 4, 5]  # Example list
numbers.pop(0)             # removes the element at index 0 (the first one)
print(numbers)
numbers = [1, 2, 3, 4, 5]
numbers = numbers[1:]      # creates a new list without the first element   
print(numbers)


# 7. Add or remove one or more values within the array from a specific index.
print("Add or remove one or more values within the array from a specific index:")

numbers = [1, 2, 3, 4, 5]   # Example list

# Equivalent of splice(2, 2, 2.5, 3.5):
# - Start at index 2
# - Remove 2 elements
# - Insert 2.5 and 3.5 at that position
numbers[2:4] = [2.5, 3.5]

print(numbers)
numbers = [1, 2, 3, 4, 5]   # Example list
numbers[2:4] = []            # Remove 2 elements starting at index 2    
print(numbers)
numbers = [1, 2, 3, 4, 5]   # Example list
numbers[2:2] = [2.5, 3.5]    # Insert 2.5 and 3.5 at index 2 without removing any elements
print(numbers)

# 8. Creating a new array by extracting a portion of an existing array.
print("Creating a new array by extracting a portion of an existing array:")

numbers = [1, 2, 3, 4, 5]   # Example list

# Equivalent of slice(2, 4):
# - Start at index 2
# - End before index 4 (exclusive)
extracted_values = numbers[2:4]

print(extracted_values)

# 9. Merge two or more arrays and create a new array.
print("Merge two or more arrays and create a new array:")

numbers1 = [1, 2, 3, 4]
numbers2 = [5, 6, 7, 8]

# Equivalent of concat in TypeScript
merged_array = numbers1 + numbers2

print(merged_array)

merged_array = numbers1 + numbers2 + [9, 10]
print(merged_array)  # [1,2,3,4,5,6,7,8,9,10]

numbers1 = [1, 2, 3, 4]
numbers2 = [5, 6, 7, 8]
numbers3 = [9, 10]

# New merged list
merged_array = numbers1 + numbers2 + numbers3
print(merged_array)
print("Merged:", merged_array)

# Spread-like unpacking
spread_merge = [*numbers1, *numbers2, *numbers3]
print("Spread merge:", spread_merge)

# Mutating the original list
numbers1.extend(numbers2)
print("After extend:", numbers1)

# 11. Iterate the values of the array.
print("Iterate the values of the array:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for index, fruit in enumerate(fruits):
    print(index, fruit)

fruits = ["apple", "banana", "cherry"]

# map → uppercase
upper_fruits = [fruit.upper() for fruit in fruits]
print("Map:", upper_fruits)

# filter → starts with 'a'
a_fruits = [fruit for fruit in fruits if fruit.startswith("a")]
print("Filter:", a_fruits)

# find → first fruit longer than 5 letters
found = next((fruit for fruit in fruits if len(fruit) > 5), None)
print("Find:", found)

# reduce → total length of all fruit names
total_length = sum(len(fruit) for fruit in fruits)
print("Reduce:", total_length)

# 12. Reverse the values within the array.
print("Reverse the values within the array:")

num = [1, 2, 7, 3, 4, 5, 6, 10]
print(num)
# Equivalent of num.reverse() in TypeScript
num.reverse()
print(num)


# 13. Sort the values within the array.
print("Sort the values within the array:")

num = [1, 2, 7, 3, 4, 5, 6, 10]
print(num)
# Ascending order
num.sort()
print(num)

# Descending order
num.sort(reverse=True)
print(num)

# Descending numeric sort
num = [1, 2, 7, 3, 4, 5, 6, 10]
num.sort(reverse=True)
print(num)  # [10, 7, 6, 5, 4, 3, 2, 1]

# Descending string sort (alphabetical)
fruits = ["banana", "apple", "cherry"]
fruits.sort(reverse=True)
print(fruits)  # ['cherry', 'banana', 'apple']

# Sort by length of strings (longest first)

fruits = ["banana", "apple", "cherry"]
fruits.sort(key=len, reverse=True)
print(fruits)  # ['banana', 'cherry', 'apple']

#Sort tuples by second element (descending)
tuples = [(1, 3), (2, 1), (3, 2)]
tuples.sort(key=lambda x: x[1], reverse=True)
print(tuples)  # [(1, 3), (3, 2), (2, 1)]

# Sort mixed values with custom rule (e.g., even numbers first, descending)
mixed_numbers = [1, 2, 3, 4, 5, 6]
mixed_numbers.sort(key=lambda x: (x % 2 == 0, -x))  # Even numbers first, then descending
print(mixed_numbers)  # [6, 4, 2, 5, 3, 1]


print('\n--- map / filter / forEach examples (translated) ---')
input_list = [1, 2, 3, 4, 5, 6]

# map: get the square of each number
square_numbers = list(map(lambda x: x * x, input_list))
print('Squares:', square_numbers)

# filter: keep only even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, input_list))
print('Evens:', even_numbers)

# forEach: iterate and print each value (Pythonic for-loop)
print('Iterate:')
for x in input_list:
    print(x)

