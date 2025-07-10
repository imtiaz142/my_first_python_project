import sys

# ----------------------------------------
# 1. split() - Splitting a string into a list
# ----------------------------------------

text = "apple,banana,grape"
# Syntax: str.split(separator, maxsplit)
fruits = text.split(",")  # Split by comma
print("split():", fruits)  # ['apple', 'banana', 'grape']

limited_split = text.split(",", 1)  # Only 1 split
print("split() with maxsplit:", limited_split)  # ['apple', 'banana,grape']

# ----------------------------------------
# 2. join() - Joining list into a string
# ----------------------------------------

# Syntax: separator.join(list)
joined = "-".join(fruits)
print("join():", joined)  # apple-banana-grape

# ----------------------------------------
# 3. replace() - Replacing substrings
# ----------------------------------------

message = "hello world world"
# Syntax: str.replace(old, new, count)
replaced_all = message.replace("world", "Python")
print("replace() all:", replaced_all)  # hello Python Python

replaced_once = message.replace("world", "Python", 1)
print("replace() once:", replaced_once)  # hello Python world

# ----------------------------------------
# 4. find() - Finding the index of a substring
# ----------------------------------------

sentence = "Python is awesome"
index = sentence.find("is")  # Returns 7
not_found = sentence.find("Java")  # Returns -1
print("find() found:", index)
print("find() not found:", not_found)

# ----------------------------------------
# 5. count() - Count occurrences of a substring
# ----------------------------------------

fruit_text = "apple banana apple grape apple"
apple_count = fruit_text.count("apple")
print("count():", apple_count)  # 3

# ----------------------------------------
# 6. String Formatting
# ----------------------------------------

name = "Ali"
age = 25
pi = 3.14159

# %-style formatting
print("Old (% formatting): My name is %s and I am %d" % (name, age))

# str.format() method
print("format(): My name is {} and I am {}".format(name, age))

# f-strings (Python 3.6+)
print(f"f-string: My name is {name} and I am {age}")
print(f"PI rounded to 2 decimals: {pi:.2f}")
print(f"Number with comma: {1000000:,}")
print(f"Padded number: {42:05}")  # 00042

# Align text using f-strings
print(f"{'Name':<10} {'Age':>5}")
print(f"{name:<10} {age:>5}")

# ----------------------------------------
# 7. String Interning vs String Pool
# --------------------------------
# ----------------------------------------
# 1. Escape Sequence Characters
# ----------------------------------------
print("Escape Sequences:")
print("Hello\nWorld")         # New line
print("Name\tAge")           # Tab space
print("C:\\Users\\Ali")       # Backslash
print('It\'s fine')           # Single quote
print("She said: \"Hi\"")     # Double quote
print("Hello\rWorld")         # Carriage return
print("Helloo\b World")       # Backspace
print("Page\fBreak")          # Form feed
print('\u2764')               # Unicode heart: ❤
print(r"Raw string: C:\new\path")  # Raw string, no escape

# ----------------------------------------
# 2. split() - Splitting a string into a list
# ----------------------------------------
print("\nString split():")
text = "apple,banana,grape"
print(text.split(","))
print(text.split(",", 2))  # Limit to 2 splits

# ----------------------------------------
# 3. join() - Joining list into a string
# ----------------------------------------
print("\nString join():")
fruits = ["apple", "banana", "grape"]
print("-".join(fruits))

# ----------------------------------------
# 4. replace() - Replacing substrings
# ----------------------------------------
print("\nString replace():")
msg = "apple apple apple"
print(msg.replace("apple", "banana"))         # Replace all
print(msg.replace("apple", "banana", 2))     # Replace first 2 only

# ----------------------------------------
# 5. find() - Finding the index of a substring
# ----------------------------------------
print("\nString find():")
sentence = "Python is awesome"
print(sentence.find("is"))     # Returns index 7
print(sentence.find("Java"))   # Returns -1 (not found)

# ----------------------------------------
# 6. count() - Counting occurrences
# ----------------------------------------
print("\nString count():")
line = "apple banana apple grape apple"
print(line.count("apple"))     # Output: 3

# ----------------------------------------
# 7. String Formatting
# ----------------------------------------
print("\nString Formatting:")
name = "Ali"
age = 25
pi = 3.14159

# %-style formatting (old style)
print("My name is %s and I am %d years old." % (name, age))

# str.format()
print("My name is {} and I am {} years old.".format(name, age))
print("Pi to 2 decimals: {:.2f}".format(pi))

# f-string (recommended)
print(f"My name is {name} and I am {age} years old.")
print(f"Pi rounded: {pi:.2f}")
print(f"Number with commas: {1000000:,}")
print(f"Padded number: {42:05}")

# Aligning text
print(f"{'Name':<10}{'Age':>5}")
print(f"{name:<10}{age:>5}")

# ----------------------------------------
# 8. String Interning and String Pool
# ----------------------------------------
print("\nString Interning:")
a = "hello"
b = "hello"
print("a is b:", a is b)  # True – auto interned

x = "hello world!"
y = "hello world!"
print("x is y (before intern):", x is y)  # May be False

# Using sys.intern to manually intern
x = sys.intern("hello world!")
y = sys.intern("hello world!")
print("x is y (after intern):", x is y)   # True

# Check using expressions
var = "python"
print(f"String from pool: {'python' is var}")  # True
# ----------------------------------------
# 9. String Slicing
# ----------------------------------------
print("\nString Slicing:")
s = "Python Programming"

# Syntax: s[start:stop:step]
print(s[0:6])         # Output: Python
print(s[7:])          # Output: Programming (from index 7 to end)
print(s[:6])          # Output: Python (start to index 6)
print(s[::2])         # Output: Pto rgamn (every 2nd char)
print(s[::-1])        # Output: gnimmargorP nohtyP (reversed)
print(s[-11:-1])      # Output: Programmin (negative indices)

# Explanation of slicing syntax in comments:
# s[start:stop] → includes characters from start to stop-1
# s[start:stop:step] → step is how many characters to skip


