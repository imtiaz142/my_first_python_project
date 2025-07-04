# =============================================
# ✅ Operator and Operand in Python - Full Demo
# =============================================

# =============================================
# 🧮 Arithmetic Operators
# =============================================
a = 10
b = 3

print("Arithmetic Operators:")
print("a + b =", a + b)    # 13
print("a - b =", a - b)    # 7
print("a * b =", a * b)    # 30
print("a / b =", a / b)    # 3.333...
print("a % b =", a % b)    # 1
print("a ** b =", a ** b)  # 1000
print("a // b =", a // b)  # 3
print()

# =============================================
# 📌 Assignment Operators
# =============================================
x = 5
print("Assignment Operators:")
print("Initial x =", x)

x += 3  # x = x + 3
print("After x += 3:", x)

x *= 2  # x = x * 2
print("After x *= 2:", x)

x -= 4  # x = x - 4
print("After x -= 4:", x)

x /= 2  # x = x / 2
print("After x /= 2:", x)
print()

# =============================================
# 📊 Comparison Operators
# =============================================
a = 10
b = 5
print("Comparison Operators:")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)
print()

# =============================================
# 🔁 Logical Operators
# =============================================
x = 7
print("Logical Operators:")
print("x > 5 and x < 10:", x > 5 and x < 10)  # True
print("x < 5 or x > 10:", x < 5 or x > 10)   # False
print("not(x > 5):", not(x > 5))             # False
print()

# =============================================
# 🧠 Bitwise Operators
# =============================================
a = 5       # 0101
b = 3       # 0011

print("Bitwise Operators:")
print("a & b:", a & b)   # 0001 -> 1
print("a | b:", a | b)   # 0111 -> 7
print("a ^ b:", a ^ b)   # 0110 -> 6
print("~a:", ~a)         # Bitwise NOT (inverts bits), -6
print("a << 1:", a << 1) # 1010 -> 10
print("a >> 1:", a >> 1) # 0010 -> 2
print()

# =============================================
# 📚 Membership Operators
# =============================================
fruits = ['apple', 'banana', 'cherry']
print("Membership Operators:")
print("'apple' in fruits:", 'apple' in fruits)
print("'mango' not in fruits:", 'mango' not in fruits)
print()

# =============================================
# 🆔 Identity Operators
# =============================================
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print("Identity Operators:")
print("a is b:", a is b)         # False (different memory)
print("a is c:", a is c)         # True (same memory)
print("a is not b:", a is not b) # True
print()

# =============================================
# 🆔 Identity Operators
# =============================================


import keyword

# Line continuation (`\`) allows printing a statement over multiple lines, improving code readability without breaking the string.
print("The list of \
keywords is : ")

# printing all keywords at once using "kwlist()"
print(keyword.kwlist)




# ============================================
# ✅ Assigning Different Values in Python
# ============================================

# --------------------------------------------
# 🔹 1. Basic Assignment
# --------------------------------------------
a = 5
b = "hello"
c = 3.14
d = True

print("Basic Assignment:")
print("a =", a)     # Output: a = 5
print("b =", b)     # Output: b = hello
print("c =", c)     # Output: c = 3.14
print("d =", d)     # Output: d = True
print()

# --------------------------------------------
# 🔹 2a. Assign Same Value to Multiple Variables
# --------------------------------------------
x = y = z = 100

print("Assign Same Value to Multiple Variables:")
print("x =", x)     # Output: x = 100
print("y =", y)     # Output: y = 100
print("z =", z)     # Output: z = 100
print()

# --------------------------------------------
# 🔹 2b. Assign Different Values to Multiple Variables
# --------------------------------------------
p, q, r = 1, 2, 3

print("Assign Different Values to Multiple Variables:")
print("p =", p)     # Output: p = 1
print("q =", q)     # Output: q = 2
print("r =", r)     # Output: r = 3
print()

# --------------------------------------------
# 🔹 3. Swapping Values (without temp variable)
# --------------------------------------------
x = 5
y = 10
print("Before Swapping: x =", x, ", y =", y)   # Output: x = 5 , y = 10

x, y = y, x

print("After Swapping: x =", x, ", y =", y)    # Output: x = 10 , y = 5
print()

# --------------------------------------------
# 🔹 4. Assigning Collections
# --------------------------------------------
fruits = ["apple", "banana", "cherry"]
person = {"name": "Ali", "age": 25}

print("Assigning Collections:")
print("fruits =", fruits)     # Output: fruits = ['apple', 'banana', 'cherry']
print("person =", person)     # Output: person = {'name': 'Ali', 'age': 25}
print()

# --------------------------------------------
# 🔹 5a. Unpacking List Values into Variables
# --------------------------------------------
colors = ["red", "green", "blue"]
r, g, b = colors

print("Unpacking List:")
print("r =", r)     # Output: r = red
print("g =", g)     # Output: g = green
print("b =", b)     # Output: b = blue
print()

# --------------------------------------------
# 🔹 5b. Unpacking with * Operator
# --------------------------------------------
a, *b = [1, 2, 3, 4]

print("Unpacking with * operator:")
print("a =", a)     # Output: a = 1
print("b =", b)     # Output: b = [2, 3, 4]
print()

# --------------------------------------------
# 🔹 6. Real-World Example
# --------------------------------------------
name, age, country = "Imtiaz", 30, "Pakistan"
print("Real-World Example:")
print(f"{name} is {age} years old from {country}.")  # Output: Imtiaz is 30 years old from Pakistan.




# --------------------------------------------
#  Delete a Variable Using del Keyword
# --------------------------------------------

a, b, c = 1, 2, 3
print(a, b, c)  # Output: 1 2 3

del a, b

# print(a)     # ❌ Error: name 'a' is not defined
print(c)       # Output: 3 (still exists)
