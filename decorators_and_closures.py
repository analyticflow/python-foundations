# =========================== DECORATORS & CLOSURES ===============================


# =========================== NESTED FUNCTIONS ===============================

# Example 1

def outer():

    def inner():
        print("Hello from Inner Function")

    inner()


outer()


# Example 2

def process():

    def helper():
        print("Processing Data...")

    helper()


process()


# Practice Q1

def outer():

    def inner():
        print("Inner Function Called")

    inner()


outer()


# =========================== CLOSURES ===============================

# Example 1

def outer():

    message = "Hello"

    def inner():
        print(message)

    return inner


func = outer()
func()


# Example 2

def multiplier(n):

    def multiply(x):
        return x * n

    return multiply


double = multiplier(2)
triple = multiplier(3)

print(double(5))
print(triple(5))


# Practice Q2

def power(n):

    def calculate(x):
        return x ** n

    return calculate


square = power(2)
cube = power(3)

print(square(4))
print(cube(4))


# Practice Q3

def greeting(message):

    def greet():
        print(message)

    return greet


hello = greeting("Welcome to Python")

hello()


# =========================== FUNCTIONS AS OBJECTS ===============================

# Example 1

def greet():
    print("Hello")


say_hello = greet

say_hello()


# Example 2

def execute(func):
    func()


execute(greet)


# =========================== BASIC DECORATORS ===============================

# Example 1

def decorator(func):

    def wrapper():

        print("Before Function")

        func()

        print("After Function")

    return wrapper


def greet():
    print("Hello")


greet = decorator(greet)

greet()


# Example 2 (@ Syntax)

def decorator(func):

    def wrapper():

        print("Before")

        func()

        print("After")

    return wrapper


@decorator
def welcome():
    print("Welcome")


welcome()


# =========================== DECORATOR WITH ARGUMENTS ===============================

# Example 1

def logger(func):

    def wrapper(*args, **kwargs):

        print("Function Started")

        result = func(*args, **kwargs)

        print("Function Finished")

        return result

    return wrapper


@logger
def add(a, b):
    return a + b


print(add(10, 20))


# Example 2

@logger
def multiply(a, b):
    return a * b


print(multiply(5, 6))


# =========================== PRACTICE Q4 ===============================

def logger(func):

    def wrapper(*args, **kwargs):

        print("Starting...")

        result = func(*args, **kwargs)

        print("Ending...")

        return result

    return wrapper


@logger
def display():
    print("Display Function Running")


display()


# =========================== PRACTICE Q5 ===============================

def timer(func):

    def wrapper(*args, **kwargs):

        print("Function Begin")

        result = func(*args, **kwargs)

        print("Function End")

        return result

    return wrapper


@timer
def task():
    print("Task Executing...")


task()


# =========================== PRACTICE Q6 ===============================

def call_counter(func):

    count = 0

    def wrapper(*args, **kwargs):

        nonlocal count

        count += 1

        print(f"Call #{count}")

        return func(*args, **kwargs)

    return wrapper


@call_counter
def hello():
    print("Hello")


hello()
hello()
hello()


# =========================== FUNCTION FACTORY ===============================

# Example 1

def discount_factory(discount):

    def apply(price):
        return price - (price * discount / 100)

    return apply


ten_percent = discount_factory(10)

print(ten_percent(1000))


# Example 2

def tax_factory(tax):

    def apply(amount):
        return amount + (amount * tax / 100)

    return apply


gst = tax_factory(18)

print(gst(1000))


# =========================== MINI PROJECT ===============================

print("\n===== USER ACTION LOGGER =====\n")


total_actions = 0


def logger(func):

    def wrapper(*args, **kwargs):

        global total_actions

        print(f"Action Started: {func.__name__}")

        result = func(*args, **kwargs)

        print(f"Action Completed: {func.__name__}")

        total_actions += 1

        print(f"Total Actions: {total_actions}")

        print("-" * 30)

        return result

    return wrapper


@logger
def login():
    print("User Logged In")


@logger
def logout():
    print("User Logged Out")


@logger
def register():
    print("User Registered")


login()
register()
logout()
login()


print(f"\nFinal Total Actions Performed: {total_actions}")