#Day 1 Python Practice Questions
print("Python setup successful")

#------------------------------------------------SECTION 1 — Print & Variables---------------------------------------------------

#Q1 Print your: Name, Age , City
Name = str(input("Enter your name : "))
Age = int(input("Enter your age : "))
City = str(input("Enter your city name : "))
print(f"Name: {Name}\nAge: {Age}\nCity: {City}")


#Q2 Store two numbers in variables and print their sum.
num1 = float(input("Enter 1st Number : "))
num2 = float(input("Enter 2nd Number : "))
sum = num1 + num2
print("Sum of",num1,"&",num2,"=",sum)


#Q3 Store your first name and last name separately and print full name.
fname = str(input("Enter your first name :"))
lname = str(input("Enter your last name : "))
fullname = fname +' '+ lname
print("Your full name : ",fullname)


#Q4 Store a float number and print its datatype.
fnumber = 24.098
print("type of given number : ",type(fnumber))


#Q5 Convert string "50" into integer and add 10.
snum = "50"
print("Type of",snum,"=",type(snum))
add = int(snum)+10
print("type of",add,"=", type(add))
print("Sum of str & int : ",add)


#-------------------------------------------------------------------SECTION 2 — User Input---------------------------------------------------------------------------

#Q6 Take user name as input and print: Welcome Mahek
user = str(input("Enter your name : "))
print("Welcome",user)


#Q7 Take two integers from user and print: addition subtraction multiplication division
num1 = float(input("Enter 1st number : "))
num2 = float(input("Enter 2nd number : "))
add = num1 + num2
print("addition of numbers = ",add)
sub = num1-num2
print("Subtraction num2 from num1 = ",sub)
multi = num1*num2
print("Multiplication of numbers = ", multi)
division = num1/num2
print("Division of numbers = ", division)


#Q8 Take age input and print : You are 21 years old
age = int(input("Enter your age : "))
print("Your are",age,"years old.")


#Q9 Take a number and print its square.
num = int(input("Enter a number to get its square : "))
sqr = num*num
print("Square of",num,"=",sqr)


#Q10 Take temperature in Celsius and convert to Fahrenheit. Formula : (F × 9/5) + 32
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius* 9/5)+32
print("Temperature in Fahrenheit:", fahrenheit)