#function_docstring

# def greatting():
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

def calculator(a: int, b: int):
    add = a + b
    subtract = a - b
    return add, subtract

x, y = calculator(10, 3)
print("Sum:", x)
print("Difference:", y)
