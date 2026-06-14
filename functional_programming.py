# =========================== FUNCTIONAL PROGRAMMING ===============================

from functools import reduce


# =========================== LAMBDA FUNCTIONS ===============================

# Example 1

square = lambda x: x * x

print(square(5))


# Example 2

add = lambda a, b: a + b

print(add(10, 20))


# Practice Q1

square = lambda x: x ** 2
double = lambda x: x * 2
cube = lambda x: x ** 3

print(square(4))
print(double(4))
print(cube(4))


# =========================== MAP ===============================

# Example 1

numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x ** 2, numbers))

print(result)


# Example 2

names = ["aman", "rahul", "priya"]

result = list(map(str.upper, names))

print(result)


# Practice Q2

numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x * 10, numbers))

print(result)


# =========================== FILTER ===============================

# Example 1

numbers = [1, 2, 3, 4, 5, 6]

result = list(filter(lambda x: x % 2 == 0, numbers))

print(result)


# Example 2

names = ["Aman", "Ravi", "Priya", "Ankit"]

result = list(filter(lambda name: name.startswith("A"), names))

print(result)


# Practice Q3

numbers = [10, 55, 70, 45, 90, 20]

result = list(filter(lambda x: x > 50, numbers))

print(result)


# =========================== REDUCE ===============================

# Example 1

numbers = [1, 2, 3, 4]

total = reduce(lambda a, b: a + b, numbers)

print(total)


# Example 2

numbers = [1, 2, 3, 4, 5]

product = reduce(lambda a, b: a * b, numbers)

print(product)


# Practice Q4

numbers = [1, 2, 3, 4, 5]

product = reduce(lambda a, b: a * b, numbers)

print(product)


# =========================== ZIP ===============================

# Example 1

names = ["Aman", "Rahul", "Priya"]
marks = [85, 70, 95]

result = list(zip(names, marks))

print(result)


# Example 2

names = ["Aman", "Rahul"]
ages = [22, 24]
cities = ["Mumbai", "Delhi"]

print(list(zip(names, ages, cities)))


# Practice Q5

names = ["Aman", "Rahul", "Priya"]
ages = [22, 24, 21]
cities = ["Mumbai", "Delhi", "Pune"]

combined = list(zip(names, ages, cities))

print(combined)


# =========================== ENUMERATE ===============================

# Example 1

names = ["Aman", "Rahul", "Priya"]

for index, name in enumerate(names):
    print(index, name)


# Example 2

for index, name in enumerate(names, start=1):
    print(index, name)


# Practice Q6

menu = ["Login", "Register", "Profile", "Logout"]

for index, item in enumerate(menu, start=1):
    print(f"{index}. {item}")


# =========================== ANY ===============================

# Example 1

numbers = [10, 20, 95, 40]

print(any(num > 90 for num in numbers))


# Example 2

students = [45, 70, 20]

print(any(mark >= 50 for mark in students))


# Practice Q7

marks = [55, 72, 91, 60]

result = any(mark > 90 for mark in marks)

print(result)


# =========================== ALL ===============================

# Example 1

marks = [60, 70, 80]

print(all(mark >= 50 for mark in marks))


# Example 2

marks = [60, 70, 30]

print(all(mark >= 50 for mark in marks))


# Practice Q8

marks = [60, 55, 78, 90]

result = all(mark >= 50 for mark in marks)

print(result)


# =========================== MINI PROJECT ===============================

students = [
    ("Aman", 85),
    ("Rahul", 40),
    ("Priya", 95),
    ("Neha", 78)
]

# Passed Students

passed_students = list(
    filter(lambda student: student[1] >= 50, students)
)

print("Passed Students:")
print(passed_students)


# Extract Names

student_names = list(
    map(lambda student: student[0], students)
)

print("\nStudent Names:")
print(student_names)


# Any Student Above 90?

above_90 = any(
    student[1] > 90
    for student in students
)

print("\nAny Student Above 90?")
print(above_90)


# Did Everyone Pass?

all_passed = all(
    student[1] >= 50
    for student in students
)

print("\nDid Everyone Pass?")
print(all_passed)


# Total Marks Using reduce()

total_marks = reduce(
    lambda total, student: total + student[1],
    students,
    0
)

print("\nTotal Marks:")
print(total_marks)


# Ranked List

ranked_students = sorted(
    students,
    key=lambda student: student[1],
    reverse=True
)

print("\nRank List")

for rank, student in enumerate(ranked_students, start=1):
    print(f"{rank}. {student[0]} - {student[1]}")