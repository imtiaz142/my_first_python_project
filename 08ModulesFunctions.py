#function_docstring

# def greatting():
#   "function_docstring"
#   print("hello welcome to python")
#   return print
# greatting()
# print(greatting())

#functions With Parameters:

# def personal_assistant(name: str, age: int, city: str) -> str:
    
#     if not isinstance(name, str) or not isinstance(age, int) or not isinstance(city, str):
#         return "Please enter correct types: name(str), age(int), city(str)"
#     return f"Hello {name}, you are {age} years old and live in {city}."

# message = personal_assistant(22, "Ali", "Lahore")
# print(message)


#3. Function with Return Value

# def calculator(a: int, b: int):
#     add = a + b
#     subtract = a - b
#     return add, subtract

# x, y = calculator(10, 3)
# print("Sum:", x)
# print("Difference:", y)

# ---------------------Default Parameters------------------

# def greet(name="Guest"):
#     print("Hello,", name)

# greet()         # Output: Hello, Guest
# greet("Imtiaz") # Output: Hello, Imtiaz

# ---------------------Position Arguments------------------

# def positionarg(name,age):
#     print(f"Your name is {name} and your age  is {age}")

# positionarg(name="imtiaz", age=33)
# positionarg(age="56", name="Ali")



#--------------Variable-Length Arguments----------------------


# def total(*numbers):
#     print(sum(numbers))

# total(1,2,3,4,5,6,7,8,9,10)



#----------------**kwargs — many key-value pairs (dictionary)--------------------


# def info(**details):
#     for key, value in details.items():
#         print(key, ":", value)

# info(name="Imtiaz", age=30)



#----------------Function Scope------------------------------

# x = 10  # Global variable

# def show():
#     x = 5  # Local variable use any where in the file
#     print("Inside function:", x)

# show()                 # Output: Inside function: 5
# print("Outside:", x)   # Output: Outside: 10


# #-------------------lambda  FUNCTIONS-----------------

# square = lambda x: x * x
# print(square(5))  # Output: 25

# numbers = [1, 2, 3, 4, 5]

# a,c, *middle, b = numbers

# print(a)       # 1
# print(middle)  # [2, 3, 4]
# print(b)       # 5
# print(c) 


# ----------------------Positional-Only Arguments?------------------


#def function_name(pos1, pos2, /, other1, other2):

# Parameters before /: Positional-only

# Parameters after /: Can be positional or keyword

# def posFun(x, y, /, z):
#     print(x,y,z)
#     print(x + y + z)

# print("Evaluating positional-only arguments: ")
# posFun(2, 1, 3)

# # uncomment to see error
# #posFun(x=1, y=2, z=3)



#----------------------Keyword-only-arguments----------------------------

# def posFun(a,b,c,*,d,e,f):
#     print(a+b+c+d+e+f)

# print("Evaluating positional-only arguments: ")
# #posFun(1,2,3,d=3,e=4,f=5)
# posFun(1,2,3,d=3,e=4,f=5)
 
#----------------------Note: / is as before and * is working as after----------------------------



#---------------------explain this in details Arbitrary Keyword Arguments, **kwargs----------------------


# def print_info(**kwargs): #** save the value in dictory and with one * the vlaue is save in tuple
#     print(kwargs)
#     print(type(kwargs))

# print_info(name="Imtiaz",age=25,myclass=9,fathername= "Mukhtar Ahmad") #you can add as many value as you want

# #-----------------------Example----------------------

def my_function(**student):
  print("\nHis last name is " + student["lname"])

  for key, value in student.items():
    print(key, value)

  print(student)

my_function(fname = "Ali", lname = "Osman")

my_function(fname = "Ali", lname = "Osman", course = "Python - 101", day="Saturday", time="1400 - 1800")

my_dict = {"fname": "Arif", "lname": "Rozani", "course":"101 - 201", "day":"Saturday | Sunday", "role":"Student"}



#-----------------------Generator Function----------------------



