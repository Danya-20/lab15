# lab15
2.1 Назва роботи:
Лабораторна робота №15: Робота з текстовими даними в Python

2.2 Мета роботи:
Метою лабораторної роботи є ознайомлення з основними методами обробки текстових даних у мові програмування Python. Очікувані результати - розробка функцій для очищення даних, фільтрації, вилучення ключових слів, нормалізації даних і т.д.

2.3 Опис завдання:
У цій лабораторній роботі потрібно реалізувати наступні функції для обробки текстових даних у Python:

Clean Data: Функція clean_data, яка приймає рядок з розділеними комами словами, очищує їх від зайвих пробілів і перетворює на нижній регістр.

Filter Emails: Функція filter_emails, яка приймає рядок з електронними адресами і фільтрує лише ті, які мають рівно один символ @.

Extract Keywords: Функція extract_keywords, яка приймає рядок зі словами і фільтрує ті, які мають довжину більше заданої.

Process Text Data: Функція process_text, яка приймає рядок з текстами, очищує їх від зайвих символів і перетворює на нижній регістр, а потім вилучає тексти, які мають довжину менше 1 символу.

Normalize Data: Функція normalize_data, яка приймає список чисел і нормалізує їх, ділячи кожне число на максимальне значення в списку.

Concatenate Strings: Функція concatenate_strings, яка приймає рядок і роздільник, розділяє його на окремі слова за заданим роздільником і з'єднує їх у єдиний рядок без роздільника.

Sum Numeric Strings: Функція sum_numeric_strings, яка приймає рядок і обчислює суму усіх чисел, які містяться в рядку, ігноруючи нечислові значення.

Filter Numbers: Функція filter_numbers, яка приймає рядок з числами і фільтрує лише ті числа, які більше заданого порогового значення.

Map to Squares: Функція map_to_squares, яка приймає рядок з числами, розділеними комами, і повертає список їх квадратів.

Reverse Strings: Функція reverse_strings, яка приймає рядок зі словами, розділеними комами, і повертає список слів у зворотному порядку.

2.4 Виконання роботи:
Для досягнення мети були виконані наступні кроки:

Написано код кожної з функцій відповідно до завдань.
Створено основний файл програми main.py, що містить всі функції.
Створено файл README.md, який містить детальне пояснення кожної функції, її призначення, структуру проекту, опис основних методів та приклади їх використання.
Завантажено проект на GitHub у папку lab15.
Підготовлено скріншоти або приклади виводу програми для файлу README.md.
2.5 Результати:
Результати виконання кожної з функцій були перевірені і продемонстровані за допомогою прикладів використання, які наведені у файлі README.md. Нижче наведено короткий приклад використання функцій:

# Використання функції clean_data
data = "  Apple, Banana , orange "
cleaned = clean_data(data)
print(cleaned)  # ['apple', 'banana', 'orange']

# Використання функції filter_emails
emails = "mail us test@example.com and invalid-email.com djwd with example@test.co"
valid_emails = filter_emails(emails)
print(valid_emails)  # ['test@example.com', 'example@test.co']

# Інші приклади використання аналогічним чином для інших функцій...
Ці приклади демонструють коректну роботу кожної з функцій у рамках лабораторної роботи.
