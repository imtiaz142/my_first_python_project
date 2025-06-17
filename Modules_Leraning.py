#Built-in Modules (Standard Library)

import math
import random
import datetime
import sys
import statistics
import json

#from math import *  # Imports everything


print(math.sqrt(25))  # Output: 5.0

print(random.randint(1, 10)) 

# Current date and time
now = datetime.datetime.now()
print(now)

print(now.date())

print(sys.version)       # Python version
print(sys.platform)      # Your OS (e.g., win32)


data = [1, 2, 3, 4, 5, 6]
print(statistics.mean(data))      # 3.5
print(statistics.median(data))    # 3.5

import json

# Python dict to JSON
data = {"name": "Ali", "age": 25}
json_str = json.dumps(data)
print(json_str)   # '{"name": "Ali", "age": 25}'

# JSON to Python dict
new_data = json.loads(json_str)
print(new_data["name"])  # Ali



