# # ----------------------------------------------------- MODULE PRACTICE ------------------------------------------------------

# import calculator
# import math
# import random

# created this file as my first module =>  calculator.py

import calculator

print(calculator.add(10,5))
print(calculator.subtract(10,5))


# ----------------------------math module----------------------------------

# Method 1
import math 
print(math.sqrt(625))
print(math.pow(6, 3))
print(math.pi)


# Method 2 - import only needed one
from math import sqrt
print(sqrt(169))


# Method 3 - multiple import
from math import sqrt, pi
print(sqrt(81))
print(pi)


# Method 4 - Alias
import math as m
print(m.sqrt(225))
print(m.pi)


# ------------------random Module -------------------------------=== > randint(), random(), choice(), shuffle()

import random

print(random.randint(1, 10))

print(random.random())

fruits = ["Apple","Banana","Mango","Orange"]
print(random.choice(fruits))

nums = [1,2,3,4,5,6,7]
random.shuffle(nums)
print(nums)

#--------------------------------- datetime Module -----------------------------------------------

import datetime

today = datetime.date.today()
print(today)

now = datetime.datetime.now()
print(now)

today = datetime.date.today()
print(today.year)
print(today.month)
print(today.day)



#--------------------------------- dir()-----------------------------------------------

import math
print(dir(math))


# -----------------------------------help()----------------------------------------------
help(math.sqrt)


# ---------------------------------name == "main"-------------------------------------
# test_module.py

print("File Started")

if __name__ == "__main__":
    print("Running directly")

print("File Ended")


# =====================================================================================================================
#                                               PRACTICE QUESTIONS
# =====================================================================================================================

#  p1 - p3 

import random

colors = ["Red","Blue","Green","Black"]
print(random.choice(colors))

names = ["Mahek","Rahul","Priya","Amit"]
print(random.choice(names))

numbers = [10, 20, 30, 40, 50]
random.shuffle(numbers)
print(numbers)


