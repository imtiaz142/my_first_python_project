
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

name = "imtiaz Ali"
# print(name[7])
# print(name*3)
#print(name[0:9:2]) #start stop steps
# print(name[:3]) #first 3
# print(name[3:]) #start from 3 to end
# print(name[-1]) #Last

# print(name.upper())
# print(name.swapcase()) #Swap lower↔upper

# print(name.replace("a","b")) # agr a lower case hy tu lower all replace ho gy a capital hy tu capital all replace ho gy 

# print(name.split()) #list bana den ga space k hisab sy

# print(name.strip()) #Bothh side space remove
# print(name.rstrip()) #right side space remove

for i in "imtiaz":
    print(i)