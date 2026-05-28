# ----------------------------------------------------- FUNCTIONS PRACTICE ------------------------------------------------------

# Q1 Create function that prints Hello World
def greet():
    print("Hello World")

greet()


# Q2 Create function that prints your name
def name(n):
    print("Hello",n)

username = input("Enter your name : ")
name(username)


# Q3 Create function to add two numbers
def addition(a,b):
    return a+b

print(addition(5,9))


# Q4 Create function to multiply two numbers
def multiplication(a,b):
    return a*b

num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))
print("Multiplication of numbers = ",multiplication(num1,num2))


# Q5 Create function that prints numbers from 1 to 10
def print_numbers():
    for i in range(1,11):
        print(i)

print_numbers()


# Q6 Create function to print even numbers from 1 to 20
def print_even():
    for i in range(1,21):
        if i % 2 == 0:
            print(i)

print_even()

    
# Q7 Create function that returns square of a number
def print_square(num):
    return num*num

number = int(input("Enter a number : "))
print("Square of",number,"=",print_square(number))


# Q8 Create function that checks even or odd
def even_odd(num):
    if num%2 == 0:
        print("even number ")
    else:
        print("odd number")

number = int(input("Enter a number : "))
even_odd(number)


# Q9 Create function that counts vowels in string
def count_vowels(name):
    count = 0
    for i in name:
     if i in 'aeiou': # took help in this line 
        count = count + 1
    print(count)

count_vowels("Chatgpt")


# Q10 Create function that finds largest number in list
def print_largest():
    numberlist = [56,78,90,45,450]
    largest = numberlist[0]
    for i in numberlist:
        if i>largest:
            largest=i
    print(largest)

print_largest()


# Q11 Create function to print all elements of a list
def print_elements_list():
    items = ['raghav','mahesh','suresh','dinesh']
    for i in items:
        print(i)

print_elements_list()


# Q12 Create function to find smallest number in list
def find_smallest():
    numberlist = [56,78,90,45,45]
    smallest = numberlist[0]
    for i in numberlist:
        if i < smallest:
            smallest=i
    print("smallest number = ",smallest)

find_smallest()


# Q13 Create function to count positive numbers in list
def count_positive_numbers():
    numberlist = [56,78,-90,45,-45,0]
    pos_count = 0
    for i in numberlist:
        if i > 0:
            pos_count = pos_count + 1
    print(pos_count)

count_positive_numbers()
            

# Q14 Create function to count negative numbers in list
def count_negative_numbers():
    numberlist = [56,78,-90,45,-45,0]
    neg_count = 0
    for i in numberlist:
        if i < 0:
            neg_count = neg_count + 1
    print(neg_count)

count_negative_numbers()


# Q15 Create function that prints multiplication table of any number
def print_multiplication(number):
    for i in range(1,11):
        print(number,"*",i,"=",number*i)

print_multiplication(5)


# Q16 Create function that returns factorial of a number
def print_factorial(number):
    fact = 1
    for i in range(1,number+1):
         fact = fact * i 
    return fact

usernumber = int(input(" 16 Enter number to print factorial : "))        
print("Factorial of",usernumber,"=",print_factorial(usernumber))


# Q17 Create function that checks whether vowel or consonant
def check_vowel_consonant(letter):
    if len(letter) != 1:
        return "please enter a single character"
    if letter.lower() in 'aeiou':
        return letter + " is vowel"
    else:
        return letter + " is consonant"
    
userinput = input("Enter a character : ")
print(check_vowel_consonant(userinput))


# Q18 Create function to count total characters in string
def count_total_characters(userstring):
    total = 0
    for i in userstring:
        total = total + 1
    print("Total characters = ",total)

count_total_characters("Python")


# Q19 Create function to find sum of list elements
def find_sum_list(itemlist):
    total = 0
    for i in itemlist:
        total = total + i
    print("Sum of Given List = ",total)

find_sum_list([12,4,6,7,8,20])


# Q20 Create function that prints numbers divisible by 5 from 1 to 100
def five_divisible():
    for i in range(1,101):
        if i % 5 == 0:
             print(i)
    
five_divisible()


# Q21 Create function that returns largest number from list
def print_largest(itemlist):
    largest = itemlist[0]
    for i in itemlist:
        if i > largest:
            largest = i
    return largest

print(print_largest([56,89,56,26,35,-899]))


# Q22 Create function that returns smallest number from list
def print_smallest(itemlist):
    smallest = itemlist[0]
    for i in itemlist:
        if i < smallest:
            smallest = i
    return smallest

n = int(input("How many numbers ? "))
userlist = []

for i in range(n):
    num = int(input("Enter number :"))
    userlist.append(num)    

result = print_smallest(userlist)
print("the smallest from list = ",result)


# Q23 Create function that counts vowels in a string
def count_vowels(userinput):
    count = 0
    for i in userinput.lower():
        if i in "aeiou":
            count = count + 1
    return count

print(count_vowels("This code is like i have wrote so many times that i think i am going mad"))


# Q24 Create function that checks whether number is positive, negative, or zero
def checking_pos_neg_zero(number):
    if number > 0:
        return "positive number"
    elif number < 0:
        return "negative number"
    else:
        return "zero number"
    
num = int(input("enter number : "))
print(checking_pos_neg_zero(num))


# Q25 Create function that returns reverse of string
def reverse_string(username):
    return username[::-1]

userinput = input("Enter you string : ")
print(reverse_string(userinput))
    