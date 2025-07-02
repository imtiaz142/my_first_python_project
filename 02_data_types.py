
# #  -------------------Integer (int)-------------------------------

# a : int = 16
# b : int = 4

# print(a//b)  #reminder ni data means point k bd wali value 
# print(a % b)  # 0 remainder dta ha 
# # print(divmod(9,4)) #(2,1) 9 // 4 → 2, 9 % 4 → 1

# print(abs(-50))  #(50) abs() function means absolute value

# print(bin(10)) #(0b10101)

# int("123") #String into int

# x = int(7.9)
# print(x) #7

# import math

# print(math.isqrt(10))

# print(2**3) #8


#---------------------------Floating-Point---------------------

# num_float: float = 3.14
# #num_float: float = .14

# print(type(num_float), " num_float = ", num_float)  # 



#----------------------------Complex (complex)---------------------


# z = 3 + 4j

# print(z.real) # 3.0
# print(z.imag)  # 4.0
# print(abs(z))  # 5.0 (9+16)=25=5.0


#----------------------------String---------------------

# name = "imtiaz Ali"
# print(name[7])
# print(name*3)
# print(name[0:9:2]) #start stop steps
# print(name[:3]) #first 3
# print(name[3:]) #start from 3 to end
# print(name[-1]) #Last

# print(name.upper())
# print(name.swapcase()) #Swap lower↔upper

# print(name.replace("a","b")) # agr a lower case hy tu lower all replace ho gy a capital hy tu capital all replace ho gy 

# print(name.split()) #list bana den ga space k hisab sy

# print(name.strip()) #Bothh side space remove
# print(name.rstrip()) #right side space remove

# for i in "imtiaz":
#     print(i)

# print(len(name)) #space b account ho gi
# print(min(name)) # i, m, t, i, a, z → 'a' comes first alphabetically. agr space ha tu space phaly ay gi
# print(max(name))
# print(sorted(name)) # Returns the characters of the string in alphabetical order as a list.

# # Revers String

# reversename = name[::-1]

# print(reversename)


# re

# no_space = name.replace(" ", "")
# print(no_space)


# text = "Imtiaz"
# encoded = text.encode()       # b'Imtiaz' when you send the data on internet 
# decoded = encoded.decode()    # 'Imtiaz'

# print(f"{encoded}{decoded}")


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
