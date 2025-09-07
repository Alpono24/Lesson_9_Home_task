

print("Lesson 9. Home task №3.")

"""
3. Напишите программу, которая считывает текст из файла (в
файле может быть больше одной строки) и выводит в новый файл
самое часто встречаемое слово в каждой строке и число – счётчик
количества повторений этого слова в строке.
"""
import re
# file_name = input("ВВедите имя файла с расширением:")



def read_text_and_count():
    file_name_input = 'for_ex_3_input.txt'
    file_name_output = 'for_ex_3_output.txt'
    with open(file_name_input, "r", encoding="utf-8") as file_input, open(file_name_output, "w", encoding="utf-8") as file_output:

        text = file_input.read()
        lines = text.splitlines()
        for i, line in enumerate(lines):
            # очистка от знаков пунктуации и приведение букв к строчным
            # #clean_line = ''.join(char.lower() if char.isalnum() or char.isspace() else '' for char in line)
            clean_line = ''
            for char in line:
                if char.isalnum() or char.isspace():
                    clean_line += char.lower()

            # формируем перечень слов в список
            all_words = clean_line.split()

            # проверяем наличие слов в строке
            if len(all_words) == 0:
                continue

            # создаём словарь для подсчёта слов
            word_count = {}
            for word in all_words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

            # print(word_count)
            # print(i+1, clean_line, "dsd", all_words)

            # находим максимальное значение
            max_freq = max(word_count.values())

            most_common_words = []
            for word, freq in word_count.items():
                if freq == max_freq:
                    most_common_words.append(word)

            # выбираем первое слово среди самых частых
            most_common_word = most_common_words[0]



            # записываем результат в файл
            file_output.write(f"В строке {i+1}: '{most_common_word}' встречается {max_freq} раз.\n")



read_text_and_count()


