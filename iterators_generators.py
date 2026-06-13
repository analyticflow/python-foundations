# =========================== ITERATORS & GENERATORS ===============================

# ITERATORS

numbers = [10, 20, 30]

it = iter(numbers)

print(next(it))
print(next(it))
print(next(it))

# StopIteration

numbers = [1, 2]

it = iter(numbers)

try:
    print(next(it))
    print(next(it))
    print(next(it))
except StopIteration:
    print("No more items")

# PRACTICE Q1

names = ["Aman", "Rahul", "Priya"]

it = iter(names)

print(next(it))
print(next(it))
print(next(it))

# PRACTICE Q2

colors = ["Red", "Blue", "Green", "Black"]

it = iter(colors)

for color in colors:
    print(color)

# PRACTICE Q3

numbers = [100, 200, 300]

it = iter(numbers)

try:
    while True:
        print(next(it))
except StopIteration:
    print("Iteration Completed")

# ITERATOR PROTOCOL => iter() and next()

class Counter:

    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration

        value = self.current
        self.current += 1
        return value

counter = Counter(1, 5)

for num in counter:
    print(num)

# PRACTICE Q4

class EvenNumbers:


    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.end:

            number = self.current
            self.current += 1

            if number % 2 == 0:
                return number

        raise StopIteration
    
for num in EvenNumbers(1, 10):
    print(num)

# PRACTICE Q5

class Countdown:


    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):

        if self.current < 1:
            raise StopIteration

        value = self.current
        self.current -= 1
        return value
    

for num in Countdown(5):
    print(num)


# GENERATORS => yield


def numbers_generator():
    yield 1
    yield 2
    yield 3

gen = numbers_generator()

print(next(gen))
print(next(gen))
print(next(gen))

# yield vs return

def demo_return():
    return 10

def demo_yield():
    yield 10

print(demo_return())
print(demo_yield())

# PRACTICE Q6

def count_up_to(n):
    for i in range(1, n + 1):
        yield i

for num in count_up_to(5):
    print(num)


# PRACTICE Q7

def even_generator(limit):
    for num in range(2, limit + 1, 2):
        yield num

for num in even_generator(20):
    print(num)

# PRACTICE Q8

def countdown(start):
    while start > 0:
        yield start
        start -= 1

for num in countdown(5):
    print(num)



# MINI PROJECT - Number Stream Generator


def number_stream(start, end):
    while start <= end:
        yield start
        start += 1

start = int(input("Enter start: "))
end = int(input("Enter end: "))

count = 0

for number in number_stream(start, end):
    print(number)
    count += 1

print("Total Generated =", count)