# --------------------------- REGULAR EXPRESSIONS (REGEX) ---------------------------

import re


# --------------------------- WHY REGEX ---------------------------

# Example 1 (Without Regex)

email = "user123@gmail.com"

if "@" in email and "." in email:
    print("Basic Validation Passed")


# Example 2 (With Regex)

email = "user123@gmail.com"

if re.search(r"^\w+@\w+\.\w+$", email):
    print("Regex Validation Passed")


# --------------------------- PATTERN MATCHING ---------------------------

# Example 1

result = re.search(r"cat", "The cat is sleeping")

print(result.group())


# Example 2

result = re.search(r"dog", "My dog is barking")

print(result.group())


# --------------------------- DIGITS (\d) ---------------------------

# Example 1

numbers = re.findall(r"\d", "A1B2C3")

print(numbers)


# Example 2

numbers = re.findall(r"\d", "Room 45 Floor 8")

print(numbers)


# --------------------------- NON-DIGITS (\D) ---------------------------

# Example

characters = re.findall(r"\D", "A1B2C3")

print(characters)


# --------------------------- WORD CHARACTERS (\w) ---------------------------

# Example

words = re.findall(r"\w", "Hello_123")

print(words)


# --------------------------- NON-WORD CHARACTERS (\W) ---------------------------

# Example

symbols = re.findall(r"\W", "Hello@123!")

print(symbols)


# --------------------------- WHITESPACE (\s) ---------------------------

# Example

spaces = re.findall(r"\s", "Python   Regex")

print(spaces)


# --------------------------- NON-WHITESPACE (\S) ---------------------------

# Example

characters = re.findall(r"\S", "Python Regex")

print(characters)


# --------------------------- CHARACTER SETS ---------------------------

# Example 1

letters = re.findall(r"[abc]", "apple banana cat")

print(letters)


# Example 2

letters = re.findall(r"[aeiou]", "programming")

print(letters)


# --------------------------- RANGES ---------------------------

# Example 1

lowercase = re.findall(r"[a-z]", "Hello123")

print(lowercase)


# Example 2

uppercase = re.findall(r"[A-Z]", "Hello123")

print(uppercase)


# Example 3

digits = re.findall(r"[0-9]", "A1B2C3")

print(digits)


# --------------------------- QUANTIFIER (*) ---------------------------

# Example

matches = re.findall(r"ab*", "a ab abb abbb")

print(matches)


# --------------------------- QUANTIFIER (+) ---------------------------

# Example

matches = re.findall(r"ab+", "a ab abb abbb")

print(matches)


# --------------------------- QUANTIFIER (?) ---------------------------

# Example

matches = re.findall(r"colou?r", "color colour")

print(matches)


# --------------------------- RE.SEARCH() ---------------------------

# Example 1

text = "I have 2 apples"

result = re.search(r"\d", text)

print(result.group())


# Example 2

text = "Order Number: 567"

result = re.search(r"\d+", text)

print(result.group())


# --------------------------- RE.MATCH() ---------------------------

# Example 1

result = re.match(r"\d", "5 apples")

print(result.group())


# Example 2

result = re.match(r"\d", "I have 5 apples")

print(result)


# --------------------------- SEARCH VS MATCH ---------------------------

text = "I have 7 apples"

print(re.search(r"\d", text).group())

print(re.match(r"\d", text))


# --------------------------- RE.FINDALL() ---------------------------

# Example 1

numbers = re.findall(r"\d", "A1B2C3")

print(numbers)


# Example 2

vowels = re.findall(r"[aeiou]", "banana")

print(vowels)


# --------------------------- RE.SUB() ---------------------------

# Example 1

text = "I love cats"

result = re.sub("cats", "dogs", text)

print(result)


# Example 2

text = "A1B2C3"

result = re.sub(r"\d", "*", text)

print(result)


# --------------------------- RAW STRINGS ---------------------------

pattern = r"\d+"

print(pattern)


# --------------------------- PRACTICE Q1 ---------------------------

digits = re.findall(r"\d", "A1B2C3D4")

print(digits)


# --------------------------- PRACTICE Q2 ---------------------------

vowels = re.findall(r"[aeiou]", "programming")

print(vowels)


# --------------------------- PRACTICE Q3 ---------------------------

text = "5Python"

result = re.match(r"\d", text)

print(bool(result))


# --------------------------- PRACTICE Q4 ---------------------------

result = re.sub(r"\d", "*", "User123")

print(result)


# --------------------------- PRACTICE Q5 ---------------------------

numbers = re.findall(r"\d+", "12 apples and 34 bananas")

print(len(numbers))


# --------------------------- PRACTICE Q6 ---------------------------

uppercase = re.findall(r"[A-Z]", "PyTHon ReGEx")

print(uppercase)


# --------------------------- PRACTICE Q7 ---------------------------

text = "Python     is      awesome"

cleaned = re.sub(r"\s+", " ", text)

print(cleaned)


# --------------------------- MINI PROJECT ---------------------------

print("\n----- USER DATA CLEANER -----\n")

data = """
Name: Aman
Phone: 9876543210
Email: aman@gmail.com
"""


phone = re.findall(r"\d{10}", data)

email = re.findall(r"\w+@\w+\.\w+", data)

masked_data = re.sub(r"\d", "*", data)

total_digits = len(re.findall(r"\d", data))

print("Phone Number:", phone)

print("Email:", email)

print("Total Digits:", total_digits)

print("\nCleaned Data:\n")

print(masked_data)