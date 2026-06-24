# --------------------------- OS MODULE ---------------------------

import os


# --------------------------- WHY OS MODULE ---------------------------

# Example 1

print("Python can interact with the operating system.")


# Example 2

print("OS module helps automate file and folder tasks.")


# --------------------------- CURRENT WORKING DIRECTORY ---------------------------

# Example 1

print(os.getcwd())


# Example 2

current_directory = os.getcwd()

print(current_directory)


# --------------------------- LIST FILES AND FOLDERS ---------------------------

# Example 1

print(os.listdir())


# Example 2

items = os.listdir()

print("Total Items:", len(items))


# --------------------------- CHANGING DIRECTORY ---------------------------

# Example 1

print("Current Directory:")

print(os.getcwd())

# os.chdir("Documents")   # Example only


# Example 2

print("Directory can be changed using os.chdir()")


# --------------------------- MKDIR ---------------------------

# Example 1

folder_name = "DemoFolder"

print("Folder Creation Example:", folder_name)


# Example 2

print("Use os.mkdir() to create a single folder")


# --------------------------- MAKEDIRS ---------------------------

# Example 1

nested_path = "Python/Data/Reports"

print(nested_path)


# Example 2

print("Use os.makedirs() for nested folders")


# --------------------------- RMDIR ---------------------------

# Example 1

print("Use os.rmdir() to remove empty folders")


# Example 2

print("Folder must be empty before removal")


# --------------------------- REMOVEDIRS ---------------------------

# Example 1

print("Use os.removedirs() for nested empty folders")


# Example 2

print("All folders must be empty")


# --------------------------- RENAME ---------------------------

# Example 1

print("old.txt -> new.txt")


# Example 2

print("Data -> Database")


# --------------------------- REMOVE FILE ---------------------------

# Example 1

print("Use os.remove() to delete files")


# Example 2

print("Always check file existence first")


# --------------------------- EXISTS ---------------------------

# Example 1

print(os.path.exists("data.txt"))


# Example 2

if os.path.exists("data.txt"):
    print("Found")
else:
    print("Not Found")


# --------------------------- ISFILE ---------------------------

# Example 1

print(os.path.isfile("data.txt"))


# Example 2

file_status = os.path.isfile("os_module.py")

print(file_status)


# --------------------------- ISDIR ---------------------------

# Example 1

print(os.path.isdir("DemoFolder"))


# Example 2

print(os.path.isdir("."))


# --------------------------- FILE SIZE ---------------------------

# Example 1

if os.path.exists(__file__):
    print(os.path.getsize(__file__))


# Example 2

if os.path.isfile(__file__):
    print("Current File Size:", os.path.getsize(__file__))


# --------------------------- PATH JOIN ---------------------------

# Example 1

path = os.path.join(
    "Projects",
    "Python",
    "main.py"
)

print(path)


# Example 2

path = os.path.join(
    "Data",
    "Reports",
    "sales.xlsx"
)

print(path)


# --------------------------- ABSOLUTE PATH ---------------------------

# Example 1

print(os.path.abspath("."))


# Example 2

print(os.path.abspath(__file__))


# --------------------------- SYSTEM COMMAND ---------------------------

# Example 1

os.system("echo Hello OS Module")


# Example 2

print("System commands can be executed using os.system()")


# --------------------------- ENVIRONMENT VARIABLES ---------------------------

# Example 1

print(os.getenv("USERNAME"))


# Example 2

print(os.getenv("PATH"))


# --------------------------- PRACTICE Q1 ---------------------------

print(os.getcwd())


# --------------------------- PRACTICE Q2 ---------------------------

print(os.listdir())


# --------------------------- PRACTICE Q3 ---------------------------

folder_name = "TestFolder"

print("Example Folder:", folder_name)


# --------------------------- PRACTICE Q4 ---------------------------

print("Rename TestFolder -> MyFolder")


# --------------------------- PRACTICE Q5 ---------------------------

print(os.path.exists("data.txt"))


# --------------------------- PRACTICE Q6 ---------------------------

print(os.path.isdir("MyFolder"))


# --------------------------- PRACTICE Q7 ---------------------------

project_path = os.path.join(
    "Projects",
    "Python",
    "main.py"
)

print(project_path)


# --------------------------- MINI PROJECT ---------------------------

print("\n----- PROJECT FOLDER CREATOR -----\n")

project_name = "StudentManagement"

folders = [
    "data",
    "reports",
    "logs",
    "src"
]

base_path = os.path.join(
    os.getcwd(),
    project_name
)

print("Project Name:", project_name)

print("\nProject Structure:\n")

print(project_name)

for folder in folders:
    print("├──", folder)

print("└── README.md")

print("\nProject Path:")

print(base_path)

print("\nVerification:")

for folder in folders:
    folder_path = os.path.join(
        base_path,
        folder
    )

    print(
        folder,
        "->",
        os.path.exists(folder_path)
    )

print("\nREADME.md -> Example File")
