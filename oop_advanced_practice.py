
# -------------------------------Student Result System-------------------------------

class Student:

    def __init__(self, name, marks):
        self.name = name 
        self.marks = marks

    def show_details(self):
        print(f"Name = {self.name}\nMarks ={self.marks}")
    
    def check_result(self):
        if 100 >= self.marks >= 40:
            print("Result = Pass")
            print("-" * 80)
        elif 0 <= self.marks < 40:
            print("Result = Fail")
            print("-" * 80)
        else:
            print("Invalid number")
            print("-" * 80)

s1 = Student("Rahul", 85)
s2 = Student("Shivam", 23)
s3 = Student("Priya", 878)

s1.show_details()
s1.check_result()
s2.show_details()
s2.check_result()
s3.show_details()
s3.check_result()

# -------------------------------Employee Bonus System-------------------------------

class Employee:
    
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary
    
    def show_details(self):
        print(f"Name = {self.name}\nSalary = {self.salary}")
    
    def calculate_bonus(self):
    
        if self.salary >= 50000:
            print(f"Total Bonus = {self.salary * 0.1}")
            print("-" * 80)
        
        elif 0 < self.salary < 50000:
            print(f"Total Bonus = {self.salary * 0.05}")
            print("-" * 80)

        else:
            print("Invalid salary")
            print("-" * 80)


e1 = Employee("Priya", 50000)
e2 = Employee("Karn", 6230)
e3 = Employee("Rahul", -9560)

e1.show_details()
e1.calculate_bonus()
e2.show_details()
e2.calculate_bonus()
e3.show_details()
e3.calculate_bonus()

# -------------------------------Bank Account System-------------------------------

class BankAccount:

    def __init__(self, name, balance):
        self.name = name 
        self.__balance = balance

    def show_balance(self):
        print(f"Balance = {self.__balance}")
        
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Current Balance = {self.__balance}")
        else:
            print(f"Invalid deposit amount = {amount}")

    def withdraw(self, amount):
        if amount <= 0:
            print(f"Withdrawal amount must be positive not {amount}")
        elif amount > self.__balance:
            print(
                f"Insufficient Balance. "
                f"Requested = {amount}, Available = {self.__balance}"
            )
        else:
            self.__balance -= amount
            print(f"Remaining Balance = {self.__balance}")

        print("-" * 80)


c1 = BankAccount("Rahul", 1000)
c2 = BankAccount("Priya", 5000)

c1.show_balance()
c1.deposit(508)
c1.withdraw(1865)

c2.show_balance()
c2.deposit(697)
c2.withdraw(-5324)

# -------------------------------Library Book System-------------------------------

class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_issued = False

    def show_details(self):
        print(f"Book: {self.title}")
        print(f"Author: {self.author}")

    def issue_book(self):

        if self.is_issued:
            print("Book already issued")

        else:
            self.is_issued = True
            print("Book issued successfully")

    def return_book(self):

        if not self.is_issued:
            print("Book is already available")

        else:
            self.is_issued = False
            print("Book returned successfully")
        
        print("-" * 80)


b1 = Book("Python", "Rahul")
b1.show_details()

b1.issue_book()
b1.issue_book()

b1.return_book()
b1.return_book()

b1.issue_book()

# -------------------------------Product Inventory System-------------------------------

class Product:

    def __init__(self, name, price, stock):
        self.name = name 
        self.price = price
        self.stock = stock

    def show_details(self):
        print(f"Product : {self.name}")
        print(f"Price : {self.price}")
        print(f"Stock : {self.stock}")

    def sell(self, quantity):
        if 0 < quantity <= self.stock:
            self.stock -= quantity
            print(f"Sold stock = {quantity}")
            print(f"Remaining stock = {self.stock}")
        elif quantity <= 0:
            print(f"Invalid quantity : {quantity}")
        else:
            print(f"Not enough stock available. Stock availabe = {self.stock} selling stock : {quantity}")
        
        print("-" * 80)

p1 = Product("Laptop", 50000, 10)
p1.show_details()

p1.sell(3)

p1.sell(20)

p1.sell(-5)

# -------------------------------School Report Card System-------------------------------

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show_details(self):
        print(f"Name = {self.name}")
        print(f"Marks = {self.marks}")

    def grade(self):

        if 90 <= self.marks <= 100:
            print("Grade = A")

        elif 75 <= self.marks < 90:
            print("Grade = B")

        elif 40 <= self.marks < 75:
            print("Grade = C")

        elif 0 <= self.marks < 40:
            print("Grade = F")

        else:
            print("Invalid Marks")

        print("-" * 80)


s1 = Student("Rahul", 85)

s1.show_details()
s1.grade()


# -------------------------------Vehicle Rental System-------------------------------

class Vehicle:

    def __init__(self, vehicle_name):
        self.vehicle_name = vehicle_name
        self.is_rented = False

    def rent_vehicle(self):

        if self.is_rented:
            print("Vehicle already rented")

        else:
            self.is_rented = True
            print("Vehicle rented successfully")

    def return_vehicle(self):

        if not self.is_rented:
            print("Vehicle already available")

        else:
            self.is_rented = False
            print("Vehicle returned successfully")

        print("-" * 80)


v1 = Vehicle("Car")

v1.rent_vehicle()
v1.rent_vehicle()

v1.return_vehicle()
v1.return_vehicle()


# -------------------------------E-Commerce Order System-------------------------------

class Order:

    def __init__(self, product, price):
        self.product = product
        self.price = price
        self.is_delivered = False

    def show_details(self):
        print(f"Product = {self.product}")
        print(f"Price = {self.price}")

    def deliver_order(self):

        if self.is_delivered:
            print("Order already delivered")

        else:
            self.is_delivered = True
            print("Order delivered successfully")

        print("-" * 80)


o1 = Order("Laptop", 50000)

o1.show_details()
o1.deliver_order()
o1.deliver_order()


# -------------------------------Hospital Management System-------------------------------

class Patient:

    def __init__(self, name, disease):
        self.name = name
        self.disease = disease

    def show_details(self):
        print(f"Patient Name = {self.name}")
        print(f"Disease = {self.disease}")

        print("-" * 80)


p1 = Patient("Rahul", "Fever")
p1.show_details()


# -------------------------------Student Attendance Tracker-------------------------------

class Student:

    def __init__(self, name):
        self.name = name
        self.attendance = 0

    def mark_attendance(self):
        self.attendance += 1

    def show_attendance(self):
        print(f"Name = {self.name}")
        print(f"Attendance = {self.attendance}")

        print("-" * 80)


s1 = Student("Rahul")

s1.mark_attendance()
s1.mark_attendance()
s1.mark_attendance()

s1.show_attendance()