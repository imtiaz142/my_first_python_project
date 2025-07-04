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