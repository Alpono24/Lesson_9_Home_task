
print("Lesson 9. Home task №6.")

"""
6. В файл записано некоторое содержимое (буквы, цифры, пробелы, специальные символы и т.д.). 
Числом назовём последовательность цифр, идущих подряд. 
Вывести сумму всех чисел, записанных в файле.
Пример.

Входные данные: 123 ааа456 1x2y3z 4 5 6
Выходные данные: 600
"""

import re

with open("for_ex_6.txt") as f:
    data = f.read()
    pattern = r'\d+'
    numbers = re.findall(pattern, data)
    print('Список полученных чисел:', numbers)
    summa = 0
    for number in numbers:
       summa += int(number)

    print('Итоговая сумма всех чисел:', summa)