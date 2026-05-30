# # # ----------------------------------------------------- FILE HANDLING PRACTICE ------------------------------------------------------

# with open("demo.txt","w") as file:
#     file.write("Hello World!")


# with open("demo.txt","w") as file:
#     file.write("Python Learning")


# with open("demo.txt","a") as file:
#     file.write(" is fun")


# with open("demo.txt","r") as file:
#     print(file.read())


# with open("demo.txt","r") as file:
#     text = file.read()

# print(len(text))
# print(text[0])
# print(text[7:15])
# print(text[-1])


# with open("about_me.txt","w") as file:
#     file.write("I am learning Python")


# with open("about_me.txt","r") as file:
#     text = file.read()

# print(text)
# print(len(text))
# print(text[0])
# print(text[-1])


# with open("about_me.txt", "a") as file:
#     text = file.write(" every day")


# with open("about_me.txt", "w") as file:
#     file.write("I am learning Python every day")


# with open("skills.txt","w") as file:
#     file.write("Python\nSQL\nGitHub")


# with open("skills.txt","r") as file:
#     print(file.readlines())



# with open("skills.txt","r") as file:
#     skills = file.readlines()

# print(skills)
# print(len(skills))


# with open("skills.txt","r") as file:
#     for line in file:
#         print(line.strip())            #print(line)


# # Practice Q2 Create a file:
#                 # Apple
#                 # Banana
#                 # Mango
#                 # Orange

# # Then write code that:
#                 # Reads the file.
#                 # Prints each fruit on a new line using a loop.
#                 # Uses .strip().

# with open("fruits.txt","w") as file:
#     file.write("Apple\nBanana\nMango\nOrango")


# with open("fruits.txt","r") as file:
#     for line in file:
#         print(line.strip())   



# #  Q2 Create a file:
#         # Python
#         # SQL
#         # GitHub
#         # Excel

# # Then write code that:
#         # Reads all lines.
#         # Counts how many lines are in the file.
#         # Prints:
#         # Total skills = 4

# with open("skills.txt","w") as file:
#     file.write("Python\nSQL\nGitHub\nExcel")

# with open("skills.txt","r") as file:
#     skills = file.readlines()
# print("Total Skills = ",len(skills))


# # Q3 Write code that prints:
#         # Skill 1 : Python
#         # Skill 2 : SQL
#         # Skill 3 : GitHub
#         # Skill 4 : Excel

# count = 1
# with open("skills.txt","r") as file:
#     for skill in file:
#         print("Skill",count,":",skill.strip())
#         count=count+1



# #  Q4 : Create a file : 85, 90, 78, 95
#         #find or print => Total Marks = 348

# with open("marks.txt","w") as file:
#     file.write("85\n90\n78\n95")


# total = 0
# with open("marks.txt","r") as file:
#     for marks in file:
#         text = marks.strip()
#         total = total + int(text) # total += int(text)
# print("Total marks = ",total)
        


# # Q5 Create: prices.txt : Content: 120 250 80 150  => Print: Highest Price = 250

# with open("prices.txt","w") as file:
#     file.write("120\n250\n80\n150")

# highest_price = 0
# with open("prices.txt","r") as file:
#     for num in file:
#         price = int(num.strip())
#         if price > highest_price:
#             highest_price = price
# print("Highest Price =",highest_price)



# Q6 Create : student_marks.txt content : 85 90 78 95 88 Print => Total Students = 5, Total Marks = 436, Highest Marks = 95

# with open("student_marks.txt","w") as file:
#     file.write("85\n90\n78\n95\n88")

with open("student_marks.txt","r") as file:
    data = file.readlines()
    Total_student = len(data)
    print("Total Students =",Total_student)

    Total_Marks = 0
    highest_Marks = 0
    for marks in data:
        m = int(marks.strip())
        Total_Marks += m
        if m > highest_Marks:
            highest_Marks = m
    print("Total Marks =",Total_Marks)
    print("Highest Marks =", highest_Marks)


