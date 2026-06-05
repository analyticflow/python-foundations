
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