# --------------------------- JSON MODULE ---------------------------

import json


# --------------------------- WHY JSON ---------------------------

# Example 1 (Python Dictionary)

student = {
    "name": "Aman",
    "age": 21,
    "city": "Vadodara"
}

print(student)


# Example 2 (JSON String)

json_data = json.dumps(student)

print(json_data)


# --------------------------- PYTHON DICTIONARY VS JSON ---------------------------

# Example 1

student = {
    "name": "Aman",
    "age": 21
}

print(type(student))


# Example 2

json_string = json.dumps(student)

print(type(json_string))


# --------------------------- JSON.DUMPS() ---------------------------

# Example 1

student = {
    "name": "Aman",
    "age": 21
}

json_data = json.dumps(student)

print(json_data)


# Example 2

employee = {
    "name": "Rahul",
    "salary": 50000,
    "department": "IT"
}

json_employee = json.dumps(employee)

print(json_employee)


# --------------------------- CHECK TYPE AFTER DUMPS ---------------------------

student = {
    "name": "Priya",
    "age": 22
}

json_data = json.dumps(student)

print(type(json_data))


# --------------------------- JSON.LOADS() ---------------------------

# Example 1

data = '''
{
    "name": "Aman",
    "age": 21
}
'''

student = json.loads(data)

print(student)


# Example 2

employee_data = '''
{
    "name": "Rahul",
    "salary": 50000,
    "department": "IT"
}
'''

employee = json.loads(employee_data)

print(employee)


# --------------------------- CHECK TYPE AFTER LOADS ---------------------------

text = '''
{
    "course":"Python",
    "duration":"3 Months"
}
'''

course = json.loads(text)

print(type(course))


# --------------------------- JSON.DUMP() ---------------------------

# Example 1

student = {
    "name": "Aman",
    "age": 21
}

with open("student.json", "w") as file:
    json.dump(student, file)

print("student.json created successfully.")


# Example 2

employee = {
    "name": "Rahul",
    "salary": 50000
}

with open("employee.json", "w") as file:
    json.dump(employee, file)

print("employee.json created successfully.")


# --------------------------- JSON.LOAD() ---------------------------

# Example 1

with open("student.json", "r") as file:
    data = json.load(file)

print(data)


# Example 2

with open("employee.json", "r") as file:
    employee = json.load(file)

print(employee)


# --------------------------- PRETTY PRINT JSON ---------------------------

# Example 1

student = {
    "name": "Aman",
    "age": 21,
    "city": "Vadodara"
}

print(
    json.dumps(
        student,
        indent=4
    )
)


# Example 2

employee = {
    "name": "Rahul",
    "salary": 50000,
    "department": "IT"
}

print(
    json.dumps(
        employee,
        indent=4
    )
)


# --------------------------- SORT KEYS ---------------------------

# Example 1

data = {
    "city": "Vadodara",
    "age": 21,
    "name": "Aman"
}

print(
    json.dumps(
        data,
        indent=4,
        sort_keys=True
    )
)


# Example 2

employee = {
    "salary": 50000,
    "department": "IT",
    "name": "Rahul"
}

print(
    json.dumps(
        employee,
        indent=4,
        sort_keys=True
    )
)


# --------------------------- JSON DATA TYPES ---------------------------

# Example 1

data = {
    "name": "Aman",
    "active": True,
    "salary": None,
    "marks": [85, 90, 95]
}

print(json.dumps(data, indent=4))


# Example 2

info = {
    "course": "Python",
    "completed": False,
    "fees": 15000
}

print(json.dumps(info, indent=4))


# --------------------------- WORKING WITH LISTS ---------------------------

# Example 1

students = [
    {"name": "Aman"},
    {"name": "Rahul"},
    {"name": "Priya"}
]

json_students = json.dumps(
    students,
    indent=4
)

print(json_students)


# Example 2

courses = [
    "Python",
    "SQL",
    "Excel"
]

print(
    json.dumps(
        courses,
        indent=4
    )
)

# --------------------------- PRACTICE Q1 ---------------------------

student = {
    "name": "Aman",
    "age": 21
}

json_data = json.dumps(student)

print(json_data)


# --------------------------- PRACTICE Q2 ---------------------------

text = '''
{
    "name":"Rahul",
    "age":22
}
'''

student = json.loads(text)

print(student)


# --------------------------- PRACTICE Q3 ---------------------------

employee = {
    "name": "Priya",
    "age": 24,
    "department": "HR"
}

with open("practice_student.json", "w") as file:
    json.dump(employee, file)

print("practice_student.json created.")


# --------------------------- PRACTICE Q4 ---------------------------

with open("practice_student.json", "r") as file:
    data = json.load(file)

print(data)


# --------------------------- PRACTICE Q5 ---------------------------

student = {
    "name": "Karan",
    "age": 23,
    "course": "Python"
}

print(
    json.dumps(
        student,
        indent=4
    )
)


# --------------------------- PRACTICE Q6 ---------------------------

students = [
    {
        "name": "Aman",
        "age": 21
    },
    {
        "name": "Rahul",
        "age": 22
    },
    {
        "name": "Priya",
        "age": 20
    }
]

print(
    json.dumps(
        students,
        indent=4
    )
)


# --------------------------- PRACTICE Q7 ---------------------------

data = {
    "city": "Ahmedabad",
    "course": "Python",
    "name": "Aman",
    "age": 21
}

print(
    json.dumps(
        data,
        indent=4,
        sort_keys=True
    )
)


# --------------------------- MINI PROJECT ---------------------------

print("\n----- STUDENT JSON MANAGER -----\n")

students = []


while True:

    print("\n1. Add Student")
    print("2. View Students")
    print("3. Save to JSON")
    print("4. Load from JSON")
    print("5. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        course = input("Enter Course: ")

        student = {
            "name": name,
            "age": age,
            "course": course
        }

        students.append(student)

        print("Student Added Successfully.")

    elif choice == "2":

        if len(students) == 0:
            print("No Students Found.")

        else:

            print("\nStudent Records\n")

            for student in students:

                print("Name   :", student["name"])
                print("Age    :", student["age"])
                print("Course :", student["course"])
                print("-" * 30)

    elif choice == "3":

        with open("students.json", "w") as file:
            json.dump(
                students,
                file,
                indent=4
            )

        print("Students Saved Successfully.")

    elif choice == "4":

        try:

            with open("students.json", "r") as file:
                students = json.load(file)

            print("\nStudents Loaded Successfully.\n")

            for student in students:

                print("Name   :", student["name"])
                print("Age    :", student["age"])
                print("Course :", student["course"])
                print("-" * 30)

        except FileNotFoundError:

            print("students.json not found.")

    elif choice == "5":

        print("\nThank You for Using Student JSON Manager.")
        break

    else:

        print("Invalid Choice. Try Again.")