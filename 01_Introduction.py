# How Python Uses Bytecode:

# Compilation: When you run a Python script, the Python interpreter first compiles it into bytecode.

# Execution: The compiled bytecode is executed by the Python Virtual Machine (PVM).

# Caching: Python caches the compiled bytecode in the pycache directory to speed up subsequent executions.

# Bytecode is an intermediate code that Python creates after reading your .py file.

# It’s not human-readable, and not machine code either. It’s a kind of "middle step" between your Python source code and the code that runs on your computer.

# hello.py
print("Hello, world!")


# Python does this:

# Reads your Python code (source code).

# Compiles it into bytecode (a .pyc file).

# Interpreter (Python Virtual Machine or PVM) runs the bytecode.

age:int= 3
name:str = "ali"
number:list[int]=[124,4,5,5,5,5,5,3,5]

print(f"The Name is {age}{name}{list}")

# everything is object in python

#Every value (no matter the data type) is an instance of a class — and because of that, it has functions (called methods) and properties that you can use directly.


