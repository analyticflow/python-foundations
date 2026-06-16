# --------------------------- CONTEXT MANAGERS ---------------------------


# --------------------------- WHY CONTEXT MANAGERS ---------------------------

# Example 1 (Without Context Manager)

file = open("data.txt", "r")

# content = file.read()

file.close()


# Example 2 (With Context Manager)

with open("data.txt", "r") as file:
    # content = file.read()
    pass


# --------------------------- WITH STATEMENT ---------------------------

# Example 1

with open("notes.txt") as file:
    print("Reading File...")


# Example 2

with open("data.txt") as file:
    print("Working With File")


# --------------------------- CUSTOM CONTEXT MANAGER ---------------------------

# Example 1

class Demo:

    def __enter__(self):
        print("Entering")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting")


with Demo():
    print("Inside Block")


# Example 2

class Resource:

    def __enter__(self):
        print("Resource Acquired")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Resource Released")


with Resource():
    print("Using Resource")


# --------------------------- UNDERSTANDING __ENTER__ ---------------------------

# Example

class Manager:

    def __enter__(self):
        print("Enter Method Called")
        return "Resource Object"

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exit Method Called")


with Manager() as resource:
    print(resource)


# --------------------------- UNDERSTANDING __EXIT__ ---------------------------

# Example

class Cleanup:

    def __enter__(self):
        print("Start")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Cleanup Complete")


with Cleanup():
    print("Doing Work")


# --------------------------- EXCEPTION HANDLING ---------------------------

# Example

class ExceptionDemo:

    def __enter__(self):
        print("Start")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("End")


try:

    with ExceptionDemo():
        10 / 0

except ZeroDivisionError:
    print("ZeroDivisionError Occurred")


# --------------------------- SUPPRESSING EXCEPTIONS ---------------------------

# Example

class SafeManager:

    def __enter__(self):
        print("Entering Safe Block")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exception Suppressed")
        return True


with SafeManager():
    10 / 0

print("Program Continues")


# --------------------------- PRACTICE Q1 ---------------------------

class MessageManager:

    def __enter__(self):
        print("Entering")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting")


with MessageManager():
    print("Inside Block")


# --------------------------- PRACTICE Q2 ---------------------------

class DatabaseConnection:

    def __enter__(self):
        print("Database Connected")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Database Closed")


with DatabaseConnection():
    print("Working...")


# --------------------------- PRACTICE Q3 ---------------------------

class CounterManager:

    count = 0

    def __enter__(self):

        CounterManager.count += 1

        print(f"Entered {CounterManager.count} Time(s)")

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting")


with CounterManager():
    print("Block 1")

with CounterManager():
    print("Block 2")

with CounterManager():
    print("Block 3")


# --------------------------- PRACTICE Q4 ---------------------------

class ErrorLogger:

    def __enter__(self):
        print("Starting")
        return self

    def __exit__(self, exc_type, exc_value, traceback):

        if exc_type:
            print("Exception Type:", exc_type)
            print("Exception Value:", exc_value)

        print("Ending")


try:

    with ErrorLogger():
        10 / 0

except ZeroDivisionError:
    pass


# --------------------------- PRACTICE Q5 ---------------------------

class Timer:

    def __enter__(self):
        print("Task Started")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Task Finished")


with Timer():
    print("Executing Task...")


# --------------------------- MINI PROJECT ---------------------------

print("\n----- SECURE FILE SESSION SIMULATOR -----\n")


class FileSession:

    def __enter__(self):
        print("Opening File")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing File")

        if exc_type:
            print("Exception Handled:", exc_value)

    def read(self):
        print("Reading File Data")

    def write(self):
        print("Writing File Data")


try:

    with FileSession() as file:

        file.read()

        print("Working with file")

        file.write()

        # 10 / 0   # Uncomment to test exception handling

except Exception as error:
    print("Error:", error)