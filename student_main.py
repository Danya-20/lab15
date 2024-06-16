# Task 1: Clean Data
def clean_data(data):
    return list(map(lambda x: x.strip().lower(), data.split(',')))

data = "  Apple, Banana , orange "
cleaned = clean_data(data)
print(cleaned)  # ['apple', 'banana', 'orange']

# Task 2: Filter Emails
def filter_emails(emails):
    return list(filter(lambda email: email.count('@') == 1, emails.split()))

emails = "mail us test@example.com and invalid-email.com djwd with example@test.co"
valid_emails = filter_emails(emails)
print(valid_emails)  # ['test@example.com', 'example@test.co']

# Task 3: Extract Keywords
def extract_keywords(words, min_length):
    return list(filter(lambda word: len(word) > min_length, words.split()))

words = "apple pear banana kiwi"
filtered_words = extract_keywords(words, 4)
print(filtered_words)  # ['apple', 'banana']

# Task 4: Process Text Data
def process_text(data):
    return list(filter(lambda text: len(text.strip()) > 1, map(lambda x: x.strip().lower(), data.split())))

texts = " Hello! , Yes? , No. ,  "
processed_texts = process_text(texts)
print(processed_texts)  # ['hello', 'yes', 'no']

# Task 5: Normalize Data
def normalize_data(numbers):
    max_value = max(numbers)
    return [num / max_value for num in numbers]

numbers = [10, 20, 30]
normalized_numbers = normalize_data(numbers)
print(normalized_numbers)  # [0.333, 0.667, 1.0]

# Task 6: Concatenate Strings
def concatenate_strings(data, separator):
    return ''.join(data.split(separator))

data = "hello*world*again"
concatenated = concatenate_strings(data, '*')
print(concatenated)  # 'helloworldagain'

# Task 7: Sum Numeric Strings
def sum_numeric_strings(numbers):
    return sum(int(num) for num in numbers.split(',') if num.strip().isdigit())

numbers = "1, 2, test, 3, 4"
total_sum = sum_numeric_strings(numbers)
print(total_sum)  # 10

# Task 8: Filter Numbers
def filter_numbers(numbers, threshold):
    return [int(num) for num in numbers.split() if num.isdigit() and int(num) > threshold]

numbers = "10 test 30 40"
filtered = filter_numbers(numbers, 25)
print(filtered)  # [30, 40]

# Task 9: Map to Squares
def map_to_squares(numbers):
    return [num ** 2 for num in map(int, numbers.split(','))]

numbers = "1, 2, 3, 4"
squared_numbers = map_to_squares(numbers)
print(squared_numbers)  # [1, 4, 9, 16]

# Task 10: Reverse Strings
def reverse_strings(words):
    return [word[::-1] for word in words.split(',')]

words = "apple,banana,carrot"
reversed_words = reverse_strings(words)
print(reversed_words)  # ['elppa', 'ananab', 'torrac']
