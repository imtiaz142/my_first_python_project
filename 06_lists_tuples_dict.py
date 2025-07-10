# -----------------------------------------
# 1. LIST CREATION
# -----------------------------------------

# Syntax: my_list = [item1, item2, ...]
empty_list = []
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "text", 3.14, True]
nested = [1, 2, [3, 4], 5]

print("Fruits:", fruits)

# -----------------------------------------
# 2. ACCESSING ELEMENTS
# -----------------------------------------

# Syntax: list[index]
print("First fruit:", fruits[0])      # apple
print("Last fruit:", fruits[-1])      # cherry
print("Nested value:", nested[2][1])  # 4

# -----------------------------------------
# 3. SLICING LISTS
# -----------------------------------------

# Syntax: list[start:end]
print("Slice [1:4]:", numbers[1:4])  # [2, 3, 4]
print("Slice [:3]:", numbers[:3])    # [1, 2, 3]
print("Slice [2:]:", numbers[2:])    # [3, 4, 5]

# -----------------------------------------
# 4. CHECK IF ITEM EXISTS
# -----------------------------------------

# Syntax: item in list
print("Is 'banana' in fruits?", "banana" in fruits)  # True

# -----------------------------------------
# 5. MODIFYING ITEMS
# -----------------------------------------

# Syntax: list[index] = new_value
fruits[1] = "mango"
print("Modified fruits:", fruits)  # ['apple', 'mango', 'cherry']

# -----------------------------------------
# 6. ADDING ITEMS
# -----------------------------------------

# append() – adds to end (no return value)
fruits.append("orange")
print("After append:", fruits)

# insert() – inserts at index
fruits.insert(1, "grape")
print("After insert:", fruits)

# extend() – adds multiple items
fruits.extend(["kiwi", "melon"])
print("After extend:", fruits)

# -----------------------------------------
# 7. REMOVING ITEMS
# -----------------------------------------

# remove() – removes first occurrence
fruits.remove("grape")
print("After remove:", fruits)

# pop() – removes and returns item
last_item = fruits.pop()
print("Popped item:", last_item)
print("After pop:", fruits)

# del – delete item at index
del fruits[0]
print("After del:", fruits)

# clear() – empties the list
# fruits.clear()
# print("After clear:", fruits)

# -----------------------------------------
# 8. LOOPING THROUGH LISTS
# -----------------------------------------

# For loop
print("For loop:")
for fruit in fruits:
    print("-", fruit)

# While loop
print("While loop:")
i = 0
while i < len(fruits):
    print("-", fruits[i])
    i += 1

# -----------------------------------------
# 9. LENGTH OF LIST
# -----------------------------------------

# Syntax: len(list)
print("Length of fruits list:", len(fruits))

# -----------------------------------------
# 10. RETURNING METHODS
# -----------------------------------------

nums = [1, 2, 2, 3, 4, 2]

# count() – returns how many times value appears
print("Count of 2:", nums.count(2))  # 3

# index() – returns index of first occurrence
print("Index of 3:", nums.index(3))  # 3

# copy() – returns a new list (shallow copy)
copy_nums = nums.copy()
print("Copied list:", copy_nums)

# -----------------------------------------
# 11. IN-PLACE METHODS (NO RETURN)
# -----------------------------------------

# sort() – sorts list (permanently changes it)
unsorted = [4, 1, 3, 5, 2]
unsorted.sort()
print("Sorted list:", unsorted)

# reverse() – reverses list
unsorted.reverse()
print("Reversed list:", unsorted)

# -----------------------------------------
# 12. LIST COMPREHENSIONS
# -----------------------------------------

# Syntax: [expression for item in iterable]
squares = [x**2 for x in range(6)]
print("Squares:", squares)  # [0, 1, 4, 9, 16, 25]

# With condition
evens = [x for x in range(10) if x % 2 == 0]
print("Even numbers:", evens)  # [0, 2, 4, 6, 8]

# -----------------------------------------
# 13. NESTED LISTS (2D LISTS)
# -----------------------------------------

# Syntax: list of lists
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print("Matrix[1][2]:", matrix[1][2])  # 6

# -----------------------------------------
# 14. COMBINE & MULTIPLY LISTS
# -----------------------------------------

# Combine lists using +
combined = [1, 2] + [3, 4]
print("Combined list:", combined)

# Repeat list using *
repeated = [0] * 5
print("Repeated list:", repeated)

# -----------------------------------------
# 15. DIFFERENCE: LIST VS TUPLE
# -----------------------------------------

my_list = [1, 2, 3]  # Mutable
my_tuple = (1, 2, 3)  # Immutable

my_list[0] = 100  # ✅ allowed
# my_tuple[0] = 100  # ❌ error
print("List modified:", my_list)
print("Tuple remains:", my_tuple)



#-------------------------------------------------Tuples---------------------------------------------------------------------------