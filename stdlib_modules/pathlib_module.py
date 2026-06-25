# --------------------------- PATHLIB MODULE ---------------------------

from pathlib import Path


# --------------------------- WHY PATHLIB ---------------------------

# Example 1

path = Path("Projects") / "Python" / "main.py"

print(path)


# Example 2

print("Pathlib provides modern path handling.")


# --------------------------- CREATE PATH OBJECT ---------------------------

# Example 1

path = Path("data.txt")

print(path)


# Example 2

file_path = Path("report.pdf")

print(file_path)


# --------------------------- CURRENT WORKING DIRECTORY ---------------------------

# Example 1

print(Path.cwd())


# Example 2

current_directory = Path.cwd()

print(current_directory)


# --------------------------- HOME DIRECTORY ---------------------------

# Example 1

print(Path.home())


# Example 2

home_directory = Path.home()

print(home_directory)


# --------------------------- JOINING PATHS ---------------------------

# Example 1

path = Path("Projects") / "Python" / "main.py"

print(path)


# Example 2

path = Path("Data") / "Reports" / "sales.xlsx"

print(path)


# --------------------------- EXISTS ---------------------------

# Example 1

file = Path("data.txt")

print(file.exists())


# Example 2

print(Path("report.pdf").exists())


# --------------------------- IS_FILE ---------------------------

# Example 1

print(Path("data.txt").is_file())


# Example 2

print(Path(__file__).is_file())


# --------------------------- IS_DIR ---------------------------

# Example 1

print(Path(".").is_dir())


# Example 2

print(Path("Projects").is_dir())


# --------------------------- MKDIR ---------------------------

# Example 1

print("Use Path('Reports').mkdir()")


# Example 2

print("Use mkdir(parents=True) for nested folders")


# --------------------------- UNLINK ---------------------------

# Example 1

print("Use unlink() to delete files")


# Example 2

print("Always check existence before deleting")


# --------------------------- RENAME ---------------------------

# Example 1

print("old.txt -> new.txt")


# Example 2

print("report.txt -> report_backup.txt")


# --------------------------- NAME ---------------------------

# Example 1

file = Path("Projects/report.pdf")

print(file.name)


# Example 2

print(Path("data.csv").name)


# --------------------------- STEM ---------------------------

# Example 1

file = Path("report.pdf")

print(file.stem)


# Example 2

print(Path("sales.xlsx").stem)


# --------------------------- SUFFIX ---------------------------

# Example 1

file = Path("report.pdf")

print(file.suffix)


# Example 2

print(Path("sales.xlsx").suffix)


# --------------------------- PARENT ---------------------------

# Example 1

file = Path("Projects/report.pdf")

print(file.parent)


# Example 2

print(Path("Data/sales.csv").parent)


# --------------------------- RESOLVE ---------------------------

# Example 1

file = Path("data.txt")

print(file.resolve())


# Example 2

print(Path(".").resolve())


# --------------------------- READ_TEXT ---------------------------

# Example 1

print("Use read_text() to read file contents")


# Example 2

print("Path('data.txt').read_text()")


# --------------------------- WRITE_TEXT ---------------------------

# Example 1

print("Use write_text() to write file contents")


# Example 2

print("Path('notes.txt').write_text('Hello')")


# --------------------------- ITERDIR ---------------------------

# Example 1

for item in Path(".").iterdir():
    print(item)
    break


# Example 2

print("iterdir() loops through directory contents")


# --------------------------- GLOB ---------------------------

# Example 1

txt_files = list(Path(".").glob("*.txt"))

print(txt_files)


# Example 2

py_files = list(Path(".").glob("*.py"))

print(py_files)


# --------------------------- PRACTICE Q1 ---------------------------

print(Path.cwd())


# --------------------------- PRACTICE Q2 ---------------------------

print(Path.home())


# --------------------------- PRACTICE Q3 ---------------------------

path = Path("Projects") / "Python" / "main.py"

print(path)


# --------------------------- PRACTICE Q4 ---------------------------

print(Path("data.txt").exists())


# --------------------------- PRACTICE Q5 ---------------------------

print("Folder Example: Reports")


# --------------------------- PRACTICE Q6 ---------------------------

file = Path("report.pdf")

print(file.name)

print(file.stem)

print(file.suffix)


# --------------------------- PRACTICE Q7 ---------------------------

for file in Path(".").glob("*.txt"):
    print(file)


# --------------------------- MINI PROJECT ---------------------------

print("\n----- PROJECT STRUCTURE GENERATOR -----\n")

project_name = "LibraryManagement"

folders = [
    "data",
    "reports",
    "logs",
    "src",
    "tests"
]

project_path = Path.cwd() / project_name

print("Project Name:", project_name)

print("\nProject Structure:\n")

print(project_name)

for folder in folders:
    print("├──", folder)

print("└── README.md")

print("\nAbsolute Path:")

print(project_path.resolve())

print("\nVerification:")

for folder in folders:
    print(folder, "->", False)

print("README.md -> Example File")