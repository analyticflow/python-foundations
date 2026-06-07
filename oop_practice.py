
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


# ------------------------------ Practice ------------------------------------

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
        


# ------------------------Decision Making inside Methods------------------------------------------------------

class BankAccount:
    def __init__(self, name, balance):
        self.name = name 
        self.balance = balance

    def show_balance(self):
        print(self.name,"balance is",self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("New balance =",self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Remaining Balance =",self.balance)

    def account_details(self):
        print("Name =", self.name)
        print("Balance =", self.balance)

c1 = BankAccount("Rahul", 50000)
c1.show_balance()
c1.deposit(5000)
c1.withdraw(8000)
c1.account_details()



class Student:
    
    def __init__(self, name, marks):
        self.name = name 
        self.marks = marks

    def show_details(self):
        print("Name =", self.name)
        print("Marks =", self.marks)

    def is_pass(self):
        if self.marks >= 40:
            print("Pass")
        else:
            print("Fail")

s1 = Student("Rahul", 78)
s1.show_details()
s1.is_pass()

        


# ------------------------Encapsulation Basics------------------------------------------------------

class Student:

    def __init__(self, name, marks):
        self.name = name 
        self._marks =marks

    def show_marks(self):
        print(self._marks)

s1 = Student("Rahul", 78)
s1.show_marks()


class BankAccount:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def show_balance(self):
        print(self._balance)

    def deposit(self, amount):
        self._balance += amount
        print("New Balance =", self._balance)

    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient Balance")
        else:
            self._balance -= amount
            print("Remaining Balance =",self._balance)

    
c1 = BankAccount("Rahul",-50000)
c1.show_balance()
c1.deposit(8000)
c1.withdraw(5902)


# ------------------------------------Getter Method-----------------------------------------------------

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

c1 = BankAccount(50000)
print(c1.get_balance())



class Student:

    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks
    
s1 = Student(78)
print(s1.get_marks())
        

# ------------------------------------Setter Method-----------------------------------------------------

class Student:
    def __init__(self, marks):
        self.__marks = marks

    def set_marks(self, marks):
        if marks >= 0:
            self.__marks = marks

    def get_marks(self):
        return self.__marks

s1 = Student(68)
s1.set_marks(90)    # s1.set_marks(-98)
print(s1.get_marks())       



class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance

c1 = BankAccount(5000)
c1.set_balance(3500)
print(c1.get_balance())
        


# ------------------------------------Inheritance-----------------------------------------------------

class Person:
    def __init__(self, name):
        self.name = name
    def show_name(self):
        print(self.name)

class Student(Person):
    pass

s1 = Student("Rahul")
s1.show_name()


class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    pass

d1 = Dog()
d1.sound()


class Employee:
    def work(self):
        print("Employee working")

class Manager(Employee):
    pass

m1 = Manager()
m1.work()



#------------------------------------Method Overriding-----------------------------------------------------

class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("bark bark")

d1 = Dog()
d1.sound()



class Employee:
    def work(self):
        print("Employee Work")

class Manager(Employee):
    def work(self):
        print("Manager managing work")

m1 = Manager()
m1.work()



class Person:
    def role(self):
        print("I am a Person")

class Student(Person):
    def role(self):
        print("I am a Student")

s1 = Student()
s1.role()



# ------------------------------------super() ----------------------------------------------------

# Normal code 
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


# Code with super()

class Person:
    def __init__(self, name):
        self.name = name
class Student(Person):
    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks

s1 = Student("Rahul", 85)        
print(s1.name)
print(s1.marks)

# Exercise - 1

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

m1 = Manager("Rahul", 50000, "IT")
print(m1.name)
print(m1.salary)
print(m1.department)
        


# ------------------------------------Multiple Inheritance----------------------------------------------------

# Exm - 1
class Father:
    def father_skill(self):
        print("Driving")

class Mother:
    def mother_skill(self):
        print("cooking")

class Child(Father, Mother):
    pass

c1 = Child()
c1.father_skill()
c1.mother_skill()

# Exm - 2
class Camera:
    def click(self):
        print("Taking Photo")

class Phone:
    def call(self):
        print("Calling")

class SmartPhone(Camera, Phone):
    pass

s1 = SmartPhone()
s1.click()
s1.call()

# Pr - 1
class Teacher:
    def teach(self):
        print("teaching")

class Singer:
    def sing(self):
        print("singing")

class Person(Teacher, Singer):
    pass

p = Person()
p.teach()
p.sing()


# ------------------------------------Polymorphism----------------------------------------------------

# Poly = Many , Morph = Forms
# Exm - 1
class Dog:
    def sound(self):
        print("Bark")
class Cat:
    def sound(self):
        print("Meow")

d1 = Dog()
c1 = Cat()

d1.sound()
c1.sound()

# Exm - 2
class Employee:
    def work(self):
        print("Employee working")
class Manager:
    def work(self):
        print("Manager managing")

e1 = Employee()
m1 = Manager()

e1.work()
m1.work()

# Exm - 3
class Dog:
    def sound(self):
        print("Bark")
class Cat:
    def sound(self):
        print("Meow")

animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()

# Pr - 1

class Car:
    def start(self):
        print("Car started")
class Bike:
    def start(self):
        print("Bike started")

vehicles = [Car(), Bike()]
for vehicle in vehicles:
    vehicle.start()


# ------------------------------------Abstraction----------------------------------------------------

# Exm - 1

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Bark")

d1 = Dog()
d1.sound()

# Pr - 1

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started")

class Bike(Vehicle):
    def start(self):
        print("Bike started")

motors = [Car(), Bike()]
for motor in motors:
    motor.start()


# ------------------------------------__str__()----------------------------------------------------

# Exm - 1
class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Student Name = {self.name}"

s1 = Student("Rahul")
print(s1)
        
# Exm - 2
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def __str__(self):
        return f"{self.name} earns {self.salary}"
    
e = Employee("Rahul", 50000)
print(e)
        
# Pr - 1
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"Book : {self.title} by {self.author}"
    
b = Book("Python","Rahul")
print(b)
        

# ------------------------------------Class Variables----------------------------------------------------

# Exm - 1
class Student:

    school = "ABC school" # Class Variable

    def __init__(self, name):
        self.name = name  # Instance Variable

s1 = Student("karn")
s2 = Student("rahul")

print(s1.school)

# Pr - 1
class Employee:
    company = "Google" # Class Variable

    def __init__(self, name):
        self.name = name # Instance Variable

e = Employee("Karn")
print(e.company)
print(e.name)


# ------------------------------------Static Methods----------------------------------------------------

class Calculator:
    @staticmethod
    def subtract(a, b):
        return a-b
    
    @staticmethod
    def divide(a, b):
        return a/b
    
print(Calculator.subtract(89,56))
print(Calculator.divide(56238,6))


# ------------------------------------Class Methods----------------------------------------------------

class Student:
    school = "ABC school"

    @classmethod
    def show_school(cls):     # Class Methods
        print(cls.school)

# Student.show_school()


# ------------------------------------HAS-A Relationship----------------------------------------------------

# Exm - 1
class Engine:
    def start(self):
        print("engine started")
class Car:
    def __init__(self):
        self.engine = Engine()
    def drive(self):
        self.engine.start()
        print("car moving")

c1 = Car()
c1.drive()
        
# Exm - 2
class CPU:
    def process(self):
        print("Processing")

class Computer:
    def __init__(self):
        self.cpu = CPU()
    
    def run(self):
        self.cpu.process()
        print("Computer running")

com = Computer()
com.run()

# Pr - 1
class Battery:
    def charge(self):
        print("Battery Charging")

class Mobile:
    def __init__(self):
        self.battery = Battery()

    def use_mobile(self):
        self.battery.charge()
        print("Mobile running")

m1 = Mobile()
m1.use_mobile()


# # ------------------------------------__repr__()----------------------------------------------------

# __str__()  -> For Users[user-friendly representation]
# __repr__() -> For Developers[developer-friendly representation]

# Exm - 1
class Student:
    def __init__(self, name):
        self.name = name 
    def __repr__(self):
        return f"Student('{self.name}')"
    
s1 = Student("Rahul")
print(s1)

# Exm - 2
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def __repr__(self):
        return f"Employee('{self.name}',{self.salary})"
    
e1 = Employee("Karn",50000)
print(e1)
        
# Pr - 1
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"
    
b1 = Book("Python","Rahul")
print(b1)


# # ------------------------------------Student Management System----------------------------------------------------

class Student:

    def __init__(self, name, marks):
        self.name = name 
        self.marks = marks
    
    def show_details(self):
        print("Name =", self.name)
        print("Marks =", self.marks)

    def check_result(self):
        if 40 <= self.marks <= 100:
            print("Result = Pass")
        elif 0 <= self.marks < 40:
            print("Result = Fail")
        else:
            print("Invalid Marks")


s1 = Student("Rahul", 85)
s2 = Student("Shivam", 23)
s3 = Student("Priya", 78)

s1.show_details()
s1.check_result()

s2.show_details()
s2.check_result()

s3.show_details()
s3.check_result()