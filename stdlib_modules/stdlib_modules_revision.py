# --------------------------- STANDARD LIBRARY MODULES REVISION ---------------------------

import math
import random
import os
import pathlib
import sys
import json
from datetime import datetime
from collections import Counter


# COLLECTIONS MODULE

print("\n===== CHAPTER 22 : COLLECTIONS =====")

# Q1
numbers = [1, 2, 2, 3, 3, 3]
counter = Counter(numbers)
print(counter)

# Q2
text = "python programming"
counter = Counter(text)
print(counter.most_common(3))

# Q3
votes = ["A", "B", "A", "C", "A", "B"]
print(Counter(votes))


# DATETIME MODULE

print("\n===== CHAPTER 23 : DATETIME =====")

# Q1
print(datetime.now())

# Q2
print(datetime.today().date())

# Q3
print(datetime.now().strftime("%d-%m-%Y"))


# MATH MODULE

print("\n===== CHAPTER 24 : MATH =====")

print(math.sqrt(144))
print(math.factorial(6))
print(math.ceil(7.2))


# RANDOM MODULE

print("\n===== CHAPTER 25 : RANDOM =====")

print(random.randint(1, 100))

colors = ["Red", "Blue", "Green", "Black"]
print(random.choice(colors))

numbers = [10, 20, 30, 40, 50]
print(random.sample(numbers, 3))


# PATHLIB MODULE

print("\n===== CHAPTER 26 : PATHLIB =====")

path = pathlib.Path("sample.txt")

print(path.name)
print(path.suffix)
print(path.exists())


# SYS MODULE

print("\n===== CHAPTER 27 : SYS =====")

print(sys.version)
print(sys.platform)
print(sys.getrecursionlimit())


# OS MODULE

print("\n===== CHAPTER 28 : OS =====")

print(os.getcwd())

print(os.path.exists("sample.txt"))

print(os.listdir())


# JSON MODULE

print("\n===== CHAPTER 29 : JSON =====")

student = {
    "name": "Aman",
    "age": 21
}

json_data = json.dumps(student)
print(json_data)

python_data = json.loads(json_data)
print(python_data)

print(json.dumps(student, indent=4))