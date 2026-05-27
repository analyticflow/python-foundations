# ----------------------------------------------------- LOOPS PRACTICE ------------------------------------------------------

# Q1 Print numbers from 1 to 10
for i in range(1, 11):
    print(i)


# Q2 Print numbers from 10 to 1
for i in range(10, 0, -1):
    print(i)


# Q3 Print even numbers from 1 to 20
for i in range(2,21,2):
    print(i)


# Q4 Print odd numbers from 1 to 20
for i in range(1,21,2):
    print(i)


# Q5 Print multiplication table of 7
num = 7
for i in range(1,11):
      print(num, "x", i, "=", num*i)


# Q6 Print numbers from 1 to 50 divisible by 5
for i in range(1,51):
    if i % 5 == 0:
        print(i)


# Q7 Find sum of numbers from 1 to 10
total = 0
for i in range(1,11):
    total = total + i
print(total)


# Q8 Take a number input and print its table
num = int(input("Enter a number :"))
for i in range(1,11):
    print(num*i)


# Q9 Count how many even numbers are between 1 to 50
even_count = 0
for i in range(2,51,2):
    even_count = even_count + 1
print(even_count)


# Q10 Print square of numbers from 1 to 10
for i in range(1,11):
    print(i*i)


# Q11 Print numbers from 1 to 100 divisible by both 3 and 5
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print(i) 


# Q12 Find factorial of 5 Example: 5! = 5*4*3*2*1
num = 1
for i in range(1,6):
    num = num*i
print(num)


# Q13 Print all characters of a string using loop
name = input("Enter name :")
for ch in name:
    print(ch)


# Q14 Count vowels in a string
name = input("Enter name :")
vowel_count = 0
for ch in name:
  if ch in "aeiou":
        vowel_count = vowel_count+1
print("Total vowels = ",vowel_count)


# Q15 Find largest number in list
numberlist = [23,45,98,78,89]
largest = numberlist[0]
for i in numberlist:
    if i >= largest:
        largest = i
print(largest)


# Q16 Print numbers from 1 to 50 divisible by 3
for i in range(1,51):
    if i % 3 == 0:
        print(i)


# Q17 Print numbers from 1 to 100 divisible by 7
for i in range(1,101):
    if i % 7 == 0:
        print(i)


# Q18 Count odd numbers from 1 to 50
odd_count = 0
for i in range(1,51,2):
    odd_count = odd_count+1
print(odd_count)


# Q19 Find sum of even numbers from 1 to 100
even_total = 0 
for i in range(2,101,2):
    even_total = even_total+i
print(even_total)


# Q20 Print cube of numbers from 1 to 10
for i in range(1,11):
    print(i*i*i)


# Q21 Take a string and count vowels using loop
name = input("Enter your name : ")
vowel_count = 0
for i in name:
    if i in 'aeiou':
         vowel_count = vowel_count+1
print(vowel_count)


# Q22 Print all elements of list using loop
item_list = [23,43,56,78,90]
for i in item_list:
    print(i)


# Q23 Find smallest number in list
item_list = [23,43,12,78,9]
smallest = item_list[0]
for i in item_list:
    if i < smallest:
        smallest = i
print(smallest)


# Q24 Count positive and negative numbers in list
item_list = [23,43,12,78,9,-8,-5,-3,-67]
pos_count = 0
neg_count = 0
for i in item_list:
    if i >= 0:
        pos_count = pos_count+1
    else:
        neg_count = neg_count+1
print(f"Positive Count = {pos_count}\nNegative Count = {neg_count}")


# Q25 Print numbers from 1 to 30 except multiples of 3
for i in range(1, 31):
    if i % 3 != 0:
        print(i)