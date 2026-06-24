# --------------------------- DATETIME MODULE ---------------------------


from datetime import date, time, datetime, timedelta


# --------------------------- WHY DATETIME ---------------------------

# Example 1 (Without Datetime)

exam_date = "25-12-2026"

print(exam_date)


# Example 2 (With Datetime)

exam_date = date(2026, 12, 25)

print(exam_date)


# --------------------------- DATE CLASS ---------------------------

# Example 1

today = date(2026, 6, 18)

print(today)


# Example 2

birthday = date(2000, 5, 10)

print(birthday)


# --------------------------- ACCESS DATE COMPONENTS ---------------------------

# Example 1

today = date(2026, 6, 18)

print(today.year)
print(today.month)
print(today.day)


# Example 2

exam = date(2026, 12, 25)

print(exam.year)
print(exam.month)
print(exam.day)


# --------------------------- CURRENT DATE ---------------------------

# Example 1

today = date.today()

print(today)


# Example 2

print(date.today())


# --------------------------- TIME CLASS ---------------------------

# Example 1

t = time(14, 30, 45)

print(t)


# Example 2

meeting_time = time(9, 15, 0)

print(meeting_time)


# --------------------------- ACCESS TIME COMPONENTS ---------------------------

# Example

t = time(14, 30, 45)

print(t.hour)
print(t.minute)
print(t.second)


# --------------------------- DATETIME CLASS ---------------------------

# Example 1

dt = datetime(2026, 6, 18, 14, 30, 45)

print(dt)


# Example 2

event = datetime(2026, 12, 25, 10, 0, 0)

print(event)


# --------------------------- CURRENT DATE AND TIME ---------------------------

# Example 1

now = datetime.now()

print(now)


# Example 2

print(datetime.now())


# --------------------------- ACCESS DATETIME COMPONENTS ---------------------------

# Example

now = datetime.now()

print(now.year)
print(now.month)
print(now.day)

print(now.hour)
print(now.minute)
print(now.second)


# --------------------------- TIMEDELTA ---------------------------

# Example 1

gap = timedelta(days=5)

print(gap)


# Example 2

duration = timedelta(hours=10)

print(duration)


# --------------------------- ADD DAYS ---------------------------

# Example 1

today = date.today()

future = today + timedelta(days=7)

print(future)


# Example 2

future = today + timedelta(days=30)

print(future)


# --------------------------- SUBTRACT DAYS ---------------------------

# Example 1

today = date.today()

past = today - timedelta(days=30)

print(past)


# Example 2

past = today - timedelta(days=7)

print(past)


# --------------------------- DIFFERENCE BETWEEN DATES ---------------------------

# Example 1

d1 = date(2026, 6, 1)
d2 = date(2026, 6, 18)

difference = d2 - d1

print(difference)


# Example 2

start = date(2026, 1, 1)
end = date(2026, 12, 31)

print(end - start)


# --------------------------- DATE COMPARISON ---------------------------

# Example 1

d1 = date(2026, 1, 1)
d2 = date(2026, 6, 1)

print(d1 < d2)


# Example 2

print(d2 > d1)


# --------------------------- STRFTIME ---------------------------

# Example 1

now = datetime.now()

print(now.strftime("%d/%m/%Y"))


# Example 2

print(now.strftime("%A"))


# --------------------------- MORE STRFTIME FORMATS ---------------------------

# Example 1

print(now.strftime("%B"))


# Example 2

print(now.strftime("%d-%m-%Y %H:%M:%S"))


# --------------------------- STRPTIME ---------------------------

# Example 1

text = "18-06-2026"

date_obj = datetime.strptime(
    text,
    "%d-%m-%Y"
)

print(date_obj)


# Example 2

text = "25-12-2026"

date_obj = datetime.strptime(
    text,
    "%d-%m-%Y"
)

print(date_obj)


# --------------------------- FORMAT VS PARSE ---------------------------

# Example

now = datetime.now()

formatted = now.strftime("%d/%m/%Y")

print(formatted)

parsed = datetime.strptime(
    formatted,
    "%d/%m/%Y"
)

print(parsed)


# --------------------------- PRACTICE Q1 ---------------------------

print(date.today())


# --------------------------- PRACTICE Q2 ---------------------------

d = date(2025, 12, 31)

print(d.year)
print(d.month)
print(d.day)


# --------------------------- PRACTICE Q3 ---------------------------

print(datetime.now())


# --------------------------- PRACTICE Q4 ---------------------------

future = date.today() + timedelta(days=15)

print(future)


# --------------------------- PRACTICE Q5 ---------------------------

d1 = date(2026, 1, 1)
d2 = date(2026, 6, 18)

print(d2 - d1)


# --------------------------- PRACTICE Q6 ---------------------------

now = datetime.now()

print(now.strftime("%d/%m/%Y"))


# --------------------------- PRACTICE Q7 ---------------------------

text = "25-12-2026"

date_obj = datetime.strptime(
    text,
    "%d-%m-%Y"
)

print(date_obj)


# --------------------------- MINI PROJECT ---------------------------

print("\n----- EXAM COUNTDOWN SYSTEM -----\n")

exam_input = "25-12-2026"

exam_date = datetime.strptime(
    exam_input,
    "%d-%m-%Y"
).date()

today = date.today()

remaining_days = (exam_date - today).days

print("Exam Date:", exam_input)

print("Days Remaining:", remaining_days)
