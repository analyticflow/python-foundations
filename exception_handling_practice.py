# =====================================================================================================================
#                                          EXCEPTION HANDLING PRACTICE
# =====================================================================================================================

# ----------------------------------- COMMON EXCEPTIONS -----------------------------------

# ZeroDivisionError
# print(10 / 0)

# ValueError
# num = int(input("Enter number : "))


# -----------------------------------TRY - EXCEPT -----------------------------------

try:
    print(10 / 0)
except:
    print("Something went wrong")


try:
    num = int(input("Enter number : "))
    print(num)
except:
    print("Something went wrong")


# ----------------------------------- SPECIFIC EXCEPTIONS -----------------------------------

try:
    num = int(input("Enter number : "))
    print(num)
except ValueError:
    print("Enter numbers only")


try:
    num = int(input("Enter number : "))
    result = 100 / num
    print(result)

except ValueError:
    print("Enter numbers only")

except ZeroDivisionError:
    print("Number cannot be divided by 0")


# ----------------------------------- ELSE -----------------------------------

try:
    num = int(input("Enter number : "))
    print("Number :", num)

except ValueError:
    print("Please enter numbers only")

else:
    print("Everything worked successfully")


# ----------------------------------- FINALLY -----------------------------------

try:
    num = int(input("Enter number : "))
    print(100 / num)

except ValueError:
    print("Enter numbers only")

except ZeroDivisionError:
    print("Cannot divide by 0")

finally:
    print("Program finished")


# ----------------------------------- RAISE -----------------------------------

age = int(input("Enter your age : "))

if age < 18:
    raise ValueError("Age must be 18 or above")

print("Access Granted!")


balance = 500

withdraw = int(input("Enter withdraw amount : "))

if withdraw > balance:
    raise ValueError("Insufficient Balance")


# ----------------------------------- CUSTOM EXCEPTIONS  -----------------------------------

class AgeError(Exception):
    pass


age = int(input("Enter age : "))

if age < 18:
    raise AgeError("Age must be 18 or above")

print("Access Granted!")


# ------------------------------------ Multiple Exception -----------------------------------------

try:
    num = int(input("enter num :"))
    print(100/num)

except(ValueError, ZeroDivisionError):
    print("Invalid input")


# ------------------------------------ Catch Actual Error Message -----------------------------------------

try:
    num = int(input("enter number :"))

except ValueError as e:
    print("error :",e)

# ---------------------------------------Generic Exception------------------------------------------------

try:
    num = int(input("enter number : "))
    result = 100/num
    print(result)

except Exception as e: # catches any unexpected error
    print("error :",e)



# =====================================================================================================================
#                                               PRACTICE QUESTIONS
# =====================================================================================================================


# Q1 Check Negative Number

num = int(input("Enter number : "))

if num < 0:
    raise ValueError("Negative numbers not allowed")

print("Square of number =", num * num)


# Q2 Check Password Length

try:
    password = input("Enter your password : ")

    if len(password) < 8:
        raise ValueError("Password too short")

    print("Password accepted!")

except ValueError as e:
    print(e)

   # Q3 File Not Found

try:
    with open("unknown.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File not found")


# Q4 Marks Validation

try:
    marks = int(input("Enter marks : "))

    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100")

    print("Marks accepted")

except ValueError as e:
    print(e)


# Q5 Username Validation

try:
    username = input("enter name : ")

    if username == "":
        raise ValueError("Username can not be empty")
    
    elif username.isdigit():
        raise ValueError("username name can not be a number")
    
    print("Welcome",username)

except ValueError as e:
    print(e)


# Q6 Name Validation

try:
    name = input("enter name :")

    if name == "":
        raise ValueError("name can not be empty")
    
    if any(char.isdigit() for char in name):
        raise ValueError("name can not contain numbers")

    print("Welcome", name)

except ValueError as e:
    print(e)


# # Q7 Email Validation (Simple)
try:
    email = input("enter email")

    if "@" not in email:
        raise ValueError("invalid email")
    
    print("email accepted = ",email)

except ValueError as e:
    print(e)


# ATM Program : Requirements:
#                 Balance = 1000
#                 Ask withdrawal amount
#                 If user enters text → show error
#                 If amount ≤ 0 → raise error
#                 If amount > balance → raise error
#                 Otherwise print:
#                             Withdrawal Successful
#                             Remaining Balance = xxx

try:
    balance = 1000
    withdrawal = int(input("enter amount :"))

    if withdrawal <= 0:
        raise ValueError("Amount must be greater than 0")    
    elif withdrawal > balance:
        raise ValueError("not enough balance")
    
    print("Withdrawal Successful")
    print("Remaining Amount =",balance-withdrawal)

except ValueError as e:
    print("Error : ",e)