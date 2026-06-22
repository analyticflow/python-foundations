# --------------------------- RANDOM MODULE ---------------------------

import random


# --------------------------- WHY RANDOM ---------------------------

# Example 1 (Without Random)

print(5)


# Example 2 (With Random)

print(random.randint(1, 6))


# --------------------------- RANDINT ---------------------------

# Example 1

print(random.randint(1, 10))


# Example 2

print(random.randint(100, 200))


# --------------------------- RANDRANGE ---------------------------

# Example 1

print(random.randrange(1, 10))


# Example 2

print(random.randrange(10, 50))


# --------------------------- RANDINT VS RANDRANGE ---------------------------

# Example

print(random.randint(1, 10))

print(random.randrange(1, 10))


# --------------------------- RANDOM ---------------------------

# Example 1

print(random.random())


# Example 2

print(random.random())


# --------------------------- UNIFORM ---------------------------

# Example 1

print(random.uniform(1, 10))


# Example 2

print(random.uniform(10, 20))


# --------------------------- CHOICE ---------------------------

# Example 1

colors = ["Red", "Blue", "Green"]

print(random.choice(colors))


# Example 2

animals = ["Cat", "Dog", "Rabbit"]

print(random.choice(animals))


# --------------------------- CHOICES ---------------------------

# Example 1

fruits = ["Apple", "Banana", "Orange"]

print(random.choices(fruits, k=3))


# Example 2

letters = ["A", "B", "C"]

print(random.choices(letters, k=5))


# --------------------------- SAMPLE ---------------------------

# Example 1

numbers = [1, 2, 3, 4, 5]

print(random.sample(numbers, 3))


# Example 2

students = ["Aman", "Rahul", "Priya", "Karan"]

print(random.sample(students, 2))


# --------------------------- CHOICES VS SAMPLE ---------------------------

# Example

items = ["A", "B", "C"]

print(random.choices(items, k=3))

print(random.sample(items, 3))


# --------------------------- SHUFFLE ---------------------------

# Example 1

cards = [1, 2, 3, 4, 5]

random.shuffle(cards)

print(cards)


# Example 2

names = ["Aman", "Rahul", "Priya"]

random.shuffle(names)

print(names)


# --------------------------- SEED ---------------------------

# Example 1

random.seed(1)

print(random.randint(1, 10))


# Example 2

random.seed(1)

print(random.randint(1, 10))


# --------------------------- RANDOM PASSWORD CHARACTER ---------------------------

# Example

chars = "abcdefghijklmnopqrstuvwxyz"

print(random.choice(chars))


# --------------------------- RANDOM OTP ---------------------------

# Example

otp = random.randint(1000, 9999)

print(otp)


# --------------------------- RANDOM DICE ---------------------------

# Example

dice = random.randint(1, 6)

print(dice)


# --------------------------- PRACTICE Q1 ---------------------------

print(random.randint(1, 100))


# --------------------------- PRACTICE Q2 ---------------------------

print(random.uniform(10, 20))


# --------------------------- PRACTICE Q3 ---------------------------

colors = ["Red", "Blue", "Green", "Black"]

print(random.choice(colors))


# --------------------------- PRACTICE Q4 ---------------------------

for _ in range(5):
    print(random.randint(1, 6))


# --------------------------- PRACTICE Q5 ---------------------------

numbers = [1, 2, 3, 4, 5]

random.shuffle(numbers)

print(numbers)


# --------------------------- PRACTICE Q6 ---------------------------

numbers = [10, 20, 30, 40, 50]

print(random.sample(numbers, 3))


# --------------------------- PRACTICE Q7 ---------------------------

otp = random.randint(1000, 9999)

print(otp)


# --------------------------- MINI PROJECT ---------------------------

print("\n----- LUCKY DRAW SYSTEM -----\n")

participants = [
    "Aman",
    "Rahul",
    "Priya",
    "Karan",
    "Neha"
]

winner = random.choice(participants)

remaining = participants.copy()

remaining.remove(winner)

runner_ups = random.sample(remaining, 2)

print("Winner:", winner)

print("\nRunner-Ups:")

for person in runner_ups:
    print(person)
