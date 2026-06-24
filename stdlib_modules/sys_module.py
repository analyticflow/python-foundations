# --------------------------- SYS MODULE ---------------------------

import sys


# --------------------------- WHY SYS MODULE ---------------------------

# Example 1

print("Sys module provides interpreter information.")


# Example 2

print("Sys module helps interact with Python runtime.")


# --------------------------- SYS.VERSION ---------------------------

# Example 1

print(sys.version)


# Example 2

print("Current Python Version Above")


# --------------------------- SYS.VERSION_INFO ---------------------------

# Example 1

print(sys.version_info)


# Example 2

print("Major Version:", sys.version_info.major)

print("Minor Version:", sys.version_info.minor)


# --------------------------- SYS.PLATFORM ---------------------------

# Example 1

print(sys.platform)


# Example 2

if sys.platform.startswith("win"):
    print("Windows User")
else:
    print("Non-Windows User")


# --------------------------- SYS.ARGV ---------------------------

# Example 1

print(sys.argv)


# Example 2

print("Program Name:", sys.argv[0])


# --------------------------- SYS.PATH ---------------------------

# Example 1

print(sys.path)


# Example 2

print("Total Search Paths:", len(sys.path))


# --------------------------- ADDING PATHS ---------------------------

# Example 1

sys.path.append("C:/MyModules")

print("Custom Path Added")


# Example 2

print(sys.path[-1])


# --------------------------- SYS.MAXSIZE ---------------------------

# Example 1

print(sys.maxsize)


# Example 2

print("Maximum Platform Integer Size Above")


# --------------------------- SYS.GETSIZEOF ---------------------------

# Example 1

numbers = [1, 2, 3]

print(sys.getsizeof(numbers))


# Example 2

text = "Python"

print(sys.getsizeof(text))


# --------------------------- RECURSION LIMIT ---------------------------

# Example 1

print(sys.getrecursionlimit())


# Example 2

print("Current Recursion Limit Displayed Above")


# --------------------------- SET RECURSION LIMIT ---------------------------

# Example 1

current_limit = sys.getrecursionlimit()

sys.setrecursionlimit(current_limit)

print(sys.getrecursionlimit())


# Example 2

print("Recursion Limit Verified")


# --------------------------- STDOUT ---------------------------

# Example 1

sys.stdout.write("Hello from stdout\n")


# Example 2

sys.stdout.write("Python Runtime Output\n")


# --------------------------- STDERR ---------------------------

# Example 1

sys.stderr.write("Example Error Message\n")


# Example 2

sys.stderr.write("Diagnostic Information\n")


# --------------------------- STDIN ---------------------------

# Example 1

print("stdin is used for reading input streams.")


# Example 2

print("input() is commonly used instead of sys.stdin.")


# --------------------------- SYS.EXIT ---------------------------

# Example 1

print("sys.exit() can terminate programs safely.")


# Example 2

print("Code below sys.exit() would not execute.")


# --------------------------- PRACTICE Q1 ---------------------------

print(sys.version)


# --------------------------- PRACTICE Q2 ---------------------------

print(sys.platform)


# --------------------------- PRACTICE Q3 ---------------------------

print(sys.maxsize)


# --------------------------- PRACTICE Q4 ---------------------------

sample_list = [10, 20, 30, 40, 50]

print(sys.getsizeof(sample_list))


# --------------------------- PRACTICE Q5 ---------------------------

print(sys.getrecursionlimit())


# --------------------------- PRACTICE Q6 ---------------------------

print("Example: sys.exit()")

# sys.exit()


# --------------------------- PRACTICE Q7 ---------------------------

print(sys.path)


# --------------------------- MINI PROJECT ---------------------------

print("\n----- SYSTEM INFORMATION VIEWER -----\n")

sample_data = [1, 2, 3, 4, 5]

print("Python Version:")

print(sys.version)

print("\nPlatform:")

print(sys.platform)

print("\nMax Size:")

print(sys.maxsize)

print("\nRecursion Limit:")

print(sys.getrecursionlimit())

print("\nList Memory:")

print(sys.getsizeof(sample_data), "bytes")