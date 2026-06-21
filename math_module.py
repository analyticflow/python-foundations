# --------------------------- MATH MODULE ---------------------------

import math


# --------------------------- WHY MATH MODULE ---------------------------

# Example 1 (Basic Math)

print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5)


# Example 2 (Math Module)

print(math.sqrt(25))


# --------------------------- MATH CONSTANTS ---------------------------

# Example 1

print(math.pi)


# Example 2

print(math.e)


# --------------------------- SQUARE ROOT ---------------------------

# Example 1

print(math.sqrt(25))


# Example 2

print(math.sqrt(144))


# --------------------------- POWERS ---------------------------

# Example 1

print(math.pow(2, 3))


# Example 2

print(math.pow(5, 2))


# --------------------------- POWER COMPARISON ---------------------------

# Example

print(math.pow(3, 4))

print(3 ** 4)


# --------------------------- ABSOLUTE VALUE ---------------------------

# Example 1

print(math.fabs(-20))


# Example 2

print(math.fabs(-99.5))


# --------------------------- ABS VS FABS ---------------------------

# Example

print(abs(-20))

print(math.fabs(-20))


# --------------------------- CEIL ---------------------------

# Example 1

print(math.ceil(4.2))


# Example 2

print(math.ceil(7.1))


# --------------------------- FLOOR ---------------------------

# Example 1

print(math.floor(4.9))


# Example 2

print(math.floor(7.8))


# --------------------------- CEIL VS FLOOR ---------------------------

# Example

print(math.ceil(4.2))

print(math.floor(4.2))


# --------------------------- FACTORIAL ---------------------------

# Example 1

print(math.factorial(5))


# Example 2

print(math.factorial(6))


# --------------------------- GCD ---------------------------

# Example 1

print(math.gcd(12, 18))


# Example 2

print(math.gcd(24, 36))


# --------------------------- SIN ---------------------------

# Example 1

print(math.sin(math.pi / 2))


# Example 2

print(math.sin(math.radians(90)))


# --------------------------- COS ---------------------------

# Example 1

print(math.cos(0))


# Example 2

print(math.cos(math.radians(60)))


# --------------------------- TAN ---------------------------

# Example 1

print(math.tan(0))


# Example 2

print(math.tan(math.radians(45)))


# --------------------------- RADIANS ---------------------------

# Example 1

print(math.radians(180))


# Example 2

print(math.radians(90))


# --------------------------- DEGREES ---------------------------

# Example 1

print(math.degrees(math.pi))


# Example 2

print(math.degrees(math.pi / 2))


# --------------------------- LOGARITHMS ---------------------------

# Example 1

print(math.log(math.e))


# Example 2

print(math.log(100))


# --------------------------- LOG10 ---------------------------

# Example 1

print(math.log10(100))


# Example 2

print(math.log10(1000))


# --------------------------- INFINITY ---------------------------

# Example

print(math.inf)


# --------------------------- ISNAN ---------------------------

# Example 1

value = float("nan")

print(math.isnan(value))


# Example 2

print(math.isnan(10.5))


# --------------------------- PRACTICE Q1 ---------------------------

print(math.pi)


# --------------------------- PRACTICE Q2 ---------------------------

print(math.sqrt(144))


# --------------------------- PRACTICE Q3 ---------------------------

print(math.pow(5, 3))


# --------------------------- PRACTICE Q4 ---------------------------

print(math.ceil(7.2))

print(math.floor(7.8))


# --------------------------- PRACTICE Q5 ---------------------------

print(math.factorial(6))


# --------------------------- PRACTICE Q6 ---------------------------

print(math.gcd(24, 36))


# --------------------------- PRACTICE Q7 ---------------------------

print(math.radians(90))


# --------------------------- PRACTICE Q8 ---------------------------

print(math.log10(1000))


# --------------------------- MINI PROJECT ---------------------------

print("\n----- GEOMETRY CALCULATOR -----\n")

radius = 7

area = math.pi * math.pow(radius, 2)

circumference = 2 * math.pi * radius

number = 81

square_root = math.sqrt(number)

print("Radius:", radius)

print("Circle Area:", area)

print("Circle Circumference:", circumference)

print("\nNumber:", number)

print("Square Root:", square_root)
