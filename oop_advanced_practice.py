
# # -------------------------------Student Result System-------------------------------

# class Student:

#     def __init__(self, name, marks):
#         self.name = name 
#         self.marks = marks

#     def show_details(self):
#         print(f"Name = {self.name}\nMarks ={self.marks}")
    
#     def check_result(self):
#         if 100 >= self.marks >= 40:
#             print("Result = Pass")
#             print("-" * 80)
#         elif 0 <= self.marks < 40:
#             print("Result = Fail")
#             print("-" * 80)
#         else:
#             print("Invalid number")
#             print("-" * 80)

# s1 = Student("Rahul", 85)
# s2 = Student("Shivam", 23)
# s3 = Student("Priya", 878)

# s1.show_details()
# s1.check_result()
# s2.show_details()
# s2.check_result()
# s3.show_details()
# s3.check_result()

# # -------------------------------Employee Bonus System-------------------------------

# class Employee:
    
#     def __init__(self, name, salary):
#         self.name = name 
#         self.salary = salary
    
#     def show_details(self):
#         print(f"Name = {self.name}\nSalary = {self.salary}")
    
#     def calculate_bonus(self):
    
#         if self.salary >= 50000:
#             print(f"Total Bonus = {self.salary * 0.1}")
#             print("-" * 80)
        
#         elif 0 < self.salary < 50000:
#             print(f"Total Bonus = {self.salary * 0.05}")
#             print("-" * 80)

#         else:
#             print("Invalid salary")
#             print("-" * 80)


# e1 = Employee("Priya", 50000)
# e2 = Employee("Karn", 6230)
# e3 = Employee("Rahul", -9560)

# e1.show_details()
# e1.calculate_bonus()
# e2.show_details()
# e2.calculate_bonus()
# e3.show_details()
# e3.calculate_bonus()

# # -------------------------------Bank Account System-------------------------------

# class BankAccount:

#     def __init__(self, name, balance):
#         self.name = name 
#         self.__balance = balance

#     def show_balance(self):
#         print(f"Balance = {self.__balance}")
        
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Current Balance = {self.__balance}")
#         else:
#             print(f"Invalid deposit amount = {amount}")

#     def withdraw(self, amount):
#         if amount <= 0:
#             print(f"Withdrawal amount must be positive not {amount}")
#         elif amount > self.__balance:
#             print(
#                 f"Insufficient Balance. "
#                 f"Requested = {amount}, Available = {self.__balance}"
#             )
#         else:
#             self.__balance -= amount
#             print(f"Remaining Balance = {self.__balance}")

#         print("-" * 80)


# c1 = BankAccount("Rahul", 1000)
# c2 = BankAccount("Priya", 5000)

# c1.show_balance()
# c1.deposit(508)
# c1.withdraw(1865)

# c2.show_balance()
# c2.deposit(697)
# c2.withdraw(-5324)

# # -------------------------------Library Book System-------------------------------

# class Book:

#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         self.is_issued = False

#     def show_details(self):
#         print(f"Book: {self.title}")
#         print(f"Author: {self.author}")

#     def issue_book(self):

#         if self.is_issued:
#             print("Book already issued")

#         else:
#             self.is_issued = True
#             print("Book issued successfully")

#     def return_book(self):

#         if not self.is_issued:
#             print("Book is already available")

#         else:
#             self.is_issued = False
#             print("Book returned successfully")
        
#         print("-" * 80)


# b1 = Book("Python", "Rahul")
# b1.show_details()

# b1.issue_book()
# b1.issue_book()

# b1.return_book()
# b1.return_book()

# b1.issue_book()

# # -------------------------------Product Inventory System-------------------------------

# class Product:

#     def __init__(self, name, price, stock):
#         self.name = name 
#         self.price = price
#         self.stock = stock

#     def show_details(self):
#         print(f"Product : {self.name}")
#         print(f"Price : {self.price}")
#         print(f"Stock : {self.stock}")

#     def sell(self, quantity):
#         if 0 < quantity <= self.stock:
#             self.stock -= quantity
#             print(f"Sold stock = {quantity}")
#             print(f"Remaining stock = {self.stock}")
#         elif quantity <= 0:
#             print(f"Invalid quantity : {quantity}")
#         else:
#             print(f"Not enough stock available. Stock availabe = {self.stock} selling stock : {quantity}")
        
#         print("-" * 80)

# p1 = Product("Laptop", 50000, 10)

# p1.show_details()
# p1.sell(3)
# p1.sell(20)
# p1.sell(-5)

# # -------------------------------School Report Card System-------------------------------

# class Student:

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def show_details(self):
#         print(f"Name : {self.name}\nMarks : {self.marks}")

#     def grade(self):
#         if 90 <= self.marks <= 100:
#             print("Grade : A")
#         elif 75 <= self.marks < 90:
#             print("Grade : B")
#         elif 40 <= self.marks < 75:
#             print("Grade : C")
#         elif 0 <= self.marks < 40:
#             print("Grade : F")
#         else:
#             print("Invalid Marks")
#         print("-" * 25)


# s1 = Student("Rahul", 85)
# s2 = Student("Karn",-45)
# s3 = Student("Priya", 25)

# s1.show_details()
# s1.grade()
# s2.show_details()
# s2.grade()
# s3.show_details()
# s3.grade()

# # -------------------------------Vehicle Rental System-------------------------------

# class Vehicle:

#     def __init__(self, vehicle_name):
#         self.vehicle_name = vehicle_name
#         self.is_rented = False
    
#     def rent_vehicle(self):
#         if self.is_rented:
#             print("Vehicle already rented")
#         else:
#             self.is_rented = True
#             print("Vehicle rented successfully")
    
#     def return_vehicle(self):
#         if not self.is_rented:
#             print("Vehicle already available")
#         else:
#             self.is_rented = False
#             print("Vehicle returned successfully")

# v1 = Vehicle("Car")

# v1.rent_vehicle()
# v1.rent_vehicle()

# v1.return_vehicle()
# v1.return_vehicle()

# # -------------------------------E-Commerce Order System-------------------------------

# class Order:

#     def __init__(self, product, price):
#         self.name = product
#         self.rate = price
#         self.is_delivered = False

#     def show_details(self):
#         print(f"Product : {self.name}")
#         print(f"Price : {self.rate}")   

#     def deliver_order(self):
#         if self.is_delivered:
#             print("Order already delivered")
#         else:
#             self.is_delivered = True
#             print("Order delivered successfully")


# o1 = Order("Shirt", 8000)
# o1.show_details()
# o1.deliver_order()
# o1.deliver_order()

# # -------------------------------Hospital Management System-------------------------------

# class Patient:

#     def __init__(self, name, disease):
#         self.name = name 
#         self.disease = disease
#         self.is_admitted = False

#     def show_details(self):
#         print(f"Pateint Name : {self.name}")
#         print(f"Disease : {self.disease}")

#     def admit_patient(self):
#         if self.is_admitted:
#             print("Patient already admitted")
#         else:
#             self.is_admitted = True
#             print("Patient admitted successfully")

#     def discharge_patient(self):
#         if not self.is_admitted:
#             print("Patient already discharged")
#         else:
#             self.is_admitted = False
#             print("Patient discharged successfully")

# p1 = Patient("Rahul", "Fever")
# p1.show_details()
# p1.admit_patient()
# p1.admit_patient()
# p1.discharge_patient()
# p1.discharge_patient()

# # -------------------------------Student Attendance Tracker-------------------------------

# class Student:
#     def __init__(self, name):
#         self.name = name 
#         self.attendance = 0

#     def mark_attendance(self):
#             self.attendance += 1
    
#     def show_attendance(self):
#         print(f"Name : {self.name}")
#         print(f"Attendance : {self.attendance}")

# s1 = Student("Rahul")

# s1.mark_attendance()
# s1.mark_attendance()
# s1.mark_attendance()

# s1.show_attendance()

# # #-------------------------------Movie Ticket Booking System-------------------------------

# class MovieTicket:
    
#     def __init__(self, movie_name):
#         self.name = movie_name
#         self.is_booked = False
    
#     def book_ticket(self):
#         if self.is_booked:
#             print("Ticket already booked")
#         else:
#             self.is_booked = True
#             print("Ticket booked successfully")

#     def cancel_ticket(self):
#         if not self.is_booked:
#             print("Ticket already available")
#         else:
#             self.is_booked = False
#             print("Ticket cancelled successfully")

# m1 = MovieTicket("Avengers")

# m1.book_ticket()
# m1.book_ticket()

# m1.cancel_ticket()
# m1.cancel_ticket()



# # RPG Battle Arena System

class Character:

    def __init__(self, name, health, level):
        self.name = name 
        self.health = health
        self.level = level
    
    def show_details(self):
        print(f"Name   : {self.name}")
        print(f"Health : {self.health}")
        print(f"Level  : {self.level}")

    def attack(self):
        pass

    def take_damage(self, damage):
        self.health -= damage

        if self.health <= 0:
            self.health = 0
       

class Warrior(Character):

    def __init__(self, name, health, level, sword_damage):
        super().__init__(name, health, level)
        self.sword_damage = sword_damage

    def attack(self):
        damage = self.sword_damage * self.level
        return damage

class Mage(Character):

    def __init__(self, name, health, level, magic_power):
        super().__init__(name, health, level)
        self.magic_power = magic_power

    def attack(self):
        damage = ( self.magic_power * self.level ) + 20
        return damage
        
class Archer(Character):
    def __init__(self, name, health, level, arrow_damage):
        super().__init__(name, health, level)
        self.arrow_damage = arrow_damage

    def attack(self):
        damage = ( self.arrow_damage * self.level ) + 10
        return damage



class Arena:

    def __init__(self, arena_name):
        self.arena_name = arena_name
        self.characters = []

    def add_character(self,character):
            for char in self.characters:
                if char.name == character.name:
                    print("Character already exists")
                    return
                self.characters.append(character)

    def show_all_characters(self):
        for char in self.characters:
            char.show_details()
            print("-" * 20)

    def search_character(self, name):
        for char in self.characters:
            if char.name == name :
                char.show_details()
                return 
            
        print("Character not found")
        
    def remove_character(self, name):
        for char in self.characters:
            if char.name == name:
                self.characters.remove(char)
                print("Character removed successfully")
                return
        
        print("Character not found")

    def battle(self, name1, name2):
            char1 = None
            char2 = None

            for char in self.characters:

                if char.name == name1:
                    char1 = char
                if char.name == name2:
                    char2 = char

            if char1 is None or char2 is None:
                print("Character not found")
                return
            
            if name1 == name2:
                print("Same character selected")
                print("Match Draw - Cannot battle with the same character.")
                return

            damage1 = char1.attack()
            damage2 = char2.attack()

            print(f"{char1.name} attacks {char2.name}")
            print(f"Damage = {damage1}")

            char2.take_damage(damage1)

            print(f"{char2.name} attacks {char1.name}")
            print(f"Damage : {damage2}")
            char1.take_damage(damage2)

            print(f"{char1.name} Health = {char1.health}")
            print(f"{char2.name} Health = {char2.health}")

            if char1.health > char2.health:
                print(f"Winner = {char1.name}")
            elif char2.health > char1.health:
                print(f"Winner = {char2.name}")
            else:
                print("Draw")




arena = Arena("Battle Arena") 
while True:

        print("\n===== RPG Battle Arena =====")
        print("1. Create Warrior")
        print("2. Create Mage")
        print("3. Create Archer")
        print("4. Show All Characters")
        print("5. Search Character")
        print("6. Remove Character")
        print("7. Start Battle")
        print("8. Exit")  

        choice = input("Enter choice : ")

        if choice == "1":
            name = input("Enter Name : ")
            health = int(input("Enter Health : "))
            level = int(input("Enter Level : "))
            sword_damage = int(input("Enter Sword Damage : "))

            warrior = Warrior(name, health, level, sword_damage)
            arena.add_character(warrior)
            print("Warrior added successfully")

        elif choice == "2":
            name = input("Enter Name : ")
            health = int(input("Enter Health : "))
            level = int(input("Enter level : "))
            magic_power = int(input("Enter magic Power : "))

            mage = Mage(name, health, level, magic_power)
            arena.add_character(mage)
            print("Mage Added Successfully")

        elif choice == "3":
            name = input("Enter Name : ")
            health = int(input("Enter Health : "))
            level = int(input("Enter Level : "))
            arrow_damage = int(input("Enter Arrow Damage : "))

            archer = Archer(name, health, level, arrow_damage)

            arena.add_character(archer)

            print("Archer added successfully")

        elif choice == "4":
            arena.show_all_characters()

        elif choice == "5":
            name = input("Enter Name : ")
            arena.search_character(name)

        elif choice == "6":
            name = input("Enter Name : ")
            arena.remove_character(name)

        elif choice == "7":
            name1 = input("Enter First Character Name : ")
            name2 = input("Enter Second Character Name : ")

            arena.battle(name1, name2)
        
        elif choice == "8":
            print("Exiting...")
            break

        else:
            print("Invalid Choice")







# print("-" * 30)
# w1 = Warrior("Thor", 500, 5, 30)
# w1.show_details()
# w1.take_damage(200)
# print(f"Damage : {w1.attack()}")
# print("-" * 30)

# m1 = Mage("Merlin", 300, 7, 50)
# m1.show_details()
# print(f"Damage : {m1.attack()}")
# print("-" * 30)


# a1 = Archer("Hawkeye", 400, 4, 25)
# a1.show_details()
# print(f"Damage : {a1.attack()}")
# print("-" * 30)

# w1 = Warrior("Thor", 500, 5, 30)
# m1 = Mage("Merlin", 300, 7, 50)
# a1 = Archer("Hawkeye", 400, 4, 25)

# arena = Arena("Battle Arena")
# arena.add_character(w1)
# arena.add_character(m1)
# arena.add_character(a1)
# arena.show_all_characters()

# arena.search_character("Merlin")
# arena.search_character("Mike")

# arena.show_all_characters()
# arena.remove_character("Merlin")
# arena.show_all_characters()
# arena.remove_character("Mike")


# w1 = Warrior("Thor", 500, 5, 30)
# m1 = Mage("Merlin", 300, 7, 50)
# a1 = Archer("Hawkeye", 400, 4, 25)

# arena = Arena("Battle Arena")
# arena.add_character(w1)
# arena.add_character(m1)
# arena.add_character(a1)

# arena.battle("Thor", "Thor")