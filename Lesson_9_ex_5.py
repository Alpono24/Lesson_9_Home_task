import re
from idlelib.sidebar import LineNumbers

print("Lesson 9. Home task №5.")

"""
5. В текстовый файл построчно записаны фамилия и имя учащихся класса и оценка за контрольную. 
Вывести на экран всех учащихся, чья оценка меньше трёх баллов.
"""


with open("for_ex_5.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip().split()
        line_fio = ' '.join(line[:-1])
        value = line[-1]
        if int(value) < int(3):
            print(f"Список учеников с баллом меньше 3: {line_fio}, балл: {value}")





