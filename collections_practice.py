#----------------------------------STRINGS------------------------------------------------

#Q1 Take a string input and print:first character middle character last character
fullname = input("Enter your full name :")
first = fullname[0]
middle = fullname[len(fullname)//2]
last = fullname[-1]
print("First character:", first)
print("Middle character:", middle)
print("Last character:", last)


#Q2 Take a string and print it in: uppercase lowercase title case
Title = input("Enter title name ")
print(f"Title in uppercase: {Title.upper()}\nTitle in lowercase : {Title.lower()}\n Title in titlecase : {Title.title()}")


#Q3 Take a string and: count total characters, count spaces
charcount = input("Enter your character :")
chartotal = len(charcount) # to get total count 
spacetotal = charcount.count(" ") # to count spaces
print(f"Total characters :{chartotal}\nTotal Space : {spacetotal}")


#Q4 Reverse a string. Example: Python → nohtyP
word = input("Enter your word : ")
revstring = word[::-1]
print("Your original word is ",word,"reverins string is ",revstring)

#Q5 Replace all spaces with _ Example: Hello World → Hello_World
space_word = input("Enter your input ")
rep_word = space_word.replace(" ","_")
print(f"Original string : {space_word}\nReplaced string : {rep_word}")


#------------------------------------------------LISTS (5)-------------------------------------------------------------

#Q6 Create list of 5 fruits and print: first fruit last fruit
fruit_list = ["Apple","Orange","Tomato","Guavava","Banana"]
first_fruit = fruit_list[0]
last_fruit =fruit_list[-1]
print(f"First Fruit : {first_fruit}\nLast Fruit : {last_fruit}")


#Q7 Add one new fruit into list.
fruit_list = ["Apple","Orange","Tomato","Guavava","Banana"]
fruit_list.append("kiwi")
print(fruit_list)


#Q8 Remove one fruit from list.
fruit_list = ["Apple","Orange","Tomato","Guavava","Banana"]
fruit_list.remove("Tomato")
print(fruit_list)


#Q9 Print total items in list. Hint: len()
fruit_list = ["Apple","Orange","Tomato","Guava","Banana"]
total_fruit = len(fruit_list)
print("Total Fruit : ",total_fruit)


#Q10 Create number list and print: maximum, minimum, sum
number_list = [1,2,3,4]
max_list = max(number_list)
min_list = min(number_list)
sum_list = sum(number_list)
print(f"maximun number = {max_list}\nminimum number = {min_list}\ntotal sum = {sum_list}")



#------------------------------------------------ TUPLES --------------------------------------------------------------

# Q11 Create tuple of 5 colors.
color_tuple = ("red","yellow","blue","black","purple")
print(color_tuple)


# Q12 Print: first item, last item, total length
color_tuple = ("red","yellow","blue","black","purple")
print(f"First item : {color_tuple[0]}\nLast item : {color_tuple[-1]}\nTotal sum : {len(color_tuple)}")


# Q13 Count how many times "red" appears.
color_tuple = ("red","yellow","blue","black","purple","red","red")
rcount = color_tuple.count("red")
print("Total red in tuple = ", rcount)


#--------------------------------------------------------------SETS --------------------------------------------------------------

# Q14 Create set with duplicate numbers. Observe duplicates removal.
duplicate_set = {1,2,3,1,2,3,4,4,5,5,6,7}
print(duplicate_set)


# Q15 Add new value into set.
duplicate_set = {1,2,3,1,2,3,4,4,5,5,6,7}
add_new = duplicate_set.add(45)
print(duplicate_set)


# Q16 Remove value from set.
duplicate_set = {1,2,3,1,2,3,4,4,5,5,6,7}
duplicate_set.remove(4)
print(duplicate_set)


#-------------------------------------------------------------- DICTIONARIES --------------------------------------------------------------

# Q17 Create dictionary: name, age, course, city
studentdict = {"name":"Mahek", "age":21, "course":"Python","city":"surat"}
print(studentdict) 


# Q18 Print only: name, course
studentdict = {"name":"Mahek", "age":21, "course":"Python","city":"surat"}
print(studentdict["name"])
print(studentdict["course"])

# Q19 Change city value.
studentdict = {"name":"Mahek", "age":21, "course":"Python","city":"surat"}
studentdict["city"]="Bangalore"
print(studentdict["city"])

# Q20 Add new key: phone and print updated dictionary.
studentdict = {"name":"Mahek", "age":21, "course":"Python","city":"surat"}
studentdict["phone"]=1010101010
print(studentdict)
