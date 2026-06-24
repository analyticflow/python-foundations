# --------------------------- COLLECTIONS MODULE ---------------------------


from collections import Counter, defaultdict, deque, namedtuple, OrderedDict


# --------------------------- WHY COLLECTIONS ---------------------------

# Example 1 (Without Collections)

words = ["apple", "banana", "apple", "orange", "apple"]

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)


# Example 2 (With Counter)

words = ["apple", "banana", "apple", "orange", "apple"]

result = Counter(words)

print(result)


# --------------------------- COUNTER ---------------------------

# Example 1

data = ["apple", "banana", "apple", "orange", "apple"]

result = Counter(data)

print(result)


# Example 2

votes = ["A", "B", "A", "C", "A", "B"]

result = Counter(votes)

print(result)


# --------------------------- ACCESS COUNT ---------------------------

# Example 1

fruits = Counter(["apple", "banana", "apple"])

print(fruits["apple"])


# Example 2

colors = Counter(["red", "blue", "red", "green"])

print(colors["red"])


# --------------------------- MOST COMMON ITEMS ---------------------------

# Example 1

data = Counter(["apple", "banana", "apple", "apple"])

print(data.most_common(1))


# Example 2

votes = Counter(["A", "B", "A", "C", "A"])

print(votes.most_common(2))


# --------------------------- DEFAULTDICT ---------------------------

# Example 1

scores = defaultdict(int)

print(scores["Math"])


# Example 2

inventory = defaultdict(int)

print(inventory["Laptop"])


# --------------------------- DEFAULTDICT WITH INT ---------------------------

# Example 1

scores = defaultdict(int)

scores["Aman"] += 10

print(scores)


# Example 2

marks = defaultdict(int)

marks["Rahul"] += 20

print(marks)


# --------------------------- DEFAULTDICT WITH LIST ---------------------------

# Example 1

students = defaultdict(list)

students["Python"].append("Aman")
students["Python"].append("Rahul")

print(students)


# Example 2

courses = defaultdict(list)

courses["SQL"].append("Priya")
courses["SQL"].append("Karan")

print(courses)


# --------------------------- DEQUE ---------------------------

# Example 1

dq = deque([1, 2, 3])

print(dq)


# Example 2

queue = deque(["A", "B", "C"])

print(queue)


# --------------------------- APPEND RIGHT ---------------------------

# Example

dq = deque([1, 2, 3])

dq.append(4)

print(dq)


# --------------------------- APPEND LEFT ---------------------------

# Example

dq = deque([1, 2, 3])

dq.appendleft(0)

print(dq)


# --------------------------- POP RIGHT ---------------------------

# Example

dq = deque([1, 2, 3, 4])

removed = dq.pop()

print(removed)
print(dq)


# --------------------------- POP LEFT ---------------------------

# Example

dq = deque([0, 1, 2, 3])

removed = dq.popleft()

print(removed)
print(dq)


# --------------------------- DEQUE AS QUEUE ---------------------------

# Example

queue = deque()

queue.append("Task1")
queue.append("Task2")
queue.append("Task3")

print(queue)

print(queue.popleft())

print(queue)


# --------------------------- NAMEDTUPLE ---------------------------

# Example 1

Student = namedtuple("Student", ["name", "age"])

s1 = Student("Aman", 22)

print(s1)


# Example 2

Employee = namedtuple("Employee", ["name", "salary"])

e1 = Employee("Rahul", 50000)

print(e1)


# --------------------------- ACCESS NAMED FIELDS ---------------------------

# Example 1

Student = namedtuple("Student", ["name", "age"])

s1 = Student("Aman", 22)

print(s1.name)
print(s1.age)


# Example 2

Employee = namedtuple("Employee", ["name", "salary"])

e1 = Employee("Priya", 60000)

print(e1.name)
print(e1.salary)


# --------------------------- ORDEREDDICT ---------------------------

# Example 1

data = OrderedDict()

data["A"] = 1
data["B"] = 2
data["C"] = 3

print(data)


# Example 2

report = OrderedDict()

report["January"] = 100
report["February"] = 200
report["March"] = 300

print(report)


# --------------------------- ITERATING ORDEREDDICT ---------------------------

# Example

data = OrderedDict()

data["A"] = 100
data["B"] = 200
data["C"] = 300

for key, value in data.items():
    print(key, value)


# --------------------------- COUNTER VS NORMAL DICTIONARY ---------------------------

# Example

items = ["pen", "pen", "book", "pen", "book"]

normal_count = {}

for item in items:
    normal_count[item] = normal_count.get(item, 0) + 1

print(normal_count)

counter_count = Counter(items)

print(counter_count)


# --------------------------- PRACTICE Q1 ---------------------------

words = ["python", "java", "python", "c++", "python"]

result = Counter(words)

print(result)


# --------------------------- PRACTICE Q2 ---------------------------

colors = ["red", "blue", "red", "green", "red"]

result = Counter(colors)

print(result.most_common(1))


# --------------------------- PRACTICE Q3 ---------------------------

scores = defaultdict(int)

scores["Aman"] += 90
scores["Rahul"] += 80
scores["Priya"] += 95

print(scores)


# --------------------------- PRACTICE Q4 ---------------------------

dq = deque()

dq.append(10)
dq.append(20)

dq.appendleft(5)

print(dq)

dq.pop()

print(dq)

dq.popleft()

print(dq)


# --------------------------- PRACTICE Q5 ---------------------------

Employee = namedtuple("Employee", ["name", "salary"])

emp = Employee("Aman", 50000)

print(emp.name)
print(emp.salary)


# --------------------------- PRACTICE Q6 ---------------------------

data = OrderedDict()

data["A"] = 100
data["B"] = 200
data["C"] = 300

for key, value in data.items():
    print(key, value)


# --------------------------- MINI PROJECT ---------------------------

print("\n----- STUDENT ENROLLMENT SYSTEM -----\n")

enrollment = defaultdict(list)

enrollment["Python"].append("Aman")
enrollment["Python"].append("Rahul")

enrollment["SQL"].append("Priya")

enrollment["Excel"].append("Karan")


for course, students in enrollment.items():
    print(course, "->", ", ".join(students))


all_courses = []

for course, students in enrollment.items():
    all_courses.extend([course] * len(students))

course_count = Counter(all_courses)

print("\nTotal Students Per Course:\n")

for course, count in course_count.items():
    print(course, ":", count)
