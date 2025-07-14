
# #  -------------------Integer (int)-------------------------------

a : int = 16
b : int = 4

print(a//b)  #reminder ni data means point k bd wali value 
print(a % b)  # 0 remainder dta ha 
# print(divmod(9,4)) #(2,1) 9 // 4 → 2, 9 % 4 → 1

print(abs(-50))  #(50) abs() function means absolute value

print(bin(10)) #(0b10101)

int("123") #String into int

x = int(7.9)
print(x) #7

import math

print(math.isqrt(10))

print(2**3) #8


#---------------------------Floating-Point---------------------

num_float: float = 3.14
#num_float: float = .14

print(type(num_float), " num_float = ", num_float)  # 



#----------------------------Complex (complex)---------------------


z = 3 + 4j

print(z.real) # 3.0
print(z.imag)  # 4.0
print(abs(z))  # 5.0 (9+16)=25=5.0


#----------------------------String---------------------





#----------------FrozanSet-------------------------

Range_Number:range = range(1,20,2)
print(type(Range_Number))

for i in range(1,10,2):
    print(i)

normal_set={1,2,3,4,4}
frozan_set =frozenset([1,22,2,2,3,4,5,6,7,7])

print(normal_set)
print(frozan_set)

#------------What is UTF-8?----------

byte_array: bytearray = bytearray([65, 66, 67, 69])
# Converting the entire bytearray to a string using decode()
print("Decoded string: ", byte_array.decode('utf-8'))  # Output: ABCE


#--------------Memoryview (memoryview)-------------------------

# A bytes object is an immutable (unchangeable) sequence of numbers from 0 to 255, used to store binary data like images, files, or messages.
# A bytearray is a mutable (changeable) version of bytes, used when you need to edit or modify binary data.



data = bytearray(b"Imtiaz")
view = memoryview(data)

print(view[0])        # 73 → ASCII of 'I'

# Change the first letter
view[0] = 90           # Replace 'I' with 'Z'
print(data)           # bytearray(b'Zmtiaz')


#--------------None Data Type-------------------------

# It is a special data type used when:

# A variable has no value yet

# A function does not return anything

# You want to reset or clear a variable


x = None       # At the beginning: no value

x = 10         # Later you assign a number
print(x)       # Output: 10
print(id(x))

x = "Imtiaz"   # You can even change to a string
print(x)       # Output: Imtiaz


print(id(x))

#The id() function returns the unique memory address (ID) of an object.


#--------------Integer Literals-------------------------

#Integer literals are just the whole numbers (no decimal point) you write directly in your code.



# Type	Base	   Example   	Explanation
# Decimal	Base 10	   100, -50	      Normal everyday numbers
# Binary	Base 2	   0b1010	     Starts with 0b (0 or 1 only)
# Octal	Base 8	   0o12	Start     with 0o (0–7 only)
# Hexadecimal	Base 16	0x1F     	Starts with 0x (0–9 + A–F)

#Decimal Literal

x = 10
y = -25
print(x + y)  # Output: -15

#Binary Literal (0b)

a = 0b1010   # Binary for 10
print(a)     # Output: 10

#Octal Literal (0o)

b = 0o12     # Octal for 10
print(b)     # Output: 10

#Hexadecimal Literal


c = 0x1F     # Hexadecimal for 31
print(c)     # Output: 31

#--------------isinstance() Function-------------------------


#isinstance() checks if a variable is of a specific data type.


name = "Imtiaz"
print(isinstance(name, str))


