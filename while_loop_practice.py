# ----------------------------------------------------- WHILE LOOPS PRACTICE ------------------------------------------------------


# Q1 Print numbers from 1 to 10 using while loop
i = 1
while i <= 10:
    print(i)
    i=i+1


# Q2 Print numbers from 10 to 1 using while loop
i = 10
while i >= 1:
    print(i)
    i = i-1


# Q3 Print even numbers from 1 to 20
i = 2
while i <= 20:
    print(i)
    i = i+2


# Q4 Print odd numbers from 1 to 20
i = 1
while i <= 20:
    print(i)
    i = i+2


# Q5 Find sum of numbers from 1 to 10
i = 1
total = 0
while i <= 10:
    total = total + i
    i = i+1
print(total)


# Q6 Print multiplication table of 5
num = 5
i = 1
while i <= 10:
    print(num,"x",i,"=",num*i)
    i=i+1


# Q7 Count numbers from 1 to 50 divisible by 3
i=1
count = 0
while i <= 50:
    if i%3 == 0:
        count = count + 1
    i=i+1
print(count)


# Q8 Print all characters of a string using while loop
name = input("Enter your name :")
i = 0
while i < len(name): # Took the help from ai
    print(name[i])
    i=i+1


# Q9 Find largest number in list using while loop
numberlist = [23,98,43,99,610]
i = 0
largest = numberlist[0]
while i < len(numberlist):
    if numberlist[i] > largest: 
        largest = numberlist[i] # Took the help from ai
    i=i+1
print(largest)


# Q10 Print numbers from 1 to 30 except multiples of 4
i = 1
while i <= 30:
    if i%4 != 0:
        print(i)
    i=i+1