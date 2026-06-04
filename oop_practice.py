
# ------------------------------ Class and Object ------------------------------------

class Student:
    pass

s1 = Student()
s2 = Student()

print(s1)
print(s2)


# ------------------------------ Adding Attributes ------------------------------------

class Student:
    pass

s1 = Student()

s1.name = "Rahul"
s1.age = 26

print(s1.name)
print(s1.age)


# ------------------------------ Multiple Objects ------------------------------------

class Student:
    pass

s1 = Student()
s2 = Student()

s1.name = "Rahul"
s2.name = "Karn"

print(s1.name)
print(s2.name)


# ------------------------------ Practice ------------------------------------

class Employee:
    pass

e1 = Employee()
e2 = Employee()

e1.name = "Amit"
e1.salary = 50000

e2.name = "Priya"
e2.salary = 70000

print(e1.name, e1.salary)
print(e2.name, e2.salary)



# ------------------------------ __init__() Constructor ------------------------------------

class Student:
    def __init__(self):
        print("Student object created")

s1 = Student()


# Constructor With Data
class Student:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

s1 = Student("Rahul", 22)
print(s1.name)
print(s1.age)


# Multiple Objects
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Rahul", 22)
s2 = Student("Karn", 24)

print(s1.name, s1.age)
print(s2.name, s2.age)


# ------------------------------ Practice ------------------------------------

class Employee:
    def __init__(self, name, salary, department):
        self.name = name 
        self.salary = salary
        self.department = department

e1 = Employee("Rahul",50000,"IT")
e2 = Employee("Karn", 70000, "HR")

print(e1.name, e1.salary, e1.department)
print(e2.name, e2.salary, e2.department)



# ------------------------------ Methods Inside Classes ------------------------------------

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print("Name =", self.name)
        print("Age =", self.age)

s1 = Student("Rahul",23)
s1.show()


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def show(self):
        print(self.name)
        print(self.salary)

e1 = Employee("Rahul", 50000)
e1.show()


# Method Using Attributes

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def bonus(self):
        print("Bonus =", self.salary * 0.10)
        
e1 = Employee("Rahul", 50000)
e1.bonus()


# # ------------------------------ Practice ------------------------------------
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def show_balance(self):
        print(self.name,"blance is",self.balance)
    def deposit(self, amount):
        self.balance += amount
        print("New balance =", self.balance)

c1 = BankAccount("Rahul", 10000)
c1.show_balance()
c1.deposit(500)
        