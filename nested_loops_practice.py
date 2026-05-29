# ----------------------------------------------------- NESTED LOOPS PRACTICE ------------------------------------------------------

for i in range(1,6):
    for j in range(i):
        print("*",end="")
    print()


for i in range(1,5):
    for j in range(1,i+1):
        print(j,end="")
    print()

# Q3 Print multiplication tables from 1 to 3
for i in range(1,11):
    for j in range(1,4):
        print(i,"x",j,"=",i*j, end="  ")
    print()

for i in range(1,4):
    print("Table of ",i)
    for j in range(1,11):
        print(i, "x", j, "=", i * j)
    print()


# Q4 Print numbers from 1 to 20 but stop at 15 using break
for i in range(1,21):
    if i == 16:
        break
    print(i)


# Q5 Print numbers from 1 to 10 except 5 using continue
for i in range(1,11):
    if i == 5:
        continue
    print(i)


for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print()


for i in range(1,5):
    for j in range(i):
        print(i,end="")
    print()

for i in range(1,5):
    for j in range(i):
        print(chr(65+j),end="")
    print()


for i in range(1,5):
    for j in range(1,5):
        print("*",end="")
    print()


for i in range(1,4):
    for j in range(1,4):
        print(j,end=" ")
    print()